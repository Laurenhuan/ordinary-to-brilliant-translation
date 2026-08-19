# Source Cleaning Guide

Version: v0.2 — Stage 2C Pilot Rule Approval

The purpose of source cleaning is to produce readable, traceable Markdown without rewriting, translating, fact-correcting, or silently repairing the source text.

## Rule status vocabulary

- Proposed — not yet approved for project use
- Approved — may be applied when its stated evidence conditions are satisfied
- Approved — Manual Review Required — the procedure is accepted, but every affected item must receive human QA before it enters authoritative cleaned or reviewed source
- Rejected — must not be applied

Approval is always limited by the conditions written below. Approved never means that an OCR correction, factual change, ambiguous layout decision, or uncertain mapping may run unattended.

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
- Approved — Manual Review Required: Do not invent captions.
- Proposed: Final handling of character cartoons integrated into page layout remains open under R011–R014. Do not force these cartoons to a fixed paragraph position, treat them automatically as independent figures, or infer final publishing layout from Markdown order.

Pilot approval basis: R010 for localization. R011–R014 remain open for visual-layout treatment.

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
- remove non-semantic line-end whitespace; and
- report suspected OCR, numbers, footnotes, duplicates, missing pages, and incomplete endings.

The following always require human review:

- every restored footnote;
- every OCR or proper-noun correction;
- every numeric, date, amount, percentage, or factual change;
- every proposed duplicate deletion;
- every ambiguous paragraph join;
- every inferred caption or integrated-image layout decision;
- every PDF physical page or missing printed-page assignment; and
- every rule approval beyond the conditions recorded here.

## 12. Approval record

Stage 2C human decisions approve R001–R010 and R015–R025. R007–R009 are approved as one footnote-validation class but remain separate records. R011–R014 remain open as Needs discussion / Awaiting visual review.

No rule in this guide authorizes translation, full-book parsing, bulk cleaning, unattended OCR correction, or factual correction.
