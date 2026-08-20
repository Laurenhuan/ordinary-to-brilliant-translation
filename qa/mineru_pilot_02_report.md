# MinerU Pilot 02 Validation Report

Stage: Stage 3A — MinerU Pilot 02 Validation

Status: Awaiting human review; Pilot 02 is not passed or closed

Purpose: test the approved Pilot 01 source-cleaning rules on an 11-page holdout sample without changing those rules.

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
| 2 | Unknown | Separator/decorative page | one English process-message block; no printed page evidence |
| 3 | Unknown | Chapter 15 opening candidate | centered `15` discarded as page_number; title block 1; image blocks 2/4; introductory text blocks 3/5–7 |
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
| heading normalization | 1 chapter opening | Pending human validation | None | Candidate chapter number `15` is absent from Markdown/DOCX after JSON classified it as page_number | Yes: P2-R003 | Cleaned heading keeps the Markdown title and does not silently restore `15`. |
| chapter-opening template | 1 chapter opening | Pending human validation | None | Chapter number is missing from the primary text layer | Yes: P2-R003 | One title, introductory prose, and two mapped illustrations are otherwise present. A mismatch warning was triggered. |
| image localization | 2 DOCX media entries | Success | None | None | No | 2/2 extracted without format or byte changes. |
| image mapping | 2 images | Success | None | None | No | Markdown → JSON page/block/bbox → DOCX media → local file mapping is one-to-one. |
| cross-page reconstruction | 3 clear joins: 4→5, 7→8, 9→10 | Success | None detected | None detected | No | Joins use explicit page boundaries, block order, and running-header evidence. |
| footnote handling | 2 markers and 2 JSON page_footnote bodies | Success | None detected | None detected | Yes: P2-R001, P2-R004 | Both mappings are proposed; neither is human-approved yet. DOCX has no usable note bodies. |
| duplicate preservation | chapter-opening prose repeats in page_idx 8 | Success | None | None | No | Both occurrences are preserved under default = preserve. |
| OCR uncertainty detection | several suspicious glyph sequences | Success | None detected | Unknown until visual review | Yes: P2-R005 | No source character was intentionally corrected. |
| number/date detection | dense dates, money, tonnage, percentages, counts | Success | None detected | Unknown until visual review | Yes: P2-R006 | One grouped sampling item limits manual workload. |
| page/block mapping | 11 pages | Success | None | None at MinerU level | No | PDF physical pages remain unavailable; two printed pages remain Unknown. |
| incomplete-boundary detection | opening and ending | Success | None | None | Yes: P2-R007, P2-R008 | Marked as pilot-boundary truncation candidates, not extraction failures. |

## Rule Success

Ten matrix rows produced successful rule behavior. In particular:

- running-header removal did not delete body text;
- both images were localized and mapped without silent loss;
- three structurally supported page joins were reconstructed;
- both footnotes were intercepted for mandatory human review;
- repeated chapter-opening prose was preserved;
- OCR and numeric candidates were flagged without correction; and
- both sample boundaries were detected.

## Rule Failure

No approved cleaning rule produced a confirmed destructive failure in this sample.

The missing chapter number is classified as an extraction anomaly rather than an approved-rule failure: the number remains in JSON evidence but MinerU labeled it `page_number`, and Markdown/DOCX omitted it. Heading normalization is therefore pending human validation rather than silently applied.

## New Anomaly

### P2-A001 — Process instruction emitted as page text

- Page/block: page_idx 2, block 0
- What happened: MinerU emitted an English statement explaining that OCR output should be empty for a stylistic horizontal line.
- Severity: High
- Manual review required: Yes, P2-R002
- Treatment: retain and isolate the exact emitted text in the cleaned sample pending PDF review; do not accept it as book body and do not delete it silently.

### P2-A002 — Chapter number classified as page number

- Page/block: page_idx 3, discarded block 0, centered bbox 277,105,322,137
- What happened: JSON contains `15` as `page_number`; Markdown and DOCX omit it while retaining the adjacent chapter title.
- Severity: Medium
- Manual review required: Yes, P2-R003
- Treatment: preserve the title without adding `15`; record the candidate and request visual confirmation.

### P2-A003 — Empty `lines_deleted` paragraph blocks

- Page/block: page_idx 7 block 1; page_idx 9 block 2
- What happened: JSON retains empty text blocks marked `lines_deleted=true`.
- Severity: Low
- Manual review required: No at present
- Treatment: record telemetry and ignore empty content only; reopen if PDF comparison indicates missing text.

## Manual Review Required triggers

Eight focused review items were created:

- two footnote mappings;
- one leaked process-message block;
- one missing/misclassified chapter number;
- one grouped OCR/proper-noun visual check;
- one grouped numeric/date/money/percentage sample; and
- two pilot-boundary truncation checks.

Normal low-risk header removals, image mappings, and unambiguous paragraph joins remain in the matrix rather than becoming extra review items.

## Destructive false-positive and loss check

- Confirmed destructive false positives: 0
- Suspected body-text loss: 0
- Suspected image loss: 0
- Structural element omission: 1 candidate chapter number, retained in JSON and explicitly flagged
- Silent high-risk content changes: 0; raw/cleaned textual parity was checked before commit

## Proposed Rule Changes

Status: Not approved

The following are observations for later human consideration only. `docs/SOURCE_CLEANING_GUIDE.md` is unchanged.

1. Consider detecting VLM/OCR process-message leakage and routing it to QA instead of body text.
2. On a recognized chapter-opening page, consider warning when a centered numeric block above the title is classified as `page_number` and absent from Markdown.
3. Continue collecting `lines_deleted` empty-block telemetry before deciding whether a rule extension is needed.

## Recommendation

Recommendation: **CONDITIONAL PASS candidate**

Reasoning: approved low-risk rules generalized without a confirmed destructive false positive, images and page/block mapping remained stable, and every manual-review-required category was intercepted. However, the leaked English process message and misclassified chapter number require human decisions before Pilot 02 can be passed.

Do not begin full-book ingestion yet. First complete the eight Pilot 02 manual review items and decide whether either high-value anomaly warrants a separately approved rule extension.
