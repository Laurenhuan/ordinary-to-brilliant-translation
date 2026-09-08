# Chapter 4 Source Freeze Record

Stage: Canonical Source — Frozen for Translation v1

Authority: Project Lead approved

Verification status: **PASS**

## Source Identity

- Exact Chinese title: `4 星标面条和阿道汽车修理厂`
- Canonical source: `source/chapters/04_chapter_04.md`
- Frozen source hash: `0b5431282b1e6d60be75a5c0f05543e57d956049`
- FB source-page range: `FB-P034–FB-P041`
- Input PDF page range: `34–41`
- Printed-page information: opening page remains `Unknown`; visible numbered pages are `22–28`. No printed opener number is inferred.
- Paragraph count: 64
- Paragraph range: `CH04-P001–CH04-P064`

## Structural Inventory

- Image anchors: 2 — `FB-I010`, `FB-I011`
- Source footnotes: 3 — `FB-F011`, `FB-F012`, `FB-F013`
- Cross-page continuation pairs: 4 — `P024/P025`, `P035/P036`, `P046/P047`, `P058/P059`
- Captions: none identified
- Next chapter boundary: `FB-P042`, Chapter 5

## Footnote Verification

| ID | Marker mapping | Body verification | Result |
|---|---|---|---|
| FB-F011 | `CH04-P010`, after `岭南` | Exact approved Chinese body restored | PASS |
| FB-F012 | `CH04-P047`, after `年产7000石` | Exact approved Chinese body and numerical statement restored | PASS |
| FB-F013 | `CH04-P052`, after `阿岘洞` | Exact approved Chinese body restored | PASS |

## Cross-Page Verification

| Pair | Continuous source reading | Stable-ID result |
|---|---|---|
| CH04-P024/P025 | `鱼产品的情况。` | Both IDs preserved |
| CH04-P035/P036 | `得出以下经营理念：` | Both IDs preserved |
| CH04-P046/P047 | `朝鲜酿造厂。` | Both IDs preserved |
| CH04-P058/P059 | `一辆掉进过临津江的私人卡车` | Both IDs preserved |

## Intentional Repetition Verification

- `CH04-P001` and its recurrence across `CH04-P035/P036`: preserved.
- `CH04-P002` and `CH04-P037`: preserved exactly.
- `CH04-P003` and `CH04-P038`: preserved exactly.
- `CH04-P004` and its recurrence at the end of `CH04-P062`: preserved exactly.

## Visual Verification

- Paragraph: `CH04-P054`
- Printed form: `私家车、火车、公共汽车`
- Project Lead visual decision: PASS
- `火车` remains unchanged; no OCR correction was applied.

## Protection Audit

- Paragraph IDs are complete, unique, and ordered.
- No paragraph was merged, split, omitted, duplicated, or renumbered.
- Only the three approved source-footnote structures were restored.
- No Chinese prose, punctuation, number, name, date, or factual statement was corrected or rewritten.
- Raw full-book Markdown, JSON, DOCX/PDF-derived evidence, and extraction files remain unchanged.
- Chapters 1–3 remain unchanged.

## Final Status

**Canonical Source — Frozen for Translation v1**

No future source change is permitted without a new explicit Project Lead source-revision decision and a resulting new frozen-source hash.
