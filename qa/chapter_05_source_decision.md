# Chapter 5 Source Decision Record

Stage: Project Lead visual decisions and controlled source restoration

Authority: Project Lead approved

Source candidate: `source/chapters/05_chapter_05.md`

Decision status: **APPROVED AND APPLIED**

## CH05-SD-001 — Printed Entity Form

- Paragraph: `CH05-P032`
- Source page: `FB-P045`
- Input PDF page: `45`
- Printed page: `32`
- Project Lead visual finding: the printed source reads exactly `Channel 商会`, with a visible space.
- Decision: preserve `Channel 商会` exactly in the canonical Chinese source.
- Prohibited source treatments: `Channel商会`, source-level translation, reinterpretation, or classification as OCR error.
- Terminology consequence: audit as an unresolved historical entity/name and investigate without assuming its identity.

## CH05-SD-002 — Verified Printed Typo

- Paragraph: `CH05-P041`
- Source page: `FB-P047`
- Input PDF page: `47`
- Printed page: `34`
- Project Lead visual finding: the printed source reads `只赚取几百块的收人，而从事建筑业的人收入达几万元`.
- Decision: preserve the first `收人` exactly in the canonical Chinese source.
- Classification: verified printed-source typographical error / highly probable typo; not an OCR error.
- Later translation treatment: English may render the intended sense as `income` after approval, but a translator/editor note must disclose the printed form. Final note wording and number remain pending terminology decision.

## CH05-SD-003 — Verified Printed Malformed Wording

- Paragraph: `CH05-P055`
- Source page: `FB-P048`
- Input PDF page: `48`
- Printed page: `35`
- Project Lead visual finding: the printed source reads exactly `打创消费市场品牌`.
- Decision: preserve `打创消费市场品牌` exactly in the canonical Chinese source.
- Classification: verified printed wording; likely source typographical/lexical error; not an OCR error.
- Later translation treatment: English may render the apparent intended meaning naturally after approval, but a translator/editor note must disclose the printed wording and approved treatment. Final English and note number remain pending terminology decision.

## CH05-SD-004 — Blank Separator Page

- Source page: `FB-P049`
- Input PDF page: `49`
- Printed page: `Unknown`
- Project Lead visual finding: the page is intentionally blank.
- Decision: preserve `FB-P049` in Chapter 5 traceability as a trailing blank/separator page between the semantic ending on `FB-P048` and Chapter 6 on `FB-P050`.
- Structural treatment: add `blank-page=true`; create no paragraph ID and invent no content.

## Approved Footnote Restoration Retained

The existing mechanically unambiguous restorations remain approved for the frozen source:

| ID | Marker location | Exact source body |
|---|---|---|
| `FB-F014` | `CH05-P006`, after `大农集团` | `以纺织业为主的集团。` |
| `FB-F015` | `CH05-P006`, after `咸兴` | `城市名，位于朝鲜咸镜道。` |
| `FB-F016` | `CH05-P006`, after `沙里院` | `城市名，位于朝鲜黄海道。` |

## Project-wide Verified Source Error Rule

Status: **Approved — Project-wide**

### Source layer

The canonical Chinese source always preserves the visually verified printed wording, including typographical errors, malformed wording, factual errors, and historical/entity errors. An OCR or extraction error is corrected only to match the printed page and normally requires no reader note.

### Translation layer

When reliable evidence establishes a printed-source error, an English correction or intended-sense rendering may be used only after Project Lead or human approval. It must not be silent. A translator/editor note must state what the printed source says and, where relevant, the verified information or approved translation treatment. Uncertain cases must not be corrected speculatively.

- Verified printed typo or malformed wording: preserve the Chinese; English may express the intended meaning after approval; add a note when materially useful or explicitly required.
- Verified factual, historical, or entity error: preserve the Chinese; English may use verified correct information after approval; a neutral discrepancy note is mandatory.

This rule supersedes the earlier translation-side requirement to reproduce every verified source error literally. It does not authorize silent or speculative correction.

Documentation action: `docs/STYLE_GUIDE.md` Sections 10 and 11 were narrowly updated. `docs/TRANSLATION_GUIDE.md` was inspected and left unchanged because it contains no conflicting rule.

## Application Audit

- Only the approved space in `Channel 商会`, blank-page metadata, and source-footnote structures were changed in the Chapter 5 source candidate.
- `收人` and `打创消费市场品牌` remain exactly as printed.
- No other Chinese wording was changed.
- No Chapter 1–4 file was retroactively altered.
- No glossary entry was modified or locked.
- No Chapter 5 translation was created.
