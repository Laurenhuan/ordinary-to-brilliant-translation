#!/usr/bin/env python3
"""Assign stable logical paragraph IDs to Stage 4A cleaned source files."""
from __future__ import annotations

import json, re
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]; ROOT=REPO/"source"/"chapters"
FILES=[ROOT/"00_front_matter.md"]+[ROOT/f"{n:02d}_chapter_{n:02d}.md" for n in range(1,29)]+[ROOT/"99_afterword.md"]
ID_RE=re.compile(r"^<!-- (?:FM|AW|CH\d{2})-P\d{3} -->\n",re.M)

def prefix(path):
 if path.name=="00_front_matter.md":return "FM"
 if path.name=="99_afterword.md":return "AW"
 return "CH"+path.name[:2]

def is_prose(block):
 stripped=block.strip()
 if not stripped:return False
 if stripped.startswith("<!--"):return False
 if stripped.startswith("#"):return False
 if stripped.startswith("!["):return False
 if re.match(r"^\[\^[^\]]+\]:",stripped):return False
 return True

def main():
 counts={}
 for path in FILES:
  if not path.is_file():raise FileNotFoundError(path)
  text=ID_RE.sub("",path.read_text(encoding="utf-8"))
  blocks=re.split(r"\n{2,}",text.strip()); out=[]; n=0; pfx=prefix(path)
  for block in blocks:
   if is_prose(block):
    n+=1; block=f"<!-- {pfx}-P{n:03d} -->\n{block}"
   out.append(block)
  path.write_text("\n\n".join(out).rstrip()+"\n",encoding="utf-8");counts[path.name]=n
 print(json.dumps({"files":len(FILES),"paragraph_ids":sum(counts.values()),"by_file":counts},ensure_ascii=False))

if __name__=="__main__":main()
