# Source-processing scripts

Stage 4A reproducible order:

1. `python scripts/full_book_ingest.py`
2. `python scripts/full_book_chapter_split.py`
3. `python scripts/freeze_chapter_01.py`
4. `python scripts/add_source_segment_ids.py`
5. `python scripts/check_full_book_numbers.py`
6. `python scripts/build_full_book_manual_review.py`

Run these only against the authorized repository copy. Review Git diffs after every generation step.

- `full_book_ingest.py` inventories immutable raw inputs, extracts DOCX `word/media` entries byte-for-byte, and builds page/image/footnote mappings.
- `full_book_chapter_split.py` slices text from MinerU Markdown using JSON page anchors, localizes verified images, removes only evidence-supported running headers, and preserves ambiguous content with QA markers.
- `freeze_chapter_01.py` refuses to freeze unless Pilot 01 and full-book Chapter 1 normalized text and image hashes match.
- `add_source_segment_ids.py` assigns stable logical paragraph IDs after the freeze step. Do not rerun it after translation starts without an explicit ID-migration review.
- `check_full_book_numbers.py` compares raw and cleaned numeric tokens page-by-page while excluding metadata IDs and image paths.
- `build_full_book_manual_review.py` generates the focused open-review register from stable mapping IDs.

No script translates正文, corrects OCR, fact-checks the book, deletes repeated prose, approves footnotes, or rewrites raw Markdown/JSON/DOCX.
