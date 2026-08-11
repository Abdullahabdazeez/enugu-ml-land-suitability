# Release Notes — v2.0.0

This release replaces the earlier Enugu modelling interpretation after a forensic methodological review.

## Main corrections

- Removed administrative and spatial-index leakage variables.
- Reconstructed the authoritative 2020–2025 label semantics.
- Rebuilt the eligible modelling population.
- Removed the original distance-driven control-selection bias.
- Reformulated the task as a near-urban transition problem using comparable 30–90 m candidate locations.
- Excluded distance-to-built-2020 from Extra Trees and retained it only as a benchmark.
- Used spatially separated Train, Validation and independent Test blocks.
- Added direct Extra Trees vs urban-proximity baseline benchmarking.
- Rebuilt probability and suitability surfaces using fixed probability thresholds.
- Retained the sparse p≥0.70 result rather than lowering the threshold for presentation.
- Repaired map axis-label / footnote collisions.

## Authoritative independent spatial Test

- Extra Trees ROC-AUC: 0.726728
- Extra Trees PR-AUC: 0.331873
- Extra Trees balanced accuracy: 0.661367
- Distance baseline ROC-AUC: 0.706780
- Distance baseline PR-AUC: 0.190279

## High-confidence result

p≥0.70 covers 37.2672 km², equivalent to 4.248669% of the valid prediction domain.

The validated interpretation is that Extra Trees adds predictive discrimination beyond simple proximity, while not outperforming the baseline on every threshold-dependent metric.
