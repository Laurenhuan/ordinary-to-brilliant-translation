"""Generate the pilot_01 cleaned Markdown without modifying raw MinerU files.

This script is intentionally pilot-specific. It validates exact input hashes,
extracts the five DOCX media files byte-for-byte when absent, verifies existing
copies, and creates source/chapters/pilot_01_cleaned.md from source.md.
It never reads DOCX text and never applies its rules to other book content.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


REPO = Path(__file__).resolve().parents[1]
PILOT = REPO / "source" / "raw" / "pilot_01"
SOURCE_MD = PILOT / "source.md"
SOURCE_JSON = PILOT / "source.json"
SOURCE_DOCX = PILOT / "source.docx"
IMAGES_DIR = PILOT / "images"
OUTPUT = REPO / "source" / "chapters" / "pilot_01_cleaned.md"

EXPECTED_HASHES = {
    SOURCE_MD: "f5dc769d01552847a86e1bb0fcfdce9ed76de792bd8c9ee3d984969e4c106d29",
    SOURCE_JSON: "7a052bd7f622e3322466884bf39b39676ccb18141a9149db51b95a33cd43079c",
    SOURCE_DOCX: "ed6e29328e8df5728f78ed53930f77e897d233d41cd51c54c18c65efc5c93c71",
}

DOCX_IMAGES = [
    ("word/media/rId10.jpg", "image_001.jpg", "3b74999b546d5803360c2c1109317c0e66b1f8814817acfa05047ce37e0e9615"),
    ("word/media/rId15.jpg", "image_002.jpg", "99a03bf9a2137bd15589dfedd0ab85d616e6c01e3b0a6c35a684191662719142"),
    ("word/media/rId18.jpg", "image_003.jpg", "08f18fc7637cfec31eb1a3fe69878dda4a1e9c0326711b04a9797e487889f430"),
    ("word/media/rId25.jpg", "image_004.jpg", "dd50fd77a958fc04e7870001af7c0759c9deac4339a18a2c09fd68d46692edb5"),
    ("word/media/rId28.jpg", "image_005.jpg", "c49e774591d7983e804a3a321ec2f734749f384394ff578c2399de8bd8d23795"),
]

CDN_URLS = [
    "https://cdn-mineru.openxlab.org.cn/result/2026-08-19/584444d2-478e-4193-9089-f1e9d865bee5/153a2a164ce711d8fd874012d1b2da9edc43d3e89c905a0ec574cc7754d22617.jpg",
    "https://cdn-mineru.openxlab.org.cn/result/2026-08-19/584444d2-478e-4193-9089-f1e9d865bee5/51879b6447583817b937d0da9b2ffff7483e2bdf694913defefb4cafff07f75f.jpg",
    "https://cdn-mineru.openxlab.org.cn/result/2026-08-19/584444d2-478e-4193-9089-f1e9d865bee5/42b4f84bf4badd9c56386a6852e9fc92fa3f5d360225d7a75022ec49f56b0687.jpg",
    "https://cdn-mineru.openxlab.org.cn/result/2026-08-19/584444d2-478e-4193-9089-f1e9d865bee5/de41bee7ec1e54bcae6c2506ae80cc1d90f57b4887157ff09abcfcab0c616420.jpg",
    "https://cdn-mineru.openxlab.org.cn/result/2026-08-19/584444d2-478e-4193-9089-f1e9d865bee5/09fa20d0b05e802b164cbf81fa3948c5308a38dafe5a3f5117d1c542ba0520c4.jpg",
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_inputs() -> None:
    for path, expected in EXPECTED_HASHES.items():
        actual = digest(path.read_bytes())
        if actual != expected:
            raise RuntimeError(f"Refusing to run: unexpected SHA-256 for {path}: {actual}")

    data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    pages = data.get("pdf_info", [])
    if [page.get("page_idx") for page in pages] != list(range(11)):
        raise RuntimeError("Refusing to run: JSON page_idx sequence is not 0 through 10.")

    raw_json = SOURCE_JSON.read_text(encoding="utf-8")
    if sum(raw_json.count(url) for url in CDN_URLS) != 10:
        raise RuntimeError("Refusing to run: JSON image references do not match the pilot.")


def extract_or_verify_images() -> None:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    with ZipFile(SOURCE_DOCX) as archive:
        for entry, filename, expected_hash in DOCX_IMAGES:
            data = archive.read(entry)
            if digest(data) != expected_hash:
                raise RuntimeError(f"Unexpected DOCX media bytes for {entry}.")
            target = IMAGES_DIR / filename
            if target.exists():
                if digest(target.read_bytes()) != expected_hash:
                    raise RuntimeError(f"Refusing to overwrite mismatched local image: {target}")
            else:
                target.write_bytes(data)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match for {label}; found {count}.")
    return text.replace(old, new, 1)


def build_cleaned_markdown() -> str:
    text = SOURCE_MD.read_bytes().decode("utf-8").replace("\r\n", "\n")

    for index, url in enumerate(CDN_URLS, start=1):
        text = replace_once(
            text,
            url,
            f"../raw/pilot_01/images/image_{index:03d}.jpg",
            f"image URL {index}",
        )

    text = replace_once(
        text,
        "contents \n",
        "contents\n",
        "decorative contents trailing whitespace",
    )

    text = replace_once(
        text,
        "庆尚南道 $^{①}$ 宜宁",
        "庆尚南道[^p005-1]宜宁",
        "page 5 footnote marker",
    )
    text = replace_once(
        text,
        "朝鲜末期 $^{①}$ 的",
        "朝鲜末期[^p006-1]的",
        "page 6 footnote marker",
    )
    text = replace_once(
        text,
        "北间岛①去",
        "北间岛[^p010-1]去",
        "page 10 footnote marker",
    )

    text = replace_once(
        text,
        "## 从平凡走向辉煌\n\n大韩民国另外一位极具代表性的杰出人物",
        "<!-- source-page: mineru_page_idx=0; printed_page=6 -->\n\n大韩民国另外一位极具代表性的杰出人物",
        "page 0 running header",
    )
    text = replace_once(
        text,
        "团队式的经营也是由他们引入韩国的一种独特的经营方式。",
        "<!-- source-page: mineru_page_idx=1; printed_page=7 -->\n\n团队式的经营也是由他们引入韩国的一种独特的经营方式。",
        "page 1 marker",
    )
    text = replace_once(
        text,
        "![image](../raw/pilot_01/images/image_001.jpg)",
        "<!-- source-page: mineru_page_idx=2; printed_page=9 -->\n\n![image](../raw/pilot_01/images/image_001.jpg)",
        "page 2 marker",
    )
    text = replace_once(
        text,
        "21. 信任与考察 …… 175",
        "<!-- source-page: mineru_page_idx=3; printed_page=10 -->\n\n21. 信任与考察 …… 175",
        "page 3 marker",
    )
    text = replace_once(
        text,
        "# 1 大地主的儿子和贫农的儿子",
        "<!-- source-page: mineru_page_idx=4; printed_page=unresolved -->\n\n# 1 大地主的儿子和贫农的儿子",
        "page 4 marker",
    )
    text = replace_once(
        text,
        "## 从平凡走向辉煌\n\n李秉哲（1910—1987）出生于大富之家。",
        "<!-- source-page: mineru_page_idx=5; printed_page=2 -->\n\n李秉哲（1910—1987）出生于大富之家。",
        "page 5 running header",
    )
    text = replace_once(
        text,
        "需要特别指出的是：尽管郑周永在私塾的学习只有短短的三年时间",
        "<!-- source-page: mineru_page_idx=6; printed_page=3 -->\n\n需要特别指出的是：尽管郑周永在私塾的学习只有短短的三年时间",
        "page 6 marker",
    )
    text = replace_once(
        text,
        "李秉哲也时常引经据典。他也是在私塾时就达到了通读\n\n## 从平凡走向辉煌\n\n《千字文》乃至《论语》的水平。",
        "李秉哲也时常引经据典。他也是在私塾时就达到了通读<!-- source-page: mineru_page_idx=7; printed_page=4 -->《千字文》乃至《论语》的水平。",
        "page 6 to 7 paragraph join",
    )
    text = replace_once(
        text,
        "## 2\n\n# “海归”和离家出走的少年",
        "<!-- source-page: mineru_page_idx=8; printed_page=unresolved -->\n\n# 2 “海归”和离家出走的少年",
        "chapter 2 heading",
    )
    text = replace_once(
        text,
        "从平凡走向辉煌\n\n1929 年 10 月李秉哲正值弱冠之年，赴日本留学。",
        "<!-- source-page: mineru_page_idx=9; printed_page=6 -->\n\n1929 年 10 月李秉哲正值弱冠之年，赴日本留学。",
        "page 9 running header",
    )
    text = replace_once(
        text,
        "日本产业界也受到经济大恐慌的影响，开始裁员。",
        "<!-- source-page: mineru_page_idx=10; printed_page=7 -->\n\n日本产业界也受到经济大恐慌的影响，开始裁员。",
        "page 10 marker",
    )

    text = text.replace(
        "小源浪平",
        "小源浪平<!-- TODO(QA): Verify this proper-name glyph against the authorized PDF; preserve the raw form until confirmed. -->",
        1,
    )

    provenance = (
        "<!--\n"
        "Non-destructive MinerU pilot cleaned sample.\n"
        "Primary text: ../raw/pilot_01/source.md\n"
        "Page/block evidence: ../raw/pilot_01/source.json\n"
        "Image fallback only: ../raw/pilot_01/source.docx\n"
        "Do not use DOCX-derived text to overwrite this Markdown.\n"
        "-->\n\n"
    )

    footnotes = (
        "\n\n<!-- TODO(QA): The pilot ends mid-sentence at mineru_page_idx=10; verify the continuation against the next authorized source page. -->\n\n"
        "[^p005-1]: 韩国的“道”相当于中国“省”一级的行政单位。\n"
        "[^p006-1]: 19世纪末20世纪初。\n"
        "[^p010-1]: 现位于中国吉林省。\n"
    )
    return provenance + text.rstrip() + footnotes


def main() -> None:
    validate_inputs()
    extract_or_verify_images()
    OUTPUT.write_text(build_cleaned_markdown(), encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
