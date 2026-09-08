# Chapter 4 Source Validation Report

Stage: Chapter 4 Source QA before freeze

Status: **RESOLVED — SOURCE QA PASS**

Source candidate: `source/chapters/04_chapter_04.md`

Pre-restoration candidate blob: `baa8cd21de3543074eb6fb7d15d4a9dc33e4f94c`

Project Lead approval and controlled restoration are recorded in `qa/chapter_04_source_decision.md`. The final frozen-source hash is recorded in `qa/chapter_04_source_freeze.md`.

## Boundary Verification

| Field | Verified result |
|---|---|
| Exact Chinese title | `4 星标面条和阿道汽车修理厂` |
| Starting boundary | `FB-P034`, after Chapter 3 ends on `FB-P033` |
| Ending boundary | End of `FB-P041`, after `CH04-P064` |
| Next chapter boundary | `FB-P042`, `5 三星物产公司和现代汽车工业公司` |
| FB source-page range | `FB-P034–FB-P041` |
| Input PDF page range | `34–41` |
| Printed-page range | Opening page number not visibly recorded (`Unknown` in the page map; TOC and sequence indicate page 21); visible numbered pages `22–28` |
| Stable paragraph range | `CH04-P001–CH04-P064` |
| Paragraph count | 64 |
| Paragraph ID order | Complete, unique, and ordered |
| Images | 2: `FB-I010`, `FB-I011` |
| Image mapping | Both verified one-to-one against JSON and DOCX media |
| Captions | None identified |
| Footnote candidates | 3: `FB-F011–FB-F013` |

## Structural QA

- The chapter start, ending, and next-chapter boundary are unambiguous.
- All eight source pages, `FB-P034–FB-P041`, are present and ordered.
- The source candidate contains 64 unique stable paragraph IDs with no missing or duplicate ID.
- The two localized image anchors remain on `FB-P034`; no caption block is recorded.
- Running headers on later pages are excluded under the existing approved running-header rule.
- No source wording has been changed during this validation pass.

## Intentional Repetition and Special Structures

The following repeated structures appear intentional and must not be deduplicated:

- `CH04-P001` is repeated across the page-boundary pair `CH04-P035`/`CH04-P036`.
- `CH04-P002` is repeated as `CH04-P037`.
- `CH04-P003` is repeated as `CH04-P038`.
- The full text of `CH04-P004` recurs at the end of `CH04-P062`, after new contextual material.

The following cross-page continuations preserve separate stable IDs and were approved by the Project Lead:

| Decision ID | Boundary | Raw ending / beginning | Continuous reading | Proposed structural treatment |
|---|---|---|---|---|
| CH04-SD-001 | `FB-P036` → `FB-P037` | `CH04-P024`: `鱼产` / `CH04-P025`: `品的情况。` | `鱼产品的情况。` | Preserve both IDs; treat as one syntactically continuous source sentence. |
| CH04-SD-002 | `FB-P037` → `FB-P038` | `CH04-P035`: `得出以` / `CH04-P036`: `下经营理念：` | `得出以下经营理念：` | Preserve both IDs; treat as one syntactically continuous source sentence. |
| CH04-SD-003 | `FB-P038` → `FB-P039` | `CH04-P046`: `朝鲜酿` / `CH04-P047`: `造厂。` | `朝鲜酿造厂。` | Preserve both IDs; treat as one syntactically continuous source sentence. |
| CH04-SD-004 | `FB-P040` → `FB-P041` | `CH04-P058`: `一辆掉进` / `CH04-P059`: `过临津江的私人卡车` | `一辆掉进过临津江的私人卡车` | Preserve both IDs; treat as one syntactically continuous source sentence. |

## Human Decisions — Approved

### CH04-SD-005 — FB-F011 Footnote Restoration

- Source page: `FB-P035`
- Marker location: `CH04-P010`, immediately after `岭南`
- JSON body: `① 韩国的鸟岭以南地区，主要是庆尚南道地区。`
- Existing QA status: `candidate — manual review required`
- Decision required: Approve or reject the marker-to-body mapping and restoration under ID `FB-F011`.

### CH04-SD-006 — FB-F012 Footnote Restoration

- Source page: `FB-P039`
- Marker location: `CH04-P047`, immediately after `年产7000石`
- JSON body: `① 石是韩国谷物和液体的容量单位，1石=47.6加仑，1加仑=4升。`
- Existing QA status: `candidate — manual review required`
- Decision required: Approve or reject the marker-to-body mapping and restoration under ID `FB-F012`.

### CH04-SD-007 — FB-F013 Footnote Restoration

- Source page: `FB-P039`
- Marker location: `CH04-P052`, immediately after `阿岘洞`
- JSON body: `② 首尔地名。`
- Existing QA status: `candidate — manual review required`
- Decision required: Approve or reject the marker-to-body mapping and restoration under ID `FB-F013`.

### CH04-SD-008 — OCR Visual Verification

- Source page: `FB-P040`
- Paragraph: `CH04-P054`
- Current source context: `1945 年解放的时候，私家车、火车、公共汽车合在一起一共是 7386 辆`
- Issue: `火车` is contextually suspicious in a vehicle-count list and may be an OCR glyph error, but Markdown and JSON do not provide independent visual confirmation.
- Required action: Compare the phrase directly with the authorized PDF page. Preserve `火车` unless the visual source clearly supports a different printed character.
- No factual or commonsense correction is authorized.

### CH04-SD-009 — Cross-Page Stable-ID Treatment

- Scope: `CH04-SD-001–CH04-SD-004`
- Decision required: Approve preserving each pair as two stable IDs while treating its text as a continuous syntactic unit during later translation.
- No source words are to be merged, deleted, or rewritten.

## Freeze Gate

**PASS**

- `FB-F011–FB-F013` were approved and restored with exact marker/body mappings.
- The four cross-page stable-ID continuations were approved without merging or renumbering.
- The Project Lead visually confirmed that `CH04-P054` prints `私家车、火车、公共汽车`; `火车` remains unchanged.
- Final frozen source hash: `0b5431282b1e6d60be75a5c0f05543e57d956049`.
- Chapter 4 terminology auditing is authorized after this source-freeze PASS.
