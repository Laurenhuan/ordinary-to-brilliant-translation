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

## Approved rule: classical text title policy

1. Use an established English title when a stable form exists. Chapter 1 examples include `The Analects`, `The Great Learning`, `Elementary Learning`, and `The Thousand-Character Classic`.
2. Retain an established scholarly romanization when it is widely recognizable in scholarship or when no single authoritative translated English title exists. Chapter 1 examples include `Zizhi Tongjian`, `Tongjian Jieyao`, and `Zizhi Tongjian Gangmu`.
3. A first-use English gloss may be approved separately from the master title. The locked master title `Zizhi Tongjian` has the first-use gloss `Comprehensive Mirror in Aid of Governance`; subsequent occurrences use only `Zizhi Tongjian`.
4. A project-created explanatory gloss must never be described as an established title. For `Tongjian Jieyao` and `Zizhi Tongjian Gangmu`, no long translated English title is locked.
5. Classical book titles follow the project's English book-title italicization rule. A parenthetical explanatory gloss is not automatically part of the italicized master title.

Master title, first-use gloss, usage rule, and evidence classification must remain separately traceable in `glossary/glossary.csv`.

## Approved rule: context-sensitive glossary matching

Glossary locking does not authorize blind global string replacement. Matching must consider source punctuation, book-title marking, segment structure, syntax, and sentence context.

The locked Chapter 1 distinction for `小学` is mandatory:

- `《小学》`, when it identifies the classical work, becomes italicized `Elementary Learning`.
- Ordinary `小学` or `小学阶段` becomes `primary school` or `primary-school level`, according to sentence context.

CH01-P015 contains both the classical-title sense and ordinary educational-stage meaning. Later terminology QA must detect and reject erroneous global substitutions.

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

## Contextual translation decision records

Historical institutions, social descriptions, corporate titles, traditional units, and cultural concepts may require a project translation decision even when no official English name exists. Researching a plausible rendering does not verify or lock it.

Each contextual decision record must state:

- the source term and, when present, its frozen-source segment ID;
- the historical and sentence context;
- a provisional candidate and material alternatives;
- the evidence or translation rationale;
- confidence in the recommendation;
- the degree of context dependency;
- whether human approval is required;
- a status of `needs_human_decision` until the project reviewer decides.

Terms prepared for later use but absent from the frozen Chapter 1 source must be labeled project-level preparation terms. They are not added to the 41-item Chapter 1 candidate inventory and may not be treated as source occurrences.

A contextual recommendation must never become an automatic global replacement. In particular:

- historical institution types must not be modernized solely because a modern English label is common;
- a Korean corporate title must be interpreted as a corporate role, not by an unrelated literal sense, while its exact English title remains context-dependent;
- traditional units may be transliterated and briefly glossed, but conversions require a period-specific approved policy;
- an unresolved source-name versus historical-name mapping must remain visible and must not trigger a source correction.

## Approved Chapter 1 cultural-concept decisions

The following Stage 5A.6 decisions are approved and authoritative for Chapter 1:

- `私塾`: first occurrence `a traditional Korean village school known as a seodang`; later occurrences `seodang`. Classification: Korean historical education institution. Do not use `private school`.
- `鸿儒`: `eminent Confucian scholar`. Classification: cultural concept; do not reduce it to ordinary `scholar`.
- `地主`: use `landowner` for a person and `landowning family` for a family. `Landlord` is prohibited for these occurrences.
- `仁、和、乐`: first occurrence `humaneness (ren), harmony (he), and joy (le)`; later occurrences `humaneness`, `harmony`, and `joy`. Do not substitute `kindness / peace / happiness` mechanically.
- `致知在格物`: `the investigation of things and the extension of knowledge`. Do not reorder or simplify the approved English, and do not alter the frozen Chinese source.
- `一勤天下无难事`: `With diligence, no task is impossible.` Classification: approved proverb/quotation translation. It is intentionally not a master-glossary entity; C1-T038 and CULT-CH01-006 are the authoritative records.
- `有志者事竟成`: `Where there is a will, there is a way.` Classification: approved conventional proverb substitution. The intentional English-idiom substitution must remain recorded.

## Proverb Translation Policy

For Chinese and Korean traditional sayings:

- prioritize natural English readability;
- preserve the intended cultural meaning;
- use established English equivalents when appropriate;
- record every substitution decision;
- do not describe a project-created rendering as an established quotation;
- preserve the distinction between a recurring glossary-controlled term and a quotation decision that has been explicitly excluded from the master glossary.

## Review and locking workflow

1. Identify the candidate and bind it to frozen-source segment IDs.
2. Record minimal context and page reference without changing the source.
3. Research according to the hierarchy and record all material evidence.
4. Flag conflicts, ambiguity, and historical-name scope.
5. Human reviewer accepts, rejects, or requests more research.
6. On approval, set `verified_english` and status `verified`.
7. Add or update the correct master glossary entry without duplication.
8. After a separate consistency check, set the authoritative entry to `locked`.

Locked terminology and approved quotation decisions must not be silently changed in translation or editing. Any later change requires a recorded QA decision and synchronized updates to every affected glossary, candidate, QA, and translation occurrence.

General first-mention and later-mention treatment remains undecided unless an item-specific human approval records a binding rule. Approved Chapter 1 rules for `seodang` and `仁、和、乐`, and the `Namihei Odaira` discrepancy note, are binding exceptions. This Stage 5A guide does not otherwise establish English prose style.
