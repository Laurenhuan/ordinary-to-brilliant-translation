# Chapter 4 Terminology Candidate Audit

Stage: Terminology Verification and Final Lock

Status: **COMPLETE — 92/92 LOCKED**

Frozen source: `source/chapters/04_chapter_04.md`

Frozen source blob: `0b5431282b1e6d60be75a5c0f05543e57d956049`

Scope: `CH04-P001`–`CH04-P064`; source footnotes `FB-F011`–`FB-F013`

Translation status: Not started

## Audit Controls

- The frozen Chapter 4 source controls Chinese wording, locations, paragraph boundaries, and factual claims.
- Compatible master-glossary locks from Chapters 1–3 are inherited without reopening them.
- The original candidate tables below are retained as the pre-decision audit snapshot. Their `proposed` and `needs_human_decision` cells record the state at extraction time and are not the current status.
- Final authority for `C4-T023`–`C4-T092` is `qa/chapter_04_terminology_decision.md`; all 70 are now locked with their occurrence-level controls and metadata.
- Historical/Factual Discrepancy Handling and the Entity Identity Conflict Policy apply whenever external evidence conflicts with the printed source.
- The visually verified `火车` in `CH04-P054` remains part of the source; terminology review may recommend a neutral note but may not alter it.

## Status Summary

| Metric | Count |
|---|---:|
| Total Chapter 4 candidates | 92 |
| Inherited locked | 22 |
| New candidates | 70 |
| Newly locked | 70 |
| Current `proposed` | 0 |
| Current `needs_human_decision` | 0 |
| Current unresolved | 0 |
| Mandatory translator/editor notes | 5 |
| Original candidates marked for external verification | 49 |
| Original possible historical/entity/terminology conflicts | 12 |

## Historical Candidate Audit Snapshot

The tables that follow preserve the original candidate wording, research starting points, uncertainty classifications, and conflict queue. Those historical status labels are superseded by the Project Lead decisions recorded in `qa/chapter_04_terminology_decision.md` and by the locked master-glossary rows.

## Inherited Locked Terms

| ID | Chinese term | CH04 locations | Category | Inherited locked form | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T001 | 李秉哲 | P005, P007, P009–P010, P013–P014, P019–P020, P022–P024, P026–P027, P029, P031–P032, P039–P045, P047, P049–P051 | person | Lee Byung-chull | inherited_locked | No — prior lock | Use established form throughout | No | None identified |
| C4-T002 | 郑周永 | P004, P007, P041, P051–P058, P062–P064 | person | Chung Ju-yung | inherited_locked | No — prior lock | Use established form throughout | No | None identified |
| C4-T003 | 三星集团 / 三星 | P001, P003, P006, P011, P013, P026, P034–P035, P038, P040, P042 | organization | Samsung Group; later natural reference Samsung | inherited_locked | No — prior lock | Distinguish the group from separately audited historical entities | No | Do not use this lock to settle 三星商会 |
| C4-T004 | 日本 | P027–P028, P045–P048, P054, P057–P058, P064 | place/adjective | Japan / Japanese according to syntax | inherited_locked | No — prior lock | Sentence-level noun/adjective choice | No | None |
| C4-T005 | 韩国 | P045, P054–P055, P064; FB-F011–F012 | place/adjective | Korea / Korean according to syntax | inherited_locked | No — prior lock | No blind global replacement | No | None |
| C4-T006 | 中国 | P012, P014–P016, P020–P024, P027–P028 | place/adjective | China / Chinese according to syntax | inherited_locked | No — conventional/prior lock | Preserve regional qualifiers separately | No | None |
| C4-T007 | 大邱 | P008, P010, P012, P020–P021, P027, P029, P031, P045, P047 | place | Daegu | inherited_locked | No — prior lock | Use Daegu | No | None |
| C4-T008 | 金海 | P005 | place | Gimhae | inherited_locked | No — prior lock | Use Gimhae | No | None |
| C4-T009 | 首尔 | P010, P019, P031, P051–P052, P054–P056; FB-F013 | place | Seoul | inherited_locked | No — prior lock | Use Seoul | No | None |
| C4-T010 | 釜山 | P010, P014 | place | Busan | inherited_locked | No — prior lock | Use Busan | No | None |
| C4-T011 | 平壤 | P014, P019 | place | Pyongyang | inherited_locked | No — prior lock | Use Pyongyang | No | None |
| C4-T012 | 上海 | P014–P016 | place | Shanghai | inherited_locked | No — prior lock | Use Shanghai | No | None |
| C4-T013 | 朝鲜（国家语境） | P022 | historical/geographic context | Korea / Korean according to sentence meaning | inherited_locked | No — prior context rule | Do not apply to 朝鲜酿造厂 | No | No global replacement |
| C4-T014 | 福兴商会 | P056 | historical business | First: Bokheung Rice Store (Bokheung Sanghoe); later: Bokheung Rice Store | inherited_locked | No — prior lock | This chapter occurrence is a later reference | No | None |
| C4-T015 | 石 | P047–P048, P050; FB-F012 | historical capacity unit | seok; first use `seok (a traditional Korean grain measure)` | inherited_locked | No — prior lock | Preserve quantities and approved source footnote | Source footnote required | Do not convert or correct FB-F012 |
| C4-T016 | 坪 | P005 | historical area unit | pyeong | inherited_locked | No — prior lock | Preserve two-million-pyeong quantity | No new note | No conversion |
| C4-T017 | 角（完整金额） | P028 | historical currency expression | sen-based rendering for complete colonial-period amounts | inherited_locked | No — prior lock | Apply only to the complete amount `1角`; verify first-use note handling | Possible first-use explanation | Never create blind 角 = sen replacement |
| C4-T018 | 日本帝国主义 | P027, P054, P064 | political/historical concept | Japanese imperialism | inherited_locked | No — prior lock | Preserve authorial register | No automatic note | None |
| C4-T019 | 中日战争 | P048 | historical event | the Second Sino-Japanese War | inherited_locked | No — prior lock | Use for the war beginning in 1937 | No | None |
| C4-T020 | 本田宗一郎 | P057 | person | Soichiro Honda | inherited_locked | No — prior lock | Use established official form | No | Preserve printed biography |
| C4-T021 | 庆尚南道 | FB-F011 | place/administrative division | Gyeongsangnam-do | inherited_locked | No — prior lock | Translate only within the source footnote | Source footnote required | None |
| C4-T022 | 本田（企业语境） | P057 | organization/contextual company reference | Honda | inherited_locked | No — prior lock | Use Honda in ordinary prose; legal entity audited separately | No | Do not force legal name globally |

## New People

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T023 | 李孟熙 | P042 | person | Lee Maeng-hee | proposed | Yes | Verify Samsung-family established usage | No | No demonstrated conflict |
| C4-T024 | 李顺根 | P033, P040 | person/manager | Lee Sun-geun | needs_human_decision | Yes | Verify Hangul, identity, and established/project romanization | Possible | Identity evidence required |
| C4-T025 | 姜晋求 | P040 | person/executive | Kang Jin-ku | proposed | Yes | Verify Samsung historical English usage and title | Possible | No demonstrated conflict |
| C4-T026 | 金光镐 | P040 | person/executive | Kim Kwang-ho | proposed | Yes | Verify Samsung historical English usage and title | Possible | No demonstrated conflict |
| C4-T027 | 李健熙 | P040 | person/executive | Lee Kun-hee | proposed | Yes | Prefer established Samsung official form | No | None identified |
| C4-T028 | 栋居 | P046 | Japanese person/surname | Romanization unresolved; retain source surname pending verification | needs_human_decision | Yes | Do not invent a given name | Possible | Source-based identity uncertain |
| C4-T029 | 李再韶 | P049 | person/executive | Lee Jae-so, pending verified Korean form | needs_human_decision | Yes | Verify Hangul and corporate-history identity | Possible | Identity evidence required |
| C4-T030 | 李昌业 | P049 | person/executive | Lee Chang-eop, pending verified Korean form | needs_human_decision | Yes | Verify Hangul and corporate-history identity | Possible | Identity evidence required |
| C4-T031 | 金再明 | P049 | person/plant manager | Kim Jae-myeong, pending verified Korean form | needs_human_decision | Yes | Verify Hangul and corporate-history identity | Possible | Identity evidence required |
| C4-T032 | 李乙鹤 | P052 | person/repair-shop worker | Lee Eul-hak, pending verified Korean form | needs_human_decision | Yes | Verify Hangul and identity | Possible | Identity evidence required |
| C4-T033 | 吴胤根 | P004, P052, P062 | person/lender | Oh Yun-geun, pending verified Korean form | needs_human_decision | Yes | Use one verified form across all three occurrences | Possible | Identity evidence required |
| C4-T034 | 尹德英 | P059 | historical person | Yun Deok-yeong, pending established form | needs_human_decision | Yes | Verify identity and historical English usage | Possible | Identity evidence required |

## New Organizations, Businesses, and Brands

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T035 | 三星商会 | P006–P009, P012, P027, P029, P040, P043–P044, P050–P051 | historical business | Samsung Sanghoe / Samsung Trading Company | needs_human_decision | Yes | Establish first/later form without conflating it with Samsung Group | Possible | Historical-name/entity boundary requires verification |
| C4-T036 | 星标面条 / 星标牌面条 | P027, P029, P042 | historical brand/product | Star-brand noodles / Byeolpyo noodles | needs_human_decision | Yes | Decide translated brand versus retained historical name | No | Brand identity requires verification |
| C4-T037 | 三星商会贸易公司 | P050 | historical registered company | Samsung Sanghoe Trading Company | needs_human_decision | Yes | Preserve source registration narrative | Possible | Verify registered historical name and relation to C4-T035 |
| C4-T038 | 第一毛纺 | P039 | historical company | Cheil Industries | needs_human_decision | Yes | Verify period-specific official form and quotation treatment | Possible | Modern/historical entity-name mismatch possible |
| C4-T039 | 三星电子 | P039–P040 | company | Samsung Electronics | proposed | Yes | Use official form if human-approved | No | None identified |
| C4-T040 | 三星半导体 | P040 | historical business/division | Samsung Semiconductor | needs_human_decision | Yes | Determine historical entity/division rather than assume a current legal name | Possible | Historical entity scope may differ |
| C4-T041 | 首尔银行大邱分行 | P031 | historical bank branch | the Daegu branch of Seoul Bank | needs_human_decision | Yes | Verify bank identity and period name; later `the branch` allowed | Possible | Historical financial-entity identity possible |
| C4-T042 | 朝鲜酿造厂 | P046/P047, P049–P050 | historical brewery | Chosun Brewery / Chosen Brewery | needs_human_decision | Yes | Preserve cross-ID first occurrence; do not treat 朝鲜 as country text | Possible | Historical company name and romanization require verification |
| C4-T043 | 京城汽车修理厂 | P052 | historical repair business | Gyeongseong Auto Repair Shop | needs_human_decision | Yes | Descriptive/project form unless official name is verified | Possible | Historical business identity unverified |
| C4-T044 | 阿道汽车修理厂 | P052, P054, P056, P058, P063–P064 | historical repair business | Ado Auto Repair Shop | needs_human_decision | Yes | Establish stable first/later form; preserve source chronology | Possible | Historical business name requires verification |
| C4-T045 | 日本氮肥厂 | P058 | historical industrial entity | Japanese Nitrogen Fertilizer plant | needs_human_decision | Yes | Do not equate with a modern successor without evidence | Possible | Entity-identity conflict possible |
| C4-T046 | 现代汽车集团 | P057 | corporate group | Hyundai Motor Group / Hyundai, according to verified historical referent | needs_human_decision | Yes | Existing `Hyundai` lock does not automatically settle the full group name | Possible | Historical/current group-name mismatch possible |
| C4-T047 | 本田技研工业株式会社 | P057 | legal company name | Honda Motor Co., Ltd. | proposed | Yes | Use legal form only for the explicit legal-entity occurrence | No | Compatible with inherited contextual `Honda` lock |

## New Places, Regions, and Transport Geography

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T048 | 仁桥洞 | P008 | neighborhood | Ingyo-dong | proposed | Yes | Verify Daegu official romanization | No | None |
| C4-T049 | 西门市场 | P008 | market/place | Seomun Market | proposed | Yes | Prefer official English usage | No | None |
| C4-T050 | 京釜铁路 | P010 | railway | Gyeongbu Line | proposed | Yes | Preserve parenthetical Seoul–Busan explanation | No | None |
| C4-T051 | 岭南 | P010; FB-F011 | historical/geographic region | Yeongnam | proposed | Yes | Retain source footnote explanation | Source footnote required | None |
| C4-T052 | 浦项 | P012, P027 | place | Pohang | proposed | Yes | Use conventional official romanization | No | None |
| C4-T053 | 新义州 | P014, P019 | place | Sinuiju | proposed | Yes | Verify project geographic convention | No | None |
| C4-T054 | 元山 | P014, P019 | place | Wonsan | proposed | Yes | Use established geographic form | No | None |
| C4-T055 | 兴南 | P014, P019 | place | Hungnam | proposed | Yes | Use established historical geographic form | No | None |
| C4-T056 | 长春 | P014, P019 | place | Changchun | proposed | No — conventional form | Use Changchun | No | None |
| C4-T057 | 沈阳 | P014, P019, P028 | place | Shenyang | proposed | No — conventional form | Use Shenyang | No | None |
| C4-T058 | 青岛 | P014 | place | Qingdao | proposed | No — conventional form | Use Qingdao | No | None |
| C4-T059 | 山海关 | P019 | place/pass | Shanhaiguan | proposed | No — conventional form | Verify whether sentence means the pass or locality during review | No | None |
| C4-T060 | 北京 | P012, P015–P016, P019, P027 | place | Beijing | proposed | No — conventional form | Use Beijing | No | None |
| C4-T061 | 丹东 | P028 | place | Dandong | proposed | No — conventional form | Use Dandong | No | None |
| C4-T062 | 中国东北 | P012, P014–P016, P020–P021, P027 | region | Northeast China | proposed | No | Preserve regional meaning; do not substitute Manchuria automatically | No | None |
| C4-T063 | 华北 | P019 | region | North China | proposed | No | Use North China | No | None |
| C4-T064 | 东海 | P020–P021 | geographic expression | the East Sea / Korea's east coast, according to referent | needs_human_decision | Yes | Decide sea name versus coastal-region sense from context | Possible | Geographic naming/referent ambiguity |
| C4-T065 | 阿岘洞 | P052; FB-F013 | neighborhood | Ahyeon-dong | proposed | Yes | Preserve and translate FB-F013 | Source footnote required | None |
| C4-T066 | 新设洞 | P063 | neighborhood | Sinseol-dong | proposed | Yes | Prefer Seoul official romanization | No | None |
| C4-T067 | 临津江 | P058/P059 | river | Imjin River | proposed | Yes | Preserve cross-ID continuation | No | None |

## Historical Events, Political Context, and Transportation

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T068 | 太平洋战争 | P064 | historical event | the Pacific War | proposed | Yes | Preserve source claim that Japan started the war | No automatic note | Apply discrepancy policy if evidence conflicts with surrounding chronology |
| C4-T069 | 韩国解放 / 解放 | P054–P055, P064 | historical event/context | Korea's liberation / the liberation of Korea | proposed | Yes | Select natural syntax without altering dates | No | None |
| C4-T070 | 日本帝国主义统治 | P054 | colonial historical context | Japanese colonial rule | proposed | No | Preserve author's register; do not modernize the claim | No | None |
| C4-T071 | 战时粮食统制语境 | P027, P048, P064 | historical economic policy/context | wartime food controls / wartime economic controls | needs_human_decision | Yes | Translate by occurrence; do not invent an official policy title | Possible | Historical-policy precision requires review |
| C4-T072 | 木炭汽车 | P052 | historical transportation term | charcoal-powered vehicle | needs_human_decision | Yes | Verify vehicle technology and period English | Possible | No source correction |
| C4-T073 | 奥兹莫比尔 | P059 | vehicle brand | Oldsmobile | proposed | Yes | Preserve as brand name; do not infer model | No | None |

## Financial, Currency, and Unit Candidates

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T074 | 元 / 韩元（Chapter 4 historical amounts） | P006, P009, P031, P043, P049, P052, P062, P064 | historical currency | Currency form unresolved; preserve complete amounts pending period verification | needs_human_decision | Yes | Do not inherit Chapter 3's occurrence-limited yen rule blindly; do not convert values | Possible/likely required | `12万韩元` and unlabeled `元` may create a source/history discrepancy |
| C4-T075 | 加仑 / 升 | FB-F012 | capacity units in source footnote | gallons / liters | proposed | No | Preserve the source equation exactly; no conversion or correction | Source footnote required | Do not normalize the numerical claim |

## Roles, Business Concepts, Cultural Expressions, and Quotations

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T076 | 会长 | P040 | corporate title | chairman | needs_human_decision | Yes | Confirm each historical corporate role; do not translate as meeting chair | No | Title is context-sensitive |
| C4-T077 | 社长 | P049 | corporate title | president | needs_human_decision | Yes | Apply only to the brewery executive context | No | Distinguish from chairman |
| C4-T078 | 总监 | P049 | corporate title | managing director / general manager | needs_human_decision | Yes | Resolve from verified historical role; no mechanical one-to-one rule | No | Role hierarchy uncertain |
| C4-T079 | 厂长 | P049 | professional title | plant manager | proposed | No | Lowercase contextual title | No | None |
| C4-T080 | 专职经理 / 专职管理者体制 | P034, P040, P049 | business-management concept | professional manager / professional management system | needs_human_decision | No | Establish consistent distinction between person and system | No | Project-specific management terminology |
| C4-T081 | 市场调查 | P014, P022, P024, P026 | business term | market research | proposed | No | Use consistently without adding methodology | No | None |
| C4-T082 | 以质量取胜 / 高品质战略 | P002, P029–P030, P037, P039 | business strategy | compete on quality / a high-quality strategy | proposed | No | Preserve repeated management-principle wording | No | Do not flatten all forms without review |
| C4-T083 | 信用 | P004, P062 | business/social concept | trust / credibility, according to context | needs_human_decision | No | Preserve identical rendering in the intentional repetition | No | Avoid modern credit-score meaning |
| C4-T084 | 经营理念 | P001, P026, P035/P036 | business concept | management principles / business philosophy | proposed | No | Preserve the deliberate repeated structure | No | Choose one contextually consistent form |
| C4-T085 | 疑人不用，用人不疑 | P034 | management maxim | Do not employ those you doubt; do not doubt those you employ. | needs_human_decision | No | Source-attributed maxim; decide punctuation and proverb treatment | No | Do not present project wording as established quotation |
| C4-T086 | 噬脐莫及 | P018 | idiom | bitter regret that came too late | needs_human_decision | No | Translate the force naturally without adding explanation unsupported by source | No | Cultural idiom decision |
| C4-T087 | 既能造福他人，又能使自己获益的事业 | P019 | source quotation/business ideal | a business that benefits others while also benefiting oneself | needs_human_decision | No | Preserve quotation status and parallel meaning | No | Project-created quotation wording requires approval |
| C4-T088 | 商界巨擘 | P004, P062 | authorial epithet | business titan | proposed | No | Use identically in the repeated passage | No | Not an official title |
| C4-T089 | 日本商界三大神话之一 | P057 | authorial label | one of the three great legends of Japanese business | needs_human_decision | Yes | Do not reuse the Chapter 1 wording `the three great myths of Korean business` blindly | Possible | Conflicts with country-specific wording in existing lock |
| C4-T090 | 万念俱灭，一蹶不振 | P061 | paired idiomatic expression | lose all hope and never recover | needs_human_decision | No | Preserve emotional intensity without over-literal wording | No | Cultural idiom decision |
| C4-T091 | 清酒 / 米酒 / 药酒 | P045 | historical food-and-drink terms | sake / rice wine / medicinal wine | needs_human_decision | Yes | Verify Korean/Japanese product distinctions and whether a gloss is needed | Possible | Avoid collapsing distinct beverages |

## Visually Verified but Historically Reviewable Wording

| ID | Chinese term | CH04 locations | Category | Proposed English | Status | External verification | Occurrence-level treatment | Note | Conflict relevance |
|---|---|---|---|---|---|---|---|---|---|
| C4-T092 | 私家车、火车、公共汽车 | P054 | historical transport-count wording | private cars, trains, and buses | needs_human_decision | Yes | Preserve `火车` because the Project Lead visually verified the printed source; do not substitute `trucks` | Possible | Historical/semantic discrepancy possible; source correction forbidden |

## Historical Conflict and Note Queue (Pre-Decision)

Twelve candidates require special historical, entity, terminology-conflict, or source-discrepancy review:

`C4-T035`, `C4-T037`, `C4-T038`, `C4-T040`, `C4-T041`, `C4-T042`, `C4-T045`, `C4-T046`, `C4-T064`, `C4-T074`, `C4-T089`, and `C4-T092`.

At the audit stage, no translator/editor note was authorized. This pre-decision queue is retained for provenance; it is superseded by the five approved notes and final dispositions in `qa/chapter_04_terminology_decision.md`.

## Final Lock Resolution

| ID range | Count | Current status | Authority |
|---|---:|---|---|
| C4-T001–C4-T022 | 22 | inherited_locked | Existing master glossary; preserved without reopening |
| C4-T023–C4-T092 | 70 | locked | `qa/chapter_04_terminology_decision.md` |

Five mandatory translator/editor notes are reserved in textual order: `TN-CH04-001` at P006, `TN-CH04-002` at P028, `TN-CH04-003` at P031, `TN-CH04-004` at P049, and `TN-CH04-005` at P054. Their authoritative wording is stored in the decision record and the relevant glossary metadata.

## Final Gate

**PASS — READY FOR CONTROLLED TRANSLATION**

- Frozen source verified: Yes
- Total candidates recorded: 92
- Compatible inherited locks: 22
- Newly approved and locked: 70
- Unresolved: 0
- Proposed remaining: 0
- Needs human decision remaining: 0
- Mandatory translator/editor notes: 5
- Frozen source modified during terminology lock: No
- Chapter 4 translation created: No
