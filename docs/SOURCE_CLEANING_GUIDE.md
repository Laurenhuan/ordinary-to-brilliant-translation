# Source Cleaning Guide

Status: Proposed v0.1

Every rule in this document is a candidate rule for review. Nothing here is a final full-book standard. The pilot may apply a rule only when the evidence is explicit and the action is recorded in qa/mineru_pilot_01_report.md.

The purpose of source cleaning is to produce readable, traceable Markdown without rewriting, translating, fact-correcting, or silently repairing the source text.

## 1. Raw source preservation

- Proposed: Treat every MinerU input as immutable raw evidence.
- Proposed: Store the Markdown, JSON, and DOCX under a pilot-specific directory with stable names.
- Proposed: Record SHA-256 hashes before any derived file is created.
- Proposed: Never overwrite source.md with text re-parsed from source.docx.
- Proposed: Store only project-authorized source artifacts. The repository may be public under the confirmed project authorization, but public visibility grants no additional license or reuse rights.
- Proposed: Put every cleaning result outside source/raw/.

## 2. Page, header, and footer handling

- Proposed: Use JSON block type, bounding box, repetition, and page position together to identify running headers, footers, and page numbers.
- Proposed: Remove a running header from cleaned Markdown only when it is high-confidence and record the removal in the pilot report.
- Proposed: Do not delete repeated text solely because it appears near a page edge.
- Proposed: Preserve page numbers as mapping metadata even when they are removed from readable text.
- Proposed: If JSON and Markdown disagree, preserve the Markdown text and open a QA item unless the element is an unambiguous page artifact.

## 3. Heading normalization

- Proposed: Treat MinerU heading levels as evidence, not as final document hierarchy.
- Proposed: Combine a chapter number and chapter title only when they are adjacent, on the same page, and clearly form one heading.
- Proposed: Normalize chapter headings to one level in cleaned Markdown.
- Proposed: Do not infer a missing title or rename a chapter from outside knowledge.
- Proposed: Record every structural merge that changes Markdown heading syntax.

## 4. Paragraph handling

- Proposed: Preserve source paragraph order and wording.
- Proposed: Join a page-boundary split only when syntax and JSON ordering show a continuous paragraph with high confidence.
- Proposed: Do not reflow paragraphs for style or readability.
- Proposed: Do not automatically remove repeated passages; a repeated passage may be an intentional chapter opener, standfirst, caption, or design element.
- Proposed: Keep incomplete text when the pilot ends mid-sentence and add a minimal QA marker.

## 5. Image handling

- Proposed: Prefer images embedded in the MinerU DOCX over downloading the same images from a temporary CDN.
- Proposed: Extract word/media entries byte-for-byte without resizing, recompression, cropping, or format conversion.
- Proposed: Map images using three signals where available: DOCX relationship order, Markdown image order, and JSON page/bounding-box order.
- Proposed: Use stable local names such as image_001.jpg in document order.
- Proposed: Replace a CDN URL in cleaned Markdown only after a unique local image mapping is verified.
- Proposed: Preserve an unresolved remote URL and report it rather than substituting a screenshot or guessed image.
- Proposed: Do not invent captions. Preserve a caption only when its relationship to the image is supported by layout or source evidence.

## 6. Footnote handling

- Proposed: Preserve both the footnote marker and footnote body.
- Proposed: Use JSON discarded page-footnote blocks to recover note bodies omitted from Markdown only when the page-level marker-to-note relationship is unambiguous.
- Proposed: Normalize unambiguous markers to stable Markdown footnote IDs that include the MinerU page index.
- Proposed: Do not attach a note to a sentence when multiple markers or multiple note bodies make the relationship uncertain.
- Proposed: Record every restored note and its source page in the QA report.

## 7. OCR uncertainty policy

- Proposed: Never silently correct a suspected OCR error.
- Proposed: Preserve the extracted characters and add a minimal TODO or QA marker when the uncertainty could affect meaning.
- Proposed: Give special review priority to visually similar characters, dates, percentages, decimal points, negative signs, and large-number units.
- Proposed: Separate OCR verification from factual verification. A statement may be faithfully extracted even if it appears surprising.

## 8. Proper noun uncertainty policy

- Proposed: Do not normalize people, places, companies, institutions, book titles, or historical names from memory or external knowledge during source cleaning.
- Proposed: Flag suspicious glyphs and inconsistent forms for comparison with the authorized PDF image.
- Proposed: Keep the raw form in cleaned Markdown until a human verifies the printed source.
- Proposed: Defer terminology approval and translation naming decisions to later project stages.

## 9. Page-reference preservation

- Proposed: Insert machine-readable HTML comments at page boundaries in cleaned Markdown.
- Proposed: Use MinerU page_idx as the stable pilot identifier and state clearly that it is zero-based.
- Proposed: Add printed_page only when JSON explicitly records it; otherwise use unresolved.
- Proposed: For a paragraph that continues across a page boundary, place the page marker inline at the exact break rather than splitting or reordering the text.
- Proposed: Keep a separate mapping table in the QA report with page_idx, printed page, first content, and detected artifacts.

## 10. Manual review requirements

- Proposed: Compare every cleaned pilot page against the authorized PDF before approving rules for broader use.
- Proposed: Review all proper nouns, numbers, dates, percentages, footnotes, image placements, and page-boundary joins.
- Proposed: Confirm whether apparent duplicates are intentional layout content.
- Proposed: Confirm that every image and caption relationship is correct.
- Proposed: Resolve every TODO or explicitly accept it before a cleaned chapter can become an authoritative source.

## 11. Rules that may be automated

The following are Proposed for automation only after pilot approval:

- hash and inventory raw inputs;
- extract DOCX word/media entries without changing bytes;
- enumerate Markdown image URLs;
- enumerate JSON pages, block order, block types, bounding boxes, and discarded blocks;
- replace a CDN URL when a verified one-to-one DOCX/Markdown/JSON mapping exists;
- insert page mapping comments from JSON;
- remove confirmed running headers using exact pilot-specific matches;
- combine an adjacent chapter number and title when the same-page relationship is unambiguous;
- remove line-end whitespace when it changes no source characters or layout meaning; and
- report empty blocks and incomplete final paragraphs without deleting text.

## 12. Rules that must remain manual

- correcting OCR characters;
- changing proper nouns, dates, figures, percentages, or factual claims;
- deciding whether repeated prose is intentional;
- resolving ambiguous paragraph joins or reading order;
- identifying a caption when layout evidence is unclear;
- restoring a footnote when marker-to-body mapping is ambiguous;
- inferring printed page numbers not explicitly recorded in JSON;
- deciding whether a surprising statement is a source error, translation error, or factual error; and
- approving any rule for full-book use.
