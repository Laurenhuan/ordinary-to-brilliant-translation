# Chapter 1 Stage 6B.3 Verification Report

## Summary

- Verification status: Passed
- Phase 2 compliance: 14/14 decisions verified; 10 accepted changes and 1 modified change were applied, and 3 rejected proposals were retained without translation changes.
- Unauthorized changes: None detected.
- Source changes: None. The frozen source blob remains `90d3a7ad61585acb88c297cd63fafb864fb08693` at the Phase 1 commit, the Phase 2 commit, and the current working tree.
- Glossary changes: None. `chapter_01_candidates.csv`, `people.csv`, `organizations.csv`, and `glossary.csv` have identical blobs at the Phase 1 and Phase 2 commits and in the current working tree.
- Existing-file changes during Stage 6B.3: None. This report is the only Stage 6B.3 artifact.
- Verification basis: Phase 1 decision state `9f93913d7e777b8b4fbd4473d8a15abfa4364879`, Phase 2 applied revision `a47cd28c183afca43fb8de049d6a46ee594103fb`, the current production draft, QA record, frozen source, and locked glossary inventory.

## TR-050–TR-063 Verification Table

| Review ID | Expected action | Actual draft state | Result |
|---|---|---|---|
| TR-050 | Insert the approved English chapter title. | Metadata contains `The Son of a Great Landowner and the Son of a Poor Farmer.` exactly as recorded. | Pass |
| TR-051 | In CH01-P002 and CH01-P010, change only `known as` to `associated with`; retain the locked phrase and both repeated passages. | The two sentences differ from their Phase 1 versions only by the approved phrase and review-status metadata. Both retain `the three great myths of Korean business`, and both paragraphs remain present. | Pass |
| TR-052 | Apply the approved meal and porridge wording identically in CH01-P003 and CH01-P011 without deduplication. | Both paragraphs contain the same approved wording: `had something to eat in the morning` and `a bowl of wild-greens porridge to fill his stomach before going to sleep`. Both paragraph records remain separate. | Pass |
| TR-053 | Replace CH01-P008 with the approved sentence. | CH01-P008 reads `Born into poverty, Chung Ju-yung ran away from home four times in search of a livelihood.` | Pass |
| TR-054 | Reject the proposed CH01-P016 revision and retain `graduates of four-year universities`. | CH01-P016 translation is byte-for-byte unchanged from the Phase 1 draft and retains the required phrase. | Pass |
| TR-055 | Reject the proposed CH01-P018 revision and retain `China's successive imperial houses over a span of 1,300 years`. | CH01-P018 translation is byte-for-byte unchanged from the Phase 1 draft and retains the required phrase. | Pass |
| TR-056 | Apply the approved CH01-P019 sentence while preserving FB-F003 and all locked historical terms. | The approved sentence is present. `Kim Ok-gyun`, `late Joseon period`, `Gapsin Coup`, `Li Hongzhang`, `Donghwa Inn`, `Shanghai`, and *Zizhi Tongjian* remain unchanged; `[^FB-F003]` remains attached to `late Joseon period`. | Pass |
| TR-057 | Reject the proposed CH01-P020 revision and retain `offers a wealth of historical perspectives`. | CH01-P020 translation is byte-for-byte unchanged from the Phase 1 draft and retains the required phrase. | Pass |
| TR-058 | Keep the first sentence of CH01-P021 and replace only the second sentence. | The first sentence, including the modern “kingdom” metaphor, is unchanged. The second sentence is `This shows the depth of Chung Ju-yung's learning.` | Pass |
| TR-059 | Apply the approved CH01-P022 paragraph and preserve all three locked quotations. | The approved paragraph is present. `With diligence, no task is impossible.`, `Where there is a will, there is a way`, and `the investigation of things and the extension of knowledge` remain in their locked forms. | Pass |
| TR-060 | Replace only the final sentence of CH01-P023. | The first two sentences are unchanged from Phase 1. The final sentence matches the approved wording beginning `Together with` and retains all three locked book titles. | Pass |
| TR-061 | Retain the first sentence of CH01-P024, replace only the second, and preserve FB-P017 at the source-corresponding position. | The first sentence remains `Lee Byung-chull also frequently quoted the classics.` The second sentence matches the modified decision. The FB-P017 marker remains after `read` and before *The Thousand-Character Classic*, corresponding to the source boundary after `通读` and before the title. | Pass |
| TR-062 | Apply the approved CH01-P027 closing sentence and keep it as an independent paragraph. | The approved sentence is present under its own `### CH01-P027` heading and has not been merged with an earlier contrast paragraph. | Pass |
| TR-063 | Remove `Translated footnote:` while preserving FB-F002, FB-F003, and their content. | The label is absent. Both IDs, markers, and definitions remain present; the two definition lines are unchanged from Phase 1. | Pass |

## Structural Verification

- The frozen source and production draft contain the same ordered sequence of 27 unique IDs: `CH01-P001` through `CH01-P027`.
- Every production-draft paragraph has a non-empty source-page field, translation field, and review-status field.
- No paragraph ID was removed, duplicated, added, merged, split, or reordered.
- CH01-P001–CH01-P003 remain the opening framing sequence.
- CH01-P009–CH01-P011 remain separate and preserve the author's intentional return to the opening material.
- The paired approved revisions in CH01-P003 and CH01-P011 are identical; no deduplication occurred.
- CH01-P027 remains a separate closing paragraph. The approved revision changes its wording only and does not compress the thematic return into earlier prose.

Structural result: Pass.

## Traceability Verification

### Paragraph mapping

- Each `CH01-Pxxx` heading in the production draft has a corresponding paragraph marker in `source/chapters/01_chapter_01.md`.
- The paragraph order in the draft exactly matches the frozen source order.
- Source-page references remain populated, including the cross-page mapping `FB-P016–FB-P017` for CH01-P024.

### Anchors and page boundaries

| Marker | Verified position | Result |
|---|---|---|
| FB-I004 | Remains before CH01-P001. | Pass |
| FB-I005 | Remains between CH01-P001 and CH01-P002, where the source sentence crosses the image anchor. | Pass |
| FB-P016 | Remains between CH01-P015 and CH01-P016. | Pass |
| FB-P017 | Remains inside CH01-P024 after `read` and before *The Thousand-Character Classic*, matching the frozen-source boundary after `通读`. | Pass |

Marker counts and relative order are unchanged from the Phase 1 draft.

### Footnotes

| Footnote | Marker and position | Content comparison | Result |
|---|---|---|---|
| FB-F002 | Marker remains after `Gyeongsangnam-do` in CH01-P006. | `In Korea, a “do” is an administrative division roughly equivalent to a province in China.` is unchanged from Phase 1. | Pass |
| FB-F003 | Marker remains after `late Joseon period` in CH01-P019. | `The late nineteenth and early twentieth centuries.` is unchanged from Phase 1. | Pass |

The first-occurrence Namihei Odaira note `TN-CH01-001` also remains in place and unchanged. Removing the non-reader-facing `Translated footnote:` label under TR-063 did not alter any footnote ID or content.

Traceability result: Pass.

## Terminology Verification

- `glossary/chapter_01_candidates.csv` contains 41 unique candidate IDs, and all 41 remain `locked`.
- The four glossary files have identical Git blobs before and after Phase 2; no glossary record or terminology decision changed.
- All locked personal names, organizations, institutions, places, historical terms, classical titles, cultural concepts, quotations, and the historical unit remain in their approved forms.
- The context-approved `Hitachi founder Namihei Odaira` rendering remains intact and does not conflict with the `Hitachi Group` master entry.
- First-use and later-use handling remains intact for `seodang`, `seok`, *Zizhi Tongjian*, and `humaneness (ren), harmony (he), and joy (le)`.
- TR-051 retains the locked phrase `the three great myths of Korean business` in both occurrences.
- TR-056, TR-059, TR-060, and TR-061 retain every locked name, historical term, quotation, and book title within their changed passages.
- Phase 2 introduced no new proper-name form, reusable terminology decision, glossary-external variant, or terminology conflict.

Terminology result: Pass — 41/41 locked candidates preserved; 0 new conflicts.

## Unauthorized-Change Audit

- The Phase 1-to-Phase 2 commit comparison changes only `translation/drafts/chapter_01_full_draft_v0.1.md` and `qa/chapter_01_translation_review.md`.
- Production-draft text changes are confined to TR-050, TR-051, TR-052, TR-053, TR-056, TR-058, TR-059, TR-060, TR-061, TR-062, and TR-063, plus the authorized workflow metadata and review-status updates.
- TR-054, TR-055, and TR-057 translation text is unchanged.
- No frozen source, glossary, pilot, image, `translation/reviewed/`, or `translation/final/` file changed in Phase 2.
- Stage 6B.3 performed verification only and did not alter any existing file.

Unauthorized-change result: Pass — none detected.

## Final Gate Decision

Stage 6B.3 passed. Chapter 1 is ready for move from drafts/ to reviewed/ after project-lead approval.

This report does not itself authorize or perform that move. No file has been moved to `translation/reviewed/` or `translation/final/`.
