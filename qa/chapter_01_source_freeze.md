# Chapter 1 Source Freeze

Status: **Canonical Source — Frozen for Translation v1**  
Stage: Chapter 1 Fast Track within Stage 4A  
Translation status: Not started

## Freeze decision

Chapter 1 is frozen because the Pilot 01 and full-book MinerU parses contain the same Chinese正文 after removing source markers, image syntax, footnote syntax, and whitespace-only formatting differences.

- Normalized Chinese text length: 1,513 characters
- Pilot 01 normalized SHA-256: `7076688964bfa2729a9fd24252da1019d4adbfb45d394553226070fc3eb171a8`
- Full-book normalized SHA-256: `7076688964bfa2729a9fd24252da1019d4adbfb45d394553226070fc3eb171a8`
- Normalized text equality: Exact
- Chapter-opening image equality: 2/2 byte-identical
- Unresolved high-risk chapter-boundary or content-loss issue: None

Frozen means the Chinese正文 in `source/chapters/01_chapter_01.md` must not be silently changed. A future source correction requires a QA record, evidence, and an explicit reviewed commit.

## Boundaries

| Boundary | Full-book evidence |
|---|---|
| Start | FB-P014, input PDF page 14; chapter-opening title block; printed page Unknown |
| End | End of FB-P017, input PDF page 17; printed page 4 |
| Next chapter | FB-P018 begins Chapter 2 with separate number and title blocks |

The table of contents, JSON title blocks, chapter-opening template, sequential chapter evidence, and Markdown order all agree on this boundary.

## Pilot 01 versus full-book parse

| Area | Comparison | Adopted treatment |
|---|---|---|
| Chapter heading | Same wording and chapter number | One logical `# 1` heading with `FB-H-CH01` marker |
| Introductory prose | Same text and order | Preserve both opening-page text fragments around the two images |
| Body paragraph order | Exact after normalization | Full-book Markdown order retained |
| Images | Pilot `image_002.jpg` = full-book `FB-I004`; Pilot `image_003.jpg` = full-book `FB-I005`, byte-identical | Use full-book local relative paths and global image IDs |
| Footnotes | Full-book Markdown omits bodies that JSON retains; Pilot 01 already restored and human-approved the two Chapter 1 notes | Restore as `FB-F002` and `FB-F003` in the frozen source |
| Running headers | Same repeated source artifact pattern | Remove only occurrences supported by top-edge/repeated JSON evidence |
| Page breaks | Same sequence; full-book uses global page IDs | Use FB-P014–FB-P017; preserve the FB-P017 marker inline at the approved cross-page join |
| Repeated prose | Same repetition in both parses | Preserve; prior human review confirmed original authorial/layout design |
| Numbers | Same正文数字 after metadata removal | No numeric correction; page-level check is exact |
| Chapter boundary | Same start/end content | Freeze FB-P014 through FB-P017 only |

## Image mapping

| Image ID | Full-book local file | Page / JSON evidence | Pilot match |
|---|---|---|---|
| FB-I004 | `source/raw/full_book/part_001_200/images/image_004.jpg` | FB-P014, block 1, bbox 169:336:207:393 | Pilot `image_002.jpg`, SHA-256 identical |
| FB-I005 | `source/raw/full_book/part_001_200/images/image_005.jpg` | FB-P014, block 3, bbox 408:332:448:395 | Pilot `image_003.jpg`, SHA-256 identical |

The images are logical chapter-opening illustrations without invented captions. Their original left/right positions remain in JSON bbox metadata.

## Footnote status

| Footnote ID | Page | Body | Status |
|---|---|---|---|
| FB-F002 | FB-P015 | 韩国的“道”相当于中国“省”一级的行政单位。 | Approved in Pilot 01 footnote-validation class; restored |
| FB-F003 | FB-P016 | 19世纪末20世纪初。 | Approved in Pilot 01 footnote-validation class; restored |

No new unattended footnote approval is inferred from this freeze.

## Source warnings that do not block the freeze

- `小源浪平` is preserved exactly as extracted and marked for visual/proper-name verification. It is not auto-corrected. The uncertainty affects terminology verification, not Chapter 1 structural completeness.
- The chapter-opening prose repetition is intentionally retained under the approved high-risk duplicate-preservation rule.
- No factual claim, date, amount, unit, or proper name was corrected from outside knowledge.

## Stable IDs

Chapter 1 has stable logical paragraph IDs `CH01-P001`–`CH01-P027`, page IDs `FB-P014`–`FB-P017`, heading ID `FB-H-CH01`, image IDs `FB-I004`–`FB-I005`, and footnote IDs `FB-F002`–`FB-F003`. Translation preparation must preserve the source-to-translation segment relationship.

## Files for the next step

Chapter 1 Translation Preparation may use:

- `source/chapters/01_chapter_01.md`
- `qa/chapter_01_source_freeze.md`
- `glossary/chapter_01_candidates.csv`

This report does not authorize starting English正文 in the current stage.
