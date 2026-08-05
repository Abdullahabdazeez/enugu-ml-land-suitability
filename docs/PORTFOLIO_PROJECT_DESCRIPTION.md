# Portfolio Project Description

## Machine-Learning-Based Land Suitability Analysis for Sustainable Urban Development — Enugu State, Nigeria

### Project overview

This project developed a spatial machine-learning framework for identifying land suitable for
sustainable urban development across Enugu State. Rather than relying exclusively on subjective
weighted-overlay scores, the model learned from quality-controlled urban land transitions observed
between 2020 and 2025.

### Problem

Urban growth can expand into environmentally sensitive, inaccessible or physically constrained
locations when development decisions lack reliable spatial evidence. A defensible planning model
must distinguish predicted expansion pressure from genuine suitability and must communicate model
uncertainty.

### Approach

I prepared terrain, land-cover, transport, hydrological and population predictors and aligned them
to a common 30-metre raster grid. Urban-gain labels were derived from Dynamic World observations
using observation-count, patch-size, proximity and neighbourhood-support rules.

Balanced samples were separated using non-overlapping spatial blocks. Four candidate algorithms
were assessed. A formal leakage audit identified that distance to existing built-up land had also
been used to construct the labels. I removed this circular predictor and rebuilt the final model
using seven leakage-safe variables.

The selected Extra Trees classifier was assessed against a completely independent spatial test set.
I then generated statewide expansion probability, environmental applicability, suitability,
uncertainty, confidence and confidence-adjusted planning-priority surfaces.

### Key results

- Independent spatial test ROC-AUC: 0.7517
- Independent spatial test F1 score: 0.7324
- Independent spatial test balanced accuracy: 0.7111
- Planning-applicable land: 6,050.85 km²
- High and very-high suitability: 531.76 km²
- High planning priority: 392.83 km²
- Very-high planning priority: 0.37 km²
- Strongest predictor: distance to roads

### Skills demonstrated

- GIS and spatial analysis
- Remote sensing
- Raster processing
- Machine learning
- Spatial sampling
- Target engineering
- Data-leakage detection
- Independent spatial validation
- Model uncertainty analysis
- Explainable machine learning
- Urban and regional planning
- Scientific cartography
- Reproducible project documentation

### Software and tools

- Python
- Google Colab
- Google Earth Engine
- GeoPandas
- Rasterio
- NumPy
- pandas
- scikit-learn
- Matplotlib
- OpenStreetMap
- Git and GitHub

### Planning significance

The final priority surface separates areas that are merely predicted to experience urban expansion
from locations that are simultaneously suitable, environmentally applicable and supported by
stronger model confidence.
