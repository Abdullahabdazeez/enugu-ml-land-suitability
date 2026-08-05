from pathlib import Path
import json
import sys
import math
import pandas as pd
import rasterio

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "project.json",
    "LICENSE",
    "CITATION.cff",
    "requirements.txt",
    "assets/project-cover.png",
    "assets/repository-social-preview.png",
    "notebooks/Project_7_Enugu_ML_Land_Suitability_Reproducible.ipynb",
    "docs/METHODOLOGY.md",
    "docs/LIMITATIONS_AND_RECOMMENDATIONS.md",
    "data/processed/tables/Enugu_Final_Independent_Test_Metrics.csv",
    "data/processed/tables/Final_Project_Key_Results.csv",
    "outputs/maps/03_urban_development_suitability.png",
]

failures = [f"Missing: {item}" for item in required if not (ROOT / item).exists()]

for path in ROOT.rglob("*"):
    if path.is_file() and path.stat().st_size > 24 * 1024 * 1024:
        failures.append(f"Browser-upload limit exceeded: {path.relative_to(ROOT)}")

try:
    metadata = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
    if not math.isclose(metadata["roc_auc"], 0.7516694444444444, abs_tol=1e-12):
        failures.append("Unexpected ROC-AUC metadata")
except Exception as exc:
    failures.append(f"Invalid project metadata: {exc}")


if failures:
    print("REPOSITORY VALIDATION: FAILED")
    for failure in failures:
        print("-", failure)
    sys.exit(1)

print("REPOSITORY VALIDATION: PASSED")
print("Required files, metrics, categorical rasters and browser-upload limits are valid.")
