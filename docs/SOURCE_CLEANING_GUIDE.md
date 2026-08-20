# Source Cleaning Guide

Version: v0.3 — Stage 2D Pilot 01 Closure

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

## 3. Heading normalization

- Approved: Treat MinerU heading levels as structural evidence rather than final Markdown hierarchy.
- Approved: A chapter number and chapter name may remain on separate visual lines in the original book while forming one logical chapter heading.
- Approved: When the number and name are adjacent, share the same visual role, and JSON/DOCX order supports one heading, cleaned Markdown may combine them into one logical heading.
- Approved: Combining the logical heading must not change, translate, correct, or otherwise rewrite the chapter-number or chapter-title text.
- Approved: Record every structural heading merge in QA.
- Approved: Do not infer missing headings or rename chapters from outside knowledge.

Pilot approval basis: R005.

## 4. Paragraph handling

- Approved: Preserve source paragraph order and wording.
- Approved: Reconstruct a cross-page paragraph only when JSON block order, the page boundary, adjacent fragments, and reliable running-header evidence support the join.
- Approved: Semantic plausibility alone is insufficient evidence for an automatic join.
- Approved: Preserve an inline page marker at the exact boundary when a paragraph is joined across pages.
- Approved: Do not reflow or rewrite Chinese paragraphs for style or readability.
- Approved — Manual Review Required: Keep incomplete text and add a QA marker until the source boundary is visually confirmed.
- Approved — Manual Review Required: Any paragraph reconstruction that lacks explicit block-order, page-boundary, or artifact evidence is ambiguous and must not be applied without human approval.

Pilot approval basis: R006 and R024.

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

Pilot approval basis: R016.

## 9. Numbers, dates, and facts

- Approved: Automatically detect and queue dates, years, amounts, percentages, counts, page references, and unusual numeric units for QA.
- Approved — Manual Review Required: Verify digits, signs, punctuation, units, and source glyphs against the visual source.
- Approved — Manual Review Required: Do not automatically change a number, date, amount, percentage, name, or factual claim.
- Approved — Manual Review Required: Keep visual transcription verification separate from historical or factual verification.

Pilot approval basis: R017–R023.

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
- join a cross-page paragraph supported by explicit block order, boundary, and running-header evidence;
- validate the expected chapter-opening structure and create a `chapter-opening-layout mismatch` warning;
- remove non-semantic line-end whitespace; and
- report suspected OCR, numbers, footnotes, duplicates, missing pages, and incomplete endings.

The following always require human review:

- every restored footnote;
- every OCR or proper-noun correction;
- every numeric, date, amount, percentage, or factual change;
- every proposed duplicate deletion;
- every ambiguous paragraph join;
- every unexpected chapter-opening or image-layout anomaly;
- every inferred caption;
- every PDF physical page or missing printed-page assignment; and
- every rule approval beyond the conditions recorded here.

## 12. Pilot 01 final rule classification

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
- incomplete-ending detection and preservation; and
- page and block mapping.

### Approved — Manual Review Required

- every footnote;
- OCR and proper-noun corrections;
- dates, numbers, monetary values, percentages, and factual corrections;
- suspected duplicate-text deletion, with default = preserve;
- ambiguous paragraph reconstruction;
- unexpected image-layout or chapter-opening anomalies;
- unresolved image mappings or inferred captions; and
- visually inferred physical or printed page references.

## 13. Approval record

Stage 2D closes Pilot 01 with R001–R025 approved. R007–R009 remain separate records within one approved footnote-validation class. Approval of a rule that requires future human review does not leave the Pilot 01 review item unresolved.

No rule in this guide authorizes translation, full-book parsing, bulk cleaning, unattended OCR correction, or factual correction.
