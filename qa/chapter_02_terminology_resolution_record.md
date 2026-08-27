# Chapter 2 Terminology Resolution Record

Stage: Controlled terminology marker resolution audit

Scope: Existing `[[C2-Txxx]]` markers in `translation/chapters/02_chapter_02.md`

Source authority: Locked or approved entries in the project glossary files only

Source hash before audit: `3dedd9702d3f2077e82767bdcb3c8bae552da80a`

Translation hash before audit: `e5b639fdede587bac67ea2db1d47adc204b31087`

## Resolution Controls

- No external research was performed.
- No new terminology decision was created.
- No `proposed` candidate was treated as approved.
- No source file or style guide was modified.
- Replacements were held as an atomic pass: because all existing markers could not be resolved from locked/approved glossary entries, no partial replacement was applied.

## Marker Audit

| Terminology ID | Original marker | Location | Locked/approved English form in glossary | Replacement result |
|---|---|---|---|---|
| C2-T038 | `[[C2-T038: 下关 — English form not locked]]` | CH02-P004 (2 occurrences); CH02-P008 | None | Not applied — candidate remains `proposed`. |
| C2-T039 | `[[C2-T039: 玄海滩 — English form not locked]]` | CH02-P005 | None | Not applied — candidate remains `proposed`. |
| C2-T019 | `[[C2-T019: 早稻田大学政治经济系 — official English form not locked]]` | CH02-P008 | None | Not applied — candidate remains `proposed`. |
| C2-T021 | `[[C2-T021: 英格兰银行 — official English form not locked]]` | CH02-P012 | None | Not applied — candidate remains `proposed`. |
| C2-T025 | `[[C2-T025: 关东大地震 — English event name not locked]]` | CH02-P014 | None | Not applied — candidate remains `proposed`. |
| C2-T041 | `[[C2-T041: 《哪怕是大学毕业》 — English title not locked]]` | CH02-P015 | None | Not applied — candidate remains `proposed`. |
| C2-T012 | `[[C2-T012: 马克思 — English name not locked]]` | CH02-P017 | None | Not applied — candidate remains `proposed`. |
| C2-T013 | `[[C2-T013: 恩格斯 — English name not locked]]` | CH02-P017 | None | Not applied — candidate remains `proposed`. |
| C2-T026 | `[[C2-T026: 九一八事变 — English event name not locked]]` | CH02-P018 | None | Not applied — candidate remains `proposed`. |
| C2-T032 | `[[C2-T032: 满洲国 — English historical name not locked]]` | CH02-P025 | None | Not applied — candidate remains `proposed`. |
| C2-T040 | `[[C2-T040: 《泥土》 — English title not locked]]` | CH02-P028; CH02-P029 | None | Not applied — candidate remains `proposed`. |
| C2-T010 | `[[C2-T010: 李光洙 — English name not locked]]` | CH02-P028 | None | Not applied — candidate remains `proposed`. |
| C2-T042 | `[[C2-T042: 《东亚日报》 — English publication title not locked]]` | CH02-P028 | None | Not applied — candidate remains `proposed`. |
| C2-T034 | `[[C2-T034: 清津 — English place name not locked]]` | CH02-P030 | `Chongjin` (`locked`) | Eligible but not applied — the all-marker pass is blocked by unresolved candidates. |
| C2-T047 | `[[C2-T047: 财务学院速成班 — English institutional description not locked]]`; `[[C2-T047: 首尔财务学院 — English institutional description not locked]]` | CH02-P037; CH02-P053 | `a local bookkeeping school` (`locked`) | Eligible but not applied — the all-marker pass is blocked by unresolved candidates. |

## Audit Summary

- Marker occurrences found: 19
- Unique terminology IDs represented: 15
- IDs with a locked/approved glossary entry: 2
- IDs without a locked/approved glossary entry: 13
- Replacements applied: 0
- Markers remaining: 19

The 13 unresolved IDs are explicitly listed among the candidates outside the approved batch in `qa/chapter_02_terminology_decision.md`. Proposed English forms in research or verification notes do not satisfy the authorization requirement for this pass.

## Integrity Verification

- CH02-P001–CH02-P086 count: 86
- Paragraph order: Unchanged
- Translator notes: Unchanged
- Source hash after audit: `3dedd9702d3f2077e82767bdcb3c8bae552da80a`
- Translation hash after audit: `e5b639fdede587bac67ea2db1d47adc204b31087`
- Source files modified: No
- Translation file modified: No
- STYLE_GUIDE modified: No

## Final Status

**BLOCKED — HUMAN TERMINOLOGY APPROVAL REQUIRED**

This pass cannot reach `PASS` until C2-T010, C2-T012, C2-T013, C2-T019, C2-T021, C2-T025, C2-T026, C2-T032, C2-T038, C2-T039, C2-T040, C2-T041, and C2-T042 receive approved/locked glossary entries.
