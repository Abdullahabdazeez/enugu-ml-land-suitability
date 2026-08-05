# Colab workflows

## Recommended publication notebook

`Project_7_Enugu_ML_Land_Suitability_Reproducible.ipynb`

This is the cleaned execution path for public use. It retains the final corrected analytical stages and removes superseded recovery attempts caused by temporary Earth Engine authentication, asynchronous export and Google Drive mount issues.

Before running, set the `EE_PROJECT` environment variable to a Google Earth Engine Cloud Project available to your account. Google Drive and Earth Engine authentication are required.

The original development notebook is retained in the author's master project archive and is not included in this lightweight GitHub package.

## Validation scope

The cleaned notebook passed static Python syntax checks across all retained code cells. Full execution was not performed in the packaging environment because it requires Google Colab, Earth Engine authentication, asynchronous cloud exports and the project files stored in the author's Google Drive.
