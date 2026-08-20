#!/usr/bin/env python3
"""Split raw MinerU Markdown into traceable Stage 4A chapter sources.

Text is sliced from source.md. JSON is used only to locate page boundaries and
verify layout. No DOCX-derived text is used. Ambiguous content is preserved.
"""
from __future__ import annotations

import bisect, csv, json, re
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
RAW=REPO/"source"/"raw"/"full_book"; OUT=REPO/"source"/"chapters"; QA=REPO/"qa"
PARTS=(("part_001_200",1,200),("part_201_243",201,243))
CHAPTERS=(
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
 (21,188,"信任与考察"),(22,192,"玩出名堂"),(23,198,"正规的高尔夫和红色的高尔夫"),
 (24,204,"李秉哲和郑周永的节俭"),(25,210,"两位巨人的最后时日"),
 (26,222,"王子之乱和接班人们"),(27,228,"王国的功臣们"),(28,238,"巨人的时代结束后"),)
URL_RE=re.compile(r"!\[[^\]]*\]\((https://cdn-mineru\.openxlab\.org\.cn/[^)]+)\)")
HEADER="从平凡走向辉煌"

def block_text(b):
 out=[]
 for c in b.get("blocks") or [b]:
  for line in c.get("lines") or []:
   for span in line.get("spans") or []:
    if span.get("content"): out.append(str(span["content"]))
 return "".join(out).strip()

def block_url(b):
 for c in b.get("blocks") or [b]:
  for line in c.get("lines") or []:
   for span in line.get("spans") or []:
    if span.get("type")=="image" and span.get("image_path"): return str(span["image_path"])
 return None

def compact_map(text):
 chars=[]; offsets=[]
 for i,ch in enumerate(text):
  if not ch.isspace(): chars.append(ch); offsets.append(i)
 return "".join(chars),offsets

def anchors(page):
 out=[]
 for b in page.get("para_blocks") or []:
  text=block_text(b)
  if text: out.append((text,f"{b.get('index','')}:{b.get('type','')}"))
  else:
   url=block_url(b)
   if url: out.append((url,f"{b.get('index','')}:image"))
 return out

def align_part(md,pages):
 compact,offsets=compact_map(md); cursor=0; rows=[]; boundaries=[]
 for i,page in enumerate(pages):
  if i==0:
   boundaries.append(0); rows.append(("part-start","",0)); continue
  found=None
  for candidate,evidence in anchors(page):
   needle="".join(candidate.split())
   if re.fullmatch(r"\d{1,2}",candidate) and evidence.endswith(":title"):
    original_cursor=offsets[cursor] if cursor<len(offsets) else len(md)
    match=re.search(rf"(?m)^#{{1,6}}\s+{re.escape(candidate)}\s*$",md[original_cursor:])
    if match:
     original=original_cursor+match.start()
     found=(bisect.bisect_left(offsets,original),evidence,candidate,original)
     break
   if len(needle)<2: continue
   pos=compact.find(needle,cursor)
   if pos>=0:
    found=(pos,evidence,candidate,None); break
  if found is None:
   boundaries.append(None); rows.append(("unresolved","","")); continue
  pos,evidence,candidate,original_override=found; original=original_override if original_override is not None else offsets[pos]
  line_start=md.rfind("\n",0,original)+1
  boundaries.append(line_start); rows.append(("mapped",evidence,candidate[:80])); cursor=pos
 for i in range(len(boundaries)-1,-1,-1):
  if boundaries[i] is None and not anchors(pages[i]):
   next_boundary=next((x for x in boundaries[i+1:] if x is not None),len(md))
   boundaries[i]=next_boundary
   rows[i]=("blank-candidate","no semantic Markdown/JSON block","visual confirmation required")
 if any(x is None for x in boundaries): return boundaries,rows
 if any(a>b for a,b in zip(boundaries,boundaries[1:])):
  raise RuntimeError("non-increasing Markdown page boundaries")
 return boundaries,rows

def target_for_page(page):
 if page<14:return "00_front_matter.md",None,None
 if page>=240:return "99_afterword.md",None,None
 selected=CHAPTERS[0]
 for ch in CHAPTERS:
  if ch[1]<=page:selected=ch
  else:break
 n,_,title=selected; return f"{n:02d}_chapter_{n:02d}.md",n,title

def structural_header(page):
 for b in page.get("para_blocks") or []:
  box=b.get("bbox") or []
  if block_text(b)==HEADER and len(box)==4 and box[1]<90 and box[0]<20:return True
 return False

def normalize_chapter_heading(text,n,title,page_id):
 lines=text.splitlines(); hits=[]
 accepted={str(n),title,f"{n} {title}"}
 for i,line in enumerate(lines):
  m=re.match(r"^#{1,6}\s+(.+?)\s*$",line)
  if m and m.group(1) in accepted:hits.append(i)
 if not hits:return text,False
 first=hits[0]; lines[first]=f"<!-- FB-H-CH{n:02d} | source-page={page_id} -->\n# {n} {title}"
 for i in reversed(hits[1:]):del lines[i]
 return "\n".join(lines),True

def clean_segment(segment,page,page_num,image_by_url,footnotes):
 page_id=f"FB-P{page_num:03d}"; target,n,title=target_for_page(page_num)
 if structural_header(page):
  segment=re.sub(rf"^(?:#{{1,6}}\s+)?{re.escape(HEADER)}\s*\n?", "", segment, count=1, flags=re.M)
 if n and page_num==next(x[1] for x in CHAPTERS if x[0]==n):
  segment,ok=normalize_chapter_heading(segment,n,title,page_id)
  if not ok: segment=f"<!-- TODO(QA): chapter heading normalization unresolved for {page_id} -->\n"+segment
 def replace_image(m):
  item=image_by_url[m.group(1)]
  return (f"<!-- {item['image_id']} | source-page={page_id} | json-block={item['json_block_index']} | "
          f"bbox={item['json_bbox']} -->\n![image]({item['local_relative_from_chapters']})")
 segment=URL_RE.sub(replace_image,segment)
 if "The OCR result should be empty" in segment:
  segment=segment.replace("The OCR result should be empty", "<!-- TODO(QA): parser/instruction leakage candidate; preserve pending visual review. -->\n\nThe OCR result should be empty",1)
 if "Document generated by Anna's Archive" in segment:
  segment=segment.replace("Document generated by Anna's Archive", "<!-- TODO(QA): external archive metadata candidate; preserve pending visual review. -->\n\nDocument generated by Anna's Archive",1)
 if re.search(r"(?m)^Qiji\s*$",segment):
  segment=re.sub(r"(?m)^Qiji\s*$", "<!-- TODO(QA): `Qiji` may be an OCR/layout artifact for the afterword heading; do not correct without visual review. -->\n\nQiji",segment,count=1)
 comments=[]
 for f in footnotes:
  comments.append(f"<!-- {f['footnote_id']} | source-page={page_id} | marker={f['marker_candidates']} | status=manual-review-required -->")
 marker=f"<!-- {page_id} | part={page_num if False else ''}"  # completed below for readability
 marker=f"<!-- {page_id} | input-pdf-page={page_num} | printed-page={printed(page)} -->"
 body=segment.strip()
 if not body and not anchors(page):
  body="<!-- TODO(QA): no Markdown/JSON semantic payload; blank-page visual confirmation required. -->"
 if comments: body += "\n\n"+"\n".join(comments)
 return target,marker+"\n\n"+body+"\n"

def printed(page):
 vals=[]
 for b in page.get("discarded_blocks") or []:
  text=block_text(b); box=b.get("bbox") or []
  if b.get("type")=="page_number" and re.fullmatch(r"\d{1,3}",text) and len(box)==4 and box[1]>=750:vals.append(text)
 return vals[0] if len(set(vals))==1 else "Unknown"

def read_csv(path):
 with path.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))

def main():
 image_by_url={r["mineru_url"]:r for r in read_csv(QA/"full_book_image_map.csv")}
 foot_by_page={}
 for r in read_csv(QA/"full_book_footnote_map.csv"):foot_by_page.setdefault(int(r["input_pdf_page"]),[]).append(r)
 docs={}; alignment=[]
 for name,first,last in PARTS:
  root=RAW/name; md=(root/"source.md").read_text(encoding="utf-8")
  pages=json.loads((root/"source.json").read_text(encoding="utf-8"))["pdf_info"]
  bounds,rows=align_part(md,pages)
  for local,(status,evidence,anchor) in enumerate(rows):
   alignment.append(dict(source_page_id=f"FB-P{first+local:03d}",part=name,local_page_idx=local,
      input_pdf_page=first+local,status=status,json_anchor_block=evidence,anchor_text=anchor,
      markdown_offset="" if bounds[local] is None else bounds[local]))
  if any(x is None for x in bounds):continue
  bounds.append(len(md))
  for local,page in enumerate(pages):
   page_num=first+local; segment=md[bounds[local]:bounds[local+1]]
   target,clean=clean_segment(segment,page,page_num,image_by_url,foot_by_page.get(page_num,[]))
   docs.setdefault(target,[]).append(clean)
 fields=["source_page_id","part","local_page_idx","input_pdf_page","status","json_anchor_block","anchor_text","markdown_offset"]
 with (QA/"full_book_markdown_alignment.csv").open("w",encoding="utf-8-sig",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(alignment)
 unresolved=[r for r in alignment if r["status"]=="unresolved"]
 if unresolved:raise RuntimeError(f"unresolved Markdown page alignments: {len(unresolved)}")
 expected={"00_front_matter.md","99_afterword.md"}|{f"{n:02d}_chapter_{n:02d}.md" for n,_,_ in CHAPTERS}
 if set(docs)!=expected:raise RuntimeError(f"missing output files: {sorted(expected-set(docs))}")
 OUT.mkdir(parents=True,exist_ok=True)
 preface=("<!--\nStage 4A non-destructive cleaned source. Text comes from full-book MinerU Markdown.\n"
          "JSON supplies page/block/layout evidence; DOCX supplies images only.\n"
          "No translation, prose rewriting, OCR correction, factual correction, or unattended footnote recovery.\n-->\n\n")
 for name,parts in docs.items():(OUT/name).write_text(preface+"\n".join(parts).rstrip()+"\n",encoding="utf-8")
 print(json.dumps({"files":len(docs),"aligned_pages":len(alignment),"blank_candidates":sum(r["status"]=="blank-candidate" for r in alignment),"unresolved":len(unresolved)},ensure_ascii=False))

if __name__=="__main__":main()
