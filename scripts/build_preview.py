#!/usr/bin/env python3
"""Build a lightweight GitHub Pages preview from approved Natural Wellness legacy assets.

The source site remains the source of truth for visual files during migration. This script:
1. copies index.html into dist/
2. downloads the approved/discovered legacy asset inventory
3. converts raster photos/graphics to WebP where practical
4. rewrites references used by the preview to local optimized files
5. leaves a remote URL untouched if an individual asset cannot be downloaded

Production launch should use the team's original source files where available and revalidate
all certification marks, product art and leadership photography before publication.
"""

from __future__ import annotations

import io
import shutil
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ASSET_DIR = DIST / "assets"

ASSETS = {
    # Brand / facility
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/nw_logo.png": "natural-wellness-logo.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/factory-picture-edited.jpg": "natural-wellness-facility.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/home_business_about.jpg": "natural-wellness-about.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/manufacture1.jpg": "manufacturing-facility.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/career.jpg": "careers.webp",

    # Service icons
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/Service-Icon-01.png": "service-rd.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/Service-Icon-02-1.png": "service-formulate.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/Service-Icon-03-1.png": "service-manufacture.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/Service-Icon-04-1.png": "service-distribute.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/Service-Icon-05-1.png": "service-commercialise.webp",

    # Quality / GMP
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/Cert-Logo.png": "certification-marks-legacy.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/GMP-edited-1.png": "gmp-legacy.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/pic1.jpg": "gmp-photo-01.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/pic2.jpg": "gmp-photo-02.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/pic3.jpg": "gmp-photo-03.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/pic4.jpg": "gmp-photo-04.webp",

    # Product categories / archive
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/Natural2.png": "category-natural.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/otc.jpg": "category-otc.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/islamic.jpg": "category-islamic.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/cosmetic.jpg": "category-cosmetic.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/therepautic-class-012.png": "therapeutic-class-legacy.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/heptex.jpg": "product-heptex-legacy.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/gingko.png": "product-gingko-plus-legacy.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/billberry-gingko.jpg": "product-berry-complex-legacy.webp",

    # Cosmetic ranges
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/EmmolientRange.jpg": "cosmetic-emollient-range.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/ACSeries.jpg": "cosmetic-ac-series.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/SunSeries.jpg": "cosmetic-sun-series.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/WhiteningNetwork.jpg": "cosmetic-whitening-network.webp",

    # R&D
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/potion-01.png": "rd-potion.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/JAM-PASIR-02.png": "rd-jam-pasir.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/research1.jpg": "research-01.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/research2.jpg": "research-02.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/research3.jpg": "research-03.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/research4.jpg": "research-04.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2014/09/research5.jpg": "research-05.webp",

    # Leadership
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/06/gambar-dr.-yacout.jpg": "leader-amr-yacout.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/06/gmbr-bos.jpg": "leader-shahnas-oli-mohamed.webp",

    # Awards
    **{
        f"https://mynaturalwellness.com/wp/wp-content/uploads/2016/06/p{i}.jpg": f"award-{i:02d}.webp"
        for i in range(1, 9)
    },

    # CSR / media
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/07/Logo-apple.png": "csr-farrash-foundation-legacy.webp",
    "https://mynaturalwellness.com/wp/wp-content/uploads/2016/05/smidex-web-cover-01.jpg": "smidex-2016-legacy.webp",
}


def download(url: str) -> bytes:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 NaturalWellnessMigration/1.0",
            "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        },
    )
    with urlopen(req, timeout=30) as response:
        return response.read()


def to_webp(raw: bytes, target: Path) -> None:
    with Image.open(io.BytesIO(raw)) as im:
        im.load()
        # Keep transparency where present. Large legacy photography is capped so the preview
        # does not ship multi-megapixel source files unnecessarily.
        if max(im.size) > 1800:
            im.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA" if "transparency" in im.info else "RGB")
        im.save(target, "WEBP", quality=80, method=6)


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    ASSET_DIR.mkdir(parents=True)

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    successes = 0
    failures = []

    for url, filename in ASSETS.items():
        target = ASSET_DIR / filename
        try:
            raw = download(url)
            to_webp(raw, target)
            html = html.replace(url, f"assets/{filename}")
            successes += 1
            print(f"OK   {filename}")
        except Exception as exc:  # keep deployment resilient during migration
            failures.append((url, str(exc)))
            print(f"WARN {url}: {exc}")

    (DIST / "index.html").write_text(html, encoding="utf-8")
    for extra in ("robots.txt", ".nojekyll"):
        src = ROOT / extra
        if src.exists():
            shutil.copy2(src, DIST / extra)

    report = [
        "Natural Wellness preview asset build",
        f"Optimized assets: {successes}/{len(ASSETS)}",
        "",
    ]
    if failures:
        report.append("Assets that remained remote because migration download failed:")
        report.extend(f"- {url}: {err}" for url, err in failures)
    else:
        report.append("All discovered/approved migration assets downloaded successfully.")
    (DIST / "asset-build-report.txt").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
