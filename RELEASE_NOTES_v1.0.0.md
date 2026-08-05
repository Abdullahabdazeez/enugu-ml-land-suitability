## First prepared release

This repository presents a machine-learning-based land-suitability assessment for sustainable urban development in Enugu State, Nigeria.

### Included

- Complete staged Google Colab production workflow
- Multi-source terrain, land-cover, accessibility and environmental predictors
- Spatially separated training, validation and independent test design
- Candidate-model evaluation and Extra Trees model selection
- Statewide urban-expansion probability surface
- Planning-constrained probability surface
- Model confidence and uncertainty outputs
- Urban-development suitability classes
- Planning-priority assessment
- High-confidence suitability screening
- Seven final maps and two multi-panel figures
- Final categorical planning GeoTIFFs and statistical tables
- Feature-importance, confusion-matrix and independent-test evidence
- Reproduction and automated repository-validation scripts
- Detailed methodology, limitations and planning recommendations

### Principal findings

- Independent test ROC-AUC: **0.7517**
- Balanced accuracy: **0.7111**
- F1 score: **0.7324**
- Cohen Kappa: **0.4222**
- Planning-applicable area: **6,050.85 km²**
- Planning-constrained area: **1,568.63 km²**
- High-suitability land: **515.09 km²**
- Very-high-suitability land: **16.67 km²**
- High planning-priority land: **392.83 km²**
- Very-high planning-priority land: **0.37 km²**
- High-confidence suitable land: **30.08 km²**

### Interpretation

The outputs provide statewide screening evidence rather than deterministic development approvals. Suitability should be interpreted together with confidence, uncertainty and planning constraints, followed by detailed local feasibility and environmental assessment.
