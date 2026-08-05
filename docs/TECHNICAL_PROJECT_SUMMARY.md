# Technical Project Summary

## Project title

Machine-Learning-Based Land Suitability Analysis for Sustainable Urban Development — Enugu State, Nigeria

## Study area

Enugu State, Nigeria

## Coordinate reference system

EPSG:32632 — WGS 84 / UTM Zone 32N

## Spatial resolution

30 metres

## Problem statement

Urban growth in Enugu State requires spatially explicit evidence that distinguishes locations with
high development potential from areas affected by physical limitations, environmental constraints
or model uncertainty. Conventional weighted-overlay suitability models often depend heavily on
subjective criterion weights. This project applied a supervised machine-learning framework based
on observed urban transitions while explicitly addressing target leakage, spatial dependence,
classification uncertainty and planning constraints.

## Objective

To develop and validate a machine-learning-based spatial model that estimates urban expansion
probability and converts the results into environmentally constrained suitability and
confidence-adjusted planning-priority classes.

## Data sources

- Copernicus DEM GLO-30 for elevation and slope
- Dynamic World V1 for 2020 and 2025 land cover
- OpenStreetMap for road-network proximity
- JRC Global Surface Water for recurring surface water
- MERIT Hydro for drainage proximity
- WorldPop for population density
- Administrative boundaries for Enugu State

## Leakage-safe predictors

- Elevation
- Slope
- Distance to roads
- Distance to recurring surface water
- Distance to drainage
- Population density
- Baseline Dynamic World land cover 2020

## Target definition

Positive samples represented reliable urban gain between 2020 and 2025:

- non-built in 2020;
- built in 2025;
- at least five valid observations;
- transition patch of at least five pixels;
- within 90 metres of stable 2020 built-up land;
- neighbourhood support of at least 0.67.

Negative samples represented stable non-built land:

- non-built in both 2020 and 2025;
- at least five valid observations;
- slope not exceeding 15 degrees;
- located 90–1,500 metres from stable 2020 built-up land;
- at least 90 metres from accepted positive samples.

## Sampling and validation

A balanced sample containing 24,000 records was generated.

- Training: 16,800 samples
- Validation: 3,600 samples
- Independent test: 3,600 samples
- Training spatial blocks: 145
- Validation spatial blocks: 40
- Test spatial blocks: 32
- Spatial block overlap: zero

## Model

Leakage-corrected Extra Trees classifier

Number of trees: 500

## Independent spatial test results

- Accuracy: 0.7111
- Balanced Accuracy: 0.7111
- Precision: 0.6822
- Recall: 0.7906
- Specificity: 0.6317
- F1 Score: 0.7324
- ROC-AUC: 0.7517
- PR-AUC: 0.6718
- Matthews Correlation Coefficient: 0.4277
- Cohen Kappa: 0.4222
- Brier Score: 0.2015
- Log Loss: 0.5956

## Confusion matrix

- True Negative: 1,137
- False Positive: 663
- False Negative: 377
- True Positive: 1,423

## Statewide results

- Valid model area: 7,619.47 km²
- Planning-applicable area: 6,050.85 km²
- Planning-constrained area: 1,568.63 km²
- Mean raw expansion probability: 0.3500
- Mean constrained probability: 0.3137
- Mean model uncertainty: 0.2844

## Suitability distribution

- Very Low: 2,177.69 km²
- Low: 1,988.35 km²
- Moderate: 1,353.05 km²
- High: 515.09 km²
- Very High: 16.67 km²

## Planning-priority distribution

- Very Low Priority: 4,166.04 km²
- Low Priority: 923.80 km²
- Moderate Priority: 567.79 km²
- High Priority: 392.83 km²
- Very High Priority: 0.37 km²

## Model-confidence distribution

- Low Confidence: 2,146.92 km² (35.48%)
- Moderate Confidence: 3,873.85 km² (64.02%)
- High Confidence: 30.08 km² (0.50%)

## Grouped feature importance

- Distance to roads: 41.67%
- Population density: 16.97%
- Distance to recurring surface water: 12.02%
- Elevation: 11.54%
- Distance to drainage: 9.06%
- Slope: 5.62%
- Baseline land cover 2020: 3.12%

## Principal interpretation

The model indicates that proximity to road infrastructure is the strongest spatial factor
associated with recent urban expansion. Population density provides an additional indicator of
development pressure. Terrain, surface-water proximity, drainage proximity and baseline land
cover influence where expansion is physically or environmentally more likely.

The confidence results show that most applicable land falls within the moderate-confidence class.
Only a small area achieved high confidence. Planning-priority results were therefore intentionally
conservative.

## Intended use

The outputs are appropriate for:

- state-level strategic planning;
- regional urban-growth screening;
- identification of candidate development corridors;
- comparison of alternative planning zones;
- prioritisation of areas for detailed site investigation;
- environmental and infrastructure planning.

## Appropriate caution

The suitability and priority outputs are screening products. They do not constitute building
approval, cadastral verification, geotechnical certification or environmental-impact clearance.
