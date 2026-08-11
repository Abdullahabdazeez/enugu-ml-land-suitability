METHODOLOGY

The reconstructed experiment addresses near-urban expansion in Enugu State between 2020 and 2025. The original case-control design was rejected after forensic auditing showed that administrative variables and distance-based sample construction could almost directly encode the target. The corrected design retains all accepted observed expansion pixels and compares them with stable non-built controls located within the same 30–90 m proximity support to 2020 built-up land.

Seven baseline/static predictors were retained: elevation, slope, distance to road, distance to recurring surface water, distance to drainage, 2020 population density, and baseline 2020 land cover. Distance to 2020 built-up was excluded from the ML predictor set and used only as a trivial benchmark.

Spatial blocks were used to separate Train, Validation and Test partitions. Extra Trees was fitted on Train data, the classification threshold was selected using Validation only, and the spatial Test blocks were used once for final independent evaluation. The final probability surface was subsequently refit using Train + Validation while preserving the R3G Test metrics as the authoritative held-out evidence.

The operating threshold is 0.36. Final map classes use fixed numerical thresholds rather than quantiles: Low < 0.36; Moderate 0.36–<0.50; High 0.50–<0.70; Very High >=0.70.
