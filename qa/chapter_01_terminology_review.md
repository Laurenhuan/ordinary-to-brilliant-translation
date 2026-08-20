# Chapter 1 Terminology Review

Stage: 5A — Chapter 1 Translation Preparation

Scope: terminology and proper-name verification only. No Chapter 1 prose has been translated, and the frozen Chinese source remains unchanged. Candidate English forms below are research findings, not approved or locked glossary entries.

## Review summary

- Candidate count: 41
- Frozen-source segment binding: complete for all candidates
- `verified_english`: intentionally blank for all candidates
- `verified` or `locked` status: none
- Human decision: pending for every candidate
- Conflict register: `qa/chapter_01_terminology_conflicts.csv`
- Verification policy: `docs/TERMINOLOGY_VERIFICATION_GUIDE.md`

## Master glossary and duplicate audit

- `glossary/people.csv`: header only; no existing person entries to merge or conflict with.
- `glossary/organizations.csv`: header only; no existing organization or school entries to merge or conflict with.
- `glossary/glossary.csv`: header only; no existing general terminology entries to merge or conflict with.
- All 41 Chapter 1 Chinese candidate terms are unique.
- No repository-level `same Chinese → different English` conflict currently exists because the master glossaries contain no data rows.
- Five research/source-context conflicts or ambiguities are recorded separately. They cover official spelling variation, source-glyph/entity uncertainty, historical organization scope, classical-title variation, and a classical-title/generic-word sense ambiguity.

## Workflow status

- `researched`: 12
- `needs_context`: 14
- `needs_human_decision`: 15
- `verified`: 0
- `locked`: 0

## Person (8)

### C1-T001 — 李秉哲

- **Type:** `person`
- **Segment:** CH01-P003; CH01-P004; CH01-P006; CH01-P011; CH01-P012; CH01-P014; CH01-P024
- **Page:** FB-P014; FB-P015; FB-P017
- **Context:** 李秉哲（1910—1987）出生于大富之家。
- **Candidate English:** Lee Byung-chull
- **Evidence/source:** official organization: https://www.samsung.com/us/about-us/leadership-and-mission/heritage/ | https://news.samsung.com/global/the-history-of-samsung-electronics-1-paving-a-new-path-19681970
- **Codex recommendation:** Retain both official Samsung spellings as evidence; human reviewer should select one project form before locking.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T002 — 郑周永

- **Type:** `person`
- **Segment:** CH01-P003; CH01-P007; CH01-P008; CH01-P010; CH01-P011; CH01-P012; CH01-P013; CH01-P015; CH01-P016; CH01-P017; CH01-P021; CH01-P022; CH01-P027
- **Page:** FB-P014; FB-P015; FB-P016; FB-P017
- **Context:** 郑周永（1915—2001）生于江原道通川郡的一个贫农家庭。
- **Candidate English:** Chung Ju-yung
- **Evidence/source:** official organization: https://www1.hyundai.com/eu/about-hyundai/brand/heritage.html
- **Codex recommendation:** Use as a strong candidate only; require human approval before glossary lock.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T003 — 盛田昭夫

- **Type:** `person`
- **Segment:** CH01-P002; CH01-P010
- **Page:** FB-P014; FB-P015
- **Context:** 索尼创始人盛田昭夫是经营学的博士。
- **Candidate English:** Akio Morita
- **Evidence/source:** official organization: https://www.sony.com/en/SonyInfo/IR/library/ar/qfhh7c000000g753-att/ar_sony_2000.pdf
- **Codex recommendation:** Use as a strong candidate only; require human approval before glossary lock.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T004 — 小源浪平

- **Type:** `person`
- **Segment:** CH01-P002; CH01-P010
- **Page:** FB-P014; FB-P015
- **Context:** 日立集团的小源浪平连小学都没毕业。
- **Candidate English:** Namihei Odaira (conditional entity candidate)
- **Evidence/source:** official organization: https://www.hitachi.com/en/about/history/comic/namihei-odaira/
- **Codex recommendation:** First verify the Chinese glyph against the authorized PDF; only then decide whether the Hitachi founder evidence maps to this source term.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T005 — 李缵宇

- **Type:** `person`
- **Segment:** CH01-P006
- **Page:** FB-P015
- **Context:** 他出生于……宜宁的地主李缵宇家。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify the PDF glyph and identify an authoritative biographical or institutional source before proposing romanization.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T006 — 李洪锡

- **Type:** `person`
- **Segment:** CH01-P006
- **Page:** FB-P015
- **Context:** 李秉哲的祖父李洪锡是当时的一位鸿儒。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify the PDF glyph and identify an authoritative biographical or institutional source before proposing romanization.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T007 — 金玉均

- **Type:** `person`
- **Segment:** CH01-P019
- **Page:** FB-P016
- **Context:** 发动了甲申政变的才俊金玉均。
- **Candidate English:** Kim Ok-gyun
- **Evidence/source:** authoritative academic institution: https://www.aks.ac.kr/ikorea/upload/intl/korean/UserFiles/UKS6_Korea_Religious_Places_eng.pdf
- **Codex recommendation:** Record the Academy of Korean Studies form as evidence and obtain human approval before locking.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T008 — 李鸿章

- **Type:** `person`
- **Segment:** CH01-P019
- **Page:** FB-P016
- **Context:** 在……和李鸿章谈判之前。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Research authoritative historical/academic usage and let the reviewer select the project form.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

## Organization (3)

### C1-T009 — 索尼

- **Type:** `organization`
- **Segment:** CH01-P001; CH01-P010
- **Page:** FB-P014; FB-P015
- **Context:** 被称为商界三大神话的索尼创始人。
- **Candidate English:** Sony
- **Evidence/source:** official organization: https://www.sony.com/en/SonyInfo/CorporateInfo/History/
- **Codex recommendation:** Use the official organization form as a candidate; lock only after human review of historical naming context.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T010 — 日立集团

- **Type:** `organization`
- **Segment:** CH01-P002; CH01-P010
- **Page:** FB-P014; FB-P015
- **Context:** 日立集团的小源浪平。
- **Candidate English:** Hitachi / Hitachi Group
- **Evidence/source:** official organization: https://www.hitachi.com/en/about/history/comic/namihei-odaira/
- **Codex recommendation:** Determine whether the sentence refers to the historical company, the modern group, or an authorial generic label before selecting one form.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T011 — 东和旅馆

- **Type:** `organization`
- **Segment:** CH01-P019
- **Page:** FB-P016
- **Context:** 1894年上海东和旅馆。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Confirm entity type, source glyph, and historically attested English/romanized name before proposing a form.
- **Human decision:** Pending
- **Status:** `needs_context`

## Place (8)

### C1-T015 — 日本

- **Type:** `place`
- **Segment:** CH01-P001; CH01-P006; CH01-P010; CH01-P012
- **Page:** FB-P014; FB-P015
- **Context:** 在日本也有这类的例子。
- **Candidate English:** Japan
- **Evidence/source:** widely established conventional English; no external source recorded yet
- **Codex recommendation:** Confirm that the project will use conventional English country names; then lock consistently.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T016 — 庆尚南道

- **Type:** `place`
- **Segment:** CH01-P006
- **Page:** FB-P015
- **Context:** 他出生于庆尚南道宜宁。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify official romanization and decide how the historical administrative level will be expressed.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T017 — 宜宁

- **Type:** `place`
- **Segment:** CH01-P006
- **Page:** FB-P015
- **Context:** 庆尚南道宜宁。
- **Candidate English:** Uiryeong
- **Evidence/source:** official municipal source: https://www.uiryeong.go.kr/index.uiryeong?menuCd=DOM_000000306001002000
- **Codex recommendation:** Record the municipal English form as evidence; confirm historical-context treatment before locking.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T018 — 江原道

- **Type:** `place`
- **Segment:** CH01-P007
- **Page:** FB-P015
- **Context:** 生于江原道通川郡。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify the historical place name and administrative context; do not substitute a current jurisdiction automatically.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T019 — 通川郡

- **Type:** `place`
- **Segment:** CH01-P007
- **Page:** FB-P015
- **Context:** 生于江原道通川郡。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify historical jurisdiction and authoritative romanization before proposing a form.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T020 — 朝鲜

- **Type:** `place`
- **Segment:** CH01-P018; CH01-P019
- **Page:** FB-P016
- **Context:** 被朝鲜时代的读书人列为必读书目。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Choose context-specific historical wording at sentence level rather than imposing one English equivalent globally.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T021 — 上海

- **Type:** `place`
- **Segment:** CH01-P019
- **Page:** FB-P016
- **Context:** 1894年上海东和旅馆。
- **Candidate English:** Shanghai
- **Evidence/source:** widely established conventional English; no external source recorded yet
- **Codex recommendation:** Confirm the project rule for conventional English place names and then lock.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T022 — 清云洞

- **Type:** `place`
- **Segment:** CH01-P022
- **Page:** FB-P016
- **Context:** 在清云洞家中的一层。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify the Korean place name and official romanization; retain contextual flexibility for the administrative suffix.
- **Human decision:** Pending
- **Status:** `needs_context`

## School (3)

### C1-T012 — 早稻田大学

- **Type:** `school`
- **Segment:** CH01-P006; CH01-P012
- **Page:** FB-P015
- **Context:** 后来又到日本的早稻田大学留学。
- **Candidate English:** Waseda University
- **Evidence/source:** official institution: https://www.waseda.jp/top/en/
- **Codex recommendation:** Use the university's official English name as a candidate; human reviewer still performs the project lock.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T013 — 文山亭书院

- **Type:** `school`
- **Segment:** CH01-P014
- **Page:** FB-P015
- **Context:** 在祖父开设的文山亭书院学习。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify the institution type and Korean name before choosing transliteration or a descriptive rendering.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T014 — 松田小学

- **Type:** `school`
- **Segment:** CH01-P007
- **Page:** FB-P015
- **Context:** 在私塾和松田小学的学习。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Verify the school and locality in an authoritative Korean or biographical source before proposing a name.
- **Human decision:** Pending
- **Status:** `needs_context`

## Historical term (3)

### C1-T030 — 朝鲜时代

- **Type:** `historical_term`
- **Segment:** CH01-P018
- **Page:** FB-P016
- **Context:** 被朝鲜时代的读书人列为必读书目。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Research authoritative historical period naming and choose a project convention with sentence-level context.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T031 — 朝鲜末期

- **Type:** `historical_term`
- **Segment:** CH01-P019
- **Page:** FB-P016
- **Context:** 朝鲜末期的著名书法家。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Confirm what time span the source intends and choose a contextual English rendering after human review.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T032 — 甲申政变

- **Type:** `historical_term`
- **Segment:** CH01-P019
- **Page:** FB-P016
- **Context:** 发动了甲申政变。
- **Candidate English:** Gapsin Coup
- **Evidence/source:** authoritative academic institution: https://dh.aks.ac.kr/Edu/wiki/index.php/GGHS_2019_Winter_-_Team_5
- **Codex recommendation:** Record the Academy of Korean Studies form as evidence and obtain human approval before locking.
- **Human decision:** Pending
- **Status:** `researched`

## Classical text (7)

### C1-T023 — 《千字文》

- **Type:** `classical_text`
- **Segment:** CH01-P014; CH01-P023; CH01-P024
- **Page:** FB-P015; FB-P016; FB-P017
- **Context:** 学习《千字文》。
- **Candidate English:** Thousand Character Classic
- **Evidence/source:** authoritative English-language cultural source: https://tile.loc.gov/storage-services/master/gdc/gdcebookspublic/20/20/71/98/19/2020719819/2020719819.pdf
- **Codex recommendation:** Record the established-looking English title as evidence; human reviewer decides title styling and first-use treatment.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T024 — 《资治通鉴》

- **Type:** `classical_text`
- **Segment:** CH01-P014; CH01-P015; CH01-P016; CH01-P018; CH01-P019; CH01-P020; CH01-P023
- **Page:** FB-P015; FB-P016
- **Context:** 学了《资治通鉴》。
- **Candidate English:** Comprehensive Mirror in Aid of Governance
- **Evidence/source:** authoritative academic source: https://afe.easia.columbia.edu/songdynasty-module/confucian-neo.html
- **Codex recommendation:** Record the Columbia form and research title variants before a human selects the project title.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T025 — 《论语》

- **Type:** `classical_text`
- **Segment:** CH01-P014; CH01-P024; CH01-P025
- **Page:** FB-P015; FB-P017
- **Context:** 五年间学了《论语》等书。
- **Candidate English:** The Analects / The Analects of Confucius
- **Evidence/source:** authoritative academic source: https://afe.easia.columbia.edu/songdynasty-module/confucian-neo.html | https://afe.easia.columbia.edu/special/china_1000bce_confucius_say.htm
- **Codex recommendation:** Preserve both documented title forms and let the human reviewer select one project form and styling rule.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T026 — 《小学》

- **Type:** `classical_text`
- **Segment:** CH01-P015; CH01-P018; CH01-P023
- **Page:** FB-P015; FB-P016
- **Context:** 三年间学了《小学》、《大学》。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** First confirm the specific classical text intended; do not confuse it with the generic word primary school.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T027 — 《大学》

- **Type:** `classical_text`
- **Segment:** CH01-P015; CH01-P016; CH01-P018; CH01-P023
- **Page:** FB-P015; FB-P016
- **Context:** 三年间学了《小学》、《大学》。
- **Candidate English:** The Great Learning
- **Evidence/source:** authoritative academic source: https://afe.easia.columbia.edu/ps/cup/zhuxi_learning.pdf
- **Codex recommendation:** Record the academic title as evidence; human reviewer decides styling and disambiguation before lock.
- **Human decision:** Pending
- **Status:** `researched`

### C1-T028 — 《通鉴节要》

- **Type:** `classical_text`
- **Segment:** CH01-P018
- **Page:** FB-P016
- **Context:** 与《通鉴节要》、《通鉴纲目》。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Identify the exact work and research an established title; otherwise prepare verified romanization for human review.
- **Human decision:** Pending
- **Status:** `needs_context`

### C1-T029 — 《通鉴纲目》

- **Type:** `classical_text`
- **Segment:** CH01-P018
- **Page:** FB-P016
- **Context:** 与《通鉴节要》、《通鉴纲目》。
- **Candidate English:** —
- **Evidence/source:** unverified; no external source recorded yet
- **Codex recommendation:** Identify the exact work and research an established title; otherwise prepare verified romanization for human review.
- **Human decision:** Pending
- **Status:** `needs_context`

## Title or role (2)

### C1-T033 — 鸿儒

- **Type:** `title_role`
- **Segment:** CH01-P006
- **Page:** FB-P015
- **Context:** 是当时的一位鸿儒。
- **Candidate English:** —
- **Evidence/source:** contextual translation required; no external source recorded yet
- **Codex recommendation:** Translate in sentence context; do not register it as a formal office without evidence.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T034 — 地主

- **Type:** `title_role`
- **Segment:** CH01-P005; CH01-P006
- **Page:** FB-P015
- **Context:** 可以收获……石的地主家庭。
- **Candidate English:** —
- **Evidence/source:** contextual translation required; no external source recorded yet
- **Codex recommendation:** Choose a historically and socioeconomically appropriate rendering; record a default only after human review.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

## Unit (1)

### C1-T035 — 石

- **Type:** `unit`
- **Segment:** CH01-P005
- **Page:** FB-P015
- **Context:** 收获 2000 石……1500 石。
- **Candidate English:** —
- **Evidence/source:** manual source and unit research required; no external source recorded yet
- **Codex recommendation:** Verify the unit in this historical context; human reviewer chooses transliteration, conversion note, or brief gloss. Preserve all numbers.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

## Cultural concept (5)

### C1-T036 — 私塾

- **Type:** `cultural_concept`
- **Segment:** CH01-P006; CH01-P007; CH01-P013; CH01-P015; CH01-P016; CH01-P024
- **Page:** FB-P015; FB-P016; FB-P017
- **Context:** 在私塾学过一阵汉学。
- **Candidate English:** —
- **Evidence/source:** contextual translation required; no external source recorded yet
- **Codex recommendation:** Compare translation, transliteration, and brief-gloss options; human reviewer selects first-use and later-use treatment.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T037 — 仁、和、乐

- **Type:** `cultural_concept`
- **Segment:** CH01-P025; CH01-P026
- **Page:** FB-P017
- **Context:** ‘仁、和、乐’的精神境界。
- **Candidate English:** —
- **Evidence/source:** manual classical-source review required; no external source recorded yet
- **Codex recommendation:** Research the classical concepts and preserve the three-part relationship; human reviewer chooses capitalization and gloss strategy.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T038 — 一勤天下无难事

- **Type:** `cultural_concept`
- **Segment:** CH01-P022
- **Page:** FB-P016
- **Context:** 他最喜欢的名句‘一勤天下无难事’。
- **Candidate English:** —
- **Evidence/source:** manual quotation-source review required; no external source recorded yet
- **Codex recommendation:** Check attribution/source status and prepare translation strategy options for human decision.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T039 — 有志者事竟成

- **Type:** `cultural_concept`
- **Segment:** CH01-P022
- **Page:** FB-P016
- **Context:** 引用‘有志者事竟成’。
- **Candidate English:** —
- **Evidence/source:** manual quotation-source review required; no external source recorded yet
- **Codex recommendation:** Research established English renderings and present alternatives with sources; human reviewer selects the project form.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

### C1-T040 — 致知在格物

- **Type:** `cultural_concept`
- **Segment:** CH01-P022
- **Page:** FB-P016
- **Context:** 引用‘致知在格物’等格言。
- **Candidate English:** —
- **Evidence/source:** manual classical-source review required; no external source recorded yet
- **Codex recommendation:** Verify the classical source and terminology, then present sourced options for human decision.
- **Human decision:** Pending
- **Status:** `needs_human_decision`

## Other (1)

### C1-T041 — 商界三大神话

- **Type:** `other`
- **Segment:** CH01-P001; CH01-P010
- **Page:** FB-P014; FB-P015
- **Context:** 被称为商界三大神话的索尼创始人。
- **Candidate English:** —
- **Evidence/source:** project-specific translation decision; no external source recorded yet
- **Codex recommendation:** Determine whether this authorial label needs quotation marks, a brief explanation, or a direct project rendering.
- **Human decision:** Pending
- **Status:** `needs_human_decision`
