# Project Abstract

## Machine-Learning-Based Land Suitability Analysis for Sustainable Urban Development — Enugu State, Nigeria

Rapid urban expansion can place pressure on infrastructure, environmentally sensitive land and
existing settlements when development decisions are not supported by reliable spatial evidence.
This project developed a machine-learning-based framework for identifying land with differing
levels of urban development suitability across Enugu State, Nigeria.

A transition-based target was constructed from Dynamic World land-cover observations for 2020
and 2025. Positive samples represented quality-controlled non-built-to-built transitions, while
negative samples represented stable non-built areas located within a defined urban influence
zone. Spatial patch size, neighbourhood support, observation count and distance-to-existing-built
criteria were used to reduce label noise. The data were divided using spatial blocks to prevent
geographical overlap among training, validation and independent test samples.

Seven leakage-safe predictors were used: elevation, slope, distance to roads, distance to recurring
surface water, distance to drainage, population density and baseline 2020 land cover. A predictor
that was also used in target construction—distance to 2020 built-up land—was removed following a
formal leakage audit. The final Extra Trees model achieved an independent spatial test ROC-AUC of
0.7517, an F1 score of
0.7324 and balanced accuracy of
0.7111.

Statewide prediction identified 531.76
km² of high or very-high suitability. After accounting for model confidence, approximately
392.83 km² was classified as high planning priority, while only
0.37 km² met the strict very-high-priority criteria.
Road accessibility was the dominant model predictor, followed by population density, proximity
to recurring surface water and elevation.

The outputs provide a screening-level decision-support framework for strategic urban planning.
They should support, rather than replace, detailed site investigation, statutory planning review,
environmental impact assessment and local stakeholder consultation.
