# Project Report: Near-Urban Expansion Suitability in Enugu State

## Background

Urban expansion is easier to model when the comparison is fair. In an earlier version of this project, some variables and sampling choices gave the model clues that were too close to the answer itself.

I rebuilt the experiment to ask a narrower and more useful question: among locations already close to the 2020 urban edge, can baseline environmental and accessibility conditions help distinguish places that became built-up by 2025 from similar places that remained non-built?

## What I did

I reconstructed the 2020-2025 labels, removed variables that could leak spatial identity or future information, and limited the analysis to a comparable **30-90 m near-urban support**.

The final Extra Trees model uses seven predictors: elevation, slope, distance to roads, distance to recurring surface water, distance to drainage, 2020 population density and baseline 2020 land cover.

Distance to the 2020 built-up edge is not used as a model predictor. I keep it only as a simple benchmark so I can see whether machine learning adds anything beyond proximity alone.

The evaluation uses spatially separated Train, Validation and Test blocks.

## What I found

On the independent test data, Extra Trees achieved:

- **0.7267 ROC-AUC**;
- **0.3319 PR-AUC**;
- **0.6614 balanced accuracy**; and
- **0.3368 F1**.

The distance-only baseline achieved **0.7068 ROC-AUC**, **0.1903 PR-AUC**, **0.6689 balanced accuracy** and **0.2937 F1**.

The ML model therefore adds useful discrimination, especially in PR-AUC, but it does not outperform the simple baseline on every metric. I keep that mixed result visible rather than describing the model as uniformly superior.

## Suitability pattern

The validation-selected operating threshold is **0.36**. The final classes use fixed probability ranges rather than quantiles.

Only **37.27 km², or 4.25% of the valid domain**, reaches probability >=0.70 and is classified as Very High suitability.

That high-confidence area is sparse. I treat the scarcity as a meaningful model result instead of lowering the threshold to make the map look fuller.

## What the model appears to use most

Population density is the strongest predictor, followed by distance to recurring surface water and elevation.

Those importance values show how the model separates cases. They do not prove that any of those variables caused urban expansion.

## What the result means

The final map is best used as a **near-urban screening layer**. It highlights places whose baseline conditions look more similar to the locations that actually transitioned to built-up land between 2020 and 2025.

It is not a planning approval map and it is not a deterministic forecast. A site that receives a high model probability still needs to be checked against planning policy, infrastructure capacity, environmental constraints, land tenure and field conditions.

## Why the rebuild matters

The most useful part of the project was identifying and removing shortcuts that could make a model look stronger than it really is. Spatial prediction is especially vulnerable to that problem because nearby samples often share information.

A slightly weaker but fair evaluation is more useful than an impressive score produced by leakage.

## What I would add next

The next step would be to test the model on a later time period or another urban area without changing the modelling rules. That would show whether the learned relationships travel beyond the current experiment.

More detailed infrastructure, land-price, zoning and development-control data could also improve the planning interpretation.

## Main outputs

Maps are in [`assets/maps`](../assets/maps/), model figures in [`assets/figures`](../assets/figures/), and tables in [`data`](../data/).

## Final note

The purpose of the model is not to predict every future building. It is to identify a defensible spatial signal and be clear about how strong that signal actually is.
