# Source Cleaning Guide

Version: v0.4 — Stage 3B Pilot 02 Closure & Rule Consolidation

The purpose of source cleaning is to produce readable, traceable Markdown without rewriting, translating, fact-correcting, or silently repairing the source text.

## Rule status vocabulary

- Proposed — not yet approved for project use
- Approved — may be applied when its stated evidence conditions are satisfied
- Approved — Manual Review Required — the procedure is accepted, but every affected item must receive human QA before it enters authoritative cleaned or reviewed source
- Rejected — must not be applied

Approval is always limited by the conditions written below. Approved never means that an OCR correction, factual change, ambiguous layout decision, or uncertain mapping may run unattended.

## Evidence-layer roles

- Approved: MinerU Markdown is the primary text layer for source cleaning.
- Approved: JSON is the page, block, order, type, bounding-box, discarded-element, and layout-evidence layer.
- Approved: DOCX is the embedded-image source and a visual/layout fallback; DOCX-derived text must never overwrite MinerU Markdown.
- Approved — Manual Review Required: Human comparison with the authorized PDF is the final evidence layer for ambiguous visual, OCR, numeric, semantic, or content decisions.

## 1. Raw source preservation

- Approved: Treat every MinerU input as immutable raw evidence.
- Approved: Store Markdown, JSON, DOCX, and extracted images under a source-specific directory with stable names.
- Approved: Record hashes for raw inputs and extracted media.
- Approved: Never overwrite source.md with text re-parsed from source.docx.
- Approved: Put every cleaned result outside source/raw/.
- Approved: Store only project-authorized source artifacts. Public repository visibility grants no additional license or reuse rights.

## 2. Page, header, and footer handling

- Approved: Identify a running header or footer using reliable layout evidence such as repeated text, page-edge position, JSON block type, bounding box, and neighboring block order.
- Approved: Remove a running header from cleaned Markdown only when the evidence is consistent and the removal is recorded in QA.
- Approved: Preserve printed page numbers as mapping metadata even when they are removed from readable body text.
- Approved — Manual Review Required: If Markdown, JSON, DOCX, and visual layout disagree, preserve the raw text and open a QA item instead of choosing silently.
- Approved: Do not classify text as a running header from semantic intuition alone.

Pilot approval basis: R001–R004.

### Blank-page scan artifact handling

- Approved: When PDF visual evidence confirms that a page is blank and detected lines, spots, scan edges, or similar marks have no semantic content, cleaned Markdown generates no body text, horizontal rule, image, or decorative element for them.
- Approved: Preserve the page mapping and record `blank page — confirmed` in QA metadata.
- Approved — Manual Review Required: If the machine cannot establish that the page is genuinely blank, preserve the raw evidence and route the page to visual review.

### Parser / instruction leakage handling

- Approved: Remove parser prompts, OCR instructions, model explanations, or other pipeline-generated text from cleaned body only when structural and PDF visual evidence confirm that the text does not exist in the source book.
- Approved: Record the removed text, page/block evidence, and human disposition in QA; never alter raw artifacts.
- Approved — Manual Review Required: Appearance or language alone is insufficient. Any ambiguous candidate remains preserved and enters human review.

Pilot 02 approval basis: P2-A001 / P2-R002.

## 3. Heading normalization

- Approved: Treat MinerU heading levels as structural evidence rather than final Markdown hierarchy.
- Approved: A chapter number and chapter name may remain on separate visual lines in the original book while forming one logical chapter heading.
- Approved: When the number and name are adjacent, share the same visual role, and JSON/DOCX order supports one heading, cleaned Markdown may combine them into one logical heading.
- Approved: Combining the logical heading must not change, translate, correct, or otherwise rewrite the chapter-number or chapter-title text.
- Approved: Record every structural heading merge in QA.
- Approved: Do not infer missing headings or rename chapters from outside knowledge.

### Chapter-number recovery from structural evidence

- Approved: Recover a chapter number omitted from Markdown only when multiple independent structural signals jointly identify it, such as a recognized chapter-opening page, title proximity, JSON content and block position, bounding box/page position, expected chapter sequence, and the confirmed fixed chapter-opening template.
- Approved: Record the recovered number and its evidence in QA; raw Markdown, JSON, and DOCX remain unchanged.
- Approved — Manual Review Required: Do not recover a number from semantic expectation or sequence guesswork alone. Conflicting or incomplete evidence requires human approval.

Pilot approval basis: R005 and P2-A002 / P2-R003.

## 4. Paragraph handling

- Approved: Preserve source paragraph order and wording.
- Approved: Reconstruct a cross-page paragraph only when JSON block order, the page boundary, adjacent fragments, and reliable running-header evidence support the join.
- Approved: Semantic plausibility alone is insufficient evidence for an automatic join.
- Approved: Preserve an inline page marker at the exact boundary when a paragraph is joined across pages.
- Approved: Do not reflow or rewrite Chinese paragraphs for style or readability.
- Approved — Manual Review Required: Keep incomplete text and add a QA marker until the source boundary is visually confirmed.
- Approved — Manual Review Required: Any paragraph reconstruction that lacks explicit block-order, page-boundary, or artifact evidence is ambiguous and must not be applied without human approval.

### Empty parser block handling

- Approved: A parser block may be skipped when it contains no text, image, footnote, or other semantic payload and ignoring it does not change meaningful block ordering.
- Approved: Preserve the block's existence in page/block mapping or parser telemetry when available.
- Approved — Manual Review Required: Any uncertainty about hidden, deleted, or visually present content requires source review before the block is ignored.

Pilot approval basis: R006, R024, and P2-A003.

## 5. Repeated prose

- Approved — Manual Review Required: Do not automatically deduplicate repeated prose.
- Approved — Manual Review Required: If identical or highly similar prose occurs in different layout positions and the PDF or DOCX shows both occurrences, preserve both.
- Approved — Manual Review Required: Repeated prose may be deleted only when all three conditions are satisfied:
  1. visual PDF evidence shows that the original contains only one occurrence;
  2. JSON or MinerU evidence shows duplicate extraction; and
  3. a human reviewer approves the deletion.
- Approved — Manual Review Required: Default to preserve when evidence is incomplete or conflicting.

Risk: High.

Pilot approval basis: R015. The Chapter 1 repetition is confirmed as original authorial/layout design and remains in cleaned source.

## 6. Image localization and layout

- Approved: Prefer images embedded in the MinerU DOCX over temporary CDN copies when the embedded media is complete.
- Approved: Extract word/media entries byte-for-byte without resizing, recompression, cropping, or format conversion.
- Approved: Cross-map images through JSON page/bbox order, Markdown image order, and DOCX relationship/media order.
- Approved: Use stable document-order local names and relative paths in cleaned Markdown.
- Approved: Replace a CDN URL only after a unique local mapping is verified.
- Approved — Manual Review Required: Preserve an unresolved URL or mapping and open QA rather than substituting a screenshot or guessed image.
- Approved: Do not invent figure captions. Neutral Markdown alt text may identify an internal resource, but a generated description must never be represented as an original caption.

### Chapter-opening layout rule

Status: Approved

The book uses a recurring chapter-opening template:

1. one chapter number / chapter title structure;
2. one introductory text block;
3. two character illustrations;
4. the illustrations are distributed on the left and right sides of the page composition; and
5. the illustrations normally have no independent captions.

Cleaned Markdown must preserve the correct chapter number, chapter title, introductory text, two correct images, logical reading order, and the logical association between the images and the chapter opening. It does not need to reproduce left/right placement, exact horizontal coordinates, text wrapping, or the original two-dimensional composition.

### Logical image anchoring

Status: Approved

Cleaned Markdown records the chapter association, approximate nearby content, document order, and local file path for each image. This is required source structure.

### Original layout metadata

Status: Approved

JSON page index, image block, bounding box, DOCX relationship/media order, and other visual evidence preserve original left/right position and page relationships. These details are layout metadata / publishing information and do not need to be encoded directly in Markdown. A later Publishing stage may reuse them to reconstruct a comparable DOCX or PDF layout.

### Chapter-opening validation

- Approved: Automatically check every parsed chapter opening for one chapter heading, one introductory text block, and two character illustrations.
- Approved — Manual Review Required: Create a `chapter-opening-layout mismatch` QA warning when a heading or introduction is missing, the heading is split abnormally, image count is not two, or images are detached from the chapter opening.
- Approved — Manual Review Required: Every mismatch must be confirmed by a human; the recurring template must not be used to silently repair or invent missing content.

Pilot approval basis: R010–R014. The project lead confirmed that the Chapter 1 and Chapter 2 openers represent the recurring book-wide template.

## 7. Footnote handling

- Approved: Programs may detect footnote markers and JSON page_footnote blocks.
- Approved: Programs may propose marker-to-body mappings, restore Markdown footnote structure, and recommend insertion positions.
- Approved — Manual Review Required: Every footnote must enter QA and receive human confirmation before it becomes authoritative cleaned or reviewed source.
- Approved — Manual Review Required: Do not attach a note when multiple markers, multiple bodies, missing visual evidence, or conflicting order makes the mapping ambiguous.
- Approved — Manual Review Required: Record the marker, body, page, block, proposed insertion point, and human decision for every footnote.

Pilot approval basis: R007–R009, approved as one footnote-validation class while retaining all three IDs for traceability.

## 8. OCR and proper-noun uncertainty

- Approved: Detect and flag suspected OCR characters without altering raw text.
- Approved: Preserve the extracted form and add a minimal QA marker when uncertainty may affect meaning.
- Approved — Manual Review Required: Never automatically correct OCR characters.
- Approved — Manual Review Required: People, places, companies, institutions, book titles, and historical names require visual source confirmation before correction or normalization.
- Approved — Manual Review Required: Do not use memory, common knowledge, or web fact checking to replace source-cleaning evidence.
- Approved: Defer English terminology and translated-name decisions to the translation and terminology stages.

Pilot approval basis: R016 and P2-R005. Pilot 02 includes the human-verified cleaned-source correction `人水式` → `入水式`; raw artifacts remain unchanged.

## 9. Numbers, dates, and facts

- Approved: Normal numbers may pass from raw to cleaned source without individual approval when structural cleaning preserves them exactly.
- Approved: Automatically compare raw and cleaned numeric tokens to detect disappearance, change, splitting, or incorrect merging.
- Approved: Automatically flag abnormal number formats, suspicious OCR/block evidence, and values located in footnotes, tables, images, or complex layouts.
- Approved — Manual Review Required: A raw/cleaned mismatch, abnormal format, suspicious evidence, complex-layout value, or suspected pipeline change requires targeted review.
- Approved: Maintain a defined human sampling program during full-book ingestion rather than creating an item for every normal number.

### Transcription accuracy

- Approved: Numeric source QA asks whether digits, signs, punctuation, units, and formatting were transcribed and structurally preserved from the source.
- Approved: Automated consistency checks plus targeted review and sampling are sufficient for normal numeric transcription after Pilot 01 and Pilot 02 samples.

### Factual accuracy

- Approved — Manual Review Required: Transcription confidence does not authorize changing a historically or factually questionable number.
- Approved — Manual Review Required: Default to preserving the original source. Any factual correction requires an explicit human decision and separate evidence.

Pilot approval basis: R017–R023 and P2-R006.

## 10. Page-reference preservation

- Approved: Insert machine-readable page-boundary comments in cleaned Markdown.
- Approved: Use MinerU page_idx as a stable zero-based source identifier.
- Approved: Add printed_page only when source evidence records it; otherwise use unresolved.
- Approved: For cross-page paragraphs, place the page marker inline at the exact original boundary.
- Approved — Manual Review Required: PDF physical page references and missing printed page numbers must be supplied from visual evidence, not inferred from the table of contents.

Pilot approval basis: R025.

## 11. Approved automation boundary

The following may be automated when their evidence conditions are satisfied:

- hash and inventory raw inputs;
- extract DOCX word/media without changing bytes;
- enumerate Markdown image URLs;
- enumerate JSON pages, block order, block types, bounding boxes, discarded blocks, and footnote candidates;
- localize a verified one-to-one image mapping;
- insert page mapping comments;
- remove running headers supported by reliable layout and JSON evidence;
- combine a verified two-line chapter number and title into one logical Markdown heading;
- recover a chapter number supported by multiple independent structural signals;
- join a cross-page paragraph supported by explicit block order, boundary, and running-header evidence;
- validate the expected chapter-opening structure and create a `chapter-opening-layout mismatch` warning;
- skip a confirmed empty parser block while retaining mapping telemetry;
- compare raw and cleaned numeric tokens and route only targeted anomalies plus samples to review;
- remove non-semantic line-end whitespace; and
- report suspected OCR, numbers, footnotes, duplicates, missing pages, and incomplete endings.

The following always require human review:

- every restored footnote;
- every OCR or proper-noun correction;
- every suspicious or mismatched numeric transcription and every sampled numeric item selected for review;
- every factual correction, including changes to numbers, dates, amounts, or percentages;
- every proposed duplicate deletion;
- every ambiguous paragraph join;
- every unexpected chapter-opening or image-layout anomaly;
- every inferred caption;
- every PDF physical page or missing printed-page assignment; and
- every rule approval beyond the conditions recorded here.

## 12. Consolidated rule classification after Pilot 02

### Approved

- raw source preservation;
- MinerU Markdown as the primary text layer;
- JSON as page, block, order, and layout evidence;
- DOCX as embedded-image and visual fallback;
- confirmed running-header removal;
- chapter-number and chapter-title logical normalization;
- structurally supported cross-page paragraph reconstruction;
- image localization and logical image anchoring;
- original layout metadata preservation;
- recurring chapter-opening layout recognition;
- expected chapter-opening image-count and structure validation;
- incomplete-ending detection and preservation;
- page and block mapping;
- blank-page scan artifact removal with confirmed visual evidence;
- parser/instruction leakage removal with structural and visual evidence;
- chapter-number recovery from multiple structural signals;
- empty parser block handling; and
- numeric raw/cleaned consistency checks with targeted review and sampling.

### Approved — Manual Review Required

- every footnote;
- OCR and proper-noun corrections;
- suspicious or mismatched numeric transcriptions and numeric QA samples;
- all factual corrections, including dates, numbers, monetary values, and percentages;
- suspected duplicate-text deletion, with default = preserve;
- ambiguous paragraph reconstruction;
- unexpected image-layout or chapter-opening anomalies;
- unresolved image mappings or inferred captions; and
- visually inferred physical or printed page references.

## 13. Approval record

Stage 2D closes Pilot 01 with R001–R025 approved. R007–R009 remain separate records within one approved footnote-validation class. Approval of a rule that requires future human review does not leave the Pilot 01 review item unresolved.

Stage 3B closes Pilot 02 with P2-R001–P2-R008 approved. Pilot 02 validates the Pilot 01 rules on an 11-page holdout sample with 10 initial rule successes, 0 rule failures, 0 destructive false positives, and no silent prose or image loss. P2-A001–P2-A003 are resolved or classified under the evidence-bounded rules above.

No rule in this guide authorizes translation, full-book parsing, bulk cleaning, unattended OCR correction, or factual correction.
