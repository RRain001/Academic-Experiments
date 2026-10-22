# Validation roadmap / 外部实验验证路线

Research target: **fast atmospheric dispersion + soil/plant compartments** (CTEAS-Atmos / UFOTRI-like models, PhD Ch.3), **dynamic CFD + atmosphere/soil interface** (OpenFOAM, Ch.4), optional ROM/multi-fidelity (Ch.5). Keep measured-vs-model comparisons distinct from code-to-code comparisons.

## V0. Source/data readiness (must pass first)
Versioned case manifest needs experiment_id, released species/activity/profile, source height/geometry, meteorology and directional convention, sampling station geometry and averaging intervals, time zone, physical measurement units/basis and uncertainty, dataset checksum, rights and source page/table. Missing required fields are declared BLOCKED, never silently guessed.

## V1. 1987 atmospheric HT dispersion
Use reported 3.54 TBq/30 min 1 m HT source and verified wind data where relevant. First validate HT passive transport at actual monitoring sites/sampling windows; compare time-resolved and integrated concentrations **only after acquiring numerical measurements**. Report scatter, factor-of-two agreement, normalized mean squared error, fractional bias and timing error where sufficient observations exist. Check atmospheric stability, spatial roughness, wind from/toward convention, measurement support and source height before tuning.

## V2. HT uptake and soil oxidation
Add HT-to-soil interface flux and soil conversion to HTO. Check HT & HTO activity balance, soil profiles, depth/time response, soil HTO losses, inventory versus published observation. No HT-to-HTO gas-phase shortcut to match a secondary HTO plume.

## V3. Secondary HTO and reemission
Couple soil HTO to reemission flux then advect in air. Compare late-time HTO concentrations and integrated budgets; retain rainwater uncertainty and do not default to zero precipitation. Test conservation and temporal lag.

## V4. Plant TFWT and OBT
Compare TFWT and OBT series with sample-specific basis and uncertainty. 1987 plant observations where accessible, then 1994 long-exposure crop plot after **8.8 vs 13 TBq** activity is resolved. Preselect fitting vs independent test windows and quantify parameter identifiability.

## V5. High-fidelity CFD / model hierarchy
Use CFD passive-scalar and interface flux after actual boundary/sampler geometry is known. Unresolved fine-scale meteorology limits conclusions. Hold out sites/periods for surrogate/multi-fidelity evaluations; CFD-to-surrogate agreement ≠ experiment validation.

## Reproducible case deliverables
`case_manifest.yml`, observation source and hashes, input transforms, code commit, compiler/solver settings, mass balance, model outputs interpolated to sampler support, observed/predicted pair table, uncertainty-aware metrics and plots, documented failure conditions. **No numerical PASS until independent observations exist.**
