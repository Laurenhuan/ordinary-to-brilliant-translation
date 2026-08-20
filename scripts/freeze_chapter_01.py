#!/usr/bin/env python3
"""Freeze Chapter 1 only after exact Pilot 01/full-book source validation."""
from __future__ import annotations

import hashlib, json, re
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]
FULL=REPO/"source"/"chapters"/"01_chapter_01.md"
PILOT=REPO/"source"/"chapters"/"pilot_01_cleaned.md"

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def normalize(text):
 text=re.sub(r"(?s)<!--.*?-->","",text)
 text=re.sub(r"(?m)^!\[[^\]]*\]\([^\r\n]+\)\s*$","",text)
 text=re.sub(r"(?m)^\[\^[^\]]+\]:.*$","",text)
 text=re.sub(r"\[\^[^\]]+\]","",text)
 text=re.sub(r"\$?\^\{[①②③④⑤⑥⑦⑧⑨⑩]\}\$?","",text)
 text=re.sub(r"(?m)^#+\s*","",text)
 return re.sub(r"\s+","",text)

def replace_once(text,old,new):
 if text.count(old)!=1:raise RuntimeError(f"expected one occurrence, found {text.count(old)}: {old[:60]}")
 return text.replace(old,new,1)

def main():
 full=FULL.read_text(encoding="utf-8")
 pilot=PILOT.read_text(encoding="utf-8")
 m=re.search(r"(?ms)^# 1 大地主的儿子和贫农的儿子.*?(?=^# 2 )",pilot)
 if not m:raise RuntimeError("Pilot 01 Chapter 1 segment not found")
 pnorm=normalize(m.group(0)); fnorm=normalize(full)
 if pnorm!=fnorm:raise RuntimeError("Pilot 01 and full-book Chapter 1 normalized text differ")
 pairs=(("image_002.jpg","image_004.jpg"),("image_003.jpg","image_005.jpg"))
 for pilot_name,full_name in pairs:
  if digest(REPO/"source"/"raw"/"pilot_01"/"images"/pilot_name)!=digest(REPO/"source"/"raw"/"full_book"/"part_001_200"/"images"/full_name):
   raise RuntimeError(f"Chapter 1 image mismatch: {pilot_name} vs {full_name}")
 full=replace_once(full,"Stage 4A non-destructive cleaned source. Text comes from full-book MinerU Markdown.",
  "Canonical Source — Frozen for Translation v1.\nStage 4A non-destructive cleaned source. Text comes from full-book MinerU Markdown.")
 proper_name="日立集团的小源浪平连小学都没毕业"
 if full.count(proper_name)!=2:raise RuntimeError(f"expected two repeated proper-name occurrences, found {full.count(proper_name)}")
 full=full.replace(proper_name,"日立集团的小源浪平<!-- TODO(QA): Verify this proper-name glyph against the authorized PDF; preserve the source form until confirmed. -->连小学都没毕业")
 full=replace_once(full,"庆尚南道 $^{①}$ 宜宁","庆尚南道[^FB-F002]宜宁")
 full=replace_once(full,"朝鲜末期 $^{①}$ 的著名书法家","朝鲜末期[^FB-F003]的著名书法家")
 full=replace_once(full,"<!-- FB-F002 | source-page=FB-P015 | marker=① | status=manual-review-required -->","")
 full=replace_once(full,"<!-- FB-F003 | source-page=FB-P016 | marker=① | status=manual-review-required -->","")
 join_pattern=(r"李秉哲也时常引经据典。他也是在私塾时就达到了通读\s*"
               r"(<!-- FB-P017 \| input-pdf-page=17 \| printed-page=4 -->)\s*"
               r"《千字文》乃至《论语》的水平。")
 full,joins=re.subn(join_pattern,r"李秉哲也时常引经据典。他也是在私塾时就达到了通读\1《千字文》乃至《论语》的水平。",full)
 if joins!=1:raise RuntimeError(f"expected one approved cross-page join, found {joins}")
 full=full.rstrip()+("\n\n<!-- FB-F002 | source-page=FB-P015 | marker=① | status=approved-pilot-01 -->\n"
  "<!-- FB-F003 | source-page=FB-P016 | marker=① | status=approved-pilot-01 -->\n\n"
  "[^FB-F002]: 韩国的“道”相当于中国“省”一级的行政单位。\n"
  "[^FB-F003]: 19世纪末20世纪初。\n")
 FULL.write_text(full,encoding="utf-8")
 print(json.dumps({"status":"Canonical Source — Frozen for Translation v1","normalized_chars":len(fnorm),
  "normalized_sha256":hashlib.sha256(fnorm.encode()).hexdigest(),"images_verified":2,"footnotes_restored":2},ensure_ascii=False))

if __name__=="__main__":main()
