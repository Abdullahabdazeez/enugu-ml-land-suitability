# Near-Urban Expansion Suitability in Enugu State, Nigeria

<p align="center">
  <img src="assets/maps/Enugu_Final_Suitability_Map.png" alt="Near-urban expansion suitability in Enugu State" width="100%">
</p>

## Planning question

**Among places already close to Enugu's 2020 urban edge, can terrain, accessibility, environmental conditions and population pressure help distinguish locations that became built-up by 2025 from places that remained non-built?**

I used an **Extra Trees** model with seven predictors and spatially separated Train, Validation and Test data. The experiment is deliberately limited to comparable non-built locations within the same **30-90 m near-urban support**, so the model is evaluated on the planning question it is intended to answer.

## Key results

| Metric | Extra Trees | Distance-only baseline |
|---|---:|---:|
| ROC-AUC | **0.7267** | 0.7068 |
| PR-AUC | **0.3319** | 0.1903 |
| Balanced Accuracy | 0.6614 | **0.6689** |
| F1 | **0.3368** | 0.2937 |

The Extra Trees model improves ROC-AUC by about **0.020** and PR-AUC by about **0.142** compared with a simple distance-to-built benchmark. The benchmark retains slightly higher balanced accuracy, so the correct interpretation is that the ML model **adds useful discrimination beyond proximity but does not outperform the benchmark on every metric**.

<p align="center">
  <img src="assets/figures/R5_ExtraTrees_vs_Distance_Benchmark.png" alt="Extra Trees model compared with a distance-only baseline" width="90%">
</p>

## What the model uses

The final model uses seven predictors:

- elevation;
- slope;
- distance to roads;
- distance to recurring surface water;
- distance to drainage;
- 2020 population density; and
- baseline 2020 land cover.

`Distance_to_Built_2020_m` is **not** used as an ML predictor. It is retained only as a benchmark so the model can be tested against simple proximity to the existing urban edge. Coordinates, sample IDs, spatial block IDs and outcome-year variables are also excluded from the predictor set.

## Probability surface

<p align="center">
  <img src="assets/maps/Enugu_Final_Probability_Map.png" alt="Predicted probability of near-urban expansion in Enugu State" width="100%">
</p>

The validation-selected operating threshold is **0.36**. Final suitability classes use fixed probability ranges rather than quantiles.

| Suitability class | Probability range | Area (km²) | Share |
|---|---|---:|---:|
| Low | p < 0.36 | 715.13 | 81.53% |
| Moderate | 0.36 ≤ p < 0.50 | 76.49 | 8.72% |
| High | 0.50 ≤ p < 0.70 | 48.26 | 5.50% |
| Very High | p ≥ 0.70 | **37.27** | **4.25%** |

Only **4.25%** of the valid near-urban prediction domain reaches probability ≥0.70. That scarcity is retained as part of the result rather than obscured through a different classification scheme.

## What seems to matter most

<p align="center">
  <img src="assets/figures/R5_Feature_Importance.png" alt="Feature importance for the Enugu Extra Trees model" width="90%">
</p>

Population density is the strongest model predictor, followed by distance to recurring surface water and elevation. Feature importance describes model reliance and predictive association; it does **not** establish causation.

## Method

1. Define observed 2020-2025 near-urban expansion and comparable stable non-built controls.
2. Restrict the experiment to the same 30-90 m near-urban support.
3. Exclude proximity-to-built, coordinates, IDs and outcome-year variables from the ML predictor set.
4. Create spatially separated Train, Validation and Test blocks.
5. Compare Extra Trees with a simple urban-proximity benchmark.
6. Select the operating threshold using Validation data only.
7. Preserve the independent Test set for final held-out evaluation.
8. Refit the locked Extra Trees design on Train + Validation.
9. Produce the continuous probability surface and fixed-threshold suitability classes.
10. Quantify high-confidence area directly.

Full methodology: [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md).

## Planning value

The final surface is best used as a **near-urban screening layer**. It highlights places with characteristics similar to locations that actually expanded between 2020 and 2025 and can support early discussion of growth management, infrastructure planning and locations that warrant closer investigation.

It is **not** a planning approval map, a causal model, a parcel-level forecast or a general statewide land-suitability map. Site-level decisions should also consider planning policy, infrastructure capacity, environmental constraints, land tenure and field verification.

## Reports and outputs

- [Final technical report - PDF](reports/Enugu_Final_Technical_Report.pdf)
- [Final technical report - DOCX](reports/Enugu_Final_Technical_Report.docx)
- [`assets/maps`](assets/maps/) - final probability and suitability maps
- [`assets/figures`](assets/figures/) - benchmark, feature-importance and confidence figures
- [`data/tables`](data/tables/) - final result tables
- [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md) - scientific limitations

## Tools

Python · scikit-learn · GeoPandas · Rasterio · Pandas · GIS · Remote Sensing · Spatial Validation

## Author

**Abdullah Abdazeez Ayomide**  
Geospatial Planner · GIS & Remote Sensing Analyst · Urban & Environmental Planning Researcher

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff).
