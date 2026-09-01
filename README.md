# Near-Urban Expansion Suitability in Enugu State, Nigeria

<p align="center">
  <img src="assets/maps/Enugu_Final_Suitability_Map.png" alt="Near-urban expansion suitability in Enugu State" width="100%">
</p>

## What this project asks

Among places already close to the 2020 urban edge, can terrain, accessibility, environmental conditions and population pressure help distinguish locations that became built-up by 2025 from locations that remained non-built?

I used an **Extra Trees** model to answer that question. The final workflow was rebuilt after an audit showed that the earlier experiment could give the model unfair clues through administrative variables and distance-driven sample separation.

The corrected version removes those shortcuts and evaluates the model on spatially separated data.

## The main result

The model adds useful predictive information beyond simple distance to existing built-up land, but the improvement is moderate rather than dramatic.

| Metric | Extra Trees | Distance-only baseline |
|---|---:|---:|
| ROC-AUC | **0.7267** | 0.7068 |
| PR-AUC | **0.3319** | 0.1903 |
| Balanced accuracy | 0.6614 | **0.6689** |
| F1 | **0.3368** | 0.2937 |

Extra Trees improves ROC-AUC by about **0.020** and PR-AUC by about **0.142**, while the distance-only baseline keeps a slightly higher balanced accuracy.

That is why I describe the result carefully: **the ML model adds discrimination beyond proximity, but it does not beat the baseline on every metric.**

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

`Distance_to_Built_2020_m` is **not** used as an ML predictor. I keep it only as a benchmark so I can test whether the model learns anything beyond simple proximity to the existing urban edge.

Coordinates, sample IDs, spatial block IDs and outcome-year variables are also excluded.

## Probability surface

<p align="center">
  <img src="assets/maps/Enugu_Final_Probability_Map.png" alt="Predicted probability of near-urban expansion in Enugu State" width="100%">
</p>

The validation-selected operating threshold is **0.36**. I use fixed probability ranges rather than quantiles for the final suitability classes.

| Suitability class | Probability range | Area (km²) | Share |
|---|---|---:|---:|
| Low | p < 0.36 | 715.13 | 81.53% |
| Moderate | 0.36 ≤ p < 0.50 | 76.49 | 8.72% |
| High | 0.50 ≤ p < 0.70 | 48.26 | 5.50% |
| Very High | p ≥ 0.70 | **37.27** | **4.25%** |

Only **4.25%** of the valid prediction domain reaches probability ≥0.70. I keep that scarcity visible rather than lowering the threshold to make the map look more dramatic.

## What seems to matter most

<p align="center">
  <img src="assets/figures/R5_Feature_Importance.png" alt="Feature importance for the Enugu Extra Trees model" width="90%">
</p>

Population density is the strongest model predictor, followed by distance to recurring surface water and elevation.

Feature importance tells us which variables the model relied on. It does **not** prove that those variables caused urban expansion.

## How I rebuilt the experiment

1. Audited the earlier labels, predictors and validation design.
2. Identified leakage from administrative variables and an unfair separation between positive and negative samples.
3. Reconstructed the 2020→2025 labels.
4. Limited the experiment to comparable non-built pixels within the same **30–90 m near-urban support**.
5. Removed distance-to-built and other fields that could leak spatial identity into the model.
6. Created spatially separated Train, Validation and Test blocks.
7. Compared Extra Trees with a simple urban-proximity baseline.
8. Locked the evaluation before refitting the final model on Train + Validation.
9. Produced the final probability and fixed-threshold suitability maps.
10. Quantified the high-confidence area instead of changing thresholds for presentation.

Full methodology: [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md).

## What this means for planning

The final surface is best used as a **near-urban screening layer**. It highlights places that look more similar to the kinds of locations that actually expanded between 2020 and 2025.

It is not a planning approval map, a causal model or a guaranteed forecast of future development. Before any site-level decision, the result should be combined with planning policy, infrastructure capacity, environmental constraints, land tenure and field verification.

## Reports and outputs

- [Final technical report — PDF](reports/Enugu_Final_Technical_Report.pdf)
- [Final technical report — DOCX](reports/Enugu_Final_Technical_Report.docx)
- [`assets/maps`](assets/maps/) — final maps
- [`assets/figures`](assets/figures/) — model and uncertainty figures
- [`data/tables`](data/tables/) — summary tables

## Tools

Python · scikit-learn · GeoPandas · Rasterio · Pandas · GIS · Remote sensing · Spatial validation

## Author

**Abdullah Abdazeez Ayomide**  
Geospatial Planner · GIS & Remote Sensing Analyst · Urban & Environmental Planning Researcher

[GitHub](https://github.com/Abdullahabdazeez) · [LinkedIn](https://ng.linkedin.com/in/abdazeez-abdullah-4b814719a)

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff).
