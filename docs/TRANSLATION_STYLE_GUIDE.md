# Chapter 1 Translation Style Guide v1

Stage: 5B.4 — Segment A Style Baseline Approval

Status: Segment A Draft v0.2 approved as the Chapter 1 biography style baseline; Segments B and C remain not started.

Use this guide together with `docs/STYLE_GUIDE.md`, `docs/TERMINOLOGY_VERIFICATION_GUIDE.md`, the locked master glossaries, and the Chapter 1 QA records. A locked project-specific decision takes priority over a general stylistic preference.

## A. Personal names

Established English form priority applies. Use the established official or conventional English form recorded in the locked glossary rather than mechanical romanization or a universal East Asian name-order rule.

Approved Chapter 1 examples:

- Lee Byung-chull
- Chung Ju-yung
- Akio Morita
- Namihei Odaira

Different ordering and hyphenation conventions are legitimate when they reflect established English usage. Do not silently normalize these names into one pattern.

## B. Classical book titles

Italicize standalone classical book titles in English prose. Use the exact locked title or scholarly romanization recorded in `glossary/glossary.csv`.

Approved English titles:

- *The Analects*
- *The Great Learning*
- *Elementary Learning*
- *The Thousand-Character Classic*

Approved scholarly romanized titles:

- *Zizhi Tongjian*
- *Tongjian Jieyao*
- *Zizhi Tongjian Gangmu*

Do not replace a romanized scholarly title with an unsourced explanatory translation. Do not confuse an ordinary source word with a book title; source punctuation and context control title identification.

## C. Cultural concepts

On first occurrence, explain and retain a cultural term when that is the approved strategy. Later occurrences should use the approved shorter form without repeating the explanation.

Chapter 1 applications include:

- `私塾`: first `a traditional Korean village school known as a seodang`; later `seodang`.
- `仁、和、乐`: first `humaneness (ren), harmony (he), and joy (le)`; later `humaneness`, `harmony`, and `joy`.

Terms such as `seodang`, `ren`, `he`, and `le` retain cultural context that may be lost through a generic modern English substitute. Do not use `private school` for `私塾`, and do not reduce the three Confucian concepts mechanically to `kindness / peace / happiness`.

Apply other locked contextual rules exactly, including `eminent Confucian scholar` for `鸿儒` and `landowner / landowning family` for `地主`. Do not use `landlord` in the approved Chapter 1 contexts.

## D. Proverbs and traditional sayings

Use natural English equivalents when appropriate, while preserving the intended cultural meaning and recording every intentional substitution.

Approved example:

- `有志者事竟成`: `Where there is a will, there is a way.`

This is an intentional conventional-proverb substitution. A project-created quotation must not be described as an established English saying. Apply the separate approved quotation decision for `一勤天下无难事` exactly as `With diligence, no task is impossible.`

## E. Translator and editor notes

- Add a translator/editor note only at the first relevant occurrence unless a later occurrence presents a genuinely new issue.
- Do not overload the English text with notes or repeat an explanation already supplied.
- Keep notes neutral, concise, and traceable to a recorded terminology or QA decision.
- Do not use a note to make an unapproved factual correction or to speculate about responsibility for a source discrepancy.
- For Namihei Odaira, follow the approved first-occurrence note decision: the Chinese edition prints `小源浪平`, while Hitachi records identify the founder as `小平浪平` (`Namihei Odaira`). Do not claim that the author made the error.

## F. Relationship to the frozen source

Every pilot translation must remain traceable to `source/chapters/01_chapter_01.md`.

Preserve:

- paragraph IDs such as `CH01-P001`;
- page-reference comments when included in the pilot range;
- image anchors and their relative order when applicable;
- footnote markers and references;
- source paragraph order and meaningful repetition.

Do not silently omit, merge, split, reorder, or add source claims. Any necessary structural departure must be logged in `qa/chapter_01_translation_review.md` and approved before it becomes reviewed translation.

The English pilot is a derived working file. It must never overwrite or modify the frozen Chinese source.

## G. Chapter 1 Biography Translation Style Rules

Segment A Draft v0.2 (`CH01-P004`–`CH01-P007`) is the approved biography style reference for future Chapter 1 translation.

- Prefer natural English biography narration over sentence-by-sentence mapping of Chinese syntax.
- Sentence boundaries and order within a paragraph may be restructured when necessary for idiomatic English, but no factual information may be removed or added. Do not alter chronology, causation, family relationships, or historical and social relationships.
- Avoid unnecessary intensifiers. Prefer precise, restrained wording when the source does not require emphasis.
- Preserve historical and social information, including family background, landholding or class position, personal relationships, dates, places, education, and quantities.
- Maintain established English names and other locked terminology exactly as recorded in the project glossaries. Do not introduce silent spelling, name-order, capitalization, or hyphenation variants.
- Follow approved glossary decisions for cultural terms, including first-use and later-use forms such as `seodang`.
- Keep every translated paragraph traceable to its source paragraph ID even when English sentence structure differs from the Chinese.
- QA markers may remain visible in a draft when terminology is unresolved. Every such marker must be resolved and removed before final translation; QA markers are not reader-facing text.

This approval establishes a style baseline only. It does not resolve pending terminology, approve translation of Segments B or C, or authorize full-chapter translation.

## Pilot review focus

The style pilot should test only a small, approved segment range. Reviewers should assess:

- fidelity and completeness;
- clear, natural American English;
- narrative tone and sentence rhythm;
- terminology and proper-name consistency;
- treatment of classical titles and cultural concepts;
- proverb and quotation handling;
- translator-note density; and
- preservation of paragraph, image, and footnote traceability.

Approval of the pilot style does not approve unresolved terminology or authorize automatic translation of the full chapter.
