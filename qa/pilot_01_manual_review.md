# Pilot 01 Manual Review

Stage: Stage 2B — Pilot Manual Validation

Status: Awaiting project-lead review

Purpose: provide a concise checklist for comparing MinerU raw output, JSON structure, DOCX layout evidence, and the current cleaned Markdown against the authorized PDF. This file records proposed human decisions; it does not approve any cleaning rule.

Evidence priority:

1. Authorized PDF visual source for human confirmation
2. source/raw/pilot_01/source.md as the primary MinerU text
3. source/raw/pilot_01/source.json for page, block, order, type, bbox, and discarded elements
4. source/raw/pilot_01/source.docx for embedded images and layout fallback only
5. source/chapters/pilot_01_cleaned.md as the current non-destructive cleaned proposal

DOCX-derived text must not overwrite source.md. The current DOCX footnotes.xml contains no usable footnote body, so the three restored footnote bodies rely on JSON evidence and still require PDF confirmation.

## Review summary

| Risk | Count |
|---|---:|
| Low | 1 |
| Medium | 12 |
| High | 12 |
| Total | 25 |

For every item, select exactly one decision and add a note when rejecting or requesting discussion.

## Page Mapping

Pilot Page is the 1-based review sequence. MinerU page_idx is the zero-based identifier in source.json. The original PDF physical page index is not present in the available MinerU artifacts and is therefore marked Unknown. Printed page numbers are included only when JSON contains a page_number block.

| Pilot Page | MinerU page_idx | PDF physical page | Printed page | Chapter/section | Important blocks |
|---:|---:|---|---:|---|---|
| 1 | 0 | Unknown | 6 | Preface/body | para 0 suspected running header; paras 1–12 body; discarded 13 page number |
| 2 | 1 | Unknown | 7 | Preface/body | paras 1–8 body; para 9 section title; discarded 0 header and 13 page number |
| 3 | 2 | Unknown | 9 | Contents | image 1; title 2; text 3–4; discarded 0 header and 5 page number |
| 4 | 3 | Unknown | 10 | Contents continuation | para 0 contents; discarded 1 page number |
| 5 | 4 | Unknown | Unknown | Chapter 1 opener | title 0; images 1 and 3; lead text 2, 4, 5 |
| 6 | 5 | Unknown | 2 | Chapter 1 | para 0 suspected running header; footnote discarded 13; page number discarded 14 |
| 7 | 6 | Unknown | 3 | Chapter 1 | para 11 cross-page fragment; discarded headers 0–1; footnote 12; page number 13 |
| 8 | 7 | Unknown | 4 | Chapter 1 continuation | para 0 suspected running header; para 1 continuation; discarded 5 page number |
| 9 | 8 | Unknown | Unknown | Chapter 2 opener | number title 0; chapter title 1; images 2 and 4 |
| 10 | 9 | Unknown | 6 | Chapter 2 | para 0 suspected running header; numeric blocks 1, 6, 8–10, 12; discarded 13 page number |
| 11 | 10 | Unknown | 7 | Chapter 2 | numeric/body blocks 2, 8, 12; truncated block 13; footnote 14; page number 15 |

Printed pages 6 and 7 occur in both front matter and Chapter 2, so printed page alone is not a unique pilot identifier.

## Image Mapping

All five local files exist and match the byte-for-byte DOCX extraction recorded in source/raw/pilot_01/README.md. No explicit caption was identified in Markdown, JSON, or DOCX. The role descriptions are observations, not captions.

| Local image | MinerU original image block | JSON page | Raw Markdown | DOCX media/order | Cleaned Markdown | Review focus |
|---|---|---:|---|---|---|---|
| image_001.jpg | block 1; bbox 135,207,194,280; CDN tail 153a2a…2617.jpg | 2 | line 51 | rId10.jpg; image paragraph 26; 1st | line 63 | Decorative contents image; count, position, no caption |
| image_002.jpg | block 1; bbox 169,336,207,393; CDN tail 51879b…f75f.jpg | 4 | line 91 | rId15.jpg; image paragraph 58; 2nd | line 107 | Chapter 1 left portrait; position and completeness |
| image_003.jpg | block 3; bbox 408,332,448,395; CDN tail 42b4f8…0687.jpg | 4 | line 96 | rId18.jpg; image paragraph 60; 3rd | line 112 | Chapter 1 right portrait; position and completeness |
| image_004.jpg | block 2; bbox 161,322,199,381; CDN tail de41be…6420.jpg | 8 | line 161 | rId25.jpg; image paragraph 92; 4th | line 175 | Chapter 2 left portrait; position and completeness |
| image_005.jpg | block 4; bbox 400,321,442,383; CDN tail 09fa20…20c4.jpg | 8 | line 166 | rId28.jpg; image paragraph 94; 5th | line 180 | Chapter 2 right portrait; position and completeness |

## Review Items

### Running headers

#### R001

- Review ID: R001
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 1; page_idx 0; printed page 6
- Block ID / JSON evidence: para 0; type title; level 2; bbox 2,59,221,80
- Issue type: Running header
- Raw state: line 1 contains heading text 从平凡走向辉煌.
- Cleaned state: text removed; page marker for page_idx 0 retained.
- Reason for change: top-edge placement and repetition on later body pages suggest a running header.
- Codex recommendation: Approve only if the PDF visually confirms it is not a body or section heading.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R002

- Review ID: R002
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 6; page_idx 5; printed page 2
- Block ID / JSON evidence: para 0; type title; level 2; bbox 4,44,217,67
- Issue type: Running header
- Raw state: line 103 contains heading text 从平凡走向辉煌.
- Cleaned state: text removed; page marker for page_idx 5 retained.
- Reason for change: top-left placement matches the repeating book header rather than the Chapter 1 body.
- Codex recommendation: Approve only after PDF visual confirmation.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R003

- Review ID: R003
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 8; page_idx 7; printed page 4
- Block ID / JSON evidence: para 0; type title; level 2; bbox 4,54,224,76
- Issue type: Running header
- Raw state: line 147 contains heading text 从平凡走向辉煌 between two sentence fragments.
- Cleaned state: header removed; fragments joined with an inline page marker.
- Reason for change: top-edge repetition and interruption of a grammatically continuous sentence suggest a running header.
- Codex recommendation: Review together with R006 and approve only after checking the PDF line break.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R004

- Review ID: R004
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 10; page_idx 9; printed page 6
- Block ID / JSON evidence: para 0; type text; bbox 5,48,222,69
- Issue type: Running header
- Raw state: line 171 contains unmarked text 从平凡走向辉煌.
- Cleaned state: text removed; page marker for page_idx 9 retained.
- Reason for change: the block sits at the same top-left position as other running headers, although JSON typed it as ordinary text.
- Codex recommendation: PDF visual verification is required because the JSON type is not header or title.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Chapter heading

#### R005

- Review ID: R005
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 9; page_idx 8; printed page Unknown
- Block ID / JSON evidence: para 0 is title level 2, bbox 287,97,315,127, text 2; para 1 is title level 1, bbox 145,139,455,170, text “海归”和离家出走的少年
- Issue type: Chapter 2 heading normalization
- Raw state: lines 157 and 159 are separate headings with different levels.
- DOCX evidence: text paragraphs 90 and 91 preserve the number and title as adjacent separate paragraphs.
- Cleaned state: line 173 combines them as one level-1 heading: # 2 “海归”和离家出走的少年.
- Reason for change: same-page adjacency and title hierarchy suggest a single chapter heading.
- Codex recommendation: Approve the merge only if the PDF visually presents the number and title as one chapter-heading unit.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Cross-page paragraph

#### R006

- Review ID: R006
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 7–8; page_idx 6–7; printed pages 3–4
- Block ID / JSON evidence: page_idx 6 para 11 ends 李秉哲也时常引经据典。他也是在私塾时就达到了通读; page_idx 7 para 0 is suspected header; page_idx 7 para 1 begins 《千字文》乃至《论语》的水平。
- Issue type: Cross-page paragraph reconstruction
- Raw state: lines 145, 147, and 149 form fragment / header / continuation.
- DOCX evidence: paragraphs 84, 85, and 86 preserve the same three-part sequence.
- Cleaned state: line 163 joins the sentence and places the page_idx 7 marker inline at the original boundary.
- Reason for change: the two text fragments form one grammatical sentence when the repeated top-edge text is treated as a header.
- Codex recommendation: Approve only after visually confirming the end of printed page 3 and beginning of printed page 4.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Footnotes

#### R007

- Review ID: R007
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 6; page_idx 5; printed page 2
- Block ID / JSON evidence: body para 3 contains the marker; discarded block 13 is page_footnote at bbox 113,769,393,787
- Issue type: Footnote recovery
- Raw state: line 109 contains $^{①}$ after 庆尚南道; source.md has no footnote body.
- JSON footnote: ① 韩国的“道”相当于中国“省”一级的行政单位。
- Cleaned state: marker becomes [^p005-1] and the JSON body is defined at line 239.
- Reason for change: one marker and one discarded footnote body occur on the same page.
- Codex recommendation: Mapping appears one-to-one, but approve only after confirming the printed marker and footnote body. DOCX supplies no usable footnote body.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R008

- Review ID: R008
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 7; page_idx 6; printed page 3
- Block ID / JSON evidence: body para 6 contains the marker; discarded block 12 is page_footnote at bbox 120,775,254,791
- Issue type: Footnote recovery
- Raw state: line 135 contains $^{①}$ after 朝鲜末期; source.md has no footnote body.
- JSON footnote: ① 19世纪末20世纪初。
- Cleaned state: marker becomes [^p006-1] and the JSON body is defined at line 240.
- Reason for change: one marker and one discarded footnote body occur on the same page.
- Codex recommendation: Mapping appears one-to-one, but approve only after PDF confirmation. DOCX supplies no usable footnote body.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R009

- Review ID: R009
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 11; page_idx 10; printed page 7
- Block ID / JSON evidence: body para 12 contains the marker; discarded block 14 is page_footnote at bbox 124,773,249,788
- Issue type: Footnote recovery
- Raw state: line 217 contains plain marker ① after 北间岛; source.md has no footnote body.
- JSON footnote: ① 现位于中国吉林省。
- Cleaned state: marker becomes [^p010-1] and the JSON body is defined at line 241.
- Reason for change: one marker and one discarded footnote body occur on the same page.
- Codex recommendation: Mapping appears one-to-one, but approve only after PDF confirmation. DOCX supplies no usable footnote body.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Images

#### R010

- Review ID: R010
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 3; page_idx 2; printed page 9
- Block ID / JSON evidence: image block 1; bbox 135,207,194,280; first Markdown/JSON image
- Issue type: Image mapping
- Raw state: line 51 uses CDN image tail 153a2a…2617.jpg.
- Cleaned state: line 63 uses ../raw/pilot_01/images/image_001.jpg.
- Reason for change: first DOCX image rId10 matches the first Markdown and JSON image order.
- Codex recommendation: Confirm image count, decorative position near 目录, and absence of a caption.
- Risk level: Low
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R011

- Review ID: R011
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 5; page_idx 4; printed page Unknown
- Block ID / JSON evidence: image block 1; bbox 169,336,207,393; second Markdown/JSON image
- Issue type: Image mapping
- Raw state: line 91 uses CDN image tail 51879b…f75f.jpg.
- Cleaned state: line 107 uses ../raw/pilot_01/images/image_002.jpg.
- Reason for change: DOCX rId15 is the second embedded image and occurs before the first lead-text fragment.
- Codex recommendation: Confirm left-side position, completeness, and whether any visible caption exists.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R012

- Review ID: R012
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 5; page_idx 4; printed page Unknown
- Block ID / JSON evidence: image block 3; bbox 408,332,448,395; third Markdown/JSON image
- Issue type: Image mapping
- Raw state: line 96 uses CDN image tail 42b4f8…0687.jpg.
- Cleaned state: line 112 uses ../raw/pilot_01/images/image_003.jpg.
- Reason for change: DOCX rId18 is the third embedded image and occurs between the two lead-text fragments.
- Codex recommendation: Confirm right-side position, completeness, and whether any visible caption exists.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R013

- Review ID: R013
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 9; page_idx 8; printed page Unknown
- Block ID / JSON evidence: image block 2; bbox 161,322,199,381; fourth Markdown/JSON image
- Issue type: Image mapping
- Raw state: line 161 uses CDN image tail de41be…6420.jpg.
- Cleaned state: line 175 uses ../raw/pilot_01/images/image_004.jpg.
- Reason for change: DOCX rId25 is the fourth embedded image and precedes the first Chapter 2 lead paragraph.
- Codex recommendation: Confirm left-side position, completeness, and absence or presence of a caption.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R014

- Review ID: R014
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 9; page_idx 8; printed page Unknown
- Block ID / JSON evidence: image block 4; bbox 400,321,442,383; fifth Markdown/JSON image
- Issue type: Image mapping
- Raw state: line 166 uses CDN image tail 09fa20…20c4.jpg.
- Cleaned state: line 180 uses ../raw/pilot_01/images/image_005.jpg.
- Reason for change: DOCX rId28 is the fifth embedded image and occurs between the two Chapter 2 lead paragraphs.
- Codex recommendation: Confirm right-side position, completeness, and absence or presence of a caption.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Suspected duplicate

#### R015

- Review ID: R015
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 5–6; page_idx 4–5; printed pages Unknown and 2
- Block ID / JSON evidence: page_idx 4 paras 2, 4, 5; page_idx 5 paras 6, 7, 8
- Issue type: Suspected duplicate text
- Raw state: the Chapter 1 opener around lines 94–101 substantially repeats the main-body passage around lines 115–119. The sentence 李秉哲自出生起就衣食无忧… is exact in both locations.
- DOCX evidence: both sequences are preserved; the first is interleaved with image paragraphs 58 and 60, while the later sequence appears as ordinary body paragraphs.
- Cleaned state: both occurrences remain unchanged.
- Reason for change: no deletion was made because the opener may be intentional design content, while duplicate recognition is also possible.
- Codex recommendation: Keep unresolved. Compare the PDF layout to decide whether the first sequence is a standfirst/design repeat or a MinerU duplication.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### OCR uncertainty

#### R016

- Review ID: R016
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 5–6; page_idx 4–5
- Block ID / JSON evidence: page_idx 4 para 4 and page_idx 5 para 7
- Issue type: Proper-name OCR uncertainty
- Raw state: 小源浪平 appears at raw lines 99 and 117.
- Cleaned state: spelling is unchanged; the first occurrence has a TODO requesting visual verification.
- Reason for change: no character correction was made because the printed glyph has not been checked.
- Codex recommendation: PDF visual verification required. Do not use common knowledge or web sources to change the name.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Numbers and dates

The following are transcription checks only. They do not ask whether a statement is historically or factually correct.

| Review ID | page_idx | JSON blocks | Values to compare visually |
|---|---:|---|---|
| R017 | 5 | paras 1 and 4 | 1910—1987; 1915—2001 |
| R018 | 9–10 | page 9 paras 1, 6, 8, 12; page 10 para 8 | 1929年10月; 1930年春天; 1929年10月24日; 1923年; 1930年 |
| R019 | 1 | para 5 | 1998年3月22日; 461/404/299/25/610亿美元 |
| R020 | 9 | para 12 | 70个百分点; 37%; 40% |
| R021 | 9–10 | page 9 paras 9–10; page 10 para 2 | 1300家; 1200万; 600万; 三百余万人 |
| R022 | 0 and 5 | page 0 para 4; page 5 para 2 | 300石; 2000石; 1500石 |
| R023 | 2–3 | page 2 para 4; page 3 para 0; page-number blocks | TOC entries 1–28, 后记, and their page references |

#### R017

- Review ID: R017
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 6; page_idx 5; printed page 2
- Block ID / JSON evidence: paras 1 and 4
- Issue type: Birth/death year verification
- Raw state: 李秉哲（1910—1987） and 郑周永（1915—2001）.
- Cleaned state: unchanged.
- Reason for change: no change; included for required numeric visual review.
- Codex recommendation: Compare every digit and dash glyph with the PDF; do not fact-check.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R018

- Review ID: R018
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 10–11; page_idx 9–10; printed pages 6–7
- Block ID / JSON evidence: page_idx 9 paras 1, 6, 8, 12; page_idx 10 para 8
- Issue type: Date verification
- Raw state: 1929年10月, 1930年春天, 1929年10月24日, 1923年, and 1930年.
- Cleaned state: unchanged.
- Reason for change: no change; dates are selected for visual transcription checking.
- Codex recommendation: Verify digits, month/day order, and spacing against the PDF only.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R019

- Review ID: R019
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 2; page_idx 1; printed page 7
- Block ID / JSON evidence: para 5
- Issue type: Financial figure verification
- Raw state: 1998年3月22日 and 461/404/299/25/610亿美元.
- Cleaned state: unchanged.
- Reason for change: no change; the dense sequence is vulnerable to OCR digit or unit errors.
- Codex recommendation: Compare each digit, unit, and sign with the PDF; do not assess factual accuracy.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R020

- Review ID: R020
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 10; page_idx 9; printed page 6
- Block ID / JSON evidence: para 12
- Issue type: Percentage verification
- Raw state: 70个百分点, 37%, and 40%.
- Cleaned state: unchanged.
- Reason for change: no change; percentage digits, signs, and wording require visual checking.
- Codex recommendation: Compare the three values and their units with the PDF only.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R021

- Review ID: R021
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 10–11; page_idx 9–10; printed pages 6–7
- Block ID / JSON evidence: page_idx 9 paras 9–10; page_idx 10 para 2
- Issue type: Count verification
- Raw state: 1300家, 1200万, 600万, and 三百余万人.
- Cleaned state: unchanged.
- Reason for change: no change; large counts are selected for visual checking.
- Codex recommendation: Verify digits, Chinese-number wording, and units against the PDF only.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R022

- Review ID: R022
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 1 and 6; page_idx 0 and 5
- Block ID / JSON evidence: page_idx 0 para 4; page_idx 5 para 2
- Issue type: Quantity and unit verification
- Raw state: 300石, 2000石, and 1500石.
- Cleaned state: unchanged.
- Reason for change: no change; the values and unit glyph require visual checking.
- Codex recommendation: Compare digits and 石 with the PDF; do not convert or normalize.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

#### R023

- Review ID: R023
- PDF / MinerU page index: PDF physical pages Unknown; Pilot Pages 3–4; page_idx 2–3; printed pages 9–10
- Block ID / JSON evidence: page_idx 2 para 4; page_idx 3 para 0; discarded page-number blocks
- Issue type: TOC and page-number verification
- Raw state: contents list contains entries 1–28 and 后记 with page references.
- Cleaned state: text and numbers are unchanged; page boundary markers were added.
- Reason for change: no numeric change; the table is included because dense page references are OCR-sensitive.
- Codex recommendation: Visually sample every entry and page reference. Do not infer PDF physical pages from the TOC.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Truncated ending

#### R024

- Review ID: R024
- PDF / MinerU page index: PDF physical page Unknown; Pilot Page 11; page_idx 10; printed page 7
- Block ID / JSON evidence: para 13; bbox 130,719,514,741
- Issue type: Truncated pilot ending
- Raw state: final line ends 郑周永十分讨厌农活儿。因为农活儿即使累死累活地干，.
- Cleaned state: incomplete text is preserved and followed by a TODO.
- Reason for change: no completion was invented because available data cannot show whether the pilot selection ended or MinerU omitted text.
- Codex recommendation: Compare the authorized PDF and the selected page range. Keep unresolved until the cause is known.
- Risk level: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

### Page reference uncertainty

#### R025

- Review ID: R025
- PDF / MinerU page index: all 11 Pilot Pages; page_idx 0–10
- Block ID / JSON evidence: page_idx plus discarded page_number blocks
- Issue type: Physical and printed page mapping
- Raw state: JSON provides pilot page_idx and some printed page numbers, but no reliable PDF physical page index. Printed page is absent for page_idx 4 and 8.
- Cleaned state: page markers use printed_page=unresolved for page_idx 4 and 8.
- Reason for change: unknown values were preserved rather than inferred.
- Codex recommendation: Reviewer should record visually confirmed PDF physical pages and printed pages. Do not guess from TOC sequence.
- Risk level: Medium
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Human note:

## Completion gate

Stage 2B is complete only when every R001–R025 item has one human decision and any Reject or Needs discussion item has a note. Decisions must then be reviewed in the later Pilot Rule Approval stage. Completing this checklist does not by itself change any Proposed rule to Approved.
