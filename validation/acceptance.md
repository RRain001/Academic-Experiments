# Evidence gates / 验收定义

| Gate | Requirement | Current status |
|---|---|---|
| L0 | Primary papers/reports and citation links identified | YES (1986/87/94) |
| L1 | Source/meteorology/sampling geometry and all time conventions independently confirmed | NO |
| L2 | Machine-readable observed concentrations, times, units, detection limits and uncertainty from rights-checked sources | NO (1987 has only 6 met rows) |
| L3 | Reproducible solver configuration, input hashes, conservation and numerical tests | NO |
| L4 | Independent observational comparison with predeclared thresholds and uncertainty | NO |

For comparisons, candidate metrics: `FB = 2(mean(P)-mean(O))/(mean(P)+mean(O))`, `NMSE = mean((P-O)^2)/(mean(P)*mean(O))`, `FAC2 = fraction(0.5<=P/O<=2)` for positive comparable concentrations, plus peak/time-integral error, plant trajectories and mass budgets. **These metrics are not pass thresholds**; define tolerances before inspecting simulation results. Guard zero denominators, censored observations, time alignments and sampling basis. Do not use model-to-model parity as proof of field validity.

1987: L0 + partial manually transcribed source table. 1994: L0 + **release activity blocker**. Model validation outcomes remain **NOT PERFORMED**.
