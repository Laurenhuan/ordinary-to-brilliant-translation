# Chapter 3 Source Freeze Record

Status: **Canonical Source — Frozen for Translation v1**

Stage: Chapter 3 Human Source Decisions and Source Freeze

Authority: Project Lead approved

Translation status: Not started

## Frozen Source

- Chapter: 3
- Chinese title: `年轻的米店老板和二十出头的大地主`
- Canonical source: `source/chapters/03_chapter_03.md`
- Global source pages: `FB-P026`–`FB-P033`
- Input PDF pages: 26–33
- Printed pages: opener `Unknown`; following pages 14–20
- Paragraph count: 70
- Paragraph range: `CH03-P001`–`CH03-P070`
- Image anchors: `FB-I008`, `FB-I009`
- Footnotes: `FB-F007`–`FB-F010`
- Frozen source Git blob: `870fb420f864c377516e88d10175dab2141b47be`

The missing printed number on the chapter-opening page remains `Unknown`. It has not been inferred from the table of contents.

## Human Source Decisions

| Decision | Scope | Project Lead decision | Applied result |
|---|---|---|---|
| CH03-SD-001 | FB-F007 | Approve正文 marker `①` after `总督府`; treat the old CSV marker `②` as stale metadata | Restored at CH03-P015 with the approved body and retained raw CSV unchanged |
| CH03-SD-002 | FB-F008 | Approve marker `②` after `面` | Restored at CH03-P021 with the approved body |
| CH03-SD-003 | FB-F009 | Approve marker `①` after `40万坪`; preserve repeated wording, formula, punctuation, and source facts exactly | Restored at CH03-P038 without normalization or correction |
| CH03-SD-004 | FB-F010 | Approve marker `①` after `国保委` | Restored at CH03-P051 with the approved body |
| CH03-SD-005 | CH03-P026 / CH03-P027 | Retain two stable IDs; do not merge or renumber | Split-ID cross-page continuation retained with `FB-P029` between the IDs |

## Applied Source Restorations

1. Retained the previously verified inline `FB-P028` boundary in CH03-P015 between `卢` and `沟`, matching JSON `cross_page=true` evidence.
2. Replaced the extracted marker at `总督府①` with the stable reference `[^FB-F007]` and restored its approved body.
3. Replaced the extracted marker at `面②` with `[^FB-F008]` and restored its approved body.
4. Replaced the extracted marker at `40万坪①` with `[^FB-F009]` and restored its approved body exactly, including the repeated phrase and unnormalized formula.
5. Replaced the extracted marker at `国保委①` with `[^FB-F010]` and restored its approved body.
6. Retained CH03-P026 and CH03-P027 as separate stable IDs without changing any later ID.

No Chinese正文 wording, punctuation, paragraph order, image, raw evidence, OCR form, factual claim, historical statement, or unapproved source structure was changed.

## Boundary and Paragraph Verification

| Check | Expected | Actual | Result |
|---|---:|---:|---|
| Chapter start | FB-P026 | FB-P026 | PASS |
| Chapter end | FB-P033 | FB-P033 | PASS |
| Next chapter | FB-P034 / Chapter 4 | FB-P034 / Chapter 4 | PASS |
| Paragraph count | 70 | 70 | PASS |
| Unique IDs | 70 | 70 | PASS |
| Continuous sequence | CH03-P001–P070 | CH03-P001–P070 | PASS |
| Added/deleted/renumbered IDs | 0 | 0 | PASS |
| Missing or duplicated正文 blocks | 0 | 0 | PASS |

The title, JSON title block, chapter-opening template, Markdown order, table-of-contents sequence, and separate Chapter 4 opening agree on the Chapter 3 boundary.

## Page-Boundary Verification

All eight global page IDs are present once and in order:

| Page ID | Input PDF page | Printed page | Important structure | Result |
|---|---:|---:|---|---|
| FB-P026 | 26 | Unknown | Chapter opening, two images, opening summary | PASS |
| FB-P027 | 27 | 14 | CH03-P015 begins | PASS |
| FB-P028 | 28 | 15 | Inline continuation inside CH03-P015; FB-F007 and FB-F008 bodies | PASS |
| FB-P029 | 29 | 16 | Boundary between retained CH03-P026 and CH03-P027 IDs | PASS |
| FB-P030 | 30 | 17 | FB-F009 body | PASS |
| FB-P031 | 31 | 18 | FB-F010 body | PASS |
| FB-P032 | 32 | 19 | Repeated five-item passage | PASS |
| FB-P033 | 33 | 20 | Final two paragraphs | PASS |

## Cross-Page Structure

### CH03-P015 / FB-P028

JSON records one paragraph continuing across the page boundary. The exact boundary is preserved inline:

`发动“卢<!-- FB-P028 ... -->沟桥事变”`

Removing the metadata comment yields the original uninterrupted source text `卢沟桥事变`.

### CH03-P026 → CH03-P027 / FB-P029

- CH03-P026 ends: `当时的马山是一个水源清澈、气候温暖的港口城市。庆尚`
- CH03-P027 begins: `南道一带的农产品都会合到那里，光是大米每年就达数百万石，几乎全都运往日本。`

`庆尚` + `南道` is continuous source text. Under CH03-SD-005, both stable IDs and the intervening `FB-P029` boundary remain. English translation may continue syntax naturally across the two mapped IDs but must preserve both mappings. This follows the established Chapter 2 split-ID precedent.

## Footnote Verification

| Footnote | Paragraph | Source page | Marker | Approved body | Reference / definition | Result |
|---|---|---|---|---|---|---|
| FB-F007 | CH03-P015 | FB-P028 | ① after `总督府` | `日本侵略韩国时，在韩国的统治机构。` | 1 / 1 | PASS |
| FB-F008 | CH03-P021 | FB-P028 | ② after `面` | `面，韩国的行政单位，属于市、郡下一级的单位。` | 1 / 1 | PASS |
| FB-F009 | CH03-P038 | FB-P030 | ① after `40万坪` | `坪，韩国耕地的计量单位，韩国耕地的计量单位，1坪= \frac{400}{121} 米 ^{2} ，1983年停止使用。` | 1 / 1 | PASS |
| FB-F010 | CH03-P051 | FB-P031 | ① after `国保委` | `“国家保卫非常对策委员会”。` | 1 / 1 | PASS |

The old `qa/full_book_footnote_map.csv` marker field for FB-F007 says `②`. CH03-SD-001 determines that this is stale/inconsistent metadata because the正文 marker and ordered JSON footnote body both support `①`. The discrepancy is retained here for auditability; the raw CSV was not modified.

## Image Verification

| Image | Source page | JSON block / bbox | Local source | Result |
|---|---|---|---|---|
| FB-I008 | FB-P026 | block 2 / `160:334:198:392` | `source/raw/full_book/part_001_200/images/image_008.jpg` | PASS |
| FB-I009 | FB-P026 | block 4 / `399:329:441:392` | `source/raw/full_book/part_001_200/images/image_009.jpg` | PASS |

Both mappings remain the verified one-to-one DOCX/JSON/Markdown mappings. They are chapter-opening character illustrations without source captions; no caption was invented.

## Intentional Repetition and Independent Blocks

- `CH03-P001`–`CH03-P008` and `CH03-P057`–`CH03-P063` both remain. JSON records them independently on FB-P026 and FB-P032, so they are authorial/layout repetition rather than duplicate extraction.
- The opening occurrence remains arranged around the two character illustrations; the later occurrence remains normal body prose.
- `CH03-P019` (`300 石米的土地。`) remains an independent source block.
- No repeated prose was removed, merged, compressed, or normalized.

## Text and Numeric Integrity

- After excluding metadata and the four approved footnote structures, normalized Chinese正文 matches the pre-restoration candidate exactly.
- Full-book numeric comparison remains exact for FB-P027–FB-P033.
- FB-P026 differs from raw numeric extraction only by the previously approved structural recovery of chapter number `3`.
- Dates, amounts, ratios, land areas, grain measures, proper names, quotations, and source claims remain unchanged.
- Suspected source forms such as `购人的所有水田` remain untouched; the freeze does not authorize OCR or factual correction.

## Protection Audit

| Protected material | Verification | Result |
|---|---|---|
| Chapter 1 frozen source | Blob `90d3a7ad61585acb88c297cd63fafb864fb08693` unchanged | PASS |
| Chapter 2 frozen source | Blob `3dedd9702d3f2077e82767bdcb3c8bae552da80a` unchanged | PASS |
| Raw full-book Markdown / JSON / DOCX / images | No working-tree modification | PASS |
| Full-book CSV evidence | No working-tree modification | PASS |
| Glossary | No modification during source freeze | PASS |
| Translation | No Chapter 3 translation file created | PASS |

## Final Gate Decision

**PASS**

Chapter 3 is **Canonical Source — Frozen for Translation v1**.

Frozen source blob: `870fb420f864c377516e88d10175dab2141b47be`.

Any later source change requires new evidence, an explicit Project Lead decision, controlled application, a new QA verification, and a new frozen blob. This freeze authorizes the terminology candidate audit only; it does not authorize translation or new glossary locks.
