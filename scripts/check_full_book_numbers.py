#!/usr/bin/env python3
"""Compare raw/cleaned numeric tokens page-by-page after removing metadata."""
from __future__ import annotations

import csv, json, re
from collections import Counter
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]; QA=REPO/"qa"; RAW=REPO/"source"/"raw"/"full_book"; CH=REPO/"source"/"chapters"
PARTS=(("part_001_200",1),("part_201_243",201)); RECOVERED={26:"3",34:"4",74:"9",136:"15",166:"18"}
COMMENT_RE=re.compile(r"(?s)<!--.*?-->"); IMAGE_RE=re.compile(r"(?m)^!\[[^\]]*\]\([^\r\n]+\)\s*$")
DEF_RE=re.compile(r"(?m)^\[\^[^\]]+\]:.*$"); REF_RE=re.compile(r"\[\^[^\]]+\]"); NUMBER_RE=re.compile(r"\d+(?:[.,]\d+)*")

def cleaned(text):
 text=COMMENT_RE.sub("",text);text=IMAGE_RE.sub("",text);text=DEF_RE.sub("",text);text=REF_RE.sub("",text)
 return Counter(NUMBER_RE.findall(text))

def read_csv(path):
 with path.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))

def main():
 align=read_csv(QA/"full_book_markdown_alignment.csv"); raw_pages={}
 for name,first in PARTS:
  md=(RAW/name/"source.md").read_text(encoding="utf-8")
  rows=[r for r in align if r["part"]==name]; offsets=[int(r["markdown_offset"]) for r in rows]+[len(md)]
  for i,row in enumerate(rows):raw_pages[int(row["input_pdf_page"])]=md[offsets[i]:offsets[i+1]]
 clean_pages={}
 files=[CH/"00_front_matter.md"]+[CH/f"{n:02d}_chapter_{n:02d}.md" for n in range(1,29)]+[CH/"99_afterword.md"]
 marker=re.compile(r"<!-- FB-P(\d{3}) \|[^>]*-->")
 for path in files:
  text=path.read_text(encoding="utf-8"); matches=list(marker.finditer(text))
  for i,m in enumerate(matches):clean_pages[int(m.group(1))]=text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)]
 rows=[]
 for page in range(1,244):
  raw=cleaned(raw_pages[page]); out=cleaned(clean_pages[page]); missing=raw-out; added=out-raw
  status="exact"
  note=""
  if missing or added:
   if page in RECOVERED and not missing and added==Counter({RECOVERED[page]:1}):
    status="approved structural chapter-number recovery";note="Chapter number recovered from TOC, sequence, chapter-opening template, and JSON title evidence."
   else:status="manual review required"
  rows.append(dict(source_page_id=f"FB-P{page:03d}",input_pdf_page=page,raw_numeric_tokens="|".join(raw.elements()),
   cleaned_numeric_tokens="|".join(out.elements()),missing_from_cleaned="|".join(missing.elements()),
   added_in_cleaned="|".join(added.elements()),status=status,note=note))
 fields=list(rows[0]);
 with (QA/"full_book_numeric_check.csv").open("w",encoding="utf-8-sig",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 print(json.dumps(dict(pages=len(rows),exact=sum(r["status"]=="exact" for r in rows),
  approved_recoveries=sum(r["status"].startswith("approved") for r in rows),
  manual_review=sum(r["status"]=="manual review required" for r in rows)),ensure_ascii=False))

if __name__=="__main__":main()
