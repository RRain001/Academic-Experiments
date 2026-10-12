# Unresolved source discrepancies / 数据冲突记录

| ID | Status | Issue and evidence | Resolution action |
|---|---|---|---|
| CR94-TOTAL | **BLOCKER** | [Kim et al. 2012](https://doi.org/10.1016/j.jenvrad.2011.08.013) historical Table 1 reports 1994 **8.8e12 Bq**; [IAEA TRS 495 (2025) §4.4.5.3](https://doi.org/10.61092/iaea.0qjt-xo5o) gives **13 TBq**. | Audit [Davis et al. 1995](https://doi.org/10.13182/FST95-A30509), original logs, HT composition and reporting period; **no canonical activity yet**. |
| CR94-GEOMETRY | HIGH | Kim et al. 2012 historical table: **line source 1 m**; complete dimensions/alignment absent. | Obtain full primary setup and coordinates. |
| CR86-SOURCE | HIGH | Kim et al. 2012 Table 1 reports **1986-08-25 15:37–16:07; 6.85e11 Bq; 1 m point source**. Full Brown et al. 1990 paper not yet audited. | Check 1986 original before treating as quantitative boundary condition. |
| CR87-WIND | MEDIUM | [Murata & Noguchi 1997 Table 1](https://www.jstage.jst.go.jp/article/jnst1964/34/2/34_2_176/_pdf) gives time and 'bearing from true north' but not time zone or wind towards/from semantics. | Preserve original times and check direction before using. |
| CR87-OBS | HIGH | JAERI-M 88-232 includes measured tables/figures, but full machine-readable observed station concentrations and uncertainty not yet acquired. | Original numerical records or legally digitized dataset with QC. |
| HT-KINETIC | HIGH | [Brown et al. 1988](https://doi.org/10.13182/FST88-A25296) estimates approx. **1.5%/h effective** HTO appearance; air HTO largely from soil oxidation/reemission. | Do not interpret as direct gas-phase HT oxidation constant. |

No unresolved entry should be deleted until source/page evidence and a reproducible resolution have been added.
