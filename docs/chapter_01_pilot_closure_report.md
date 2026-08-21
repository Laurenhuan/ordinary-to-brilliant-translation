# Chapter 1 Pilot Closure Report

Stage: 5C.1 — Resolve Remaining Chapter 1 Terminology and Close the Style Pilot

Status: Complete — terminology closed; pilot drafts remain in `translation/drafts/`

Canonical source: `source/chapters/01_chapter_01.md`

Frozen source blob: `90d3a7ad61585acb88c297cd63fafb864fb08693`

## 1. Pilot purpose and scope

The Chapter 1 style pilot tested three deliberately limited kinds of prose before any full-chapter translation was authorized. Every translated passage retains its `CH01-Pxxx` mapping to the frozen source.

### Segment A — Biography narrative test

- Scope: CH01-P004–CH01-P007
- Focus: personal names, places, family background, and historical narration
- Outcome: established natural English biography narration as the baseline while preserving all factual and social information.

### Segment B — Cultural translation test

- Scope: CH01-P014–CH01-P018
- Focus: `seodang`, classical Chinese texts, Joseon historical context, and Confucian education terminology
- Outcome: established first-use cultural explanation, later-use short forms, approved classical-title handling, and context-sensitive historical terminology.

### Segment C — Philosophical and business-value translation test

- Scope: CH01-P025–CH01-P026
- Focus: Confucian concepts, abstract values, and corporate-value expression
- Outcome: established concept-preserving English phrasing for `humaneness (ren), harmony (he), and joy (le)` and a natural business-value register without unsupported explanation.

No paragraph outside these three pilot regions was translated during the pilot.

## 2. Translation rules established by the pilot

1. Biography passages should use natural English narrative rather than reproduce Chinese sentence order mechanically.
2. Natural restructuring may improve rhythm, but it must not remove, add, or factually reinterpret source information.
3. Cultural terms should preserve the source concept when an ordinary English substitution would be misleading. When approved, the first occurrence supplies a concise explanation and later occurrences use the shortened locked form.
4. Classical Chinese book titles must use their approved English or romanized forms and be italicized as standalone titles.
5. Personal names and place names must follow locked glossary forms, including established English forms and approved context-sensitive geographic rules.
6. Philosophical concepts must preserve their conceptual meaning without unnecessary explanation or mechanical substitution with superficially similar English words.
7. Approved conventional proverb substitutions may be used only when recorded. Project-created quotation translations must not be presented as established English proverbs.
8. Paragraph IDs, page references, image anchors, and footnote references must remain traceable wherever they occur.
9. Draft QA markers must be resolved through recorded decisions before final translation. No unresolved Chapter 1 terminology marker remains after Stage 5C.1.

## 3. Locked terminology summary

The Chapter 1 candidate inventory contains 41 unique source terms. After Stage 5C.1, all 41 are `locked` and none remains `needs_human_decision`.

### Personal names

Locked personal-name forms include `Lee Byung-chull`, `Chung Ju-yung`, `Akio Morita`, `Namihei Odaira`, `Lee Chan-woo`, `Lee Hong-seok`, `Kim Ok-gyun`, and `Li Hongzhang`. Established official or conventional English forms take priority over mechanical romanization; project romanizations remain explicitly identified as such.

### Places and historical geography

Locked forms include `Japan`, `Gyeongsangnam-do`, `Uiryeong`, `Gangwon Province`, `Tongcheon County`, `Shanghai`, and `Cheongun-dong`. `朝鲜` remains a locked context-sensitive rule: use `Joseon period`, `Joseon Dynasty`, `Korean people`, `Korean Peninsula`, `Korea`, or `Korean` according to the source sentence rather than applying a blind replacement.

### Cultural and historical terminology

- `私塾`: first `a traditional Korean village school known as a seodang`; later `seodang`
- `文山亭书院`: `Munsanjeong, a seodang`, with additional source-supported explanation only when the sentence contains it
- Joseon-period terms: use the separately locked period and context-sensitive forms
- `仁、和、乐`: first `humaneness (ren), harmony (he), and joy (le)`; later `humaneness`, `harmony`, and `joy`
- Classical titles: follow the locked titles and italicization rules recorded in the master glossary and translation style guide

### Final four Stage 5C.1 decisions

| Candidate ID | Chinese | Locked English | Binding rule |
|---|---|---|---|
| C1-T011 | 东和旅馆 | Donghwa Inn | Use `Inn`, not `Hotel`, for the historical lodging establishment. |
| C1-T014 | 松田小学 | Songjeon Elementary School | Use the standard English school-category rendering; do not use `Songjeon School`. |
| C1-T035 | 石 | seok | First `seok (a traditional Korean grain measure)`; later `seok`. Do not convert to modern weight units. |
| C1-T041 | 商界三大神话 | the three great myths of Korean business | Treat as an authorial expression; do not use `mythology`, `miracles`, or `legends`. |

Master records are maintained in `glossary/people.csv`, `glossary/organizations.csv`, and `glossary/glossary.csv`. The complete 41-item audit trail remains in `glossary/chapter_01_candidates.csv`. C1-T038 is intentionally controlled as a locked candidate and QA quotation decision rather than duplicated as a master-glossary entity.

## 4. Remaining unresolved terminology

No unresolved Chapter 1 terminology candidates remain after Stage 5C.1.

- `locked`: 41
- `needs_human_decision`: 0
- Open terminology conflicts: 0

All Chapter 1 glossary candidates are locked. This terminology closure does not convert the draft translation into a reviewed or final artifact.

## 5. Rules for the full Chapter 1 translation stage

Any future full Chapter 1 translation must:

1. use the frozen source whose blob is `90d3a7ad61585acb88c297cd63fafb864fb08693`;
2. preserve every source paragraph ID and maintain page, image, and footnote traceability;
3. follow all locked glossary decisions and recorded context-sensitive usage rules;
4. preserve translation review records and add stable QA IDs for new issues;
5. proceed in controlled, reviewable batches rather than as an unreviewed full-chapter rewrite;
6. leave the frozen source files unchanged;
7. keep draft material out of `translation/final/` until separately reviewed and approved; and
8. avoid silently correcting source facts, names, numbers, or historical claims.

## Closure statement

The Chapter 1 style pilot and its terminology-preparation phase are closed. The project has a frozen canonical source, reviewed style examples across three prose types, a complete 41-item locked terminology inventory, and a traceable QA record. Full Chapter 1 translation may begin only under a separately authorized next stage.
