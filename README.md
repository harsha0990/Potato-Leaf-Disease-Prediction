# Potato Leaf Disease Classification

An academic machine-learning project for early detection of viral diseases in potato plants from leaf images.

## Models
- Gaussian Naive Bayes
- Random Forest Classifier

## Classes
The notebook is designed around these three classes:
- `Potato_leafroll_virus`
- `Potato_healthy`
- `Potato_mosaic_virus`

## Project structure

```text
potato_leaf_disease_classification/
├── data/
│   ├── dataset/
│   │   ├── Potato_leafroll_virus/
│   │   ├── Potato_healthy/
│   │   └── Potato_mosaic_virus/
│   └── test_images/
├── models/
├── notebooks/
│   └── potato_leaf_disease_classification.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

## How to run

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Place the image dataset in `data/dataset/`, with one folder per class.
5. Place a test image in `data/test_images/sample.jpg`.
6. Open the notebook:

```bash
jupyter notebook notebooks/potato_leaf_disease_classification.ipynb
```

7. Run the cells from top to bottom.

## Notes

- The notebook no longer contains machine-specific Windows paths.
- Generated `.npy` arrays and trained `.pkl` models are ignored by Git.
- Do not commit private datasets or large files unless you have permission and your repository is prepared for them.
- This project is intended for academic/educational use and should not be treated as a clinical or agricultural diagnosis system without further validation.


## Training dataset

The repository does not store the large training-image collection directly.

The notebook expects:

```text
data/
└── dataset/
    ├── Potato_leafroll_virus/
    ├── Potato_healthy/
    └── Potato_mosaic_virus/
```

To prepare an exact three-class dataset that you have legally obtained:

```bash
python scripts/setup_dataset.py --source /path/to/source_dataset
```

See `data/README.md` for the dataset requirements and the PlantVillage reference setup.

**Important:** The standard PlantVillage potato subset contains Early Blight, Late Blight and healthy classes. It should not be relabeled as leafroll virus or mosaic virus. The setup script therefore refuses to perform such relabeling.
