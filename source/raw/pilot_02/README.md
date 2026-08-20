# Pilot 02 Raw Source Inventory

Status: immutable Pilot 02 input and extracted media

This directory contains the original MinerU Pilot 02 export moved from the repository root into canonical filenames. The move was verified by SHA-256 before and after relocation. The raw Markdown, JSON, and DOCX have not been rewritten.

## Evidence roles

- `source.md` is the primary MinerU text layer.
- `source.json` is the page, block, order, type, bounding-box, discarded-element, and layout-evidence layer.
- `source.docx` is the embedded-image source and a visual/layout fallback. DOCX-derived text must not overwrite `source.md`.
- `images/` contains byte-for-byte extractions from DOCX `word/media/`.

## Input inventory

| File | Bytes | SHA-256 |
|---|---:|---|
| source.md | 17,325 | `236FCDBE5CBD396EEE2AC6A8DD7A4E4BDF6F13E782223970F65AF692A1E41703` |
| source.json | 283,891 | `0D9EC1854312A73C29F2E7C2B63CEF35C6807FBCCEB20412F1817334BE46127A` |
| source.docx | 34,617 | `441AD7037B0D3B9C5C8DF122E9A2FEE4C4DC36C7E156050CCEBF56417F568E85` |

JSON contains 11 pages with zero-based `page_idx` values 0–10.

## Extracted images

Naming rule: images use stable document-order names. No resizing, recompression, cropping, or format conversion was performed.

| Local image | DOCX entry / relationship | DOCX order | JSON page/block/bbox | Markdown image order | Dimensions | Bytes | SHA-256 |
|---|---|---:|---|---:|---:|---:|---|
| images/image_001.jpg | word/media/rId9.jpg / rId9 | 1 | page_idx 3, block 2, bbox 161,331,198,389 | 1 | 103×162 | 6,066 | `4FACC634A10D1DCCC441F277DC5560D270D2CAE7288EA08B4BEA4D4C5BF3A110` |
| images/image_002.jpg | word/media/rId12.jpg / rId12 | 2 | page_idx 3, block 4, bbox 401,330,440,392 | 2 | 110×173 | 6,148 | `6A350033946E5CAA8E426C9074AFFB6AD5823FFE54583E45F6F7EEE1FBFCB13A` |

Both DOCX images have unique one-to-one mappings to Markdown and JSON. No image remains dependent on the MinerU CDN in the cleaned sample.

## Preservation notes

- `source.md`, `source.json`, and `source.docx` are raw evidence and must not be edited.
- The DOCX `footnotes.xml` contains only separator records and no usable footnote bodies.
- JSON `page_footnote` blocks are retained as evidence but every proposed recovery requires manual review.
- The original long-named MinerU files no longer remain in the repository root; their canonical raw copies above are the same bytes.
