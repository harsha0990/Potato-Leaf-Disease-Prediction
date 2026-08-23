# Training Dataset

The project expects the training images in exactly this structure:

```text
data/
└── dataset/
    ├── Potato_leafroll_virus/
    ├── Potato_healthy/
    └── Potato_mosaic_virus/
```

The image dataset itself is **not committed to GitHub** because large binary datasets make repositories unnecessarily large.

## Exact three-class dataset

For the notebook's original experiment, use a dataset that genuinely contains these three labels:

- `Potato_leafroll_virus`
- `Potato_healthy`
- `Potato_mosaic_virus`

Do **not** rename Early Blight or Late Blight images to these virus labels.

## Setup

If you have legally obtained the exact three-class dataset:

```bash
python scripts/setup_dataset.py --source /path/to/source_dataset
```

The source folder must already contain:

```text
source_dataset/
├── Potato_leafroll_virus/
├── Potato_healthy/
└── Potato_mosaic_virus/
```

The script copies the images into the project's expected directory structure.

## Public PlantVillage reference

The public PlantVillage dataset contains 54,306 healthy/diseased leaf images across 14 crops and 26 diseases. Its potato subset uses classes such as Early Blight, Late Blight and healthy; it does **not** provide the exact three virus classes required by this notebook.

You can inspect/download PlantVillage with:

```bash
python scripts/setup_dataset.py --plantvillage
```

This mode only verifies the available potato classes and deliberately does not relabel them.

## Dataset citation

If you use PlantVillage or a derived dataset, follow its original citation and licensing requirements:

Mohanty, S. P., Hughes, D. P., & Salathé, M. (2016).
"Using Deep Learning for Image-Based Plant Disease Detection."
Frontiers in Plant Science, 7, 1419.
DOI: 10.3389/fpls.2016.01419
