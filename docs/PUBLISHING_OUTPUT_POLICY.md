# Publishing Output Policy

Status: Project-wide policy

Scope: All current and future chapters

## Purpose

After a chapter reaches **Final Acceptance / Freeze**, passes the Publication Readiness Gate, and records its accepted translation hash, generate two reader-facing derivatives:

1. Reader Edition
2. Bilingual Edition

Both editions must be derived from the frozen source and accepted/reviewed translation. Generation must never modify source files, authoritative translation files, glossary files, style guides, or QA records.

## 1. Reader Edition

Location: `reader/`

Naming convention: `chapter_XX_reader.md`

The Reader Edition is a clean, publication-style English reading version.

Remove:

- paragraph IDs;
- source-page markers;
- review status;
- QA metadata;
- internal workflow comments;
- unresolved draft markers.

Preserve:

- the approved English chapter title;
- every translated paragraph in its original order;
- the frozen paragraph structure;
- approved translator/editor notes;
- publication-relevant Markdown formatting.

A Reader Edition may be generated only from a frozen translation. If the frozen translation contains unresolved draft markers whose removal would delete or alter content, generation must stop and the conflict must be resolved through an approved revision decision before publication output is created.

## 2. Bilingual Edition

Location: `bilingual/`

Naming convention: `chapter_XX_bilingual.md`

The Bilingual Edition is a Chinese-English parallel reading version.

Each paragraph must use this structure:

```markdown
## CHXX-P001

### 中文原文

[Chinese source paragraph]

### English Translation

[English translation paragraph]
```

Requirements:

- Chinese source text appears first.
- English translation appears second.
- Paragraph IDs and one-to-one correspondence are preserved.
- Paragraphs are not merged, split, reordered, omitted, or duplicated.
- Neither language is rewritten during output generation.
- Approved translator/editor notes are preserved where applicable.
- Publication-relevant formatting is retained.

## 3. Permanent Chapter Workflow

Every current and future chapter must follow this sequence:

1. Source Freeze
2. Terminology Preparation / Verification
3. Controlled Translation
4. Human Review
5. Approved Revision
6. Final Terminology Lock
7. Terminology Resolution
8. Publication Readiness Verification
9. Final Acceptance / Freeze
10. Transition to `translation/reviewed/`
11. Generate Reader Edition
12. Generate Bilingual Edition
13. Publication Output QA

A chapter must not be treated as publication-ready merely because a translation hash was frozen earlier in the workflow. Earlier hashes remain part of the audit history but do not replace the Final Acceptance gate.

### Publication Readiness Gate

Before Final Acceptance, the chapter must have:

- zero unresolved terminology markers;
- zero pending terminology placeholders;
- formally locked terminology for every former unresolved-marker position;
- intact and ordered paragraph mappings;
- complete required source footnotes;
- complete required translator/editor notes;
- zero unauthorized translation changes; and
- a verified frozen-source hash.

If any condition fails, the chapter remains `BLOCKED` and publication outputs must not be generated.

### Authoritative Hierarchy

```text
Frozen source
    +
Accepted/reviewed translation
    ↓
Reader Edition
Bilingual Edition
```

Reader and Bilingual files are derived outputs, not independent translation sources. They must never be edited in ways that diverge from the accepted translation. Any substantive correction must first pass through the controlled revision process and receive a new accepted translation hash; the derived outputs must then be regenerated.

## 4. Generation Rule

After a chapter receives Publication Readiness `PASS` and Final Acceptance / Freeze:

1. Verify the recorded frozen source and translation hashes.
2. Confirm that no unresolved draft marker blocks publication-safe extraction.
3. Generate the Reader Edition.
4. Generate the Bilingual Edition.
5. Run the consistency checks below.

## 5. Consistency Checks

Every generated pair must pass all of the following checks:

- Paragraph count matches the frozen translation.
- Every frozen paragraph is present.
- Paragraph order is unchanged.
- No paragraph is merged, split, duplicated, or omitted.
- Reader Edition prose matches the frozen English paragraph content after removal of workflow-only formatting.
- Bilingual Chinese text matches the frozen source paragraph content after removal of source-workflow comments.
- Bilingual English text matches the frozen translation paragraph content after removal of workflow-only formatting.
- Required translator/editor notes are preserved.
- No unresolved draft marker remains in a reader-facing output.
- No pending terminology placeholder or unresolved terminology ID remains.
- Source, translation, glossary, style-guide, and QA files remain unchanged.

If any check fails, the output status is `BLOCKED`. The generator must not silently repair, translate, or reinterpret content. A new approved source, terminology, or translation revision decision is required before generation can resume.

## 6. Publication Output QA and Status

Publication Output QA must verify both editions after generation:

- Reader Edition contains clean English only, with no internal metadata and all necessary approved notes preserved.
- Bilingual Edition is Chinese first and English second, contains exactly one aligned pair per source paragraph, and preserves the approved notes.
- Neither edition contains unresolved terminology markers, pending placeholders, QA statuses, glossary IDs, or internal workflow comments.
- Visible prose remains content-equivalent to the accepted/reviewed translation.

Generated files are derivatives only. They do not replace or supersede the frozen source, frozen translation, decision records, glossary, or style guides.
