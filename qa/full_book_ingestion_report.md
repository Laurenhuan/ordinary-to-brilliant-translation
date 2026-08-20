# Full-book Source Ingestion Report

Stage: Stage 4A — Full-book Source Ingestion  
Translation status: Not started

## Executive result

The two MinerU batches supplied as input PDF pages 1–200 and 201–243 were preserved separately and ingested without modifying their bytes. Together they contain 243 JSON pages. All pages were mapped, all 59 Markdown/JSON/DOCX images were uniquely localized, front matter, Chapters 1–28, and the afterword were identified, and 30 cleaned source files were generated.

Chapter 1 passed the Pilot 01/full-book comparison and is frozen separately as `Canonical Source — Frozen for Translation v1`. The rest of the book is structurally split but is not frozen and has not entered translation.

## Raw input overview

| Batch | File | Bytes | MiB | SHA-256 | GitHub-size assessment |
|---|---|---:|---:|---|---|
| part_001_200 | source.md | 314,884 | 0.300 | `8e7d1cb6a7c178d74b21071dfe63e9807d4a41b98392d7c9f76da39dad217494` | Suitable for ordinary Git |
| part_001_200 | source.json | 5,545,676 | 5.289 | `23523bdecaf53529177b0f25c0e47a5817fc953a6d69079c483f2938ef24da13` | Suitable for ordinary Git |
| part_001_200 | source.docx | 692,572 | 0.660 | `66da38b6bbf4852a82e958a9be586f28e87f8785e0b65e7e2dae18874e240771` | Suitable for ordinary Git |
| part_201_243 | source.md | 70,528 | 0.067 | `2d72e16fd56f88c280496c9547275b67d2f05fb2212ef8af8787ccf0990ee5a0` | Suitable for ordinary Git |
| part_201_243 | source.json | 963,897 | 0.919 | `b7651c2d2e60116d1e808a967d0338e9b05b575141a27bb5d3a0797b99330572` | Suitable for ordinary Git |
| part_201_243 | source.docx | 108,742 | 0.104 | `b2bb311208d9ffd40eee7b6ab3cf5ba4ab06d006b096ca0b0be7aeefb2ef71ab` | Suitable for ordinary Git |

No original copyright PDF was added. No file approaches GitHub's ordinary single-file limit, and Git LFS was not enabled.

## Evidence roles and preservation

- MinerU Markdown remained the primary text layer.
- JSON supplied local `page_idx`, block order/type, bbox, discarded headers/page numbers, image blocks, and footnote candidates.
- DOCX supplied byte-for-byte `word/media` images and document relationship order only. DOCX-derived text was not used to overwrite Markdown.
- The two raw batches were not concatenated or rewritten. Global IDs `FB-P001`–`FB-P243` are an additional mapping layer based on the input page ranges supplied by the project lead.

## Page and block mapping

- Total MinerU JSON pages: 243
- Mapped pages: 243 (100%)
- Part 1 local `page_idx`: 0–199 → input PDF pages 1–200
- Part 2 local `page_idx`: 0–42 → input PDF pages 201–243
- Reliable printed-page values: 197
- Printed page `Unknown`: 46
- Markdown page alignments: 243
- Zero-semantic-block blank-page candidates: 8

The complete machine-readable records are in `qa/full_book_page_map.csv` and `qa/full_book_markdown_alignment.csv`. Printed pages were recorded only from bottom-positioned JSON `page_number` evidence; missing values were not inferred from the table of contents.

## Image localization

- Markdown image URLs: 59
- JSON image blocks: 59
- DOCX images in document order: 59
- Extracted local images: 59
- Verified one-to-one mappings: 59
- Unmapped or ambiguous images: 0
- Modified, recompressed, resized, or caption-invented images: 0

All 28 chapter-opening pages contain exactly two mapped character illustrations. The remaining three images belong to front matter. Detailed mappings are in `qa/full_book_image_map.csv` and each part's `images/image_map.csv`.

## Book structure

- Front matter: input PDF pages 1–13
- Table of contents: input PDF pages 12–13
- Chapters detected: 1–28, continuous
- Missing chapters: 0
- Duplicate chapter headings: 0
- Chapter-title mismatches against the TOC and opening evidence: 0
- Afterword: input PDF pages 240–242
- External archive-metadata candidate: input PDF page 243, preserved pending review
- Canonical/candidate source files generated: 28 chapter files plus front matter and afterword

Every chapter opening passed the approved template check: one logical chapter heading, an introductory text block, and two character illustrations. Five chapter numbers absent from the MinerU heading text were recovered through the approved multi-signal rule:

| Anomaly ID | Chapter | Input PDF page | Evidence | Status |
|---|---:|---:|---|---|
| FB-A013 | 3 | 26 | TOC title/number, chapter sequence, opening template, JSON title position | Resolved by Approved rule |
| FB-A014 | 4 | 34 | Same evidence class | Resolved by Approved rule |
| FB-A015 | 9 | 74 | Same evidence class | Resolved by Approved rule |
| FB-A016 | 15 | 136 | Same evidence class | Resolved by Approved rule |
| FB-A017 | 18 | 166 | Same evidence class | Resolved by Approved rule |

## Cleaning actions and checks

| Check/action | Result |
|---|---|
| Confirmed running-header removal | 85 Markdown header occurrences removed using repeated text plus top-edge JSON bbox evidence |
| JSON-discarded header evidence retained in mapping | 145 blocks |
| Cross-page paragraph reconstruction | 1, Chapter 1 only; previously approved in Pilot 01 |
| Blank pages | 8 candidates preserved with TODO; none silently declared blank without visual review |
| Parser/instruction leakage | 4 candidates detected; 0 removed pending PDF visual confirmation |
| Empty parser blocks | 8 zero-semantic page candidates retained in telemetry and source markers |
| Chapter numbers recovered | 5, under the approved multi-signal rule |
| Numeric raw/cleaned comparison | 238 pages exact; 5 pages differ only by approved chapter-number recovery; 0 unexplained mismatches |
| Known OCR/proper-name warning | `小源浪平`, source form preserved; translation terminology verification remains pending |
| Duplicate-text warning | Chapter 1 opening repetition preserved under the previously approved authorial/layout decision |
| Duplicate deletion | 0 |
| Factual correction | 0 |
| Translation or Chinese rewriting | 0 |

The numeric audit is recorded in `qa/full_book_numeric_check.csv`.

## Footnotes

- JSON `page_footnote` blocks: 49
- Exact Pilot 01 mappings with existing human approval: 3 (`FB-F002`, `FB-F003`, `FB-F004`)
- Restored in frozen Chapter 1: 2 (`FB-F002`, `FB-F003`)
- Still open for human validation: 46

No unapproved footnote body was inserted into authoritative cleaned source. Candidate evidence is in `qa/full_book_footnote_map.csv`; open decisions are in `qa/full_book_manual_review.md`.

## New anomaly register

Nineteen non-footnote anomalies were recorded: five resolved and fourteen unresolved.

| IDs | Count | Category | Current treatment |
|---|---:|---|---|
| FB-A001–FB-A008 | 8 | Zero-semantic-block / blank-page candidates at FB-P049, P083, P109, P145, P161, P165, P197, P227 | Page marker and TODO preserved; visual review required |
| FB-A009–FB-A012 | 4 | Parser/instruction leakage candidates at FB-P091, P135, P177, P237 | Text preserved with TODO; visual review required |
| FB-A013–FB-A017 | 5 | Missing chapter numbers 3, 4, 9, 15, 18 | Resolved using approved structural evidence rule |
| FB-A018 | 1 | `Qiji` / afterword-heading uncertainty at FB-P240 | Preserved with TODO; visual review required |
| FB-A019 | 1 | External archive metadata at FB-P243 | Preserved with TODO; scope decision required |

## Manual review load

- Open review items: 60
- High risk: 5
- Medium risk: 55
- Open footnote validations: 46
- Other open items: 8 blank-page candidates, 4 parser-leakage candidates, 1 afterword-heading issue, and 1 archive-metadata scope issue

Normal pages, mapped images, confirmed chapter openings, resolved chapter-number recoveries, and exact numeric pages were not turned into manual-review items.

## Reproducibility

The repository includes scripts for raw inventory/image extraction, Markdown page alignment/chapter splitting, Chapter 1 freeze validation, stable paragraph IDs, numeric comparison, and manual-review generation. Raw files remain immutable; regenerated cleaned files must be reviewed through Git diff before acceptance.

## Recommendation

MinerU remains suitable as the full-book structural extraction layer because all 243 pages mapped, all 59 images cross-mapped, and Chapters 1–28 were found without missing or duplicate chapters. It is not suitable for unattended final source production: all footnotes, ambiguous blank pages, parser leakage, OCR/proper names, and afterword/rear-matter uncertainties still require human review.

Stage 4A source ingestion can be considered structurally complete. The project may proceed immediately to **Chapter 1 Translation Preparation only**, using the frozen Chapter 1 and its terminology candidates. Do not begin full-book translation or treat Chapters 2–28 as frozen.
