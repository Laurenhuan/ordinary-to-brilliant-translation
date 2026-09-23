# Final Human Decision Packet — Chapters 5–28 + Afterword

Status: Project-lead decisions approved and applied by the final controlled revision.

Scope: the 74 formerly open Review IDs in `qa/chapters_05_28_full_translation_review.md`, plus the evidence check for the already-remediated CH10-P071 parser item.

## Part 1 — Critical Blockers

### BR-CH15-001

- Chapter: 15
- Paragraph: chapter-level; body begins at CH15-P001
- Source page: FB-P136; input PDF page 136; printed page unknown
- Chinese excerpt: `# 15 郑周永的船和李秉哲的彩色电视` / `可是技术工人很成问题……`
- Current English excerpt: `Chung Ju-yung's Ships and Lee Byung-chull's Color Television` / `Skilled workers, however, posed a serious problem.`
- Problem: the title promises a Lee Byung-chull color-television section, but all 73 available body paragraphs concern Chung Ju-yung and shipbuilding before Chapter 16 begins.
- Proposed revision: do not revise yet. Compare the complete printed Chapter 15 with FB-P136–FB-P145. If content is missing from extraction, restore it with stable mappings and translate it; if the printed book itself contains the mismatch, preserve it and add a neutral editorial note.
- Why Critical: an entire thematic section may be missing, so publication could omit substantial source content.
- PDF visual verification result: the printed title/body mismatch is confirmed; no body content is missing.
- Approved human decision: preserve the title and complete body; add TN-CH15-001.
- Final status: resolved.

### BR-CH26-001

- Chapter: 26
- Paragraph: CH26-P001
- Source page: FB-P222; input PDF page 222; printed page unknown
- Chinese excerpt: `品性将决定一个人的。`
- Current English excerpt: `Character will determine a person's. . . .`
- Problem: the source sentence is truncated before its object.
- Proposed revision: if the printed page supplies the missing word(s), restore and translate them exactly; if the printed page is also incomplete, retain the fragment and add a short source-condition note.
- Why Critical: the chapter-opening maxim is semantically incomplete and cannot be responsibly reconstructed by inference.
- PDF visual verification result: the printed sentence ends `品性将决定一个人的命运。`
- Approved human decision: restore `命运` in canonical source and translate `Character will determine a person's destiny.`
- Final status: resolved.

## Part 2 — PDF Visual Verification Queue

The twelve checks below are ordered by chapter and source page. They cover 14 formerly open Review IDs; A-V09 is an additional evidence check for the already-remediated CH10-P071 parser item. All twelve checks are now resolved by project-lead visual decisions.

### A-V03 — BR-CH06-001

- Chapter / location: Chapter 6, CH06-P026
- Page: FB-P053; input PDF 53; printed 40
- Suspect source: `在奈良的一家旅馆神堂屋于16世纪开业`
- Possibilities: `神堂屋` is printed as extracted; or one or more characters are OCR errors.
- Current English: `The Shindoya inn in Nara opened in the sixteenth century...`
- Confirm visually: the exact three-character inn name.
- Result paths: OCR error → correct canonical extraction and revise the romanization/name; printed as-is → preserve Chinese and keep `Shindoya inn` as a source-based form unless stronger identity evidence is approved.

### A-V01 — BR-CH07-002

- Chapter / location: Chapter 7, CH07-P100 and CH07-P102
- Page: FB-P063; input PDF 63; printed 50
- Suspect source: `纯利润就达到了1.6亿元` versus `第一年的纯利润还是达到了30亿元`
- Possibilities: both figures are printed; or one figure contains an OCR digit/unit error.
- Current English: `160 million won` and `three billion won`.
- Confirm visually: every digit, decimal point, and unit in both statements.
- Result paths: OCR error → correct source and translation to the printed figure; both printed → preserve both and approve a neutral source-conflict note.

### A-V04 — BR-CH08-001

- Chapter / location: Chapter 8, CH08-P036
- Page: FB-P069; input PDF 69; printed 56
- Suspect source: `依被苍生`
- Possibilities: printed `依被苍生`; or OCR for `衣被苍生`.
- Current English: `Clothe the People.`
- Confirm visually: first character and the complete four-character inscription.
- Result paths: OCR error → correct Chinese to the printed form; printed as extracted → preserve Chinese. The current semantic English may remain unless the confirmed characters require another rendering.

### A-V05 — BR-CH08-002

- Chapter / location: Chapter 8, CH08-P065
- Page: FB-P071; input PDF 71; printed 58
- Suspect source: `连接大邱和局昌之间`
- Possibilities: printed `局昌`; or OCR for `居昌`.
- Current English: `connected Daegu and Geochang`.
- Confirm visually: the first character of the place name.
- Result paths: OCR error → correct source to `居昌`; printed `局昌` → preserve Chinese and retain verified/contextual `Geochang` with disclosure only if the project lead considers the discrepancy material.

### A-V06 — BR-CH08-003

- Chapter / location: Chapter 8, CH08-P066
- Page: FB-P071; input PDF 71; printed 58
- Suspect source: `整个工程总额为5457亿` and `共损失6500余万元`
- Possibilities: `5457亿` is printed; or digits/decimal/unit were misread.
- Current English: `545.7 billion won` and `more than 65 million won`.
- Confirm visually: all digits and the currency unit in both amounts.
- Result paths: OCR error → correct source and English amount; printed as-is → preserve both and consider a neutral scale-discrepancy note.

### A-V02 — BR-CH09-002

- Chapter / location: Chapter 9, CH09-P055
- Page: FB-P078; input PDF 78; printed 65
- Suspect source: `每年给一个人投入8000千万韩元，共投入1600亿韩元给两千余名职员`
- Possibilities: malformed printed amount; OCR error; or intended 80 million inferred from the stated total and headcount.
- Current English: `80 million won per person ... a total of 160 billion won ... more than two thousand employees`.
- Confirm visually: the complete per-person amount, especially the characters around `8000` and `千万`.
- Result paths: OCR error → use the printed amount; printed malformed form → preserve source, retain any approved inferred English only with a neutral note; printed unambiguously different → revise English literally.

### A-V07 — BR-CH09-003

- Chapter / location: Chapter 9, CH09-P060
- Page: FB-P079; input PDF 79; printed 66
- Suspect source: `现代比三春晚一年`
- Possibilities: printed `三春`; or OCR for `三星`.
- Current English: `Hyundai ... one year later than Samsung.`
- Confirm visually: final character of the company name.
- Result paths: OCR error → correct source to `三星`; printed `三春` → preserve Chinese and keep contextual `Samsung`, adding a neutral disclosure if approved.

### A-V08 — BR-CH09-004

- Chapter / location: Chapter 9, CH09-P090
- Page: FB-P081; input PDF 81; printed 68
- Suspect source: `丰田麦芽糖工厂`
- Possibilities: the four-character factory name is printed as extracted; or one or more characters are OCR errors.
- Current English: `the Toyoda Malt-Sugar Factory`.
- Confirm visually: exact factory name and any adjacent identifying text.
- Result paths: OCR error → correct source and use the identified factory's verified name; printed as-is → keep the descriptive source-based English and do not claim official status.

### A-V09 — CH10-P071 evidence follow-up

- Chapter / location: Chapter 10, CH10-P071
- Page: FB-P091; input PDF 91; printed page unknown
- Suspect source: `The OCR result should be empty ... only a stylistic horizontal line...`
- Possibilities: blank/separator page with only a decorative rule; or actual printed content omitted by extraction.
- Current English: no publication-facing prose; an HTML comment records the blank-page interpretation.
- Confirm visually: whether FB-P091 contains semantic text.
- Result paths: blank/separator → retain current hidden metadata; semantic content present → restore canonical source content and translate it under CH10-P071.

### A-V10 — BR-CH11-002, BR-CH11-003, BR-CH11-004

- Chapter / locations: Chapter 11 title; CH11-P046; CH11-P061
- Pages: FB-P092/input 92/printed unknown; FB-P096/input 96/printed 83; FB-P097/input 97/printed 84
- Suspect source: `权利面前的两个人`; `金字中的大宇汽车`; `郑州永要求给两个星期`
- Possibilities: OCR for `权力`, `金宇中`, and `郑周永`; or those differing forms are printed in the book.
- Current English: `Two Men in the Face of Power`; `Kim Woo-choong`; `Chung Ju-yung`.
- Confirm visually: each disputed character on the three printed pages.
- Result paths: OCR errors → correct canonical extraction while retaining current English; printed-source forms → preserve Chinese, retain the intended/verified English forms, and add concise neutral disclosures where material.

### A-V11 — BR-CH11-005 and BR-CH12-002

- Chapter / locations: FB-F017, FB-F018, FB-F019, FB-F020
- Pages: FB-P094/input 94/printed 81; FB-P096/input 96/printed 83; FB-P097/input 97/printed 84; FB-P100/input 100/printed 87
- Suspect source bodies: `① 1961年……议长为张都焕……`; `① 昌原，位于韩国庆尚南道。`; `① 全经联，韩国“全国经济人联合会”的简称。`; `① 京纺，韩国“京城纺织株式会社”的简称。`
- Possibilities: the page-map bodies and markers correspond exactly; one or more bodies/markers are absent, displaced, or mapped to a different paragraph.
- Pre-decision English state: four provisionally restored footnotes under stable IDs; FB-F017 used verified `Chang Do-yong` with disclosure, while FB-F020's marker was still unresolved.
- Confirm visually: marker occurrence, marker symbol, body wording, and paragraph-to-footnote association for all four notes.
- Result paths: mapping confirmed → approve restored footnotes and clear provisional metadata; mismatch → correct only the affected marker/body/location while retaining each stable ID where possible.

### A-V12 — BR-CH12-003

- Chapter / location: Chapter 12, CH12-P084
- Page: FB-P106; input PDF 106; printed 93
- Suspect source: `韩国是如果掘地的`
- Possibilities: malformed printed sentence; or OCR corruption of a grammatical phrase.
- Current English: `In Korea, digging into the ground would turn up either stones or bedrock.`
- Confirm visually: the complete clause before `挖出来的`.
- Result paths: OCR error → correct source and align English to the printed reading; printed malformed form → preserve Chinese and retain the conservative contextual English, with a note only if requested.

## Part 3 — Non-Visual Human Decisions

The 58 items below are every other formerly open Review ID after excluding the two Critical blockers and the 14 IDs represented by the twelve-check visual queue. Their recommendations were approved.

### A. Major translation corrections

| Review ID | Chapter / paragraph | Severity | One-sentence problem | Exact proposed action | Recommended decision |
|---|---|---|---|---|---|
| BR-CH13-005 | CH13-P078 | Major | Annual output appears as both 33 and 330,000 tons. | Preserve both figures and add the neutral note proposed in Part 5 unless later page evidence resolves the conflict. | KEEP SOURCE CLAIM + NOTE |
| BR-CH14-004 | CH14-P068/P072 | Major | Expressway cost comparisons and 31.5 billion won do not align. | Preserve all figures and add the neutral internal-inconsistency note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH14-005 | CH14-P082 | Major | The text says Korea had 1,400 machines but Chung purchased 1,900. | Preserve both figures and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH14-007 | CH14-P108 | Major | A visible “No semantic source text” placeholder can leak into publication output. | Replace visible placeholder prose with an HTML metadata comment while retaining CH14-P108 and its page position. | APPROVE |
| BR-CH15-004 | CH15-P057 | Major | September 1971 plus one year three months conflicts with March 22, 1972. | Preserve the chronology and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH16-002 | CH16-P026 | Major | “Ten years later, in 1984” conflicts with the preceding 1969 reference. | Preserve the source dates and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH16-005 | CH16-P124 | Major | The sequence repeats 1982 and includes a literal 113 dollars. | Preserve the source sequence and amount and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH18-002 | CH18-P010/P011 | Major | Six billion is called both roughly one quarter of and four times smaller than 21 billion. | Preserve the author's comparison and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH18-004 | CH18-P089 | Major | “World first,” second-place market share, and first-place capacity are not clearly distinguished. | Retain the rankings and add the clarifying source-preserving note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH18-006 | CH18-P102 | Major | A visible decorative-page placeholder can enter publication output. | Convert the visible explanation to an HTML metadata comment without removing the stable paragraph. | APPROVE |
| BR-CH22-004 | CH22-P032 | Major | The source says the British Museum itself was completed in 1997. | Keep the source statement and add the neutral Korean-Gallery note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH23-003 | CH23-P042 | Major | “Sink nine shots each week” is intelligible only as a highly uncertain golf rendering. | Leave the current conservative wording unchanged until the printed wording is supplied; do not invent a golf statistic. | KEEP AS IS |
| BR-CH26-002 | CH26-P006 | Major | “Father and three sons” is followed by only two named sons and then three brothers. | Preserve the enumeration and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH26-003 | CH26-P021 | Major | A February 1995 statement is attributed to Lee Byung-chull, who died in 1987. | Preserve the source attribution and add the Entity Identity Conflict note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH27-002 | CH27-P017 | Major | Samsung Life assets appear as only five billion won. | Preserve the amount and add the neutral scale-warning note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH27-003 | CH27-P030 | Major | The memory-chip quantities 157.8 million and 23 billion may contain malformed units or digits. | Preserve both quantities and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH27-004 | CH27-P058 | Major | A visible “No semantic text” placeholder remains publication-facing. | Convert the explanation to HTML metadata while preserving CH27-P058 and its page position. | APPROVE |
| BR-AW-001 | AW-P001 | Major | `Qiji` may be an OCR artifact in the afterword heading. | Keep the current heading until the printed page is supplied; do not guess a replacement. | KEEP AS IS |
| BR-AW-004 | AW-P022/P023 | Major | Anna's Archive metadata appears under `Translation:`. | Move the archive/extraction explanations into HTML metadata while preserving both stable IDs. | APPROVE |

### B. Entity / historical identity decisions

| Review ID | Chapter / paragraph | Severity | One-sentence problem | Exact proposed action | Recommended decision |
|---|---|---|---|---|---|
| BR-CH10-002 | CH10-P009–P016 | Note | Chohung and Heunghwa historical company names are source-based transliterations. | Retain them as source-based forms and make no official-name claim. | KEEP AS IS |
| BR-CH13-003 | CH13-P058–P060 | Note | 郑载霞/郑载葭 may be variants for the same person. | Use `Chung Jae-ha` consistently as provisional project romanization. | KEEP AS IS |
| BR-CH13-004 | CH13-P062 | Note | `Weecho` has no verified official historical form. | Retain `Weecho` and label it source-based in internal terminology records. | KEEP AS IS |
| BR-CH14-002 | CH14-P045 | Note | `乔治亚男` is contextually treated as Giorgetto Giugiaro. | Keep `Giorgetto Giugiaro`; do not alter the Chinese source without page evidence. | KEEP AS IS |
| BR-CH14-003 | CH14-P047/P050 | Note | H. W. Benki and Camina remain unverified historical forms. | Retain both source-based forms without official-status claims. | KEEP AS IS |
| BR-CH14-006 | CH14-P100 | Note | `Hunpin` cannot be reliably tied to a historic television brand. | Retain `Hunpin` provisionally. | KEEP AS IS |
| BR-CH15-003 | CH15-P016/P067 | Note | Lombardon and Ireland Shipping Company are unverified historical names. | Retain the conservative source-based forms. | KEEP AS IS |
| BR-CH16-003 | CH16-P066/P069 | Note | ASRY and the Jamsil comparison depend on provisional source interpretation. | Retain the abbreviation and mapped explanation without expansion. | KEEP AS IS |
| BR-CH16-004 | CH16-P072/P073 | Note | Several foreign engineering-company names derive from Chinese transliteration. | Retain the current contextual forms and avoid official-name claims. | KEEP AS IS |
| BR-CH21-002 | CH21-P018 | Note | `Yeri in Gunsan` lacks a verified modern place form. | Retain the source-based place rendering. | KEEP AS IS |
| BR-CH22-003 | CH22-P030/P031 | Note | Museum artifact titles are descriptive rather than catalog-verified. | Retain descriptive titles and do not present them as official catalog names. | KEEP AS IS |
| BR-CH23-001 | CH23-P008 | Note | `Haruyoshi Kobari` is not definitively verified. | Retain it as source-based romanization. | KEEP AS IS |
| BR-CH23-002 | CH23-P021 | Note | `Kennedy Smith` may not reproduce the historic golf-club brand exactly. | Retain the readable source-based brand form. | KEEP AS IS |
| BR-CH25-003 | CH25-P017 | Note | A dense affiliate chronology contains unverified historical brand forms. | Keep the current consistent forms; defer archive-level verification. | KEEP AS IS |
| BR-CH25-004 | CH25-P040–P042 | Note | The vessel name `Waterwill` is unverified. | Retain the source-based vessel name without claiming official spelling. | KEEP AS IS |
| BR-CH25-005 | CH25-P046 | Note | Two Chinese organization forms are normalized to Korea-Soviet Economic Association. | Keep the consistent contextual English form. | KEEP AS IS |
| BR-CH27-001 | Chapter 27 name lists | Note | Numerous executive names rely on project romanization. | Retain current consistent forms unless corporate archival spellings are later supplied. | KEEP AS IS |
| BR-AW-003 | AW-P012 | Note | 古灵台 differs from the earlier 高灵桥 form. | Retain contextual `Goryeong Bridge` without changing the Chinese source. | KEEP AS IS |

### C. Translator/editor-note decisions

| Review ID | Chapter / paragraph | Severity | One-sentence problem | Exact proposed action | Recommended decision |
|---|---|---|---|---|---|
| BR-CH10-003 | CH10-P034 | Note | The source says Japan earned 6.2 billion dollars from postwar UN supply sales. | Preserve the claim and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH19-001 | CH19-P033 | Note | The source characterizes April 19 as a military coup. | Preserve the wording and add the neutral historical-label note in Part 5. | KEEP SOURCE CLAIM + NOTE |
| BR-CH25-006 | CH25-P064 | Note | Cumulative export and company-scale figures are compared without a common basis. | Preserve the comparison and add the neutral note in Part 5. | KEEP SOURCE CLAIM + NOTE |

### D. Minor issues worth fixing

| Review ID | Chapter / paragraph | Severity | One-sentence problem | Exact proposed action | Recommended decision |
|---|---|---|---|---|---|
| BR-CH14-008 | CH14-P028 | Minor | The source's explicit `100%` became only “wholly Korean-made.” | Change the phrase to `a 100-percent Korean-made car`, with no other sentence change. | APPROVE |

### E. Issues recommended to leave unchanged

| Review ID | Chapter / paragraph | Severity | One-sentence problem | Exact proposed action | Recommended decision |
|---|---|---|---|---|---|
| BR-CH13-001 | FB-F021–FB-F024 | Note | Four footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-CH13-002 | CH13-P023 | Note | `自保不前` is malformed and was conservatively rendered as “hesitated.” | Keep the approved contextual rendering. | KEEP AS IS |
| BR-CH14-001 | FB-F025–FB-F028 | Note | Four footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-CH15-002 | FB-F029 | Note | The footnote body is a page-map restoration. | Keep the stable ID and current body; defer visual certification. | KEEP AS IS |
| BR-CH15-005 | CH15-P061 | Note | “Completed 1.947 million tons” has an uncertain technical referent. | Keep the literal conservative wording. | KEEP AS IS |
| BR-CH16-001 | FB-F030–FB-F035 | Note | Six footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-CH18-001 | FB-F036–FB-F037 | Note | Two footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-CH18-003 | CH18-P039/P062/P063 | Note | 64KD/64MD/4GD were normalized as DRAM generations. | Keep the technically intelligible normalization. | KEEP AS IS |
| BR-CH18-005 | CH18-P101 | Note | The hair-width/four-hundred-story comparison is technically imprecise. | Preserve the author's analogy without editorial correction. | KEEP AS IS |
| BR-CH21-001 | FB-F038–FB-F039 | Note | Two footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-CH22-001 | CH22-P001 | Note | A false Markdown heading interrupted a quoted question in the source extraction. | Keep the current uninterrupted English structure. | KEEP AS IS |
| BR-CH22-002 | FB-F040–FB-F045 | Note | Six footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-CH24-001 | FB-F046 | Note | The footnote body is a page-map restoration. | Keep the stable ID and current body; defer visual certification. | KEEP AS IS |
| BR-CH24-002 | CH24-P039–P043 | Note | Yarn-count and wool claims need specialist confirmation. | Preserve the source figures and current readable terminology. | KEEP AS IS |
| BR-CH25-001 | CH25-P001/P067–P070 | Note | Repeated lyrics have uncertain printed lineation. | Preserve wording, stable paragraphs, and current lineation. | KEEP AS IS |
| BR-CH25-002 | FB-F047–FB-F048 | Note | Two footnotes are page-map restorations. | Keep stable IDs and current bodies; defer visual certification. | KEEP AS IS |
| BR-AW-002 | FB-F049 | Note | The footnote body is a page-map restoration. | Keep the stable ID and current body; defer visual certification. | KEEP AS IS |

## Part 4 — Recommended for Bulk Approval

- `BR-CH14-007` — obvious publication-facing parser/decorative placeholder; hide it as metadata while retaining structure.
- `BR-CH18-006` — same parser/decorative leakage pattern and same non-semantic remedy.
- `BR-CH27-004` — same visible “No semantic text” leakage; metadata-only conversion is lossless.
- `BR-AW-004` — external archive metadata is not book content and should be hidden without removing stable IDs.
- `BR-CH14-008` — direct omission of the explicit source quantity `100%`; restoring `100-percent` changes no underlying meaning.

Recommended bulk-approval count: 5.

## Part 5 — Recommended Source-Preserving Notes

| Review ID | Proposed final note wording |
|---|---|
| BR-CH10-003 | `The source gives the figure as 6.2 billion dollars; this claim is reproduced here without independent historical correction.` |
| BR-CH13-005 | `The source gives two different annual-output figures—33 tons and 330,000 tons—which are preserved as printed/extracted.` |
| BR-CH14-004 | `The source's expressway cost figures and comparisons do not fully reconcile; they are preserved without silent correction.` |
| BR-CH14-005 | `The source states that Korea had about 1,400 such machines while also stating that Chung purchased 1,900; both figures are preserved.` |
| BR-CH15-004 | `The dates and elapsed time in the source do not fully reconcile; the source chronology is preserved.` |
| BR-CH16-002 | `The source describes 1984 as ten years after a 1969 reference; both dates are preserved.` |
| BR-CH16-005 | `The source repeats the year 1982 in this sequence and gives the amount as 113 dollars; these details are preserved without correction.` |
| BR-CH18-002 | `The source describes the relationship between six billion and twenty-one billion in two inconsistent ways; both statements are preserved.` |
| BR-CH18-004 | `The source distinguishes market share, production capacity, and an overall world ranking without fully clarifying their bases.` |
| BR-CH19-001 | `The source characterizes the April 19 event as a military coup; the historical label is preserved as part of the author's account.` |
| BR-CH22-004 | `The source states that the British Museum was completed in 1997; the date appears to correspond instead to the opening of its Korean Gallery.` |
| BR-CH25-006 | `The source compares cumulative national export figures with company-scale figures that are not presented on a common statistical basis.` |
| BR-CH26-002 | `The family count and the individuals named in the source do not fully correspond; the enumeration is preserved.` |
| BR-CH26-003 | `The source attributes this February 1995 statement to Lee Byung-chull, who died in 1987; the source attribution is preserved.` |
| BR-CH27-002 | `The source gives Samsung Life's assets as five billion won; the figure is preserved without independent correction.` |
| BR-CH27-003 | `The memory-chip production figures and units are reproduced from the source and may require verification against the printed edition.` |

Recommended note-only decision count: 16.

## Part 6 — Recommended No-Action / Defer

The following 37 Review IDs do not presently justify changing reader-facing prose in an accelerated publication:

- `BR-CH10-002`, `BR-CH13-003`, `BR-CH13-004`, `BR-CH14-002`, `BR-CH14-003`, `BR-CH14-006`, `BR-CH15-003`, `BR-CH16-003`, `BR-CH16-004`, `BR-CH21-002`, `BR-CH22-003`, `BR-CH23-001`, `BR-CH23-002`, `BR-CH25-003`, `BR-CH25-004`, `BR-CH25-005`, `BR-CH27-001`, `BR-AW-003` — harmless or low-value historical-name/romanization uncertainty; current forms are readable and consistently treated as source-based rather than official.
- `BR-CH13-001`, `BR-CH14-001`, `BR-CH15-002`, `BR-CH16-001`, `BR-CH18-001`, `BR-CH21-001`, `BR-CH22-002`, `BR-CH24-001`, `BR-CH25-002`, `BR-AW-002` — mapped footnote bodies and IDs are internally consistent; retain them and defer page-image certification.
- `BR-CH13-002`, `BR-CH15-005`, `BR-CH18-003`, `BR-CH18-005`, `BR-CH22-001`, `BR-CH24-002`, `BR-CH25-001` — the current conservative renderings preserve meaning and structure, while further intervention would be speculative or specialist-only.
- `BR-CH23-003`, `BR-AW-001` — the wording/heading is too uncertain to improve responsibly without printed-page evidence, so retain the current provisional form.

Recommended no-action/defer count: 37 Review IDs.

## Part 7 — Counts and Reconciliation

- Critical requiring decision: 2
- PDF visual checks: 12, covering 14 formerly open Review IDs; A-V09 is a separate evidence follow-up for one already-remediated item
- Non-visual Major decisions: 19
- Note-only decisions: 16
- Minor decisions: 1
- Recommended bulk approvals: 5
- Recommended no-action/defer: 37
- Total formerly unresolved Review IDs represented: 74

Reconciliation: 2 Critical IDs + 14 IDs represented in the visual queue + 58 non-visual IDs = 74 resolved Review IDs.

## Final Applied Outcomes

### Resolved with approved revision — 35 IDs

`BR-CH07-002`, `BR-CH08-001`, `BR-CH08-002`, `BR-CH08-003`, `BR-CH09-002`, `BR-CH09-003`, `BR-CH10-003`, `BR-CH11-002`, `BR-CH11-003`, `BR-CH11-004`, `BR-CH11-005`, `BR-CH12-002`, `BR-CH12-003`, `BR-CH13-005`, `BR-CH14-004`, `BR-CH14-005`, `BR-CH14-007`, `BR-CH14-008`, `BR-CH15-001`, `BR-CH15-004`, `BR-CH16-002`, `BR-CH16-005`, `BR-CH18-002`, `BR-CH18-004`, `BR-CH18-006`, `BR-CH19-001`, `BR-CH22-004`, `BR-CH25-006`, `BR-CH26-001`, `BR-CH26-002`, `BR-CH26-003`, `BR-CH27-002`, `BR-CH27-003`, `BR-CH27-004`, `BR-AW-004`.

Human decision: Approved. Status: resolved.

### Resolved with no reader-facing change — 39 IDs

`BR-CH06-001`, `BR-CH09-004`, `BR-CH10-002`, `BR-CH13-001`, `BR-CH13-002`, `BR-CH13-003`, `BR-CH13-004`, `BR-CH14-001`, `BR-CH14-002`, `BR-CH14-003`, `BR-CH14-006`, `BR-CH15-002`, `BR-CH15-003`, `BR-CH15-005`, `BR-CH16-001`, `BR-CH16-003`, `BR-CH16-004`, `BR-CH18-001`, `BR-CH18-003`, `BR-CH18-005`, `BR-CH21-001`, `BR-CH21-002`, `BR-CH22-001`, `BR-CH22-002`, `BR-CH22-003`, `BR-CH23-001`, `BR-CH23-002`, `BR-CH23-003`, `BR-CH24-001`, `BR-CH24-002`, `BR-CH25-001`, `BR-CH25-002`, `BR-CH25-003`, `BR-CH25-004`, `BR-CH25-005`, `BR-CH27-001`, `BR-AW-001`, `BR-AW-002`, `BR-AW-003`.

Human decision: Approved. Status: resolved-no-change.

All 74 Review IDs are resolved. PDF visual checks unresolved: 0. Human decisions pending: 0.

No source, translation, glossary, style-guide, or Chapters 1–4 file was modified while preparing this packet. No status was resolved. No commit or push was performed.
