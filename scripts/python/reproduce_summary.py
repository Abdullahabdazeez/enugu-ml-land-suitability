from pathlib import Path
import math
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "data" / "processed" / "tables"

metrics = pd.read_csv(TABLES / "Enugu_Final_Independent_Test_Metrics.csv").iloc[0]
key = pd.read_csv(TABLES / "Final_Project_Key_Results.csv")
values = dict(zip(key["Indicator"], key["Value"]))

checks = {
    "ROC_AUC": 0.7516694444444444,
    "Balanced_Accuracy": 0.7111111111111111,
    "F1_Score": 0.7323726196603191,
    "Cohen_Kappa": 0.4222222222222223,
}

for column, expected in checks.items():
    actual = float(metrics[column])
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=1e-12):
        raise ValueError(f"{column}: expected {expected}, found {actual}")

area_checks = {
    "Planning-applicable area": 6050.85,
    "Planning-constrained area": 1568.63,
    "High suitability": 515.09,
    "Very high suitability": 16.67,
    "High planning priority": 392.83,
    "Very high planning priority": 0.37,
}

for indicator, expected in area_checks.items():
    actual = float(values[indicator])
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=0.01):
        raise ValueError(f"{indicator}: expected {expected}, found {actual}")

print("RESULT REPRODUCTION: PASSED")
print(f"ROC-AUC: {metrics['ROC_AUC']:.4f}")
print(f"Balanced accuracy: {metrics['Balanced_Accuracy']:.4f}")
print(f"F1 score: {metrics['F1_Score']:.4f}")
print(f"Planning-applicable area: {values['Planning-applicable area']:,.2f} km²")
print(f"High + very-high suitability: {values['High suitability'] + values['Very high suitability']:,.2f} km²")
