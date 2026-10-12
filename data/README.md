# Data status and schema / 数据可用性

Only one limited source-table transcription is in this repository: `derived/1987_meteorology_5min.csv` (+ provenance). **No complete experimental raw concentration datasets have been secured.**

`raw/`: authorized original observations with checksums, rights, sample definitions, unmodified content (currently empty).  
`derived/`: documented tabular transcription / authorized digitization with extraction method and uncertainty.  
`results/`: future simulated-vs-observed evaluation artifacts; never place model predictions in raw experimental datasets.

Proposed observation schema:
`experiment_id,station_id,time_start,time_end,time_zone,x_m,y_m,z_m,species,measurement_basis,value,unit,uncertainty,detection_limit,censor_flag,source_id,source_locator,extraction_method`.

Rules: no default `0` for missing; preserve below-detection flags; keep Bq/m³ air distinct from Bq/L water and Bq/kg dry mass; document sampler height, wind direction convention, time zone, local coordinate system. Generated data must be labelled model/synthetic, **not** observation. Publishing bulk data needs rights assessment.
