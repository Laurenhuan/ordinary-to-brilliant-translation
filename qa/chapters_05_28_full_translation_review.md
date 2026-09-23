# Chapters 5–28 Accelerated Translation Review

Stage: Risk-driven accelerated review

Scope: Chapters 5–28 + Afterword

Review rule: Record only Critical, Major, Minor, and source-discrepancy/verification Notes worth action. Ordinary acceptable prose was not line-edited.

## Original Evidence Limitation

At the time of the accelerated review, no original book PDF or full-page scan was present in the local workspace. The later project-lead visual decisions recorded in `qa/chapters_05_28_final_human_decision_packet.md` are authoritative and resolved the twelve-item visual queue and both Critical findings.

## Batch A Visual Verification Queue

| Item | Location | Available evidence | Classification | Treatment |
|---|---|---|---|---|
| A-V01 | CH07-P100/P102, 1.6亿元 vs 30亿元 | Printed PDF 63 | PRINTED_SOURCE_AS_IS | Both figures preserved; TN-CH07-001 added. |
| A-V02 | CH09-P055, 8000千万韩元 | Printed PDF 78 | PRINTED_SOURCE_ERROR | Chinese preserved; inferred 80 million won retained with TN-CH09-002. |
| A-V03 | CH06-P026, 神堂屋 | Printed PDF 53 | PRINTED_SOURCE_AS_IS | `Shindoya inn` retained as source-based/unverified; no reader note. |
| A-V04 | CH08-P036, 依被苍生 | Printed PDF 69 | PRINTED_SOURCE_ERROR | Chinese preserved; intended-sense English retained with TN-CH08-001. |
| A-V05 | CH08-P065, 局昌 | Printed PDF 71 | PRINTED_SOURCE_ERROR | Chinese preserved; contextual `Geochang` retained with TN-CH08-002. |
| A-V06 | CH08-P066, 5457亿 | Printed PDF 71 | PRINTED_SOURCE_AS_IS | 545.7 billion won preserved with TN-CH08-003. |
| A-V07 | CH09-P060, 三春 | Printed PDF 79 | PRINTED_SOURCE_ERROR | Chinese preserved; `Samsung` retained with TN-CH09-003. |
| A-V08 | CH09-P090, 丰田麦芽糖工厂 | Printed PDF 81 | PRINTED_SOURCE_AS_IS | Descriptive `Toyoda Malt-Sugar Factory` retained without official-name claim. |
| A-V09 | CH10-P071 blank/separator page | Printed PDF 91 | PRINTED_SOURCE_AS_IS | Blank separator confirmed; hidden metadata only. |
| A-V10 | CH11 金字中 / 郑州永 / 权利面前的两个人 | Printed PDFs 92, 96, 97 | MIXED | 金字中 corrected as OCR error; printed 权利 and 郑州永 preserved with neutral notes. |
| A-V11 | FB-F017–FB-F020 | Printed PDFs 94, 96, 97, 100 | VERIFIED MAPPING | All four marker/body mappings approved; provisional metadata cleared. |
| A-V12 | CH12-P084, 韩国是如果掘地的 | Printed PDF 106 | PRINTED_SOURCE_ERROR | Chinese preserved; contextual English retained with TN-CH12-002. |

## Batch A — Chapters 5–12

| Review ID | Paragraph / source | Category | Severity | Finding and shortest source evidence | Proposed/approved treatment | Human decision | Status |
|---|---|---|---|---|---|---|---|
| BR-CH06-001 | CH06-P026 | Entity identity | Note | `神堂屋` has no independently verified historical identity. | Retain `Shindoya inn` provisionally; verify visually/historically. | Approved | resolved-no-change |
| BR-CH07-001 | CH07-P043 | Omission | Major | Source includes `## 60 亿元能做什么呢？`; English omitted it. | Restore `## What Could Six Billion Won Accomplish?` inside CH07-P043. | Approved | resolved |
| BR-CH07-002 | CH07-P100/P102 | Number conflict | Note | First-year profit appears as both 1.6亿元 and 30亿元. | Preserve both until printed-page verification. | Approved | resolved |
| BR-CH08-001 | CH08-P036 | OCR/source form | Note | `依被苍生` may be `衣被苍生`. | Retain “Clothe the People”; do not alter source without page evidence. | Approved | resolved |
| BR-CH08-002 | CH08-P065 | Place/OCR | Note | `局昌` is contextually rendered `Geochang`. | Retain provisional form; verify print. | Approved | resolved |
| BR-CH08-003 | CH08-P066 | Number scale | Major | `5457亿` is far larger than the nearby 65-million-won loss. | Preserve 545.7 billion won; require visual verification before revision. | Approved | resolved |
| BR-CH09-001 | CH09-P005–P008 | Person identity | Major | Source variants 广口太郎/广口会长/光口会长 identify the same Asahi executive. | Use `Hirotaro Higuchi` and disclose inconsistent source forms in TN-CH09-001. | Approved | resolved |
| BR-CH09-002 | CH09-P055 | Undisclosed numerical inference | Major | `8000千万韩元` was rendered 80 million won to fit the printed total. | Keep open until visual verification; if retained, approve a neutral disclosure note. | Approved | resolved |
| BR-CH09-003 | CH09-P060 | Entity/OCR | Note | `三春` was contextually rendered `Samsung`. | Retain English identity; determine OCR vs printed-source status visually. | Approved | resolved |
| BR-CH09-004 | CH09-P090 | Historical entity | Note | `丰田麦芽糖工厂` lacks verified English identity. | Retain source-based `Toyoda Malt-Sugar Factory`. | Approved | resolved-no-change |
| BR-CH10-001 | CH10-P071 | Parser leakage | Major | Internal parser explanation appeared under `Translation:`. | Move explanation into HTML metadata; keep stable ID/page position. | Approved | resolved |
| BR-CH10-002 | CH10-P009–P016 | Historical company names | Note | 朝兴/兴华 names remain conservative transliterations. | Retain pending historical verification. | Approved | resolved-no-change |
| BR-CH10-003 | CH10-P034 | Historical claim | Note | Source states Japan earned 6.2 billion dollars from postwar UN supplies. | Preserve source claim; fact-check before publication note decision. | Approved | resolved |
| BR-CH11-001 | FB-F017 | Person identity | Major | `Chang Do-hwan` conflicts with the verified first council chairman. | Use `Chang Do-yong`; append neutral source-form disclosure. | Approved | resolved |
| BR-CH11-002 | CH11 occurrence of 金字中 | Entity/OCR | Note | English uses intended `Kim Woo-choong`. | Keep English; determine OCR vs printed-source status visually. | Approved | resolved |
| BR-CH11-003 | CH11 occurrence of 郑州永 | Entity/OCR | Note | English uses intended `Chung Ju-yung`. | Keep English; determine OCR vs printed-source status visually. | Approved | resolved |
| BR-CH11-004 | Chapter 11 title | Title/OCR | Note | `权利面前的两个人` is rendered “Two Men in the Face of Power.” | Keep English; verify 权利/权力 on printed title page. | Approved | resolved |
| BR-CH11-005 | FB-F017–FB-F019 | Footnote recovery | Note | Bodies come from JSON page mapping, not canonical Markdown. | Preserve provisional recovery and stable IDs; require visual confirmation. | Approved | resolved |
| BR-CH12-001 | CH12-P066 | Geographic discrepancy | Note | Source places Taehwa and Imjin rivers near Ulsan. | Preserve main text and add neutral TN-CH12-001 explaining the geography. | Approved | resolved |
| BR-CH12-002 | FB-F020 | Footnote recovery | Note | Body mapping existed while the marker location was initially unresolved. | Printed PDF 100 verified marker `①` at `京纺`; stable ID retained and provisional metadata cleared. | Approved | resolved |
| BR-CH12-003 | CH12-P084 | Malformed source | Note | `韩国是如果掘地的` is grammatically malformed. | Retain conservative contextual English; verify print. | Approved | resolved |

Batch A totals: Critical 0 · Major 6 · Minor 0 · Note 15. Resolved: 21. Open: 0.

## Batch B — Chapters 13–20

| Review ID | Paragraph / source | Category | Severity | Finding | Proposed treatment | Human decision | Status |
|---|---|---|---|---|---|---|---|
| BR-CH13-001 | FB-F021–FB-F024 | Footnote recovery | Note | Four bodies were restored from page mapping only. | Preserve stable IDs; visually confirm markers/bodies. | Approved | resolved-no-change |
| BR-CH13-002 | CH13-P023 | Malformed source | Note | `自保不前` is malformed; draft uses “hesitated.” | Retain conservative meaning; verify print. | Approved | resolved-no-change |
| BR-CH13-003 | CH13-P058–P060 | Name variants | Note | 郑载霞/郑载葭 appear to be one person. | Keep `Chung Jae-ha` provisionally and verify Chinese form. | Approved | resolved-no-change |
| BR-CH13-004 | CH13-P062 | Company identity | Note | `唯超` lacks a verified historical English name. | Retain `Weecho` as source-based, not official. | Approved | resolved-no-change |
| BR-CH13-005 | CH13-P078 | Number conflict | Major | Annual output appears as both 33 and 330,000 tons. | Preserve both; verify likely missing digits on printed page. | Approved | resolved |
| BR-CH14-001 | FB-F025–FB-F028 | Footnote recovery | Note | Four bodies are provisional page-map restorations. | Preserve stable IDs; visually confirm. | Approved | resolved-no-change |
| BR-CH14-002 | CH14-P045 | Entity identity | Note | `乔治亚男` is contextually identified as Giorgetto Giugiaro. | Keep verified identity; determine OCR/printed-source status visually. | Approved | resolved-no-change |
| BR-CH14-003 | CH14-P047/P050 | Entity/product identity | Note | H. W. 本基 and 卡米纳 remain unverified. | Retain `H. W. Benki` and `Camina` provisionally. | Approved | resolved-no-change |
| BR-CH14-004 | CH14-P068/P072 | Number/currency conflict | Major | Expressway cost comparisons and 315亿元 do not align. | Preserve all figures; verify print and units. | Approved | resolved |
| BR-CH14-005 | CH14-P082 | Number conflict | Major | Korea has 1,400 machines while Chung purchases 1,900. | Preserve both; verify printed quantities. | Approved | resolved |
| BR-CH14-006 | CH14-P100 | Product identity | Note | `混频` cannot be matched reliably to a TV brand. | Retain `Hunpin` provisionally. | Approved | resolved-no-change |
| BR-CH14-007 | CH14-P108 | Parser leakage | Major | Visible “No semantic source text” placeholder remains publication-facing. | Convert to HTML metadata during controlled revision. | Approved | resolved |
| BR-CH14-008 | CH14-P028 | Quantitative emphasis | Minor | `100%的国产汽车` became only “a wholly Korean-made car.” | Restore explicit “a 100-percent Korean-made car.” | Approved | resolved |
| BR-CH15-001 | Chapter-level | Possible missing content | Critical | Title promises Lee Byung-chull's color television, but all aligned body text is shipbuilding before Chapter 16. | Obtain printed-page images/PDF and determine whether material is missing or the printed title/body mismatch is original. | Approved | resolved |
| BR-CH15-002 | FB-F029 | Footnote recovery | Note | Body restored from page mapping only. | Preserve stable ID; visually confirm. | Approved | resolved-no-change |
| BR-CH15-003 | CH15-P016/P067 | Entity identity | Note | Lombardon and Ireland Shipping Company are unverified source forms. | Retain provisionally; do not claim official names. | Approved | resolved-no-change |
| BR-CH15-004 | CH15-P057 | Date/duration conflict | Major | September 1971 + one year three months conflicts with March 22, 1972. | Preserve all statements; verify printed chronology. | Approved | resolved |
| BR-CH15-005 | CH15-P061 | Quantity meaning | Note | “Completed 1.947 million tons” may mean orders, output, or tonnage. | Keep conservative wording; verify technical referent. | Approved | resolved-no-change |
| BR-CH16-001 | FB-F030–FB-F035 | Footnote recovery | Note | Six bodies are provisional page-map restorations. | Preserve IDs; visually confirm. | Approved | resolved-no-change |
| BR-CH16-002 | CH16-P026 | Date conflict | Major | “Ten years later, in 1984” follows a 1969 prediction. | Preserve both; verify printed year/interval. | Approved | resolved |
| BR-CH16-003 | CH16-P066/P069 | Entity/scale terms | Note | ASRY is transliterated; Jamsil comparison depends on mapped note. | Keep abbreviation and provisional note. | Approved | resolved-no-change |
| BR-CH16-004 | CH16-P072–P073 | Company identities | Note | Several foreign engineering names derive from Chinese transliteration. | Retain contextual forms; verify against historical records. | Approved | resolved-no-change |
| BR-CH16-005 | CH16-P124 | Year/amount corruption | Major | Sequence repeats 1982 and includes a literal 113 dollars. | Preserve source sequence; printed-page verification required. | Approved | resolved |
| BR-CH18-001 | FB-F036–FB-F037 | Footnote recovery | Note | Two bodies are provisional page-map restorations. | Preserve IDs; visually confirm. | Approved | resolved-no-change |
| BR-CH18-002 | CH18-P010–P011 | Arithmetic conflict | Major | 6 billion is described as about one quarter of and four times smaller than 21 billion. | Preserve source comparison; verify printed wording. | Approved | resolved |
| BR-CH18-003 | CH18-P039/P062–P063 | Technical terminology | Note | 64KD/64MD/4GD were normalized as DRAM generations. | Retain provisional normalization; verify notation. | Approved | resolved-no-change |
| BR-CH18-004 | CH18-P089 | Ranking conflict | Major | Source claims world first, then 19% share ranked second while capacity ranked first. | Preserve distinct rankings; verify print/context. | Approved | resolved |
| BR-CH18-005 | CH18-P101 | Technical analogy | Note | Hair-width/four-hundred-story analogy is imprecise. | Preserve authorial analogy; technical fact-check before publication. | Approved | resolved-no-change |
| BR-CH18-006 | CH18-P102 | Parser leakage | Major | Visible decorative-page placeholder remains publication-facing. | Convert to HTML metadata during controlled revision. | Approved | resolved |
| BR-CH19-001 | CH19-P033 | Historical discrepancy | Note | April 19 is called a military coup before the Second Republic. | Preserve main text; decide on a neutral editor note. | Approved | resolved |

Batch B totals: Critical 1 · Major 10 · Minor 1 · Note 18. Resolved: 30. Open: 0.

## Batch C — Chapters 21–28 + Afterword

| Review ID | Paragraph / source | Category | Severity | Finding | Proposed treatment | Human decision | Status |
|---|---|---|---|---|---|---|---|
| BR-CH21-001 | FB-F038–FB-F039 | Footnote recovery | Note | Two bodies are provisional page-map restorations. | Preserve IDs; visually confirm. | Approved | resolved-no-change |
| BR-CH21-002 | CH21-P018 | Place identity | Note | 群山礼里 lacks a verified modern English form. | Retain `Yeri in Gunsan` provisionally. | Approved | resolved-no-change |
| BR-CH22-001 | CH22-P001 | Extraction structure | Note | A false Markdown heading interrupted a quoted question. | Current uninterrupted English is structurally sound; verify print. | Approved | resolved-no-change |
| BR-CH22-002 | FB-F040–FB-F045 | Footnote recovery | Note | Six bodies are provisional page-map restorations. | Preserve IDs; visually confirm. | Approved | resolved-no-change |
| BR-CH22-003 | CH22-P030–P031 | Museum terminology | Note | Artifact titles are descriptive rather than catalog-verified. | Obtain museum catalog terminology before publication. | Approved | resolved-no-change |
| BR-CH22-004 | CH22-P032 | Historical discrepancy | Major | Source says the British Museum itself was completed in 1997. | Preserve source statement pending approval; likely add neutral note identifying the Korean Gallery referent. | Approved | resolved |
| BR-CH23-001 | CH23-P008 | Person identity | Note | 小针春芳 is rendered `Haruyoshi Kobari` without definitive evidence. | Retain as source-based; verify. | Approved | resolved-no-change |
| BR-CH23-002 | CH23-P021 | Product identity | Note | 肯尼迪史密斯 may not reproduce the historic club brand exactly. | Retain `Kennedy Smith` provisionally. | Approved | resolved-no-change |
| BR-CH23-003 | CH23-P042 | Unclear golf statement | Major | `每周进球9次` became “sink nine shots each week,” which remains unclear English. | Verify printed wording and approve an intelligible rendering. | Approved | resolved-no-change |
| BR-CH24-001 | FB-F046 | Footnote recovery | Note | Stellar note is a provisional page-map restoration. | Preserve ID; visually confirm. | Approved | resolved-no-change |
| BR-CH24-002 | CH24-P039–P043 | Technical terminology | Note | Yarn-count definition and wool claims require specialist confirmation. | Preserve source figures; textile review before publication. | Approved | resolved-no-change |
| BR-CH25-001 | CH25-P001/P067–P070 | Verse formatting | Note | Same lyrics appear unpunctuated and split across stable paragraphs. | Preserve wording and IDs; verify printed lineation. | Approved | resolved-no-change |
| BR-CH25-002 | FB-F047–FB-F048 | Footnote recovery | Note | Two bodies are provisional page-map restorations. | Preserve IDs; visually confirm. | Approved | resolved-no-change |
| BR-CH25-003 | CH25-P017 | Historical company names | Note | Long affiliate chronology mixes historical brand forms. | Verify against corporate history before final copy. | Approved | resolved-no-change |
| BR-CH25-004 | CH25-P040–P042 | Vessel identity | Note | 沃特威尔号 remains unverified as *Waterwill*. | Retain source-based form; verify vessel record. | Approved | resolved-no-change |
| BR-CH25-005 | CH25-P046 | Organization wording | Note | 韩苏经纪人协会 differs from later 韩苏经济协会. | Current consistent `Korea-Soviet Economic Association` remains provisional. | Approved | resolved-no-change |
| BR-CH25-006 | CH25-P064 | Statistical comparison | Note | Cumulative exports are compared with company-scale figures without a shared basis. | Preserve all figures; fact-check and note if needed. | Approved | resolved |
| BR-CH26-001 | CH26-P001 | Truncated source | Critical | `品性将决定一个人的。` lacks the final object. | Obtain printed page; do not supply the likely missing word without evidence. | Approved | resolved |
| BR-CH26-002 | CH26-P006 | Family/count conflict | Major | “Father and three sons” lists only Mong-koo and Mong-joon, then names three brothers. | Preserve disclosure in draft; verify printed line and approve correction/note. | Approved | resolved |
| BR-CH26-003 | CH26-P021 | Entity/date conflict | Major | A February 1995 statement is attributed to Lee Byung-chull despite his 1987 death. | Preserve source identity; prepare neutral Entity Identity Conflict note. | Approved | resolved |
| BR-CH27-001 | CH27 name lists | Name verification | Note | Dense historical executive names rely on source-based romanization. | Verify corporate archives; do not claim official status meanwhile. | Approved | resolved-no-change |
| BR-CH27-002 | CH27-P017 | Number scale | Major | Samsung Life assets appear as only five billion won. | Preserve extracted number; visually verify unit/digits. | Approved | resolved |
| BR-CH27-003 | CH27-P030 | Number/technical scale | Major | 157.8 million and 23 billion memory-chip quantities may contain malformed units/digits. | Preserve figures; verify printed page and historical context. | Approved | resolved |
| BR-CH27-004 | CH27-P058 | Parser leakage | Major | Visible “No semantic text” placeholder remains publication-facing. | Convert to HTML metadata during controlled revision. | Approved | resolved |
| BR-AW-001 | AW-P001 | Heading/OCR uncertainty | Major | `Qiji` is visible but may be an OCR artifact for the afterword heading. | Obtain page image and replace only if verified; otherwise disclose/retain. | Approved | resolved-no-change |
| BR-AW-002 | FB-F049 | Footnote recovery | Note | Gwacheon body is provisional page-map recovery. | Preserve ID; visually confirm. | Approved | resolved-no-change |
| BR-AW-003 | AW-P012 | Place/source variant | Note | 古灵台 differs from earlier 高灵桥. | Retain contextual `Goryeong Bridge`; verify printed form. | Approved | resolved-no-change |
| BR-AW-004 | AW-P022–P023 | External metadata leakage | Major | Anna's Archive metadata remains visible under `Translation:`. | Preserve IDs but move explanations to HTML metadata before publication output. | Approved | resolved |

Batch C totals: Critical 1 · Major 9 · Minor 0 · Note 18. Resolved: 28. Open: 0.

## Global Terminology Conflict Resolution

| ID | Chinese forms | Approved project form | Evidence basis | Action | Status |
|---|---|---|---|---|---|
| GTR-001 | 沈铉荣 | Shim Hyun-young | Contemporaneous English reporting identifies the Hyundai executive by this form. | Chapter 9 and fast lexicon normalized; later chapters already matched. | resolved |
| GTR-002 | 金润规 / 金润圭 | Kim Yoon-kyu | Hyundai Group English material and contemporaneous reporting use this form for the Hyundai Asan executive. | Chapters 25/27 and fast lexicon normalized; Chapters 9/19 already matched. | resolved |
| GTR-003 | 姜晋求 | Kang Jin-ku | Master glossary is authoritative. | Fast lexicon corrected; translations were already correct. | resolved |

Evidence references:

- Shim Hyun-young: https://www.koreajoongangdaily.com/business/shakeup-begins-at-hyundai/11458690
- Kim Yoon-kyu: https://www.hyundaigroup.com/mobile/eng/media/list.asp?idx=9973&mode=view&page=34&pageSize=5&searchStr=

## Automated Sanity Scan

- Chapter 7–28 + Afterword mapped paragraphs scanned: 1,522.
- Missing/duplicate paragraph IDs: none.
- Every `Translation:` block contains translated content or approved hidden metadata for a confirmed blank/decorative/metadata-only page.
- Obvious untranslated Chinese in English prose: none. The only Chinese detected is inside the approved explanatory note for FB-F017.
- Exact duplicate prose: all detected cases correspond to source repetition, repeated quotations, attributions, or metadata placeholders; no unauthorized deduplication was performed.
- Footnote ID sets in Chapters 13–28 + Afterword: source/translation sets match.
- Year/percentage heuristic: the CH14-P028 omission was corrected to `a 100-percent Korean-made car`; other hits were correctly translated as words or continued across a page boundary.

## Consolidated Status

Historical finding totals: Critical 2 · Major 25 · Minor 1 · Note 51 = 79.

Global terminology conflicts tracked separately: 3, all resolved.

Review-ID outcomes: 40 resolved with an approved revision; 39 resolved with no reader-facing change. Global terminology conflicts: 3 resolved separately.

Open review items: 0. Critical unresolved: 0. Major unresolved: 0. Minor unresolved: 0. Note decisions unresolved: 0. PDF visual checks unresolved: 0. Human decisions pending: 0.

Source files modified by final controlled revision: 2 (`11_chapter_11.md` and `26_chapter_26.md`), limited to visually verified extraction errors.

Translation files modified: 25. Nineteen received approved text, note, footnote-process, or hidden-metadata changes; six received workflow-status metadata only.

New approved translator/editor notes added: 26.

Publication-facing parser/archive leakage removed: 4 Review IDs (5 visible placeholder lines); the earlier CH10-P071 remediation remains intact.

Chapter 1–4 files modified: 0.

Reader/Bilingual outputs created: No.

Commit/push: No.

## Final Controlled-Revision Verification

- Paragraph mappings checked: 1,612
- Missing, duplicate, reordered, merged, or split paragraph IDs: 0
- Page-boundary mismatches: 0
- Image-anchor mismatches: 0
- Footnote-ID mismatches: 0
- Empty or unaccounted-for translation blocks: 0
- Translator-note reference/definition mismatches: 0
- Publication-facing parser/archive placeholders: 0
- Pending translation/review markers: 0
- Canonical source changes:
  - Chapter 11: `bdb54502b67cfa7133220eecb9b00cd355b2eca7` → `248ee152a7051e820cc556a1e7d43d24ddc8b910` (`金字中` extraction corrected to printed `金宇中`)
  - Chapter 26: `b06a35dc1654493dd35493f1740e5375080648ac` → `851dfe840d47dfe84fb8f54733eb9c109ef6fd3c` (printed `命运` restored in CH26-P001)
- Unexpected canonical source changes: 0
- Chapters 1–4 and their accepted outputs: unchanged
- Raw full-book evidence: unchanged
- Reader/Bilingual generated: No
- Commit/push: No

Final gate: all review blockers cleared; ready for final publication build.
