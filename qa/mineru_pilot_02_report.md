# MinerU Pilot 02 Validation Report

Stage: Stage 3B — MinerU Pilot 02 Closure & Rule Consolidation

Status: Passed

Purpose: record the completed holdout validation of Pilot 01 rules, the final human dispositions, and the limited rule consolidation supported by evidence from both pilots.

## Pilot input overview

- MinerU pages: 11 (`page_idx` 0–10)
- Raw inputs: Markdown, JSON, DOCX
- DOCX embedded images: 2, both extracted byte-for-byte
- Primary text layer: Markdown
- Structural/layout evidence: JSON
- Image/visual fallback: DOCX
- Cleaned validation sample: `source/chapters/pilot_02_cleaned.md`
- Pilot boundaries: the sample starts and ends mid-sentence

The three original long-named MinerU files were moved from the repository root to `source/raw/pilot_02/` under canonical names. SHA-256 verification confirmed that relocation did not change their bytes.

## Page and block mapping

All 11 JSON pages and their paragraph/discarded blocks were enumerated. PDF physical page indices are unavailable. Printed pages are recorded only when JSON provides a reliable `page_number` block.

| page_idx | Printed page | Section | Important evidence |
|---:|---:|---|---|
| 0 | 120 | Prior chapter continuation | opening truncation; header; footnote marker/body; blocks 1–8 |
| 1 | 121 | Prior chapter continuation | chapter 14 running header discarded; blocks 2–5 |
| 2 | Unknown | Confirmed blank page | scan-line artifact and leaked English process message removed from cleaned body; page mapping retained |
| 3 | Unknown | Chapter 15 opening | centered `15` misclassified as page_number; human-approved structural recovery; title block 1; image blocks 2/4; introductory text blocks 3/5–7 |
| 4 | 124 | Chapter 15 body | running header in Markdown; footnote marker/body; cross-page ending in block 8 |
| 5 | 125 | Chapter 15 body | cross-page continuation block 2; header discarded; blocks 2–11 |
| 6 | 126 | Chapter 15 body | running header in Markdown; blocks 1–13 |
| 7 | 127 | Chapter 15 body | header discarded; blank `lines_deleted` block 1; cross-page ending block 13 |
| 8 | 128 | Chapter 15 body | running header in Markdown; continuation block 1; repeated opener prose blocks 4–6 |
| 9 | 129 | Chapter 15 body | header discarded; blank `lines_deleted` block 2; cross-page ending block 9 |
| 10 | 130 | Chapter 15 body | running header in Markdown; continuation block 1; ending truncation block 7 |

The mapping is complete at MinerU page/block level. Printed page values for page_idx 2 and 3 remain Unknown rather than inferred.

## Image mapping

| Local image | Markdown | JSON | DOCX | Result |
|---|---|---|---|---|
| `image_001.jpg` | first CDN image | page_idx 3, block 2, bbox 161,331,198,389 | rId9 / word/media/rId9.jpg / first embed | Mapped |
| `image_002.jpg` | second CDN image | page_idx 3, block 4, bbox 401,330,440,392 | rId12 / word/media/rId12.jpg / second embed | Mapped |

Both images are the expected uncaptioned character illustrations for the chapter-opening template. The cleaned sample uses local relative paths and logical anchors; original left/right positions remain in JSON/DOCX metadata.

## Rule Validation Matrix

| Rule | Opportunity | Result | False Positive | Missed Case | Manual Review Triggered | Notes |
|---|---|---|---|---|---|---|
| running-header removal | 4 textual running headers entered Markdown; additional headers were discarded in JSON | Success | None detected | None detected | No | Removed only where repeated page-edge text and JSON/layout evidence agree. |
| heading normalization | 1 chapter opening | Resolved — structural recovery approved | None | MinerU omitted `15` from Markdown/DOCX after classifying it as page_number | Yes, resolved: P2-R003 | Human review approved `# 15 郑周永的船和李秉哲的彩色电视` using JSON/layout/template evidence. |
| chapter-opening template | 1 chapter opening | Success after human validation | None | Initial chapter-number omission | Yes, resolved: P2-R003 | Heading, introductory prose, and two mapped illustrations now satisfy the confirmed template. |
| image localization | 2 DOCX media entries | Success | None | None | No | 2/2 extracted without format or byte changes. |
| image mapping | 2 images | Success | None | None | No | Markdown → JSON page/block/bbox → DOCX media → local file mapping is one-to-one. |
| cross-page reconstruction | 3 clear joins: 4→5, 7→8, 9→10 | Success | None detected | None detected | No | Joins use explicit page boundaries, block order, and running-header evidence. |
| footnote handling | 2 markers and 2 JSON page_footnote bodies | Success | None detected | None detected | Yes, resolved: P2-R001, P2-R004 | Both mappings received human approval. Future footnotes still require individual manual review. |
| duplicate preservation | chapter-opening prose repeats in page_idx 8 | Success | None | None | No | Both occurrences are preserved under default = preserve. |
| OCR uncertainty detection | several suspicious glyph sequences | Success | None detected | One OCR error confirmed | Yes, resolved: P2-R005 | PDF review confirmed `入水式`; cleaned source records the human-verified correction. Other sampled terms were confirmed. |
| number/date detection | dense dates, money, tonnage, percentages, counts | Success | None detected | None in the human sample | Yes, resolved: P2-R006 | Sample passed; policy advances to automated consistency checks plus targeted review and sampling. |
| page/block mapping | 11 pages | Success | None | None at MinerU level | No | PDF physical pages remain unavailable; two printed pages remain Unknown. |
| incomplete-boundary detection | opening and ending | Success | None | None | Yes, resolved: P2-R007, P2-R008 | Human review confirmed both are pilot-range boundaries, not extraction failures. |

## Rule Success

Ten matrix rows produced successful rule behavior during the initial holdout run; the two pending chapter-opening rows were subsequently resolved by human validation. In particular:

- running-header removal did not delete body text;
- both images were localized and mapped without silent loss;
- three structurally supported page joins were reconstructed;
- both footnotes were intercepted for mandatory human review;
- repeated chapter-opening prose was preserved;
- OCR and numeric candidates were flagged without correction; and
- both sample boundaries were detected.

## Rule Failure

No approved cleaning rule produced a confirmed destructive failure in this sample.

The missing chapter number is classified as a resolved extraction anomaly rather than an approved-rule failure: the number remained in JSON evidence, human review approved its structural recovery, and raw artifacts were not changed.

## New Anomaly

### P2-A001 — Process instruction emitted as page text

- Page/block: page_idx 2, block 0
- What happened: MinerU emitted an English statement explaining that OCR output should be empty for a stylistic horizontal line.
- Severity: High
- Manual review required: Completed, P2-R002
- Disposition: Resolved. Human PDF review confirms the page is blank, the line is a scan artifact, and the English instruction is non-source parser output. Cleaned Markdown preserves only page mapping and `blank page — confirmed` metadata.

### P2-A002 — Chapter number classified as page number

- Page/block: page_idx 3, discarded block 0, centered bbox 277,105,322,137
- What happened: JSON contains `15` as `page_number`; Markdown and DOCX omit it while retaining the adjacent chapter title.
- Severity: Medium
- Manual review required: Completed, P2-R003
- Disposition: Resolved. JSON content/position, title proximity, and the fixed chapter-opening template jointly support recovery; cleaned heading now includes `15`.

### P2-A003 — Empty `lines_deleted` paragraph blocks

- Page/block: page_idx 7 block 1; page_idx 9 block 2
- What happened: JSON retains empty text blocks marked `lines_deleted=true`.
- Severity: Low
- Manual review required: Not required after structural checks
- Disposition: Classified as empty parser noise. Blocks contain no text, image, footnote, or semantic content; they may be skipped while their existence remains available in page/block mapping.

## Manual Review Required triggers

Eight focused review items were created and all are resolved:

- two footnote mappings;
- one leaked process-message block;
- one missing/misclassified chapter number;
- one grouped OCR/proper-noun visual check;
- one grouped numeric/date/money/percentage sample; and
- two pilot-boundary truncation checks.

Normal low-risk header removals, image mappings, and unambiguous paragraph joins remain in the matrix rather than becoming extra review items. Pilot 02 now has zero open or Needs discussion item.

## Destructive false-positive and loss check

- Confirmed destructive false positives: 0
- Suspected body-text loss: 0
- Suspected image loss: 0
- Structural element omission: resolved chapter number `15`, recovered only in cleaned source after human approval
- Silent high-risk content changes: 0
- Human-verified OCR correction: `人水式` → `入水式` in cleaned source only

## Rule Consolidation

Status: Approved based on completed human review

The following rules are incorporated into `docs/SOURCE_CLEANING_GUIDE.md`:

1. Blank-page scan artifacts may be omitted only after visual confirmation; page mapping remains.
2. Parser/instruction leakage may be removed only with structural/visual evidence that it is absent from the source.
3. A misclassified chapter number may be recovered from multiple independent structural signals, never semantic guesswork alone.
4. Empty parser blocks with no semantic payload may be ignored while mapping records their existence.
5. Numeric transcription QA uses automated raw/cleaned consistency checks, targeted manual triggers, and sampling; factual correction remains manual.

## Recommendation

Recommendation: **PASS**

Reasoning: approved low-risk rules generalized without a destructive false positive, prose or image loss, page/block mapping remained stable, all manual-review-required categories were intercepted, and all eight human review items are resolved. The three anomalies are small, explainable, and now classified under evidence-bounded rules.

Pilot 02 supports proceeding to Stage 4 — Full-book Source Ingestion under a separate authorization. This report does not start Stage 4.

## Pilot 02 Closure Summary

- Status: Passed
- Rule successes: 10 in the initial holdout matrix
- Rule failures: 0
- Destructive false positives: 0
- Silent prose loss: 0
- Silent image loss: 0
- Manual review items: all 8 resolved
- New anomalies: resolved/classified
- Existing cleaning rules: validated on holdout sample
- Page/block mapping: stable across all 11 pages

Pilot 02 is a holdout validation of the rules approved from Pilot 01, not a new rule-training set. The limited consolidated rules above were adopted only after separate human review of the observed anomalies.
