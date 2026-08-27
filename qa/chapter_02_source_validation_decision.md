# Chapter 2 Source Validation Decision Record

Stage: Chapter 2 Source Validation and Freeze Preparation — Human Decision Recording

Decision authority: Project Lead

Record status: Decisions recorded; no approved operation has been applied to the source in this stage

Source under review: `source/chapters/02_chapter_02.md`

Source blob at decision-record time: `5eb890156fd704339fe4a70e8c78acc62ca8fbdf`

Preparation record: `qa/chapter_02_preparation.md`

## Scope and Controls

- This record captures Project Lead decisions only.
- No Chapter 2 translation draft is authorized or created in this stage.
- No source text or source structure is changed in this stage.
- No Chapter 1 file is changed.
- No glossary entry or locked terminology decision is added or changed.
- Any approved technical source operation must be applied and verified in a separate, controlled source-freeze stage.

## Decision 1 — Paragraph Structure

**Decision:** Approved

**Applies to:**

- Entire stable range `CH02-P001`–`CH02-P086`
- Cross-page sequence `CH02-P026` / `CH02-P027`
- Cross-page sequence `CH02-P051` / `CH02-P052`
- Preparation items `C2-PREP-R002` and `C2-PREP-R003`

**Approved rule:**

- Retain all 86 stable paragraph IDs.
- Do not merge paragraph IDs.
- Do not delete paragraph IDs.
- Do not renumber paragraph IDs.
- Retain the existing source paragraph mapping across page boundaries.
- During a future authorized translation stage, English syntax may connect naturally across the mapped paragraphs, but source traceability must remain explicit and unchanged.

**Decision status:** Closed — approved for the Chapter 2 source-freeze specification.

**Implementation status:** No source change required at this decision-record stage.

## Decision 2 — CH02-P077 Page Continuation

**Decision:** Approved

**Applies to:**

- `CH02-P077`
- Boundary `FB-P024` / `FB-P025`
- Preparation item `C2-PREP-R004`

**Approved interpretation:**

The text at the beginning of `FB-P025`:

> 己，而福特却离家出走到机械工厂做了实习工。

is a continuation of `CH02-P077`.

**Approved rule:**

- Do not treat the continuation as a new heading.
- Preserve its source wording and meaning.
- In the controlled source-freeze operation, correct only the erroneous Markdown extraction structure.
- Do not alter the source content.
- Retain the `CH02-P077` paragraph ID and the `FB-P025` page-boundary trace.

**Decision status:** Closed — continuation relationship approved.

**Implementation status:** Pending controlled source-freeze application. The current source is unchanged in this stage.

## Decision 3 — Footnote Handling

**Decision:** Approved — Manual Application and Verification Required

**Applies to:**

- `FB-F004` mapped to `CH02-P025` / `FB-P020`
- `FB-F005` mapped to `CH02-P030` / `FB-P021`
- `FB-F006` mapped to `CH02-P046` / `FB-P022`
- Preparation item `C2-PREP-R007`

**Approved mapping evidence:**

| Footnote ID | Paragraph mapping | Approved body source |
|---|---|---|
| FB-F004 | CH02-P025 | Existing page mapping: `① 现位于中国吉林省。` |
| FB-F005 | CH02-P030 | Existing page mapping: `① 位于现朝鲜民主主义人民共和国咸镜北道东北部，为一港口城市。` |
| FB-F006 | CH02-P046 | Existing page mapping: `① 位于咸镜北道。` |

**Approved rule:**

- Restore all three footnotes before Chapter 2 source freeze.
- Preserve each existing Footnote ID.
- Preserve marker-to-paragraph mapping.
- Use the existing page mapping as the restoration evidence.
- Verify restored placement and content before recording the frozen source blob.
- Do not translate the footnotes in this decision-record stage.

**Decision status:** Closed — restoration and mappings approved.

**Implementation status:** Pending controlled source-freeze application and verification. No footnote was inserted into the source in this stage.

## Decision 4 — Chapter 1 Locked Terminology Inheritance

**Decision:** Approved

The following locked English forms remain binding in Chapter 2:

| Source entity | Inherited locked English |
|---|---|
| 李秉哲 | Lee Byung-chull |
| 郑周永 | Chung Ju-yung |
| 小源浪平 | Namihei Odaira |
| 盛田昭夫 | Akio Morita |
| 索尼 | Sony |
| 日立集团 | Hitachi Group |
| 早稻田大学 | Waseda University |

**Approved rule:**

- Do not research or select replacement English forms for these entities.
- Existing Chapter 1 notes, context rules, and discrepancy records continue to govern their use.
- Terminology inheritance does not authorize translation in this stage.

**Decision status:** Closed — inheritance confirmed.

**Implementation status:** No glossary change required.

## Decision 5 — New Terminology Verification

**Decision:** Remains Proposed / Unverified

**Candidate:** `丰田喜一郎`

**Applies to:** `CH02-P079`–`CH02-P081`; preparation item `C2-PREP-T006` and the terminology portion of `C2-PREP-R009`.

**Approved rule:**

- Send the candidate through the Chapter 2 terminology-verification workflow.
- Do not select, verify, or lock an English form in this stage.
- Do not infer the English identity from model knowledge.
- Preserve the source text unchanged.

**Decision status:** Open — terminology verification required.

## Decision 6 — 朝鲜 Context Treatment

**Decision:** Context-sensitive rule confirmed

**Locations requiring separate pre-translation review:**

- `CH02-P005`
- `CH02-P006`
- `CH02-P050`

**Approved rule:**

- Do not perform a global or blind replacement of `朝鲜`.
- Determine the appropriate English rendering from each sentence's historical, geographic, or adjectival meaning.
- Record each contextual decision before translating the affected paragraph.
- Do not change the source text or create a new locked replacement in this stage.

**Decision status:** Policy closed; occurrence-level decisions remain open.

## Source Validation Issue Disposition

| Preparation item | Decision outcome | Current state |
|---|---|---|
| C2-PREP-R002 | Stable split mapping approved for P026/P027 | Decision closed; no source edit required |
| C2-PREP-R003 | Stable split mapping approved for P051/P052 | Decision closed; no source edit required |
| C2-PREP-R004 | P077 continuation relationship approved | Decision closed; technical Markdown correction pending freeze operation |
| C2-PREP-R007 | FB-F004–FB-F006 restoration and mappings approved | Decision closed; restoration and verification pending freeze operation |
| Chapter 1 locked-form inheritance | Existing forms confirmed | Closed; no glossary edit required |
| C2-PREP-R009 / C2-PREP-T006 | `丰田喜一郎` remains unverified | Open terminology item |
| C2-PREP-R010 | Context-sensitive policy confirmed | P005, P006, and P050 remain open for individual decisions |

Other preparation findings not explicitly decided by the Project Lead in this record retain their prior status in `qa/chapter_02_preparation.md`.

## Remaining Terminology Verification

At minimum, the following explicitly identified items remain unresolved after this decision round:

1. `丰田喜一郎` — authoritative identity and English-form verification.
2. `朝鲜` in `CH02-P005` — individual contextual rendering.
3. `朝鲜` in `CH02-P006` — individual contextual rendering.
4. `朝鲜` in `CH02-P050` — individual contextual rendering.

All other Chapter 2 provisional candidates in `qa/chapter_02_preparation.md` remain Proposed / unverified unless a later human-approved terminology record changes their status.

## Source Freeze Readiness

**Decision gate:** Passed for the paragraph structure, P077 continuation, and FB-F004–FB-F006 handling addressed in this round.

**Operational freeze status:** Not yet complete.

Chapter 2 may proceed to a controlled source-freeze application and verification stage, but it is not yet a frozen source because this stage intentionally made no source changes. Before freeze completion, the approved technical operations must be applied non-destructively, all 86 paragraph mappings and page boundaries must be rechecked, all three footnotes must be verified, and a final source blob must be recorded.

Terminology verification remains a separate pre-translation gate and does not authorize prose translation.

## Stage Result

- Human source-validation decisions recorded: 6
- Translation started: No
- Source modified: No
- Chapter 1 modified: No
- Glossary modified: No
- New locked terminology added: No
- Chapter 2 frozen: No
- Next permitted action: controlled Chapter 2 source-freeze application and verification, followed by terminology verification
