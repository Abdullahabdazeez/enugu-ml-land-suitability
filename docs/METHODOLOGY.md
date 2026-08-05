# Methodology

## 1. Study-area preparation

The Enugu State administrative boundary was prepared in WGS 84 geographic coordinates and
reprojected to WGS 84 / UTM Zone 32N for area, distance and raster analysis.

## 2. Predictor preparation

The modelling predictors were prepared from terrain, land-cover, hydrological, population and
transport datasets. All continuous predictor rasters were aligned to a common 30-metre reference
grid using bilinear resampling where required. Categorical land cover was aligned using
nearest-neighbour resampling.

The final predictors were:

1. Elevation
2. Slope
3. Distance to roads
4. Distance to recurring surface water
5. Distance to drainage
6. Population density
7. Baseline Dynamic World 2020 land cover

## 3. Urban-transition target

Dynamic World observations for 2020 and 2025 were compared to derive stable non-built, stable
built, urban-gain and apparent urban-loss transitions. Observation-count and spatial-persistence
tests showed that raw transitions contained substantial noise.

A conservative spatial reliability procedure was therefore applied. Accepted gain pixels had to
meet minimum observation, patch-size, proximity and neighbourhood-support thresholds.

## 4. Negative-sample construction

Negative samples were selected from stable non-built locations that were physically plausible
candidates for expansion but did not transition during the observation period. Restricting
negative samples to the urban influence zone prevented the model from learning an overly simple
contrast between remote rural areas and urban-edge expansion.

## 5. Spatial sampling

Positive and negative samples were balanced. Spatial block allocation was solved using mixed
integer linear programming to preserve class balance while maintaining complete separation
between training, validation and test blocks.

## 6. Leakage audit

The initial feature set included distance to 2020 built-up land. Because this variable also formed
part of the target-label definition, it created circular prediction and unrealistically high model
performance.

A rule-based leakage test achieved approximately 97.9% accuracy using the 90-metre label boundary
alone. The distance-to-built predictor was therefore removed from the official model.

## 7. Candidate models

The following algorithms were evaluated:

- Logistic Regression
- Random Forest
- Extra Trees
- Histogram Gradient Boosting

Training data were used for fitting, validation data were used for model comparison and the test
set remained untouched until final evaluation.

## 8. Independent evaluation

The final Extra Trees classifier was evaluated against the spatially independent test set using:

- accuracy;
- balanced accuracy;
- precision;
- recall;
- specificity;
- F1 score;
- ROC-AUC;
- precision-recall AUC;
- Matthews correlation coefficient;
- Cohen's kappa;
- Brier score;
- log loss;
- confusion matrix.

## 9. Model interpretation

Model interpretation used grouped native feature importance, validation permutation importance,
independent-test permutation importance and partial-dependence analysis.

## 10. Statewide prediction

The fixed final model was applied across Enugu State using tiled raster processing. Predictor order,
band identity, categorical resampling and output ranges were validated during prediction.

## 11. Planning constraints

The raw probability surface was converted to a planning-applicable surface by excluding or
constraining unsuitable land such as existing built-up areas, water-related zones and steep terrain.

## 12. Suitability classes

The constrained probability surface was reclassified into:

- Very Low
- Low
- Moderate
- High
- Very High

## 13. Confidence and uncertainty

Tree-level prediction variation was used to estimate uncertainty and confidence. Confidence was
classified into low, moderate and high categories.

## 14. Planning priority

Planning priority combined development suitability with model confidence. This ensured that high
predicted suitability did not automatically translate into high planning priority where predictive
confidence was weak.

## 15. Cartography and reporting

All final maps were produced using a consistent professional layout, projected coordinate grid,
scale bar, north arrow, legend, boundary overlay and 450-dpi PNG/PDF export.
