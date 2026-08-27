# Chapter 2 Terminology Human Decision Record

Stage: Chapter 2 Terminology Verification — Human Decision Recording

Decision authority: Project Lead

Decision status: **APPROVED FOR CONTROLLED GLOSSARY LOCK PREPARATION**

Frozen source: `source/chapters/02_chapter_02.md`

Frozen source blob: `3dedd9702d3f2077e82767bdcb3c8bae552da80a`

Translation status: Not started

## Scope and Controls

- This record captures the Project Lead's approved decisions; it does not itself write or lock master-glossary entries.
- Fifteen Chapter 2 candidate IDs are approved in twelve decision groups and are marked `approved_pending_glossary_lock` below.
- No candidate outside this approval set may be inferred to be approved or locked.
- The frozen Chinese source remains unchanged.
- No Chapter 1 file, existing locked glossary entry, or translation draft is modified in this stage.
- Context-sensitive decisions must not be converted into blind global replacements.

## Project-wide Policy Decision

The following policy is approved for Chapter 2 and all future chapters and is recorded in `docs/TRANSLATION_STYLE_GUIDE.md`:

### Historical/Factual Discrepancy Handling

The translation must preserve the source author's statements and must not silently correct historical claims.

When reliable external evidence reveals a discrepancy:

1. Preserve the source identity, date, or statement in the main translation.
2. Add a translator/editor note explaining the discrepancy.
3. Do not rewrite the author's narrative.
4. Allow readers to distinguish the source text from verified historical information.

## Approved Decisions

| Decision | Candidate ID(s) | Chinese term | Approved English / treatment | Application constraint | Lock-preparation status |
|---|---|---|---|---|---|
| D01 | C2-T008 | 丰田喜一郎 | Kiichiro Toyoda | Preserve source dates `(1867–1930)` in the main text and add the approved discrepancy note; do not correct the frozen source. | approved_pending_glossary_lock |
| D02 | C2-T027 | 朝鲜 | P005 `a Korean`; P006 `Korea at the time`; P050 `North Korea` | Context-specific only; no global replacement entry. | approved_pending_glossary_lock |
| D03 | C2-T043, C2-T044 | 角、分 | Render complete amounts in `sen`; e.g. `4角5分钱` → `45 sen` | Add a first-use note on the Japanese-yen subdivision used during the colonial period; do not convert to modern currency. | approved_pending_glossary_lock |
| D04 | C2-T020 | 纽约的美国银行 | an American bank in New York | Descriptive phrase only; do not identify a specific bank. | approved_pending_glossary_lock |
| D05 | C2-T022 | 澳大利亚中央银行 | Australia's central bank | Historical contextual rendering; do not use `Reserve Bank of Australia` here. | approved_pending_glossary_lock |
| D06 | C2-T018 | 福兴商会 | First: `Bokheung Rice Store (Bokheung Sanghoe)`; later: `Bokheung Rice Store` | Retain the first-use/later-use distinction. | approved_pending_glossary_lock |
| D07 | C2-T023, C2-T024 | 世界性经济大恐慌、世界金融危机 | `the Great Depression`; `the global financial crisis` | Keep the two source terms distinct; do not collapse them into one glossary term. | approved_pending_glossary_lock |
| D08 | C2-T033 | 北间岛 | northern Gando | Historical place rendering. | approved_pending_glossary_lock |
| D09 | C2-T035 | 安边 | Anbyon | Use the approved non-diacritic form. | approved_pending_glossary_lock |
| D10 | C2-T028 | 亡国奴 | the misery of a people deprived of their country | Preserve the source's historical and emotional force without a misleading literal label. | approved_pending_glossary_lock |
| D11 | C2-T029 | 四无国家 | a “four-withouts” country | Explain the four missing elements at the first occurrence using only information supplied by the source context. | approved_pending_glossary_lock |
| D12 | C2-T030, C2-T031 | 左翼思想、无产阶级思想 | `leftist thought`; `proletarian ideology` | Keep the two political concepts distinct. | approved_pending_glossary_lock |

## Controlled Note Requirements

### C2-T008 — 丰田喜一郎

Main-text rule:

- Use `Kiichiro Toyoda` for the source's printed identity.
- Retain the source dates `(1867–1930)`.
- Do not rewrite the narrative as though it named Sakichi Toyoda.

Translator/editor note requirement:

> The source appears to conflate Kiichiro Toyoda (1894–1952), founder of Toyota Motor Corporation, with Sakichi Toyoda (1867–1930), inventor of the automatic loom.

The note must be presented as an editorial clarification, separate from the author's narrative. It must not imply that the frozen source has been corrected or assign responsibility for the discrepancy.

### C2-T027 — 朝鲜

| Segment | Approved rendering | Function |
|---|---|---|
| CH02-P005 | `a Korean` | Colonial-period reference to a person |
| CH02-P006 | `Korea at the time` | Historical country/political context |
| CH02-P050 | `North Korea` | Geographic destination in the 1998 context |

These are three occurrence-level decisions, not a reusable equation of `朝鲜` with one English form.

### C2-T043 and C2-T044 — Historical currency

- Treat `角` and `分` as a coordinated amount-level decision rather than independent word substitutions.
- Express the source amounts in `sen`, including `4角5分钱` as `45 sen`.
- At the first relevant occurrence, add a concise translator/editor note explaining that `sen` was the subdivision of the Japanese yen used in the colonial-period monetary context.
- Do not convert the amount into a modern currency or silently modernize its value.

### C2-T018 — 福兴商会

- First occurrence: `Bokheung Rice Store (Bokheung Sanghoe)`.
- Later occurrences: `Bokheung Rice Store`.
- The retained form in parentheses is a historical-name aid, not a second competing glossary translation.

### C2-T029 — 四无国家

Use `a “four-withouts” country` and explain the four missing elements at first occurrence. The explanation must follow the source's own enumeration and must not add an external political interpretation.

## Glossary Lock Preparation

The entries below are ready to be written in a later controlled glossary-lock operation. Their current state is not yet `locked`.

| Candidate ID | Planned master glossary | Lock value / rule to prepare | Current state |
|---|---|---|---|
| C2-T008 | `glossary/people.csv` | `Kiichiro Toyoda`, with source-discrepancy and mandatory-note metadata | approved_pending_glossary_lock |
| C2-T018 | `glossary/organizations.csv` | `Bokheung Rice Store (Bokheung Sanghoe)` first; `Bokheung Rice Store` later | approved_pending_glossary_lock |
| C2-T020 | `glossary/glossary.csv` | Descriptive contextual rule: `an American bank in New York`; no entity identification | approved_pending_glossary_lock |
| C2-T022 | `glossary/glossary.csv` | Historical contextual rule: `Australia's central bank` | approved_pending_glossary_lock |
| C2-T023 | `glossary/glossary.csv` | `the Great Depression` | approved_pending_glossary_lock |
| C2-T024 | `glossary/glossary.csv` | `the global financial crisis`; remain distinct from C2-T023 | approved_pending_glossary_lock |
| C2-T027 | `glossary/glossary.csv` | Three occurrence-level renderings; prohibit global replacement | approved_pending_glossary_lock |
| C2-T028 | `glossary/glossary.csv` | `the misery of a people deprived of their country` | approved_pending_glossary_lock |
| C2-T029 | `glossary/glossary.csv` | `a “four-withouts” country`, with first-use explanation | approved_pending_glossary_lock |
| C2-T030 | `glossary/glossary.csv` | `leftist thought` | approved_pending_glossary_lock |
| C2-T031 | `glossary/glossary.csv` | `proletarian ideology` | approved_pending_glossary_lock |
| C2-T033 | `glossary/glossary.csv` | `northern Gando` | approved_pending_glossary_lock |
| C2-T035 | `glossary/glossary.csv` | `Anbyon` | approved_pending_glossary_lock |
| C2-T043 | `glossary/glossary.csv` | Coordinated `sen` amount rule; no standalone blind replacement | approved_pending_glossary_lock |
| C2-T044 | `glossary/glossary.csv` | Coordinated `sen` amount rule; no standalone blind replacement | approved_pending_glossary_lock |

## Candidates Outside This Approval Batch

The following 23 new Chapter 2 candidates retain their prior `proposed` or `needs_human_decision` status. They are not ready for glossary locking solely on the authority of this record:

`C2-T009`, `C2-T010`, `C2-T011`, `C2-T012`, `C2-T013`, `C2-T014`, `C2-T015`, `C2-T016`, `C2-T017`, `C2-T019`, `C2-T021`, `C2-T025`, `C2-T026`, `C2-T032`, `C2-T034`, `C2-T036`, `C2-T037`, `C2-T038`, `C2-T039`, `C2-T040`, `C2-T041`, `C2-T042`, and `C2-T045`.

The seven Chapter 1 inherited entries (`C2-T001`–`C2-T007`) remain `inherited_locked` and are not relocked by this record.

## Change-Control Confirmation

- Approved decision groups recorded: 12.
- Candidate IDs approved for later controlled lock: 15.
- New master-glossary entries written in this stage: 0.
- Existing locked glossary entries changed: 0.
- Frozen Chapter 2 source changed by this stage: No.
- Chapter 1 files changed by this stage: No.
- Chapter 2 translation draft created: No.
- Chapter 2正文 translation started: No.

## Gate Status

**This approved 15-candidate batch is READY FOR CONTROLLED GLOSSARY LOCKING.**

The remaining 23 new candidates are outside this approval batch and must retain their existing status until separately approved.
