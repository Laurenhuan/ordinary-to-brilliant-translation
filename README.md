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

Current phase: Stage 2C — Pilot Rule Approval.

Human decisions have approved 21 of the 25 Pilot 01 review items. R011–R014 remain open for discussion of integrated character-cartoon layout. The project has not entered a second pilot, full-book parsing, or translation.

## Repository structure

| Path | Purpose |
|---|---|
| docs/ | Translation, style, and proposed source-cleaning guidance |
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

Translation versions are represented by Git history and the drafts, reviewed, and final directories. Do not create filenames such as final2, final_final, 最新版, or 最终修改版.

## Rights and authorization

This repository contains materials used in an authorized Chinese-to-English book translation project conducted under academic supervision.

Public availability of this repository does not by itself grant additional rights to reproduce, redistribute, adapt, or commercially use the original work or its translation.

No public-domain status, open-source book license, Creative Commons license, or other third-party copyright permission is asserted by this repository. Any license or more detailed rights statement must come from the project lead or supervising teacher.
