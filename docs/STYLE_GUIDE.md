# Style Guide

This is the initial house style for the English translation of 《从平凡走向辉煌》. Use it together with the glossary files and `docs/TERMINOLOGY_VERIFICATION_GUIDE.md`. When a documented project-specific decision conflicts with a general rule below, follow the project-specific decision and update this guide.

## 1. Language and spelling

- Use American English spelling, punctuation, and usage.
- Use Merriam-Webster as the default spelling reference when a form is uncertain.
- Prefer clear, contemporary, professional prose. Avoid unnecessary jargon, archaic phrasing, and literal Chinese syntax.
- Use the serial comma in lists of three or more items.

## 2. Proper nouns

- Use an established official English name when one exists and can be verified.
- A researched candidate is not yet an approved form. Use a proper name as project-authoritative only after it is recorded as `locked` in the appropriate master glossary.
- For Chinese personal names without an established English form, use Hanyu Pinyin without tone marks, normally with family name first when discussing a Chinese historical or institutional context. Record the approved order and spelling in glossary/people.csv.
- Capitalize formal titles only when they directly precede a person's name or form part of an official name; otherwise use lowercase.
- Record every recurring person and organization in the appropriate glossary file. Do not create competing variants in the translation.
- First-mention and later-mention treatment remains a separate editorial decision. Do not infer it from a candidate record or settle it silently during translation.

## 3. Dates

- Use the American order: Month D, YYYY, as in July 1, 1997.
- Use Month YYYY when no day is given, as in July 1997.
- Use numerals for decades: the 1980s. Do not use an apostrophe before the s.
- Use en dashes for inclusive ranges: 1998–2002.
- Preserve the precision of the source. Do not invent a day or month.

## 4. Numbers and measurements

- Spell out whole numbers from one through nine; use numerals for 10 and above.
- Use numerals for dates, ages, percentages, measurements, currency, statistics, addresses, chapter references, and other data-heavy contexts.
- At the beginning of a sentence, spell out a number or recast the sentence.
- Use commas in numbers of four or more digits: 1,000 and 25,000.
- Use a leading zero for decimals below one: 0.5.
- Use the percent sign with numerals: 8%.
- Convert Chinese large-number units carefully. Verify every occurrence of 万 and 亿; express the result in reader-friendly English without changing the value.
- Keep source units unless conversion is necessary for comprehension or required by the publication plan. If converting, retain the original value when accuracy or context requires it.

## 5. Currency

- Identify the currency unambiguously. For Chinese renminbi, use RMB followed by the amount, such as RMB 100 million, unless the context or publisher requires the ISO code CNY.
- Use the appropriate currency symbol only when there is no risk of ambiguity.
- Do not silently convert historical or current monetary values into another currency.
- Preserve the date and basis of any approved conversion and explain it in a note when relevant.

## 6. Quotation marks and punctuation

- Use double quotation marks for ordinary quotations and single quotation marks for a quotation within a quotation.
- In American style, place periods and commas inside closing quotation marks. Place colons and semicolons outside; place question marks and exclamation points according to meaning.
- Use curly quotation marks and apostrophes in publication output when the toolchain supports them.
- Use an em dash without surrounding spaces for a strong break in a sentence.
- Use an en dash for ranges and certain compound relationships.
- Preserve quotation status accurately. Do not turn paraphrase into direct quotation.

## 7. Titles and headings

- Use title case for English chapter and major section titles.
- Use sentence case for lower-level descriptive headings unless the output format specifies otherwise.
- Italicize titles of books, periodicals, films, and other standalone works.
- Put titles of chapters, articles, speeches, and other parts of larger works in double quotation marks.
- Use the official English title of a work when available. Otherwise create a faithful provisional translation and record it in the glossary.
- Keep heading levels parallel and concise. Do not end headings with periods.

## 8. Tone and voice

- Preserve the author's intended level of formality, confidence, restraint, and emotional force.
- Prefer idiomatic English over word-for-word imitation, but do not soften, intensify, modernize, or editorialize the author's claims.
- Avoid contractions in formal exposition unless the passage has a deliberately conversational voice.
- Preserve meaningful repetition; remove only accidental repetition introduced during translation.
- Translate slogans and rhetorical parallelism for both meaning and effect. Log important tradeoffs when exact reproduction is impossible.
- Use inclusive, respectful language when it does not distort the historical context or the author's meaning.

## 9. Consistency and exceptions

- Treat master-glossary entries marked `locked` as authoritative. `pending`, `researched`, `needs_context`, and `needs_human_decision` entries remain non-authoritative.
- Locked terminology must not be silently changed. A later change requires a recorded QA decision and synchronized updates to every affected glossary and translation occurrence.
- Use one English form for the same person, organization, place, event, concept, and recurring phrase throughout the project.
- Verify names, dates, figures, quotations, titles, and cross-references during every review.
- Record unresolved choices in qa/questions.csv with enough context for another reviewer to decide.
- When an exception is approved, document the reason and apply it consistently to comparable passages.
- Do not rely on memory for project-wide decisions; update this guide or the relevant glossary.
