# Terminology and Proper-Name Verification Guide

Status: Stage 5A working policy. This guide governs terminology research before translation. It does not authorize prose translation or changes to frozen Chinese source files.

## Core rule

A plausible machine-generated English form is not a verification source. Every retained English form must be traceable to recorded evidence or to an explicit project decision. Research may produce a candidate, but only human review may move an entry to `verified` or `locked`.

## Verification hierarchy

Use the strongest source reasonably available, in this order:

1. A person's or organization's own official English usage.
2. An official institutional source, including government, university, museum, foundation, archive, or memorial sources.
3. An authoritative English-language historical or academic source.
4. A widely established conventional English form documented by reliable reference works.
5. A documented standard romanization or translation rule.
6. A project-specific translation decision approved by the project lead.

One source is not automatically sufficient. Record material variants, historical-name scope, and conflicts instead of silently selecting the first form found.

## Approved rule: established English form priority

For personal names, an established official or conventional English form takes priority over mechanical romanization and over any universal East-Asian name-order rule. Locked forms may therefore legitimately follow different ordering, capitalization, spacing, and hyphenation conventions. Examples already approved by the project include `Lee Byung-chull`, `Chung Ju-yung`, `Akio Morita`, and `Namihei Odaira`.

Do not normalize these locked forms merely to make them look uniform. The correct project form is the evidence-backed form recorded in `glossary/people.csv`.

## Approved rule: Korean names without established English forms

1. If a person has an established official or conventional English form, use that form under the established-English-form priority rule.
2. If reasonable research finds no stable established English form:
   - first verify the Korean name;
   - then generate the English form using the project-approved Korean romanization convention;
   - retain a project-established common surname form where applicable, such as `Lee`;
   - mark the glossary `evidence_type` explicitly as `project romanization based on verified Korean name`;
   - never describe the resulting project form as the person's official English name.
3. If an authoritative established English form is found later, it may replace the project romanization only after QA review and synchronized glossary updates.

Project romanization is an editorially approved controlled form, not evidence of a person's own English usage. The verified Korean source form, the project-generated English form, and the supporting evidence classification must remain separately traceable.

## Candidate record requirements

Each candidate must retain:

- a stable candidate ID;
- the exact Chinese source term;
- a controlled type;
- one or more frozen-source segment IDs;
- only the minimum context needed for identification;
- a source-page reference when available;
- current workflow status;
- a candidate English form, if research supports one;
- a separate verified English field;
- evidence type and a retrievable source URL or bibliographic reference;
- evidence confidence, recommendation, human decision, and decision note;
- any conflict flag and the intended master glossary file.

The `candidate_english` and `verified_english` fields are deliberately separate. A researched candidate must not be copied into `verified_english` without human approval.

## Status values

- `pending`: identified but not yet researched.
- `researched`: one or more credible sources have been recorded; no final approval is implied.
- `verified`: a human reviewer has accepted the evidence and English form for the stated context.
- `locked`: the verified form has become the project-authoritative glossary form.
- `needs_context`: source identity, source glyph, sense, date, or historical scope must be clarified first.
- `needs_human_decision`: evidence or translation options exist, but the project must choose among them.

Only a human reviewer may assign `verified` or `locked`.

## Category rules

### Person

Prefer stable English usage from the person, company, foundation, memorial institution, or an authoritative biography. Record surname order, capitalization, hyphenation, and spacing variants. Do not mechanically replace an established English name with a new romanization. If the Chinese source glyph may be wrong, verify the authorized visual source before mapping the name to an English entity.

### Verified source-text proper-name discrepancy

When human visual review confirms that the authorized Chinese edition prints a form different from the name used in authoritative entity records:

- treat the printed Chinese form as verified source text, not as an OCR error;
- do not alter the frozen Chinese source;
- record both the Chinese edition's printed form and the verified entity form;
- use the approved locked English entity name in translation;
- add a neutral translator/editor note at the first relevant occurrence when the discrepancy materially affects identification;
- do not claim that the author made the error when the stage at which the discrepancy arose is unknown.

Chapter 1 application: the Chinese edition prints `小源浪平`; Hitachi records identify the founder as `小平浪平` (`Namihei Odaira`). The English translation uses `Namihei Odaira`, with the approved neutral note policy above.

### Organization

Prefer the official English name used in the historical period concerned. A modern corporate name must not silently replace a historical entity. Record merger, predecessor, successor, brand, group, and legal-entity distinctions when relevant.

### Place

Prefer an authoritative English place name or the relevant Korean official romanization. Historical jurisdictions and historical-period names must remain context-sensitive; current administrative names cannot automatically replace them.

### School

Use the institution's official English name when it exists. For historical schools, academies, and local schools, first establish the institution type and name in the source language; do not translate a generic institution label mechanically.

### Historical term

Prefer established usage in authoritative historical or academic sources. Record date range and political-geographic context. Do not fact-correct the frozen source while establishing an English label.

### Classical text

Prefer titles established in English-language scholarship. When multiple well-known titles exist, record all supported variants and the sources for each, then obtain a project decision on title, article, capitalization, italicization, transliteration, and first-use gloss.

### Title or role

Do not force a context-dependent social description, honorific, or role into a universal one-to-one translation. Record a glossary default only if its limits and contextual exceptions are explicit.

### Unit

Verify the historical and regional unit before choosing among translation, transliteration, conversion, or brief gloss. Never change a source number as part of terminology handling. Conversions require an approved policy and must remain distinguishable from the source quantity.

### Cultural concept

Translation, transliteration, a brief gloss, or retention of the source term may all be valid. Classical provenance, rhetorical function, and first-use/later-use treatment require human review.

### Other

Use for authorial labels or items that do not yet fit a stable category. Record the sentence function and obtain a project-specific decision rather than manufacturing an established term.

## Conflict detection

Check at least the following before verification and again before locking:

- same Chinese source term mapped to different English forms;
- different Chinese forms that may refer to the same entity;
- capitalization, spacing, hyphenation, or surname-order differences;
- modern organization name substituted for a historical entity;
- classical-title variants;
- a source glyph or OCR uncertainty that undermines entity mapping.

Conflicts are reported, not silently normalized. A locked master-glossary entry is authoritative only after the conflict record is resolved or explicitly accepted.

## Relationship to master glossaries

- `glossary/people.csv` is the master list for people.
- `glossary/organizations.csv` is the master list for organizations and schools.
- `glossary/glossary.csv` is the master list for other controlled terminology.

Chapter candidate files are research queues, not competing master glossaries. Before adding a locked entry, search all three master files for identical Chinese terms, aliases, and English-form variants. Do not create different English spellings for the same person or entity across files.

## Review and locking workflow

1. Identify the candidate and bind it to frozen-source segment IDs.
2. Record minimal context and page reference without changing the source.
3. Research according to the hierarchy and record all material evidence.
4. Flag conflicts, ambiguity, and historical-name scope.
5. Human reviewer accepts, rejects, or requests more research.
6. On approval, set `verified_english` and status `verified`.
7. Add or update the correct master glossary entry without duplication.
8. After a separate consistency check, set the authoritative entry to `locked`.

Locked terminology must not be silently changed in translation or editing. Any later change requires a recorded QA decision and synchronized updates to every affected glossary and translation occurrence.

General first-mention and later-mention treatment remains undecided and must be approved separately. Item-specific note decisions already recorded in a locked glossary entry, including the Chapter 1 `Namihei Odaira` discrepancy note, remain binding. This Stage 5A guide does not otherwise establish English prose style.
