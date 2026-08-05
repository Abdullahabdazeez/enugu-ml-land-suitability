# Data and reproducibility

The complete Colab notebook is included in `notebooks/`. It records the production workflow used to acquire, preprocess and model the project data.

The repository publishes the final validation tables, selected browser-safe rasters and planning outputs. Large raw and intermediate datasets are not duplicated because they can be regenerated from the notebook or obtained from their original providers.

Continuous probability, confidence and uncertainty rasters are omitted from the lightweight browser-upload repository because the combined web commit exceeded GitHub's practical upload limit. Their final maps, area statistics and generation workflow remain available. The full rasters are preserved in the author's master deliverables archive and can be regenerated from the included notebook.

Primary inputs documented in the workflow include:

- Copernicus DEM GLO-30;
- Dynamic World land cover;
- Sentinel-2 imagery and derived spectral indices;
- population and built-environment indicators;
- road and accessibility variables;
- environmental constraints;
- administrative boundaries.

Google Earth Engine and Google Drive authentication are required for a full rerun.
