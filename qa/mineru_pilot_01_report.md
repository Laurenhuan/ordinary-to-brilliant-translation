# MinerU Pilot 01 QA Report

Status: Source Ingestion Pilot / MinerU Source QA

Scope: This report evaluates a limited MinerU extraction only. It does not translate, rewrite, fact-correct, or approve the text for publication.

## Pilot input overview

| Input | Role | Observation |
|---|---|---|
| source/raw/pilot_01/source.md | Primary text | 219 lines; 14,521 bytes; five MinerU CDN image links |
| source/raw/pilot_01/source.json | Page and layout evidence | 11 zero-based page_idx records; page size, block order/type, bbox, discarded blocks, and image paths |
| source/raw/pilot_01/source.docx | Image and visual fallback | Five embedded JPG files in word/media/; DOCX text was not used to replace Markdown |

MinerU metadata in JSON: version 3.4.4, hybrid backend, medium effort, OCR enabled.

All three inputs were renamed to stable names without byte changes. SHA-256 hashes and extracted-image hashes are recorded in source/raw/pilot_01/README.md.

The original copyrighted PDF is not in the repository. The repository visibility setting was not changed.

Authorization update: on 2026-08-19, the pilot push was paused because the remote was public. On 2026-08-20, the project lead confirmed that this academically supervised translation project has the required authorization for the project materials to remain in a public repository. The pilot may therefore be pushed without removing raw text, JSON, DOCX, extracted images, or the cleaned sample. This distribution decision does not change any conservative Source QA rule or permit unverified text correction.

## MinerU strengths

- Main Chinese prose order is largely coherent and readable across the pilot.
- Paragraph units are generally sensible; most body blocks correspond cleanly to Markdown paragraphs.
- JSON preserves page_idx, block index, block type, bounding boxes, page size, discarded headers, page numbers, and page footnotes.
- MinerU correctly discarded many printed page numbers and some running headers from Markdown.
- Chapter 1 was recognized as a level-1 title.
- All five Markdown CDN images have corresponding JSON image blocks and corresponding embedded images in the DOCX.
- The DOCX image order, Markdown image order, and JSON page/bbox order form a consistent one-to-one mapping.
- No meaningless HTML tags were detected in source.md.

## Detected issues and proposed treatment

| ID | Problem and concrete example | Severity | Proposed treatment | Safe to automate? |
|---|---|---|---|---|
| P01 | Running header leaked into Markdown as content: 从平凡走向辉煌 at raw lines 1, 103, 147, and 171. JSON places these at the top edge on page_idx 0, 5, 7, and 9. | Medium | Remove only these confirmed pilot instances from cleaned Markdown and retain page markers. | Yes for these exact pilot matches; not yet as a general rule. |
| P02 | Printed page numbers and several headers are absent from Markdown but available in JSON discarded_blocks. | Low | Preserve them as page mapping metadata rather than readable body text. | Yes. |
| P03 | Three footnote bodies were classified as discarded page_footnote blocks and omitted from Markdown: page_idx 5, 6, and 10. Markers are inconsistent: LaTeX-style $^{①}$ at raw lines 109 and 135, plain ① at line 217. | High | Restore the unambiguous note bodies from JSON and normalize markers to stable Markdown footnote IDs in the cleaned sample. | Yes for this pilot after page-level verification; ambiguous cases must remain manual. |
| P04 | Chapter 2 number and title were split into different heading levels: raw lines 157 and 159. | Medium | Combine as one level-1 heading without changing the title text. | Yes when adjacent on the same page and confirmed by JSON. |
| P05 | A paragraph was split by the page_idx 6 to 7 boundary and a leaked running header: raw lines 145 to 149. | Medium | Join the two fragments and place the page marker inline at the exact break. | Yes for this exact case; generalized paragraph joining requires review. |
| P06 | Chapter 1 opener text on page_idx 4 substantially repeats prose on page_idx 5. One exact repeated sentence appears at raw lines 101 and 119; the surrounding passage is also repeated in split and joined forms. | Medium | Preserve both occurrences. Verify against the PDF whether the first is an intentional standfirst/design element. | No. |
| P07 | Five images depend on temporary cdn-mineru.openxlab.org.cn URLs. | High | Extract the five embedded DOCX images byte-for-byte and replace URLs only in cleaned Markdown. | Yes because the mapping is one-to-one in all three inputs. |
| P08 | Images have no explicit captions. Page_idx 4 and 8 place small portrait illustrations beside lead text; page_idx 2 contains a decorative image near the contents heading. | Low | Keep image order and placement. Do not invent captions. | Placement can be automated; caption interpretation cannot. |
| P09 | Proper noun 小源浪平 appears at raw lines 99 and 117 and contains a potentially confusable glyph. This report does not assert a correction. | Medium | Preserve the extracted form and add one QA marker for comparison with the authorized PDF. | No. |
| P10 | Numerically dense claims require visual verification, including 461/404/299/25/610 亿美元 at raw line 35 and 70/37/40 percent at line 195. | Medium | Compare digits, units, punctuation, and signs with the PDF. Do not fact-correct during source cleaning. | Detection may be automated; correction must be manual. |
| P11 | JSON page_idx 6 contains an empty first para block although Markdown proceeds with readable text. | Low | Ignore the empty block in cleaned prose but retain it as a structural QA observation. | Yes for reporting; deletion rules are not yet approved globally. |
| P12 | The pilot ends mid-sentence at raw line 219 and page_idx 10. | High | Preserve the incomplete sentence and add a TODO. Include the next authorized source page in a future pilot check. | Detection is safe; completion must be manual from source. |

## Image mapping

The five DOCX images were extracted without modification. CDN download was unnecessary.

| Local image | DOCX media | Markdown/JSON CDN tail | page_idx | JSON bbox | Interpreted role |
|---|---|---|---:|---|---|
| image_001.jpg | rId10.jpg | 153a2a…2617.jpg | 2 | 135,207,194,280 | Decorative contents image |
| image_002.jpg | rId15.jpg | 51879b…f75f.jpg | 4 | 169,336,207,393 | Small portrait illustration |
| image_003.jpg | rId18.jpg | 42b4f8…0687.jpg | 4 | 408,332,448,395 | Small portrait illustration |
| image_004.jpg | rId25.jpg | de41be…6420.jpg | 8 | 161,322,199,381 | Small portrait illustration |
| image_005.jpg | rId28.jpg | 09fa20…20c4.jpg | 8 | 400,321,442,383 | Small portrait illustration |

The role labels above are visual QA descriptions, not source captions. No caption text was found or created.

## Page mapping evidence

MinerU page_idx is zero-based and identifies the order inside this pilot JSON. printed_page comes only from JSON page_number blocks; unresolved means JSON did not explicitly record a page number.

| page_idx | printed_page | First meaningful content | Detected structural evidence |
|---:|---:|---|---|
| 0 | 6 | 大韩民国另外一位… | Leaked running header; page number discarded |
| 1 | 7 | 团队式的经营… | Header 前言 and page number discarded |
| 2 | 9 | Contents image / 目录 | One image; header 目录 and page number discarded |
| 3 | 10 | 21. 信任与考察… | Continuation of contents; page number discarded |
| 4 | unresolved | Chapter 1 title | Two image blocks; no explicit page number |
| 5 | 2 | 李秉哲（1910—1987）… | Leaked running header; footnote and page number discarded |
| 6 | 3 | 需要特别指出的是… | Header, footnote, and page number discarded; one empty para block |
| 7 | 4 | Continuation beginning 《千字文》… | Leaked running header; page number discarded |
| 8 | unresolved | Chapter 2 number and title | Split title; two image blocks; no explicit page number |
| 9 | 6 | 1929 年 10 月… | Leaked running header; page number discarded |
| 10 | 7 | 日本产业界也受到… | Header, footnote, and page number discarded; pilot ends mid-sentence |

Proposed mapping design: insert HTML comments of the form source-page: mineru_page_idx=N; printed_page=P at each cleaned Markdown page boundary. For a cross-page paragraph, place the marker inline at the original boundary. A future mapping file could additionally store block index and bbox, but that complexity is not needed for this pilot.

## Cleaned sample treatment log

source/chapters/pilot_01_cleaned.md is generated from source.md by scripts/clean_mineru_pilot.py. The script validates exact hashes and refuses to run on different inputs.

Applied only to the pilot:

- removed four confirmed leaked running headers;
- inserted 11 page mapping comments;
- replaced five CDN URLs with verified local relative image paths;
- combined the split Chapter 2 number and title;
- joined one high-confidence paragraph across page_idx 6 and 7;
- normalized three footnote markers and restored their bodies from JSON;
- removed one non-semantic trailing space from the decorative contents line;
- added one proper-name QA marker without changing the extracted name; and
- added one TODO for the incomplete final sentence.

Not removed or corrected:

- the apparent Chapter 1 opener/body repetition;
- any suspected OCR character;
- any proper noun;
- any date, number, percentage, currency amount, or factual claim;
- any Chinese wording; and
- the incomplete final sentence.

## Items requiring manual verification

- Compare all 11 pilot pages against the authorized PDF.
- Confirm whether the page_idx 4 and page_idx 5 repeated passage is intentional.
- Verify 小源浪平 and all other people, place, and company names directly from the printed glyphs.
- Verify all dates, years, percentages, amounts, and large-number units.
- Confirm the three footnote marker-to-body mappings.
- Confirm that the five images are complete and correctly positioned.
- Determine the printed page numbers for page_idx 4 and 8; the table of contents suggests possible values, but this report does not infer them.
- Supply the next source page to complete the final sentence before treating this excerpt as a complete unit.

## Safe automation versus manual decisions

Safe for this pilot:

- inventory and hash inputs;
- extract DOCX media byte-for-byte;
- enumerate JSON pages and structural blocks;
- map the five images by verified order;
- localize the five CDN links;
- insert explicit JSON-based page markers;
- remove the four exact running-header instances; and
- detect the incomplete ending.

Must remain manual:

- OCR corrections;
- proper-noun normalization;
- factual or numerical correction;
- duplicate removal;
- ambiguous paragraph repair;
- caption assignment;
- ambiguous footnote restoration; and
- approval of any rule for full-book processing.

## Recommendation

Qualified yes: MinerU is suitable as the extraction layer for continued testing, but not as an unattended Markdown-only full-book workflow.

The pilot shows strong body-text order and useful JSON structure. It also shows that Markdown alone loses footnote bodies, inconsistently retains running headers, and depends on temporary CDN images. A reliable workflow therefore needs all three artifacts: Markdown as the primary text, JSON for page and block evidence, and DOCX for embedded images only.

Do not parse or clean the full book yet. First, manually compare this cleaned pilot with the authorized PDF, resolve the listed questions, and approve or revise the Proposed rules in docs/SOURCE_CLEANING_GUIDE.md. A second small pilot should then test the approved rules on pages with additional layout types before any full-book batch decision.
