# Chapter 2 Source Freeze Verification

Status: **Canonical Source — Frozen for Translation v1**

Stage: Chapter 2 Controlled Source-Freeze Application and Verification

Verification date: 2026-08-24

Translation status: Not started

## Source Freeze Blobs

| State | Git blob |
|---|---|
| Before approved restoration | `5eb890156fd704339fe4a70e8c78acc62ca8fbdf` |
| Frozen source after restoration | `3dedd9702d3f2077e82767bdcb3c8bae552da80a` |

Frozen source: `source/chapters/02_chapter_02.md`

The frozen blob records only the source-structure restoration approved in `qa/chapter_02_source_validation_decision.md`. Any later source correction requires new evidence, an explicit human decision, a QA record, and a new frozen version.

## Applied Changes

1. Restored the `FB-P025` opening text as the continuation of `CH02-P077`.
   - Removed the erroneous H2 extraction markup.
   - Preserved the complete Chinese text without rewriting.
   - Moved the existing `FB-P025` marker inline at its exact cross-page position, following the established Chapter 1 page-boundary convention.
   - Did not add, delete, merge, or renumber a paragraph ID.
2. Restored `FB-F004` at the marker in `CH02-P025` using the approved body from the existing page mapping.
3. Restored `FB-F005` at the marker in `CH02-P030` using the approved body from the existing page mapping.
4. Restored `FB-F006` at the marker in `CH02-P046` using the approved body from the existing page mapping.
5. Replaced the extracted visual marker forms with stable Markdown footnote references while retaining every original `FB-Fxxx` ID and the recorded marker metadata.

No translation, factual correction, OCR correction, terminology decision, or prose rewriting was performed.

## Paragraph Verification

| Check | Expected | Actual | Result |
|---|---:|---:|---|
| Stable paragraph count | 86 | 86 | PASS |
| First paragraph ID | CH02-P001 | CH02-P001 | PASS |
| Last paragraph ID | CH02-P086 | CH02-P086 | PASS |
| Unique IDs | 86 | 86 | PASS |
| Continuous sequence | P001–P086 | P001–P086 | PASS |
| Added paragraph IDs | 0 | 0 | PASS |
| Deleted paragraph IDs | 0 | 0 | PASS |
| Merged paragraph IDs | 0 | 0 | PASS |
| Renumbered paragraph IDs | 0 | 0 | PASS |

The approved cross-page mappings remain unchanged:

- `CH02-P026` / `CH02-P027`
- `CH02-P051` / `CH02-P052`

After removing metadata, Markdown heading syntax, footnote-definition lines, whitespace-only formatting differences, and normalizing the three approved marker representations, all 86 pre-existing paragraph texts compare equal before and after restoration.

`CH02-P077` resolves to the same uninterrupted Chinese sentence before and after normalization:

> 美国福特公司的创始人亨利·福特（1863—1947），也只读到小学毕业。福特的父亲也是希望福特务农，能够帮帮自己，而福特却离家出走到机械工厂做了实习工。

## Page-Boundary Verification

All eight Chapter 2 page-boundary IDs remain present exactly once and in order:

| Page ID | Input PDF page | Printed page | Result |
|---|---:|---:|---|
| FB-P018 | 18 | Unknown | PASS |
| FB-P019 | 19 | 6 | PASS |
| FB-P020 | 20 | 7 | PASS |
| FB-P021 | 21 | 8 | PASS |
| FB-P022 | 22 | 9 | PASS |
| FB-P023 | 23 | 10 | PASS |
| FB-P024 | 24 | 11 | PASS |
| FB-P025 | 25 | 12 | PASS — retained inline within CH02-P077 at the source-corresponding boundary |

Page-boundary count: 8/8. Sequence: exact.

## Footnote Verification

| Footnote ID | Page | Paragraph marker | Restored body | Marker count | Definition count | Result |
|---|---|---|---|---:|---:|---|
| FB-F004 | FB-P020 | CH02-P025 | 现位于中国吉林省。 | 1 | 1 | PASS |
| FB-F005 | FB-P021 | CH02-P030 | 位于现朝鲜民主主义人民共和国咸镜北道东北部，为一港口城市。 | 1 | 1 | PASS |
| FB-F006 | FB-P022 | CH02-P046 | 位于咸镜北道。 | 1 | 1 | PASS |

For each footnote:

- The original `FB-Fxxx` ID is unchanged.
- The source-page metadata is unchanged.
- The marker remains mapped to the approved paragraph.
- One Markdown reference and one Markdown definition are present.
- The body matches the approved existing page-mapping evidence.
- No footnote was translated.

## Image-Anchor Verification

| Image ID | Verified source position | Result |
|---|---|---|
| FB-I006 | Before CH02-P001 | PASS |
| FB-I007 | Between CH02-P001 and CH02-P002 | PASS |

Image-anchor count: 2/2. Both IDs, relative paths, and source ordering are unchanged.

## Chapter 1 Protection

| Protected source | Expected frozen blob | Current blob | Result |
|---|---|---|---|
| `source/chapters/01_chapter_01.md` | `90d3a7ad61585acb88c297cd63fafb864fb08693` | `90d3a7ad61585acb88c297cd63fafb864fb08693` | PASS |

No Chapter 1 file was modified during this stage.

## Unauthorized Change Audit

- Tracked source diff inspected line by line: only the approved P077 structural restoration, three marker normalizations, three footnote-status updates, and three approved footnote bodies are present.
- Existing Chinese paragraph content changed: No.
- Paragraph structure outside the approved P077 restoration changed: No.
- Page-boundary ID added, removed, or reordered: No.
- Image anchor changed: No.
- Glossary changed: No.
- Chapter 1 changed: No.
- Translation file created or changed: No.
- Chapter 2 translation prose created: No.
- Unapproved OCR or factual correction: No.
- Unauthorized change detected: None.

## Remaining Non-Source Work

The source freeze does not resolve Chapter 2 terminology. `丰田喜一郎`, the three context-specific occurrences of `朝鲜`, and the other Proposed candidates recorded in `qa/chapter_02_preparation.md` remain subject to terminology verification. They do not alter the structural freeze result and do not authorize prose translation in this stage.

## Final Gate Decision

**PASS**

- Chapter 2 source is frozen as **Canonical Source — Frozen for Translation v1**.
- Frozen source blob: `3dedd9702d3f2077e82767bdcb3c8bae552da80a`.
- Chapter 2 may proceed to terminology verification.
- Chapter 2 translation has not started and is not authorized by this report alone.
