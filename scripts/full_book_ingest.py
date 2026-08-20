#!/usr/bin/env python3
"""Stage 4A raw inventory, DOCX media extraction, and JSON mappings.

Markdown is the primary text layer. JSON supplies structure only. DOCX
supplies embedded media only; DOCX-derived text never overwrites Markdown.
"""
from __future__ import annotations

import csv, hashlib, json, re, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
RAW = REPO / "source" / "raw" / "full_book"
QA = REPO / "qa"
PARTS = (("part_001_200", 1, 200), ("part_201_243", 201, 243))
CHAPTERS = (
    (1,14,"大地主的儿子和贫农的儿子"),(2,18,"“海归”和离家出走的少年"),
    (3,26,"年轻的米店老板和二十出头的大地主"),(4,34,"星标面条和阿道汽车修理厂"),
    (5,42,"三星物产公司和现代汽车工业公司"),(6,50,"理发师的启示"),
    (7,54,"大麦草坪和白糖"),(8,66,"高级布料和高灵桥工程"),
    (9,74,"先发制人和后发制人"),(10,84,"汉江大桥和东京构想"),
    (11,92,"权利面前的两个人"),(12,98,"开办工厂和对外出口"),
    (13,110,"越战工程和韩国肥料公司"),(14,120,"Pony（小马）汽车和东洋电视台"),
    (15,136,"郑周永的船和李秉哲的彩色电视"),(16,146,"中东特运和三星电子"),
    (17,162,"先想后做和先做后想"),(18,166,"李秉哲、郑周永在半导体业的较量"),
    (19,178,"对属下的爱与培养"),(20,184,"优秀的企业家具有识人的慧眼"),
    (21,188,"信任与考察"),(22,192,"玩出名堂"),
    (23,198,"正规的高尔夫和红色的高尔夫"),(24,204,"李秉哲和郑周永的节俭"),
    (25,210,"两位巨人的最后时日"),(26,222,"王子之乱和接班人们"),
    (27,228,"王国的功臣们"),(28,238,"巨人的时代结束后"),
)
URL_RE = re.compile(r"!\[[^\]]*\]\((https://cdn-mineru\.openxlab\.org\.cn/[^)]+)\)")
MARKER_RE = re.compile(r"(?:\^\{)?([①②③④⑤⑥⑦⑧⑨⑩])(?:\})?")

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def file_sha(path: Path) -> str: return sha(path.read_bytes())

def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

def block_text(block: dict) -> str:
    out = []
    for container in block.get("blocks") or [block]:
        for line in container.get("lines") or []:
            for span in line.get("spans") or []:
                if span.get("content"): out.append(str(span["content"]))
    return "".join(out).strip()

def image_url(block: dict) -> str | None:
    for container in block.get("blocks") or [block]:
        for line in container.get("lines") or []:
            for span in line.get("spans") or []:
                if span.get("type") == "image" and span.get("image_path"):
                    return str(span["image_path"])
    return None

def bbox(block: dict) -> str:
    return ":".join(str(x) for x in block.get("bbox") or [])

def docx_media(path: Path) -> list[dict]:
    ns = {"a":"http://schemas.openxmlformats.org/drawingml/2006/main",
          "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships",
          "p":"http://schemas.openxmlformats.org/package/2006/relationships"}
    with zipfile.ZipFile(path) as z:
        doc = ET.fromstring(z.read("word/document.xml"))
        rels = ET.fromstring(z.read("word/_rels/document.xml.rels"))
        relmap = {x.attrib["Id"]:x.attrib["Target"] for x in rels.findall("p:Relationship",ns)}
        out=[]
        for n, blip in enumerate(doc.findall(".//a:blip",ns),1):
            rid=blip.attrib[f"{{{ns['r']}}}embed"]; target=relmap[rid].replace("\\","/")
            entry="word/"+target.lstrip("/"); data=z.read(entry)
            out.append(dict(ordinal=n,rid=rid,entry=entry,suffix=Path(entry).suffix.lower(),data=data))
        return out

def section(page: int) -> tuple[str,str]:
    if page < 14: return "00_front_matter.md","front matter"
    if page >= 240: return "99_afterword.md",("archive metadata candidate" if page==243 else "afterword")
    selected=CHAPTERS[0]
    for ch in CHAPTERS:
        if ch[1] <= page: selected=ch
        else: break
    n,_,title=selected
    return f"{n:02d}_chapter_{n:02d}.md",f"Chapter {n}: {title}"

def printed_page(page: dict) -> str:
    found=[]
    for b in page.get("discarded_blocks") or []:
        text=block_text(b); box=b.get("bbox") or []
        if b.get("type")=="page_number" and re.fullmatch(r"\d{1,3}",text) and len(box)==4 and box[1]>=750:
            found.append(text)
    return found[0] if len(set(found))==1 else "Unknown"

def process_part(name: str, first: int, last: int, image_n: int, foot_n: int):
    root=RAW/name; mdp=root/"source.md"; jp=root/"source.json"; dp=root/"source.docx"
    for p in (mdp,jp,dp):
        if not p.is_file(): raise FileNotFoundError(p)
    md=mdp.read_text(encoding="utf-8"); md_urls=URL_RE.findall(md)
    parsed=json.loads(jp.read_text(encoding="utf-8")); pages=parsed["pdf_info"]
    if len(pages) != last-first+1: raise RuntimeError(f"{name}: page count mismatch")
    page_rows=[]; json_images=[]; footnotes=[]
    for p in pages:
        local=int(p["page_idx"]); global_page=first+local; sid=f"FB-P{global_page:03d}"
        para=p.get("para_blocks") or []; disc=p.get("discarded_blocks") or []
        image_ids=[]; foot_ids=[]
        for b in para:
            if b.get("type")=="image":
                url=image_url(b)
                if not url: raise RuntimeError(f"{sid}: missing image URL")
                iid=f"FB-I{image_n:03d}"; image_n+=1; image_ids.append(iid)
                json_images.append(dict(image_id=iid,part=name,local_page_idx=local,
                    input_pdf_page=global_page,source_page_id=sid,json_block_index=b.get("index",""),
                    json_bbox=bbox(b),mineru_url=url))
        page_text="\n".join(block_text(b) for b in para if block_text(b))
        markers=MARKER_RE.findall(page_text)
        for b in disc:
            if b.get("type")=="page_footnote":
                fid=f"FB-F{foot_n:03d}"; foot_n+=1; foot_ids.append(fid)
                footnotes.append(dict(footnote_id=fid,part=name,local_page_idx=local,
                    input_pdf_page=global_page,source_page_id=sid,json_block_index=b.get("index",""),
                    json_bbox=bbox(b),marker_candidates="|".join(markers) or "unresolved",
                    footnote_body=block_text(b),mapping_status="candidate — manual review required"))
        sec,label=section(global_page)
        headers=[block_text(b) for b in disc if b.get("type")=="header" and block_text(b)]
        footers=[block_text(b) for b in disc if b.get("type") in {"footer","page_number"} and block_text(b)]
        page_rows.append(dict(source_page_id=sid,part=name,local_page_idx=local,input_pdf_page=global_page,
            printed_page=printed_page(p),section_file=sec,chapter_or_section=label,
            block_sequence="|".join(f"{b.get('index','')}:{b.get('type','')}" for b in para),
            block_types="|".join(str(b.get("type","")) for b in para),
            block_bboxes="|".join(f"{b.get('index','')}:{bbox(b)}" for b in para),
            image_ids="|".join(image_ids),footnote_ids="|".join(foot_ids),
            discarded_header_text="|".join(headers),discarded_footer_or_page_number="|".join(footers),
            mapping_status="mapped",note=""))
    if md_urls != [x["mineru_url"] for x in json_images]:
        raise RuntimeError(f"{name}: Markdown/JSON image order mismatch")
    media=docx_media(dp)
    if len(media)!=len(json_images): raise RuntimeError(f"{name}: DOCX/JSON image count mismatch")
    images_dir=root/"images"; images_dir.mkdir(exist_ok=True); image_rows=[]
    for item,m in zip(json_images,media,strict=True):
        local=f"image_{m['ordinal']:03d}{m['suffix']}"; path=images_dir/local; data=m["data"]
        if path.exists() and path.read_bytes()!=data: raise RuntimeError(f"refusing overwrite: {path}")
        if not path.exists(): path.write_bytes(data)
        item=dict(item,local_image=f"source/raw/full_book/{name}/images/{local}",
            local_relative_from_chapters=f"../raw/full_book/{name}/images/{local}",
            source_docx_entry=m["entry"],docx_relationship_id=m["rid"],document_order=m["ordinal"],
            bytes=len(data),sha256=sha(data),mapping_status="verified one-to-one")
        image_rows.append(item)
    image_fields=["image_id","part","local_page_idx","input_pdf_page","source_page_id","json_block_index",
        "json_bbox","mineru_url","local_image","local_relative_from_chapters","source_docx_entry",
        "docx_relationship_id","document_order","bytes","sha256","mapping_status"]
    write_csv(images_dir/"image_map.csv",image_fields,image_rows)
    lines=[f"# Raw full-book source: {name}","",f"Supplied input PDF page range: {first}–{last}.","",
        "Immutable MinerU evidence. Markdown is the primary text source; JSON provides page/block/layout evidence; DOCX is the embedded-image and visual fallback only. DOCX-derived text must never overwrite source.md.","",
        "## Raw file integrity","","| File | Bytes | SHA-256 |","|---|---:|---|"]
    for p in (mdp,jp,dp): lines.append(f"| {p.name} | {p.stat().st_size} | `{file_sha(p)}` |")
    lines += ["",f"Extracted DOCX images: {len(image_rows)}. Images are byte-identical word/media copies in DOCX document order and are cross-mapped in images/image_map.csv.","","No original copyright PDF is stored here.",""]
    (root/"README.md").write_text("\n".join(lines),encoding="utf-8")
    return page_rows,image_rows,footnotes,image_n,foot_n

def main() -> None:
    pages=[]; images=[]; footnotes=[]; image_n=1; foot_n=1
    for args in PARTS:
        p,i,f,image_n,foot_n=process_part(*args,image_n,foot_n); pages+=p; images+=i; footnotes+=f
    page_fields=["source_page_id","part","local_page_idx","input_pdf_page","printed_page","section_file",
        "chapter_or_section","block_sequence","block_types","block_bboxes","image_ids","footnote_ids",
        "discarded_header_text","discarded_footer_or_page_number","mapping_status","note"]
    image_fields=["image_id","part","local_page_idx","input_pdf_page","source_page_id","json_block_index",
        "json_bbox","mineru_url","local_image","local_relative_from_chapters","source_docx_entry",
        "docx_relationship_id","document_order","bytes","sha256","mapping_status"]
    foot_fields=["footnote_id","part","local_page_idx","input_pdf_page","source_page_id","json_block_index",
        "json_bbox","marker_candidates","footnote_body","mapping_status"]
    write_csv(QA/"full_book_page_map.csv",page_fields,pages)
    write_csv(QA/"full_book_image_map.csv",image_fields,images)
    write_csv(QA/"full_book_footnote_map.csv",foot_fields,footnotes)
    summary=["# Full-book MinerU raw ingestion","",
        "Two MinerU batches are preserved separately so raw artifacts remain byte-for-byte traceable; they are not concatenated or rewritten.","",
        "- part_001_200: supplied input PDF pages 1–200","- part_201_243: supplied input PDF pages 201–243","",
        f"Verified JSON pages: {len(pages)}",f"Verified/localized DOCX images: {len(images)}",
        f"JSON footnote candidates: {len(footnotes)} (all require manual review)","",
        "Global IDs FB-P001–FB-P243 follow the supplied input page ranges. Local zero-based MinerU page_idx values remain in qa/full_book_page_map.csv.","",
        "No original copyright PDF is stored here. Source possession grants no additional redistribution rights.",""]
    (RAW/"README.md").write_text("\n".join(summary),encoding="utf-8")
    print(json.dumps({"pages":len(pages),"images":len(images),"footnotes":len(footnotes)},ensure_ascii=False))

if __name__=="__main__": main()
