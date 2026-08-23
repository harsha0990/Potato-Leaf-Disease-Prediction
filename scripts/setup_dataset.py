"""
Download and prepare the potato training dataset.

IMPORTANT:
The public PlantVillage dataset does NOT contain the exact
Potato_leafroll_virus / Potato_mosaic_virus classes used by the
original notebook. Therefore this script does not silently relabel
other potato diseases as those virus classes.

This script supports two modes:
1. --source <folder>: use a legally obtained source dataset and copy/
   map the exact three classes into data/dataset/.
2. --plantvillage: download the standard PlantVillage dataset and
   prepare only the potato classes that actually exist there
   (Potato___Early_blight, Potato___Late_blight, Potato___healthy).
   This mode is intentionally NOT compatible with the original
   three-virus-class experiment and is provided only as a reference.

For the exact three-class project, supply a dataset containing:
    Potato_leafroll_virus/
    Potato_healthy/
    Potato_mosaic_virus/

Example:
    python scripts/setup_dataset.py --source /path/to/source_dataset
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "data" / "dataset"

EXACT_CLASSES = [
    "Potato_leafroll_virus",
    "Potato_healthy",
    "Potato_mosaic_virus",
]

PLANTVILLAGE_CLASSES = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
]

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def copy_exact_classes(source: Path) -> None:
    missing = [c for c in EXACT_CLASSES if not (source / c).is_dir()]
    if missing:
        raise FileNotFoundError(
            "The supplied source does not contain the required exact "
            f"classes: {', '.join(missing)}"
        )

    DEST.mkdir(parents=True, exist_ok=True)

    for class_name in EXACT_CLASSES:
        target = DEST / class_name
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)

        files = [
            p for p in (source / class_name).rglob("*")
            if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
        ]

        for i, src in enumerate(files, start=1):
            target_name = f"{i:05d}_{src.name}"
            shutil.copy2(src, target / target_name)

        print(f"{class_name}: {len(files)} images copied")


def download_plantvillage() -> None:
    """Download the upstream PlantVillage repository as a reference dataset."""
    tmp = ROOT / ".plantvillage_download"
    if tmp.exists():
        shutil.rmtree(tmp)

    print("Downloading PlantVillage...")
    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "https://github.com/spMohanty/PlantVillage-Dataset.git",
            str(tmp),
        ],
        check=True,
    )

    color = tmp / "raw" / "color"
    if not color.exists():
        raise FileNotFoundError(f"Expected PlantVillage color data at {color}")

    print("\nPlantVillage potato classes found:")
    for class_name in PLANTVILLAGE_CLASSES:
        count = sum(
            1 for p in (color / class_name).rglob("*")
            if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
        )
        print(f"  {class_name}: {count} images")

    print(
        "\nThe downloaded PlantVillage data contains Early blight, "
        "Late blight and healthy potato classes—not the exact "
        "leafroll-virus/mosaic-virus classes required by this project."
    )
    print("No incorrect relabeling was performed.")

    shutil.rmtree(tmp, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    parser.add_argument("--plantvillage", action="store_true")
    args = parser.parse_args()

    if bool(args.source) == bool(args.plantvillage):
        parser.error("Choose exactly one: --source or --plantvillage")

    if args.source:
        copy_exact_classes(args.source)
        print(f"\nDataset prepared at: {DEST}")
    else:
        download_plantvillage()


if __name__ == "__main__":
    main()
