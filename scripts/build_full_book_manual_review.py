#!/usr/bin/env python3
"""Generate the concise Stage 4A manual-review register."""
from __future__ import annotations

import csv, json
from pathlib import Path

REPO=Path(__file__).resolve().parents[1]; QA=REPO/"qa"

def read_csv(path):
 with path.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))

def esc(value):return str(value).replace("|","\\|").replace("\n"," ").strip()

def main():
 rows=[]; rid=1
 for page in (49,83,109,145,161,165,197,227):
  rows.append(dict(id=f"FB-R{rid:03d}",page=f"FB-P{page:03d}",category="blank-page candidate",risk="Medium",
   raw="No semantic Markdown/JSON para block; page mapping retained.",cleaned="Page marker plus TODO only.",
   recommendation="Compare the authorized PDF page visually. Approve blank only if it contains no semantic content."));rid+=1
 for page in (91,135,177,237):
  rows.append(dict(id=f"FB-R{rid:03d}",page=f"FB-P{page:03d}",category="parser/instruction leakage candidate",risk="High",
   raw="English OCR instruction text appears in MinerU Markdown/JSON.",cleaned="Preserved with TODO; not silently removed.",
   recommendation="Confirm against the authorized PDF. Remove from cleaned source only if absent from the book."));rid+=1
 rows.append(dict(id=f"FB-R{rid:03d}",page="FB-P240",category="afterword heading / OCR",risk="High",
  raw="`Qiji`; JSON also contains discarded `后记` header evidence.",cleaned="`Qiji` preserved with TODO.",
  recommendation="Use the authorized PDF to determine whether `Qiji` is source text, OCR noise, or the stylized afterword heading."));rid+=1
 rows.append(dict(id=f"FB-R{rid:03d}",page="FB-P243",category="external archive metadata",risk="Medium",
  raw="Anna's Archive / DuXiu generation notice.",cleaned="Preserved in 99_afterword.md with TODO.",
  recommendation="Confirm whether this non-book wrapper page should remain outside canonical book content."));rid+=1
 footnotes=read_csv(QA/"full_book_footnote_map.csv")
 transferred={"FB-F002","FB-F003","FB-F004"}
 for f in footnotes:
  if f["footnote_id"] in transferred:continue
  rows.append(dict(id=f"FB-R{rid:03d}",page=f["source_page_id"],category=f"footnote validation ({f['footnote_id']})",risk="Medium",
   raw=f"marker candidate={f['marker_candidates']}; JSON body={f['footnote_body']}",
   cleaned="Body not restored into authoritative cleaned source.",
   recommendation="Confirm marker-to-body mapping and insertion point, then explicitly approve or reject restoration."));rid+=1
 if rid!=61:raise RuntimeError(f"expected 60 open review items, generated {rid-1}")
 lines=["# Full-book Manual Review","","Stage: Stage 4A — Full-book Source Ingestion","",
  "This register contains only unresolved decisions that cannot be safely completed from MinerU data alone. Raw files remain unchanged. No item authorizes translation, OCR correction, factual correction, inferred captions, or duplicate deletion.","",
  "## Summary","",f"- Open review items: {len(rows)}","- Medium risk: 55","- High risk: 5",
  "- Footnotes detected: 49; 3 exact Pilot 01 matches already have human approval; 46 remain open here.",
  "- Chapter-opening mismatches: 0","- Unmapped images: 0","- Unexplained numeric mismatches: 0","",
  "## Open items","",
  "| Review ID | Page | Category | Risk | Raw state | Cleaned state | Codex recommendation | Human decision | Human note | Status |",
  "|---|---|---|---|---|---|---|---|---|---|"]
 for r in rows:
  lines.append("| {id} | {page} | {category} | {risk} | {raw} | {cleaned} | {recommendation} |  |  | open |".format(**{k:esc(v) for k,v in r.items()}))
 lines += ["","## Previously approved footnote mappings reused by exact evidence match","",
  "| Full-book footnote ID | Page | Prior approval | Current treatment |","|---|---|---|---|",
  "| FB-F002 | FB-P015 | Pilot 01 R007–R009 footnote class | Restored in frozen Chapter 1 |",
  "| FB-F003 | FB-P016 | Pilot 01 R007–R009 footnote class | Restored in frozen Chapter 1 |",
  "| FB-F004 | FB-P020 | Pilot 01 R007–R009 footnote class | Mapping recognized; Chapter 2 is not frozen in this stage |","",
  "The three historical Pilot review IDs remain unchanged; the FB-F IDs are full-book mapping identifiers, not replacements for Pilot history.",""]
 (QA/"full_book_manual_review.md").write_text("\n".join(lines),encoding="utf-8")
 print(json.dumps({"open_review_items":len(rows),"medium":55,"high":5,"open_footnotes":46},ensure_ascii=False))

if __name__=="__main__":main()
