# From Ordinary to Brilliant — English Translation

A structured Chinese-to-English translation project for 《从平凡走向辉煌》. The repository supports chapter preparation, translation, terminology management, quality assurance, and reproducible publishing.

The English title From Ordinary to Brilliant is provisional and may be revised before publication.

## Project goals

- Produce an accurate, natural, and consistent American English translation.
- Preserve the author's meaning, argument, tone, and historical context.
- Record terminology, names, organizations, and unresolved questions in shared files.
- Keep source preparation, translation, review, and publication outputs traceable with Git.

## Repository structure

    docs/
      TRANSLATION_GUIDE.md   Translation workflow and principles
      STYLE_GUIDE.md         English style and consistency rules
      SOURCE_CLEANING_GUIDE.md  Proposed source-ingestion and cleaning rules
    source/
      raw/                   Authorized intermediate source material only
      chapters/              Cleaned, chapter-level Chinese source text
    translation/             English chapter drafts and reviewed translations
    glossary/
      glossary.csv           General terms and recurring expressions
      people.csv             Personal names and titles
      organizations.csv      Organization names and abbreviations
    qa/
      questions.csv          Ambiguities and issues requiring resolution
    scripts/                 Reusable processing and QA scripts
    output/                  Generated review and publication files

## Current stage

Source Ingestion Pilot / MinerU Source QA. The current work validates a traceable PDF-to-MinerU-to-clean-Markdown workflow before chapter-level translation begins. No translation is being performed during this stage.

## Copyright and access

This repository is intended to be a private working repository. Do not upload the original copyrighted PDF or any other source file that the project is not authorized to store or redistribute. Only authorized, minimum-necessary working text should be added under source/. Generated files must not be published or shared outside the authorized project team until rights and permissions have been confirmed.
