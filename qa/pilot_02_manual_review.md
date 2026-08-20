# Pilot 02 Manual Review

Stage: Stage 3A — MinerU Pilot 02 Validation

Status: Awaiting project-lead review

Only Manual Review Required cases, new anomalies, and uncertain boundaries are listed. Approved low-risk cases that behaved normally remain in the validation matrix.

## Review summary

| Category | Items |
|---|---:|
| Footnotes | 2 |
| New anomalies | 2 |
| OCR / proper-noun sampling | 1 |
| Number/date/money/percentage sampling | 1 |
| Pilot-boundary truncation | 2 |
| Total | 8 |

## Review items

### P2-R001

- Review ID: P2-R001
- page_idx: 0
- Printed page: 120
- Block evidence: body block 3 marker after KBS; discarded block 9 `page_footnote`, bbox 131,780,254,795
- Issue category: Footnote recovery
- Raw state: Markdown contains `$^{①}$`; JSON body is `① KBS，韩国电视台。`; DOCX has no usable footnote body.
- Cleaned state: proposed marker `[^p000-1]` and proposed JSON-derived definition are present with a TODO.
- Existing rule involved: Footnote handling — Approved — Manual Review Required
- Codex assessment: Same-page one-marker/one-body mapping is structurally strong but cannot become authoritative without visual confirmation.
- Risk: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Status: open
- Human note:

### P2-R002

- Review ID: P2-R002
- page_idx: 2
- Printed page: Unknown
- Block evidence: sole para block 0, bbox 1,10,594,864
- Issue category: New anomaly / process-message leakage
- Raw state: Markdown, JSON, and DOCX contain the English sentence beginning `The OCR result should be empty...`.
- Cleaned state: exact text is retained in a blockquote with a TODO and is not accepted as book body.
- Existing rule involved: No approved rule directly covers VLM/OCR process-message leakage.
- Codex assessment: The message describes a stylistic horizontal line rather than book content. Authorized PDF visual verification is required before exclusion.
- Risk: High
- Human decision: [ ] Approve exclusion from body  [ ] Preserve as body  [ ] Needs discussion
- Status: open
- Human note:

### P2-R003

- Review ID: P2-R003
- page_idx: 3
- Printed page: Unknown
- Block evidence: discarded block 0 is centered text `15`, type `page_number`, bbox 277,105,322,137; title block 1 is `郑周永的船和李秉哲的彩色电视`, bbox 114,147,484,178
- Issue category: Chapter heading / chapter-opening-layout mismatch
- Raw state: JSON retains `15`, but Markdown and DOCX contain only the chapter title.
- Cleaned state: the title remains without a number; a TODO records `15` as a candidate chapter number.
- Existing rule involved: Chapter-number + chapter-title logical normalization; chapter-opening validation
- Codex assessment: Placement and the known chapter-opening template strongly suggest a chapter number, but primary Markdown and DOCX do not supply it. Do not restore without visual confirmation.
- Risk: High
- Human decision: [ ] Approve `15` as chapter number  [ ] Reject  [ ] Needs discussion
- Status: open
- Human note:

### P2-R004

- Review ID: P2-R004
- page_idx: 4
- Printed page: 124
- Block evidence: body block 1 marker after `妹夫`; discarded block 9 `page_footnote`, bbox 128,779,405,794
- Issue category: Footnote recovery
- Raw state: Markdown contains plain marker `①`; JSON body is `① 尼亚尔霍斯的妻子和奥纳西斯的妻子是一对姐妹。`; DOCX has no usable footnote body.
- Cleaned state: proposed marker `[^p004-1]` and proposed JSON-derived definition are present with a TODO.
- Existing rule involved: Footnote handling — Approved — Manual Review Required
- Codex assessment: Same-page one-marker/one-body mapping is structurally strong but requires visual approval.
- Risk: High
- Human decision: [ ] Approve  [ ] Reject  [ ] Needs discussion
- Status: open
- Human note:

### P2-R005

- Review ID: P2-R005
- page_idx: 0, 9, 10
- Printed page: 120, 129, 130
- Block evidence: page 0 block 5; page 9 block 9; page 10 block 3
- Issue category: OCR / proper-noun uncertainty sampling
- Raw state: suspicious sequences include `天擎或混频电视机`, `船舶号位40%`, and `人水式`.
- Cleaned state: all sequences remain unchanged.
- Existing rule involved: OCR and proper-noun uncertainty — Approved — Manual Review Required
- Codex assessment: PDF visual verification required. No replacement characters or factual alternatives are proposed.
- Risk: High
- Human decision: [ ] Source glyphs confirmed  [ ] OCR issue found  [ ] Needs discussion
- Status: open
- Human note:

### P2-R006

- Review ID: P2-R006
- page_idx: 0, 4–10
- Printed page: 120, 124–130
- Block evidence: representative blocks 0/5; 4/1,6; 5/7–8; 7/8–13; 8/9–11; 9/3–9; 10/2–7
- Issue category: Number/date/money/percentage sampling
- Raw state: representative values include `1966`, `1999年8月24日`, `27年`, `1972年`, `26万吨`, `8000万美元`, `500元`, `3035万美元`, `14亿韩元`, `1972年3月22日`, `51.8万吨`, `1.75%`, `194.7万吨`, `2.64%`, `3%`, `7302/7308/7310`, and `1974年6月/11月`.
- Cleaned state: values remain unchanged.
- Existing rule involved: Numbers, dates, and facts — Approved — Manual Review Required
- Codex assessment: Compare digits, punctuation, units, and percent signs with the authorized PDF only; do not perform historical fact checking.
- Risk: High
- Human decision: [ ] Sample confirmed  [ ] Transcription issue found  [ ] Needs discussion
- Status: open
- Human note:

### P2-R007

- Review ID: P2-R007
- page_idx: 0
- Printed page: 120
- Block evidence: first body block 1 begins `首，晃动小国旗的经历。`
- Issue category: Pilot-boundary truncation — beginning
- Raw state: the sample begins with an apparent sentence fragment.
- Cleaned state: text is preserved unchanged with a boundary TODO.
- Existing rule involved: Incomplete-boundary detection
- Codex assessment: Likely caused by holdout sampling rather than MinerU extraction, but the selected PDF range must confirm this.
- Risk: Medium
- Human decision: [ ] Pilot boundary confirmed  [ ] Extraction failure  [ ] Needs discussion
- Status: open
- Human note:

### P2-R008

- Review ID: P2-R008
- page_idx: 10
- Printed page: 130
- Block evidence: final body block 7 ends `而郑`
- Issue category: Pilot-boundary truncation — ending
- Raw state: the sample ends mid-sentence.
- Cleaned state: incomplete text is preserved unchanged with a boundary TODO.
- Existing rule involved: Incomplete-boundary detection
- Codex assessment: Likely caused by holdout sampling rather than MinerU extraction, but the selected PDF range must confirm this.
- Risk: Medium
- Human decision: [ ] Pilot boundary confirmed  [ ] Extraction failure  [ ] Needs discussion
- Status: open
- Human note:

## Completion gate

Pilot 02 remains open. Its final Pass/Conditional Pass/Fail decision requires human decisions for P2-R001–P2-R008. Closing these items does not authorize full-book ingestion or translation.
