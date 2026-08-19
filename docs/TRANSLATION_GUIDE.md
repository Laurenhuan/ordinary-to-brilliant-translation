# Translation Guide

This document defines the initial workflow and translation principles for the Chinese-to-English translation of 《从平凡走向辉煌》, provisionally titled From Ordinary to Brilliant.

Status: Initial draft. Update this guide when the team adopts a new project-wide decision.

## 1. Scope and source handling

- Translate only from source material the project is authorized to use.
- Do not add the original copyrighted PDF to this repository.
- Keep authorized raw intermediate material in source/raw/ and cleaned chapter text in source/chapters/.
- Preserve chapter boundaries, headings, notes, captions, and other structural information during source preparation.
- Check cleaned text against the authorized source before translation. Record uncertain OCR or transcription in qa/questions.csv.

## 2. File and status conventions

- Use stable chapter identifiers such as chapter-01, chapter-02, and so on.
- Keep the cleaned Chinese source and English translation in separate files with matching chapter identifiers.
- Treat translations as draft, reviewed, or final. Do not label a chapter final until its open QA questions are resolved or explicitly accepted.
- Keep generated review or publication artifacts in output/, not alongside editable translation files.

## 3. Translation principles

1. Accuracy: Preserve meaning, logic, factual details, emphasis, and relationships between ideas.
2. Natural English: Write idiomatic American English without reproducing Chinese syntax mechanically.
3. Completeness: Do not omit, summarize, or add substantive content unless the change is documented and approved.
4. Voice and tone: Preserve the author's level of formality, narrative distance, and rhetorical force.
5. Terminology: Apply approved terms, names, and organization names consistently. Update the glossary when a recurring choice is made.
6. Context: Translate titles, institutions, historical references, and culture-specific concepts for the intended English reader while retaining necessary specificity.
7. Uncertainty: Do not silently guess. Log ambiguity, damaged source text, conflicting facts, or uncertain terminology in qa/questions.csv.
8. Traceability: Make corrections in the editable source or translation file, then regenerate outputs.

## 4. Workflow

### Step 1 — Prepare the source

- Extract only the authorized material needed for the current chapter.
- Remove page furniture and obvious OCR artifacts without changing meaning.
- Restore paragraphs, headings, notes, lists, and captions.
- Compare the cleaned chapter with the authorized source.

### Step 2 — Register terminology

- Review names, organizations, titles, technical terms, slogans, and repeated phrases.
- Reuse approved entries from glossary/.
- Add new proposals with a status that makes clear whether they are provisional or approved.

### Step 3 — Draft the translation

- Translate by complete thought units while preserving paragraph structure where practical.
- Prefer clear English sentences over word-for-word correspondence.
- Retain deliberate repetition and rhetorical patterns when they serve the author's argument.
- Add unresolved issues to qa/questions.csv instead of embedding private comments in final prose.

### Step 4 — Self-review

- Compare the full draft against the Chinese source for omissions, additions, mistranslations, numbers, names, dates, and references.
- Read the English independently for clarity, flow, tone, and internal logic.
- Check the draft against docs/STYLE_GUIDE.md and the glossary files.

### Step 5 — Editorial and QA review

- Resolve or document every relevant open question.
- Verify terminology and cross-chapter consistency.
- Confirm quotations, notes, tables, captions, and references.
- Record any project-wide decision in the appropriate guide or glossary rather than leaving it only in a commit or discussion.

### Step 6 — Finalize and publish

- Mark a chapter final only after review is complete.
- Generate review or publishing files into output/.
- Perform a final check of structure, formatting, metadata, and copyright status before distribution.

## 5. Quality checklist

A reviewed chapter should:

- contain every translatable element in the source;
- preserve facts, reasoning, tone, and emphasis;
- use approved names and terms consistently;
- follow the style guide for punctuation, numbers, dates, currency, and titles;
- contain no unresolved placeholder text;
- have all remaining exceptions recorded in qa/questions.csv; and
- be readable as polished English without access to the Chinese source.
