# MinerU Pilot 01 Raw Manifest

This directory preserves the three user-provided MinerU artifacts under stable names. Renaming did not change file contents.

## Source roles

- source.md — primary text source for QA and cleaning
- source.json — page, block, order, type, bounding-box, discarded-element, and image mapping evidence
- source.docx — embedded-image and visual-layout fallback only; its text must not overwrite source.md
- images/ — byte-for-byte images extracted from source.docx word/media/

## Input hashes

| File | Bytes | SHA-256 |
|---|---:|---|
| source.md | 14,521 | F5DC769D01552847A86E1BB0FCFDCE9ED76DE792BD8C9EE3D984969E4C106D29 |
| source.json | 283,137 | 7A052BD7F622E3322466884BF39B39676CCB18141A9149DB51B95A33CD43079C |
| source.docx | 53,407 | ED6E29328E8DF5728F78ED53930F77E897D233D41CD51C54C18C65EFC5C93C71 |

## Image extraction map

Images use stable document-order names. No image was resized, recompressed, cropped, or converted.

| Local file | DOCX entry | Dimensions | Bytes | SHA-256 |
|---|---|---:|---:|---|
| images/image_001.jpg | word/media/rId10.jpg | 164 × 203 | 8,069 | 3B74999B546D5803360C2C1109317C0E66B1F8814817ACFA05047CE37E0E9615 |
| images/image_002.jpg | word/media/rId15.jpg | 106 × 159 | 5,742 | 99A03BF9A2137BD15589DFEDD0AB85D616E6C01E3B0A6C35A684191662719142 |
| images/image_003.jpg | word/media/rId18.jpg | 112 × 176 | 5,883 | 08F18FC7637CFEC31EB1A3FE69878DDA4A1E9C0326711B04A9797E487889F430 |
| images/image_004.jpg | word/media/rId25.jpg | 106 × 165 | 6,054 | DD50FD77A958FC04E7870001AF7C0759C9DEAC4339A18A2C09FD68D46692EDB5 |
| images/image_005.jpg | word/media/rId28.jpg | 117 × 173 | 6,221 | C49E774591D7983E804A3A321EC2F734749F384394FF578C2399DE8BD8D23795 |

## Copyright and access

These files are pilot working materials intended only for a private repository. They must not be treated as permission to publish or redistribute the source text or images. The original copyrighted PDF is not stored here.

Pre-push safety status on 2026-08-19: GitHub's unauthenticated public API reported the remote repository as public. These pilot assets must remain local and must not be pushed until the repository owner confirms that the remote is Private.
