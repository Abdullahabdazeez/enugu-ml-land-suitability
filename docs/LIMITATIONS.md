LIMITATIONS

1. The model predicts observed near-urban expansion under the reconstructed 2020–2025 experiment; it should not be interpreted as causal probability, planning approval, or a universal land-suitability score.
2. Independent spatial Test performance is moderate rather than near-perfect: ROC-AUC 0.727, PR-AUC 0.332, and balanced accuracy 0.661.
3. Extra Trees improves discrimination relative to the distance-only benchmark, particularly PR-AUC (+0.142), but the distance baseline retains slightly higher threshold-dependent balanced accuracy (0.669 vs 0.661). Therefore the correct claim is added discrimination, not superiority on every metric.
4. The redesigned target is restricted to a 30–90 m near-urban support. Results should not be extrapolated to the entire state or to locations outside the prediction domain without further validation.
5. Feature importance measures model usage, not causality. Population density, water proximity and elevation should therefore be interpreted as predictive associations.
6. High-confidence p>=0.70 predictions remain sparse: 37.27 km² (4.25% of the valid prediction domain). This result should be reported explicitly rather than hidden by lowering the threshold.
7. The experiment is based on available 2020/2025 land-cover and environmental data; uncertainty in source data propagates into the labels and model outputs.
