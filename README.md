# Authorized Chinese-to-English Book Translation Project

A structured Chinese-to-English book translation project supporting source preservation, document parsing, terminology management, translation consistency, quality assurance, version control, and a reproducible publishing workflow.

## Project purpose

- Preserve authorized source artifacts and their provenance.
- Convert parsed source material into traceable, structurally cleaned Chinese Markdown.
- Manage terminology, people, organizations, and unresolved questions consistently.
- Separate draft, reviewed, and final English translations.
- Keep source preparation, translation, review, and publishing changes traceable with Git.
- Build a reproducible workflow without silently changing source text.

## Project status

Current phase: Stage 4A — Full-book Source Ingestion completed; targeted manual review remains open.

Pilot 01 and Pilot 02 have both passed. The full-book MinerU source was supplied in two batches covering input PDF pages 1–200 and 201–243. All 243 JSON pages, 59 images, front matter, Chapters 1–28, and the afterword are mapped. The raw batches remain separate and immutable.

Chapter 1 Fast Track: **Canonical Source — Frozen for Translation v1**. Pilot 01 and the full-book parse match exactly after normalization, and the two chapter-opening images are byte-identical. Chapter 1 Translation Preparation may begin next; English正文 translation has not started.

The rest of the book is structurally split but is not frozen. Open human decisions are concentrated in `qa/full_book_manual_review.md`, primarily footnotes, blank-page candidates, parser-leakage candidates, and afterword/rear-matter scope.

## Repository structure

| Path | Purpose |
|---|---|
| docs/ | Translation, style, and approved source-cleaning guidance |
| source/raw/ | Immutable MinerU output and associated source artifacts |
| source/chapters/ | Structurally cleaned Chinese source; no translation or rewriting |
| translation/drafts/ | First English drafts produced with AI assistance and human work |
| translation/reviewed/ | Drafts that have completed meaning, terminology, name, number, omission, and English review |
| translation/final/ | Approved chapter files used for book assembly and publishing output |
| glossary/ | General terminology, people, and organization records |
| qa/ | Pilot reports, unresolved questions, and verification records |
| scripts/ | Reproducible source-processing and QA tools |
| output/ | Generated review and publishing artifacts |

Raw source is never overwritten. Changes to structure, page artifacts, image paths, footnotes, or OCR uncertainty markers are written to a separate cleaned source file. Suspected OCR errors, proper nouns, dates, numbers, amounts, and factual claims must be marked and manually verified before correction.

Full-book source uses stable page, paragraph, heading, image, and footnote IDs for source-to-translation alignment. Once translation begins, these IDs must not be silently renumbered.

Translation versions are represented by Git history and the drafts, reviewed, and final directories. Do not create filenames such as final2, final_final, 最新版, or 最终修改版.

## Rights and authorization

This repository contains materials used in an authorized Chinese-to-English book translation project conducted under academic supervision.

Repository access or visibility does not by itself grant additional rights to reproduce, redistribute, adapt, or commercially use the original work or its translation. The repository must not be made public merely because source ingestion is complete.

No public-domain status, open-source book license, Creative Commons license, or other third-party copyright permission is asserted by this repository. Any license or more detailed rights statement must come from the project lead or supervising teacher.
