# Machine-Learning-Based Near-Urban Expansion Suitability — Enugu State, Nigeria

## Overview
This project evaluates where near-urban land in Enugu State showed characteristics associated with observed 2020–2025 urban expansion. The final workflow was rebuilt after a methodological audit identified target leakage and an unfair distance-based control design.

**Research question:** Among comparable near-urban pixels within 30–90 m of existing 2020 built-up land, can environmental, accessibility, population and baseline land-cover variables distinguish locations that transitioned to built-up by 2025?

## Method
The final Extra Trees model uses seven leakage-safe predictors: elevation, slope, distance to roads, distance to recurring surface water, distance to drainage, 2020 population density and 2020 baseline land cover. Urban proximity was excluded from the ML predictors and used only as a benchmark. Train, Validation and Test sets were separated by spatial blocks.

## Key Results
- Independent spatial Test ROC-AUC: **0.727**
- Independent spatial Test PR-AUC: **0.332**
- Balanced accuracy: **0.661**
- Distance baseline ROC-AUC: **0.707**
- Distance baseline PR-AUC: **0.190**
- ML gain over distance baseline: **+0.020 ROC-AUC** and **+0.142 PR-AUC**
- Very High probability (p>=0.70): **37.27 km² (4.25%)**

## Interpretation
The clean ML model adds useful ranking/discrimination beyond simple proximity to existing urban development, especially under PR-AUC, but does not dominate the baseline on every threshold-dependent metric. High-confidence predictions remain spatially limited, which is treated as a substantive result rather than hidden through threshold adjustment.

## Planning Relevance
The probability surface can support exploratory urban-growth monitoring and prioritization of near-urban locations for further planning assessment. It should be combined with planning policy, infrastructure capacity, environmental constraints and field verification rather than used as a stand-alone development approval tool.
