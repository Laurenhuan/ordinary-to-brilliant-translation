# Chapter 2 Translation Preparation

Stage: Chapter 2 translation preparation

Status: Preparation complete — source exists but is not frozen; formal translation must not start

## 1. Repository and Chapter 2 status

| Area | Current state |
|---|---|
| `source/` | Full-book raw materials, page/image/footnote mappings, and cleaned chapter files are present. |
| `source/chapters/02_chapter_02.md` | Present. Git blob: `5eb890156fd704339fe4a70e8c78acc62ca8fbdf`. |
| Chapter 2 source designation | Stage 4A non-destructive cleaned source. It does **not** carry a `Canonical Source — Frozen for Translation` designation. |
| `glossary/` | Chapter 1 master glossaries and its 41-item locked candidate inventory are present. No Chapter 2 candidate inventory exists. |
| `translation/` | Chapter 1 draft and reader version are present. No Chapter 2 draft or reader/reviewed artifact exists. |
| `qa/` | Full-book ingestion QA and Chapter 1 records are present. No Chapter 2-specific QA record existed before this file. |
| Git state before preparation | `main` synchronized with `origin/main`; working tree clean at `ed59d72bbec2c12ad410ba7045070dba107f3b2f`. |

Chapter 2 translation status: **not started**.

Preparation gate: the source exists, but source validation and an explicit Chapter 2 freeze are still required before production translation.

## 2. Source structure

### Chapter metadata

- Source file: `source/chapters/02_chapter_02.md`
- Source title: `2 “海归”和离家出走的少年`
- Stable paragraph range: `CH02-P001`–`CH02-P086`
- Stable paragraph count: 86
- Unique paragraph IDs: 86
- Sequence check: exact continuous sequence from P001 through P086
- MinerU/page range: `FB-P018`–`FB-P025`
- Input PDF pages: 18–25
- Printed pages: first chapter-opening page unknown; then 6–12
- Local image anchors: 2
- Footnote mappings: 3

### Page mapping summary

| Page ID | Input PDF page | Printed page | Paragraph starts | Structural notes |
|---|---:|---:|---|---|
| FB-P018 | 18 | Unknown | CH02-P001–P002 (2) | Chapter-opening page; FB-I006 precedes P001 and FB-I007 lies between P001 and P002. |
| FB-P019 | 19 | 6 | CH02-P003–P014 (12) | Contains study-abroad arrival and global financial-crisis chronology. |
| FB-P020 | 20 | 7 | CH02-P015–P026 (12) | Contains FB-F004 marker evidence; P026 ends mid-sentence at the page boundary. |
| FB-P021 | 21 | 8 | CH02-P027–P038 (12) | P027 continues P026; contains FB-F005 marker evidence. |
| FB-P022 | 22 | 9 | CH02-P039–P051 (13) | Contains FB-F006 marker evidence; P051 ends mid-sentence. |
| FB-P023 | 23 | 10 | CH02-P052–P064 (13) | P052 continues P051. |
| FB-P024 | 24 | 11 | CH02-P065–P077 (13) | P077 continues across the next page. |
| FB-P025 | 25 | 12 | CH02-P078–P086 (9) | Opens with an unnumbered continuation of P077 incorrectly formatted as an H2 heading. |

The page-map records for FB-P018–FB-P025 are all marked `mapped` in `qa/full_book_page_map.csv`.

### Image anchors

| Image ID | Source page | JSON block | Local source path | Existing mapping status | Preparation result |
|---|---|---:|---|---|---|
| FB-I006 | FB-P018 | 2 | `source/raw/full_book/part_001_200/images/image_006.jpg` | Verified one-to-one across JSON, Markdown, and DOCX | Present; retain its position before CH02-P001. |
| FB-I007 | FB-P018 | 4 | `source/raw/full_book/part_001_200/images/image_007.jpg` | Verified one-to-one across JSON, Markdown, and DOCX | Present; retain its position between CH02-P001 and CH02-P002. |

Both relative Markdown paths resolve to existing local files. No remote CDN dependency remains for these two images.

### Footnotes

| Footnote ID | Marker location | JSON/map body evidence | Current source treatment | Status before translation |
|---|---|---|---|---|
| FB-F004 | `北间岛①` in CH02-P025; page FB-P020 | `① 现位于中国吉林省。` | Marker remains in source; body is not restored. Existing full-book QA recognizes the mapping through prior approved pilot evidence. | Mapping recognized, but Chapter 2 still requires an explicit source-freeze treatment decision. |
| FB-F005 | `清津 $^{①}$` in CH02-P030; page FB-P021 | `① 位于现朝鲜民主主义人民共和国咸镜北道东北部，为一港口城市。` | Marker remains in LaTeX-like form; body is not restored. | Open manual review item FB-R016. |
| FB-F006 | `安边 $^{①}$` in CH02-P046; page FB-P022 | `① 位于咸镜北道。` | Marker remains in LaTeX-like form; body is not restored. | Open manual review item FB-R017. |

No footnote body should be inserted into a frozen or translated artifact until the mapping and placement decision is explicitly recorded. FB-F005 and FB-F006 remain unresolved; FB-F004 has recognized prior evidence but is not yet restored in this unfrozen chapter source.

## 3. Structural findings requiring review

| Preparation ID | Location | Severity | Finding | Required treatment before translation |
|---|---|---|---|---|
| C2-PREP-R001 | Chapter-level | High | `02_chapter_02.md` is cleaned but not frozen. | Complete Chapter 2 source QA and create an explicit source-freeze record. Do not translate from an unfrozen source. |
| C2-PREP-R002 | CH02-P026–P027 / FB-P020–P021 | High | One sentence is split into two stable paragraph IDs at a page/footnote boundary: P026 ends `因为农活儿即使累死累活地干，` and P027 continues `一日三餐还是没有保证。` | Human must approve whether the translation keeps two traceable IDs with a documented cross-paragraph sentence or normalizes the logical paragraph while preserving both mappings. Do not guess from semantics alone. |
| C2-PREP-R003 | CH02-P051–P052 / FB-P022–P023 | High | One sentence is split across two IDs and a page/footnote boundary: P051 ends `是` and P052 continues `出于对这段往事的多少悔恨啊。` | Approve a traceable cross-page reconstruction rule before drafting. |
| C2-PREP-R004 | CH02-P077 / FB-P024–P025 | High | P077 continues onto FB-P025, but the continuation is unnumbered and formatted as `## 己，而福特却离家出走到机械工厂做了实习工。` The H2 markup is a likely structural extraction error, not a verified heading. | Compare the authorized page visually and approve the logical P077 reconstruction. Do not edit the source during preparation. |
| C2-PREP-R005 | CH02-P001–P002 and P041–P042 | High | The chapter intentionally repeats its opening summary later. | Preserve both occurrences. Do not deduplicate or compress the repeated framing. |
| C2-PREP-R006 | CH02-P010, P047, P059–P060 | Medium | The author uses short fragments and rhetorical setup lines (`1929 年 10 月 24 日。`, `几个烂了的苹果。`, and a colon followed by a separate paragraph). | Preserve paragraph-level rhetoric unless human review approves a specific structural adjustment. |
| C2-PREP-R007 | FB-F004–FB-F006 | High | Three footnote bodies are absent from the chapter source; two mappings remain open and two markers use LaTeX-like syntax. | Resolve every footnote manually before Chapter 2 source freeze. |
| C2-PREP-R008 | CH02-P069–P073 | High | The source repeats the Chapter 1 printed form `小源浪平` and associates it with dates and biographical details. Chapter 1 already records this as a verified source-text proper-name discrepancy. | Preserve the Chinese source. Use the locked English only after human review confirms entity treatment, date/biography handling, and whether the Chapter 1 editor note should be repeated in a standalone Chapter 2 deliverable. |
| C2-PREP-R009 | CH02-P079–P081 | High | The `丰田喜一郎` name/date/biography bundle requires entity-level verification before an English name can be selected. | Do not correct or translate the identity from model knowledge. Perform authoritative verification and record the human decision. |
| C2-PREP-R010 | CH02-P005–P006 and P050 | High | `朝鲜` appears in colonial-person, historical-country, and later geographic/destination contexts. The Chapter 1 rule explicitly forbids blind replacement. | Decide each occurrence contextually; P050 especially requires a separate geographic/historical decision. |
| C2-PREP-R011 | CH02-P003–P018, P025, P050, P064 | Medium | Historical events, political language, colonial terminology, and nation/state references carry factual and register risk. | Verify terminology and translation policy without silently fact-correcting the source. |
| C2-PREP-R012 | CH02-P032, P046, P050, P064 and numeric passages | Medium | Historical currency (`角`/`分`), distance (`里`), quantities, percentages, dates, and financial figures require exact preservation. Existing numeric extraction alignment is exact, but factual accuracy has not been verified. | Establish unit treatment and perform source-visual number checking; do not convert values without approval. |
| C2-PREP-R013 | CH02-P015, P028–P029, P061, P083 | Medium | Film, novel, newspaper, proverb, and quotation titles require established-form or project-specific decisions. | Verify titles and quotation policy before translating the affected segments. |
| C2-PREP-R014 | FB-I006–FB-I007 | Low | Two portrait/cartoon images belong to the chapter-opening layout rather than ordinary captioned figures. | Preserve source order and mapping; do not invent captions or infer final publication placement from Markdown alone. |
| C2-PREP-R015 | CH02-P064 | Medium | The source contains the form `抑是`, which may be unusual or OCR-sensitive. | Require PDF visual verification. Preserve the source form unless a source-cleaning decision is approved. |

## 4. Chapter 1 locked terminology crossover

The following 12 Chapter 1 candidates occur verbatim in Chapter 2. Their locked English forms remain binding; this preparation does not modify or relock them.

| Chapter 1 ID | Source term | Locked English / rule | Chapter 2 occurrence |
|---|---|---|---|
| C1-T001 | 李秉哲 | Lee Byung-chull | P001, P002, P003, P005, P007, P008, P018–P021, P041, P042, P067, P085, P086 |
| C1-T002 | 郑周永 | Chung Ju-yung | P001, P002, P021, P026, P028, P029, P038, P039, P041–P043, P045, P048–P050, P054–P056, P058, P059, P062, P067, P071, P075, P078, P081 |
| C1-T003 | 盛田昭夫 | Akio Morita | P069, P070 |
| C1-T004 | 小源浪平 | Namihei Odaira, with the recorded source-text discrepancy policy | P069–P072 |
| C1-T009 | 索尼 | Sony | P069 |
| C1-T010 | 日立集团 | Hitachi Group; contextual natural rendering allowed where recorded | P069, P073 |
| C1-T012 | 早稻田大学 | Waseda University | P008, P018, P067 |
| C1-T014 | 松田小学 | Songjeon Elementary School | P021 |
| C1-T015 | 日本 | Japan | P002–P005, P007, P008, P014–P016, P018, P021, P042, P067, P069, P079 |
| C1-T020 | 朝鲜 | Context-sensitive; no blind replacement | P005, P006, P050 |
| C1-T034 | 地主 | landowner / landowning family according to context | P085 (`大地主`) |
| C1-T039 | 有志者事竟成 | Where there is a will, there is a way. | P061 |

C1-T041 (`商界三大神话`) was checked separately and does not occur verbatim in Chapter 2. No Chapter 1 locked entry was changed.

Special crossover decisions still requiring human interpretation:

- `朝鲜` must be resolved independently in P005, P006, and P050 under the locked context-sensitive rule.
- `小源浪平` must not be treated as a new OCR correction. Chapter 1's verified source-text discrepancy record remains authoritative, but note repetition and the Chapter 2 biography bundle require review.
- `大地主` in P085 must follow the existing `landowner / landowning family` rule in prose; the approved Chapter 1 English title does not create a blind replacement rule.
- The P061 proverb must use the locked conventional substitution if and when translation is authorized.

## 5. Provisional Chapter 2 terminology candidates

All entries below are **Proposed / unverified**. They are preparation candidates only, not glossary entries and not approved English forms.

### People, organizations, institutions, and works

| Provisional ID | Source term | Type | Segment(s) | Verification need |
|---|---|---|---|---|
| C2-PREP-T001 | 马克思 | person | P017 | Established English form; confirm quotation/book context if later supplied. |
| C2-PREP-T002 | 恩格斯 | person | P017 | Established English form. |
| C2-PREP-T003 | 李光洙 | person | P028 | Authoritative Korean literary English form and name order. |
| C2-PREP-T004 | 本田宗一郎 | person | P069–P075 | Established official English form; cross-check the attached dates and biography without modifying source. |
| C2-PREP-T005 | 亨利·福特 | person | P077–P078 | Established English form. |
| C2-PREP-T006 | 丰田喜一郎 | person | P079–P081 | High-risk entity verification across name, dates, family relationship, loom, and automotive biography. |
| C2-PREP-T007 | 赵治勋 | person | P083–P084 | Established English/Korean-Japanese professional usage and name order. |
| C2-PREP-T008 | 早稻田大学政治经济系 | school subdivision | P008 | Historical-period official English unit name; do not infer from the modern unit without verification. |
| C2-PREP-T009 | 纽约的美国银行 | historical financial institution | P011 | Entity identification is ambiguous; verify the intended historical bank before selecting English. |
| C2-PREP-T010 | 澳大利亚中央银行 | historical financial institution | P012 | Historical-period institution identification and official English name. |
| C2-PREP-T011 | 英格兰银行 | organization | P012 | Established official English name and historical context. |
| C2-PREP-T012 | 《哪怕是大学毕业》 | film title | P015 | Verify established English film title and italicization policy. |
| C2-PREP-T013 | 《泥土》 | novel title | P028–P029 | Verify established English literary title; do not create a literal title silently. |
| C2-PREP-T014 | 《东亚日报》 | newspaper | P028 | Official/established English name and publication-title style. |
| C2-PREP-T015 | 财务学院 | historical school/institution | P037, P053 | Identify the institution and historical English rendering; source context may be non-formal training. |
| C2-PREP-T016 | 福兴商会 | historical business | P040 | Verify Korean source form and whether an established English name exists. |
| C2-PREP-T017 | 本田汽车集团 | organization | P069, P074 | Official corporate English form appropriate to historical context. |
| C2-PREP-T018 | 美国福特公司 | organization | P077 | Official corporate form and historical naming. |
| C2-PREP-T019 | 丰田汽车 | organization/brand | P079 | Official English form, kept separate from the unresolved founder identity bundle. |
| C2-PREP-T020 | 三星集团 | organization | P067 | Official English form and context-sensitive corporate rendering. |
| C2-PREP-T021 | 现代 | organization | P067 | Confirm the intended Hyundai entity and natural contextual form. |
| C2-PREP-T022 | “学校会使人变傻” | quotation | P083 | Project quotation decision; preserve attribution and do not invent an established quote. |
| C2-PREP-T023 | “釜关”号轮船 | vessel/route name | P004 | Historical ferry/vessel identification, romanization, and quotation treatment. |

### Historical, cultural, geographic, and unit candidates

| Provisional ID | Source term | Type | Segment(s) | Verification need |
|---|---|---|---|---|
| C2-PREP-T024 | “海归” | cultural/historical term | Chapter title | Historical-context rendering; modern shorthand may be anachronistic in English. Preserve the source quotation marks until a title decision is approved. |
| C2-PREP-T025 | 弱冠 | cultural age term | P003 | Contextual rendering rather than mechanical transliteration. |
| C2-PREP-T026 | 亡国奴 | colonial/historical expression | P005 | Sensitive historical register; preserve the source's emotional force without adding editorial judgment. |
| C2-PREP-T027 | 四无国家 | authorial historical phrase | P006 | Project-specific rendering of the phrase and its four-part definition. |
| C2-PREP-T028 | 世界性经济大恐慌 / 世界金融危机 | historical event/variant cluster | P002, P009–P015, P019–P020, P042 | Determine when to use the established event name versus generic financial/economic crisis language. |
| C2-PREP-T029 | 关东大地震 | historical event | P014 | Established English historical name. |
| C2-PREP-T030 | 左翼思想 | historical/political term | P017 | Contextual political register. |
| C2-PREP-T031 | 无产阶级思想 | historical/political term | P018 | Contextual political register; do not collapse into C2-PREP-T030 automatically. |
| C2-PREP-T032 | 九一八事变 | historical event | P018 | Established historical English form and event-naming policy. |
| C2-PREP-T033 | “满洲国” | historical state term | P025 | Established historical form, quotation treatment, and colonial-context policy. |
| C2-PREP-T034 | 北间岛 | historical place | P025 | Korean/Chinese historical geographic naming plus FB-F004 treatment. |
| C2-PREP-T035 | 清津 | place | P030–P031 | Established geographic form plus unresolved FB-F005. |
| C2-PREP-T036 | 金刚山 | place | P035 | Established Korean geographic English form. |
| C2-PREP-T037 | 安边 | place | P046 | Established geographic form plus unresolved FB-F006. |
| C2-PREP-T038 | 龟船 | historical/cultural object | P064 | Established historical term and first-use explanation policy. |
| C2-PREP-T039 | 角 / 分 | historical currency units | P032 | Identify currency context and decide retention, explanation, or conversion policy; never convert silently. |
| C2-PREP-T040 | 里 | historical distance unit | P046 | Decide transliteration, descriptive rendering, or approved conversion policy. |
| C2-PREP-T041 | 围棋大师 | title/role | P083 | Contextual professional title; avoid rigid one-to-one use outside this sentence. |
| C2-PREP-T042 | 釜山 | place | P004 | Established official/conventional English form. |
| C2-PREP-T043 | 下关 | place | P004–P005 | Established Japanese place form appropriate to route context. |
| C2-PREP-T044 | 玄海滩 | place/geographic feature | P005 | Geographic identification and established English form. |
| C2-PREP-T045 | 东京 | place | P002, P008, P017, P074, P077, P081 | Established conventional English form. |
| C2-PREP-T046 | 华尔街 | place/financial metonym | P009 | Contextual conventional English form. |
| C2-PREP-T047 | 纽约 | place | P011 | Established conventional English form. |
| C2-PREP-T048 | 首尔 | place | P029, P037, P039–P040, P053 | Established official English form; historical-period context must be considered. |
| C2-PREP-T049 | 仁川 | place | P039, P056 | Established official English form and port/wharf context. |
| C2-PREP-T050 | 底特律 | place | P078 | Established conventional English form. |

Provisional candidate count: 50. These entries must not be marked verified or locked merely because an English form appears obvious.

## 6. Translation risk summary

### High risk

- Unfrozen Chapter 2 source.
- Three footnote decisions, including two open full-book manual-review items.
- Cross-page logical sentences at P026/P027 and P051/P052.
- P077's unnumbered page continuation and erroneous H2 formatting.
- Intentional repeated framing at P001/P002 and P041/P042.
- Proper-name/entity bundles at P069–P073 and P079–P081.
- Context-sensitive `朝鲜`, especially P050.

### Medium risk

- Colonial and political terminology, historical event naming, and source-author evaluation.
- Film, novel, newspaper, corporate, and historical institution names.
- Currency, distance, quantities, dates, percentages, and financial figures.
- Rhetorical fragments and paragraph-level cadence.
- Potential OCR-sensitive form `抑是` in P064.

### Lower but controlled risk

- Two image anchors are already localized and verified, but their visual page-layout role must not be converted into invented captions.
- Common place names still require consistent project forms and historical-context awareness.

## 7. Manual decisions required before translation

1. Approve Chapter 2 source QA scope and decide whether the current 86-ID structure is retained or receives a non-destructive reconstruction layer.
2. Resolve C2-PREP-R002, R003, and R004 using the authorized PDF/page evidence.
3. Approve restoration and placement for FB-F004; approve or reject FB-F005 and FB-F006 mappings.
4. Confirm the two chapter-opening image positions and whether no-caption treatment remains appropriate.
5. Review the P069–P073 and P079–P081 entity/name/date/biography bundles without modifying the source from model knowledge.
6. Decide the three Chapter 2 contexts for `朝鲜`, including P050.
7. Decide whether the Namihei Odaira source-discrepancy note is book-level only or should repeat in a standalone Chapter 2 reader version.
8. Approve a Chapter 2 terminology-candidate inventory and verification batch; no provisional term in this report is locked.
9. Approve historical currency/distance treatment and the title/quotation verification batch.
10. Freeze Chapter 2 source with a recorded blob before authorizing any translation draft.

## 8. Preparation gate

- Source present: Yes.
- Stable paragraph IDs present: Yes — 86.
- Page mapping present: Yes — 8 pages.
- Images localized: Yes — 2/2.
- Footnotes closed: No — source-freeze treatment still required; FB-F005 and FB-F006 remain open.
- Structural issues closed: No.
- Chapter 2 terminology verified: No.
- Chapter 2 source frozen: No.
- Formal translation authorized: No.

Recommended next stage: **Chapter 2 Source Validation and Freeze Preparation**, followed by a separately approved terminology-verification stage. Do not begin prose translation until both gates are complete.

## 9. Scope protection

- No Chapter 1 file was modified.
- No source file was modified.
- No glossary record or locked terminology was modified.
- No Chapter 2 translation draft was created.
- This preparation report contains no translated Chapter 2 prose.
