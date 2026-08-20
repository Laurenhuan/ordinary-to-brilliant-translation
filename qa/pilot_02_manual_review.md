# Pilot 02 Manual Review

Stage: Stage 3B — MinerU Pilot 02 Closure & Rule Consolidation

Status: Passed — all eight manual review items resolved

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

| Decision status | Items |
|---|---:|
| Approved | 8 |
| Open / Needs discussion | 0 |

## Review items

### P2-R001

- Review ID: P2-R001
- page_idx: 0
- Printed page: 120
- Block evidence: body block 3 marker after KBS; discarded block 9 `page_footnote`, bbox 131,780,254,795
- Issue category: Footnote recovery
- Raw state: Markdown contains `$^{①}$`; JSON body is `① KBS，韩国电视台。`; DOCX has no usable footnote body.
- Cleaned state: marker `[^p000-1]` and the JSON-derived definition are retained with an approval record.
- Existing rule involved: Footnote handling — Approved — Manual Review Required
- Codex assessment: Same-page one-marker/one-body mapping is structurally strong but cannot become authoritative without visual confirmation.
- Risk: High
- Human decision: [x] Approve  [ ] Reject  [ ] Needs discussion
- Status: approved
- Human note: Same-page mapping confirmed by human PDF visual review. The long-term rule still requires manual review for every footnote.

### P2-R002

- Review ID: P2-R002
- page_idx: 2
- Printed page: Unknown
- Block evidence: sole para block 0, bbox 1,10,594,864
- Issue category: New anomaly / process-message leakage
- Raw state: Markdown, JSON, and DOCX contain the English sentence beginning `The OCR result should be empty...`.
- Cleaned state: the leaked English instruction is removed; the page marker remains with `blank page — confirmed` metadata.
- Existing rule involved: Blank-page scan artifact handling; parser / instruction leakage handling
- Codex assessment: Human PDF review confirms the page is blank and the line is a scan artifact, not source text, an illustration, a divider, or authorial design.
- Risk: High
- Human decision: [x] Approve exclusion from body  [ ] Preserve as body  [ ] Needs discussion
- Status: approved
- Human note: Exclusion approved after visual confirmation. Page mapping is preserved and no Markdown horizontal rule or image is generated.

### P2-R003

- Review ID: P2-R003
- page_idx: 3
- Printed page: Unknown
- Block evidence: discarded block 0 is centered text `15`, type `page_number`, bbox 277,105,322,137; title block 1 is `郑周永的船和李秉哲的彩色电视`, bbox 114,147,484,178
- Issue category: Chapter heading / chapter-opening-layout mismatch
- Raw state: JSON retains `15`, but Markdown and DOCX contain only the chapter title.
- Cleaned state: the heading is restored as `# 15 郑周永的船和李秉哲的彩色电视` with a human-approval record.
- Existing rule involved: Chapter-number recovery from structural evidence; chapter-opening validation
- Codex assessment: JSON content/position, title proximity, and the confirmed recurring chapter-opening template jointly establish `15` as the chapter number.
- Risk: High
- Human decision: [x] Approve `15` as chapter number  [ ] Reject  [ ] Needs discussion
- Status: approved
- Human note: Structural recovery approved. Raw Markdown, JSON, and DOCX remain unchanged.

### P2-R004

- Review ID: P2-R004
- page_idx: 4
- Printed page: 124
- Block evidence: body block 1 marker after `妹夫`; discarded block 9 `page_footnote`, bbox 128,779,405,794
- Issue category: Footnote recovery
- Raw state: Markdown contains plain marker `①`; JSON body is `① 尼亚尔霍斯的妻子和奥纳西斯的妻子是一对姐妹。`; DOCX has no usable footnote body.
- Cleaned state: marker `[^p004-1]` and the JSON-derived definition are retained with an approval record.
- Existing rule involved: Footnote handling — Approved — Manual Review Required
- Codex assessment: Same-page one-marker/one-body mapping is structurally strong but requires visual approval.
- Risk: High
- Human decision: [x] Approve  [ ] Reject  [ ] Needs discussion
- Status: approved
- Human note: Same-page mapping confirmed by human PDF visual review. The long-term rule still requires manual review for every footnote.

### P2-R005

- Review ID: P2-R005
- page_idx: 0, 9, 10
- Printed page: 120, 129, 130
- Block evidence: page 0 block 5; page 9 block 9; page 10 block 3
- Issue category: OCR / proper-noun uncertainty sampling
- Raw state: suspicious sequences include `天擎或混频电视机`, `船舶号位40%`, and `人水式`.
- Cleaned state: the other sampled terms remain unchanged; human-verified `人水式` is corrected to `入水式`.
- Existing rule involved: OCR and proper-noun uncertainty — Approved — Manual Review Required
- Codex assessment: PDF visual verification required. No replacement characters or factual alternatives are proposed.
- Risk: High
- Human decision: [x] Human-verified correction applied  [ ] Reject  [ ] Needs discussion
- Status: approved
- Human note: The other sampled professional terms are confirmed correct. PDF visual verification confirms `入水式`; this is recorded as a human-verified OCR correction and raw artifacts remain unchanged.

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
- Human decision: [x] Sample confirmed  [ ] Transcription issue found  [ ] Needs discussion
- Status: approved
- Human note: Sample accepted. Future numeric transcription QA uses automated consistency checks, targeted review triggers, and sampling; factual correction remains manual.

### P2-R007

- Review ID: P2-R007
- page_idx: 0
- Printed page: 120
- Block evidence: first body block 1 begins `首，晃动小国旗的经历。`
- Issue category: Pilot-boundary truncation — beginning
- Raw state: the sample begins with an apparent sentence fragment.
- Cleaned state: text is preserved unchanged with a human-confirmed boundary record.
- Existing rule involved: Incomplete-boundary detection
- Codex assessment: Likely caused by holdout sampling rather than MinerU extraction, but the selected PDF range must confirm this.
- Risk: Medium
- Human decision: [x] Pilot boundary confirmed  [ ] Extraction failure  [ ] Needs discussion
- Status: approved
- Human note: The apparent fragment is caused by the selected holdout range, not a MinerU extraction failure.

### P2-R008

- Review ID: P2-R008
- page_idx: 10
- Printed page: 130
- Block evidence: final body block 7 ends `而郑`
- Issue category: Pilot-boundary truncation — ending
- Raw state: the sample ends mid-sentence.
- Cleaned state: incomplete text is preserved unchanged with a human-confirmed boundary record.
- Existing rule involved: Incomplete-boundary detection
- Codex assessment: Likely caused by holdout sampling rather than MinerU extraction, but the selected PDF range must confirm this.
- Risk: Medium
- Human decision: [x] Pilot boundary confirmed  [ ] Extraction failure  [ ] Needs discussion
- Status: approved
- Human note: The incomplete ending is caused by the selected holdout range, not a MinerU extraction failure.

## Completion gate

Pilot 02 is closed with P2-R001–P2-R008 approved and no unresolved review item. This closure supports proceeding to the separately authorized Full-book Source Ingestion stage but does not start ingestion or translation.
