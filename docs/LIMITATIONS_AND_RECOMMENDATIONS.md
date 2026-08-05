# Limitations and Planning Recommendations

## Limitations

### Dynamic World transition noise

The target variable depends on satellite-derived land-cover classifications. Apparent built-up gain
or loss can reflect spectral confusion, seasonal variation, mixed pixels or incomplete observation
coverage rather than actual land development.

### Conservative positive labels

The quality-control thresholds improved target reliability but excluded some genuine expansion
that did not satisfy the patch, proximity or support requirements.

### Temporal scope

The model explains transitions observed between 2020 and 2025. Development relationships may
change under future infrastructure investment, policy changes, migration or economic shocks.

### Road-network completeness

OpenStreetMap road data may be more complete in urban centres than in remote locations. Distance
to roads therefore reflects both accessibility and mapping completeness.

### Population uncertainty

WorldPop provides modelled population estimates rather than a complete building- or
household-level census.

### Missing planning variables

The model does not include every factor required for statutory land-allocation decisions. Examples
include:

- land ownership and cadastral status;
- property prices;
- soil-bearing capacity;
- detailed flood-depth modelling;
- protected-area regulations;
- utility-service capacity;
- detailed transport capacity;
- cultural-heritage constraints;
- community preferences.

### Moderate generalisation

The independent spatial test performance was useful but not perfect. The model should therefore be
interpreted as a planning-screening tool rather than a deterministic prediction of future
development.

### Limited high-confidence area

Only a small proportion of applicable land achieved high model confidence. This reinforces the need
for ground verification before planning decisions.

## Planning recommendations

1. Prioritise high-priority zones for detailed local planning and field investigation.
2. Treat very-high-priority zones as focused candidate areas rather than automatic development sites.
3. Require environmental and drainage assessment before development near surface-water systems.
4. Coordinate future road investment with compact-growth and infrastructure-capacity objectives.
5. Protect steep terrain and environmentally sensitive land from poorly controlled expansion.
6. Use moderate-priority zones for longer-term monitoring rather than immediate allocation.
7. Update the model when improved census, road, cadastral and development-permit data become available.
8. Conduct local-scale modelling before neighbourhood or parcel-level planning.
9. Integrate the outputs with flood-risk, agricultural-value and ecosystem-service assessments.
10. Maintain a transparent audit trail of model assumptions, exclusions and confidence levels.
