FINAL INTERPRETATION LOCK

This reconstructed project supersedes the earlier leakage-contaminated modelling interpretation.

Authoritative independent spatial Test:
- Extra Trees ROC-AUC: 0.726728
- Extra Trees PR-AUC: 0.331873
- Extra Trees Balanced Accuracy: 0.661367
- Distance baseline ROC-AUC: 0.706780
- Distance baseline PR-AUC: 0.190279

Extra Trees improves ROC-AUC by +0.019948 and PR-AUC by +0.141594 relative to simple urban proximity. It does not outperform the baseline on every threshold-dependent metric, so final public language must say that ML adds predictive discrimination beyond proximity, not that it universally dominates the baseline.

The final map uses fixed thresholds and no quantile classification. The p>=0.70 high-confidence class covers 37.2672 km² (4.2487% of the valid prediction domain). The spatial scarcity of high-confidence predictions is an important result and belongs in the abstract, results and discussion.

Forbidden public claims:
- near-perfect model performance;
- random-CV-only validation;
- distance-to-built as an ML predictor;
- Positive_Component_ID / coordinates / raster indices as predictors;
- causal probability;
- universal statewide suitability;
- arbitrary lowering of the 0.70 high-confidence threshold.
