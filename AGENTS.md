# AGENTS.md — academic field experiment evidence rules

This repository is a **bibliographic/evidence + benchmark preparation project**, not an OpenFOAM/CTEAS solver repository. Scope: Chapters 3 and 4 nuclear environmental multiphase/multimedia tritium validation, including non-tritium atmospheric tracer benchmarks.

1. **Do not invent observations**: numeric activity, concentration, timestamps, sampling coordinates, emission rates, meteorology, uncertainty, test results or rights must be traceable to page/table/official archive.
2. Distinguish `SOURCE_IDENTIFIED`, `FILE_ACQUIRED`, `TABLE_TRANSCRIBED`, `QC_PASSED`, `BENCHMARK_READY`, and `EXPERIMENTALLY_VALIDATED`; link/abstract never implies acquisition.
3. **HT is not HTO**: soil microbial HT oxidation and secondary HTO release differ from direct HTO primary emission; SO₂ may deposit/react; SF₆ and propylene validate flow/transport only.
4. Keep original/referenced evidence immutable. Preserve Chalk River 1994 **8.8 vs 13 TBq** conflict until original source logs resolve it; do not silently adopt either.
5. Treat 1992 Canadian HTO field observations as an **independent environmental study**, including Chalk River/Pickering sites, not automatically a controlled source trial.
6. Separate observations, transcriptions, synthetic tests, solver outputs and parameter-fitted subsets; no calibration/test leakage. Model–model parity ≠ field validation.
7. Ingest case requires source geometry/rate and uncertainties, sampling coordinates/time windows, wind conventions and time zone, topography/roughness, applicable chemistry/deposition assumptions, QC/rights and SHA256. If critical input missing, fail closed.
8. For CFD, report URANS closure, boundary meteorology, mesh/time-step independence, field initialization, concentration windowing, tracer mass and air–soil interface conservation. Compare URANS means with averaging-compatible observations, not individual turbulent spikes.
9. Keep primary DOI/publisher and official government/institution archive links; do not commit copied journal PDFs without redistribution permission.
10. Changes to literature indexes and datasets require provenance, auditable file status, date and a concise updated issue/roadmap entry. Don't delete original Chalk River context.
11. User's fourth chapter priority is integrated atmosphere–soil–plant–food-chain dynamics, not a WRF vs CALMET driver contest. Meteorology can come from suitably verified observation-based ABL boundary conditions.
12. No model result may be labeled PASS until independent experimental observations and predeclared quantitative acceptance criteria have been tested.

Navigation: [README](README.md) · [validation matrix](validation/matrix.md) · [plan](validation/roadmap.md) · [catalog](sources/catalog.csv).
