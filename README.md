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

### Repository visibility policy

- The repository remains Public.
- The project lead has confirmed that authorized original text, images, MinerU output, cleaned source, QA material, and subsequent project translations may be committed and pushed to this Public repository as part of the formal translation project.
- Public accessibility is an approved project condition and must not, by itself, stop later Codex stages or trigger another request to convert the repository to Private.
- Reconsider repository visibility only if new, explicit information conflicts with this recorded authorization.
- Do not change repository visibility as part of normal source, translation, QA, or publishing work.

Public repository visibility does not place the original work, project materials, or translations in the public domain and does not automatically grant third parties permission to reproduce, redistribute, adapt, or commercially use them.

No public-domain status, open-source book license, Creative Commons license, MIT license, or other reuse license is asserted by this repository. Do not add a CC, MIT, or other copyright/software license unless the project lead or supervising teacher explicitly requests it.
