# Translation Workflow

The translation directory separates chapter files by review state. Git records every revision; filenames should identify the chapter and language, not informal version labels.

## drafts/

First English drafts produced through AI assistance and human translation work.

Example: 01_chapter_01_en.md

## reviewed/

Translations that have completed at least:

- source-versus-translation meaning review;
- terminology review;
- proper-noun verification;
- dates and numbers review;
- omission review; and
- English editing.

Example: 01_chapter_01_en.md

## final/

Approved chapter files used for book assembly and publishing output.

Example: 01_chapter_01_en.md

Do not create filenames such as final2, final_final, 最新版, or 最终修改版. Move a chapter forward only when it satisfies the documented review requirements, and use Git history for version changes.

Current status: no formal full-book translation has started.
