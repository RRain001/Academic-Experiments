# Chalk River experiment overview / 实验概览

Controlled atmospheric **HT (tritiated hydrogen)** releases at Chalk River Laboratories, Canada, in 1986, 1987 and 1994 were designed to study short-range atmospheric transport and the environmental oxidation/redistribution of tritium.

## Causal chain
```text
HT released to near-surface air -> HT plume
  -> uptake/deposition into soil -> soil microbial HT to HTO oxidation
  -> HTO in soil pore-water
     -> HTO reemission into air (secondary atmospheric HTO)
     -> root/leaf-associated TFWT -> plant OBT
```

### Event comparison
| Event | Source and timing | What is supported | Missing |
|---|---|---|---|
| Aug 1986 | Short atmospheric HT release | Primary 1990 paper studies HT soil deposition, HTO reemission, and vegetation response | Complete experiment inputs/observations |
| 1987-06-10 | 3.54 TBq HT, 30 minutes, 1 m point source | JAERI technical report and 1988 papers; 1997 paper gives 6 rows of 5-minute near-ground weather | Full numerical HT/HTO sampling stations and errors |
| 1994-07-27 – 1994-08-08 | Continuous 12-day HT release | HTO and OBT time dynamics, rainfall sensitivity, four plots | Total source activity disputed: 8.8 vs 13 TBq; numerical records |

1987 sources: [JAERI-M 88-232](https://jopss.jaea.go.jp/pdfdata/JAERI-M-88-232.pdf), [Brown et al. 1988](https://doi.org/10.13182/FST88-A25296), [Murata & Noguchi 1997](https://doi.org/10.3327/jnst.34.176). 1994 sources: [Davis et al. 1995](https://doi.org/10.13182/FST95-A30509), [Ichimasa et al. 1995](https://doi.org/10.13182/FST95-A30503). 1986: [Brown et al. 1990](https://pubmed.ncbi.nlm.nih.gov/2298573/).

## Scientific interpretation
- Brown et al. (1988) estimate about **1.5%/h apparent/effective** atmospheric HTO emergence from downwind HTO/HT ratios but attribute much of the HTO to **soil oxidation and subsequent reemission**. **This is not an intrinsic air HT oxidation rate.**
- 1986 HT soil deposition velocities are not HTO deposition parameters.
- Plant **TFWT** and **OBT** evolve at different rates and can use different measurement concentration bases.
- The 1994 controlled exposure must not be confused with routine tritium releases from the facility or later soil legacy measurements (Kim et al. 2012).
- The 1987 short near-surface case is best for staged HT dispersion/soil coupling; the 1994 chronic case is best for TFWT/OBT and rain effects, **after retrieving missing input**.

Useful research connection: quick diagnostic-wind/puff + soil/plant compartments (doctoral Chapter 3), transient CFD scalar + atmosphere/soil boundary models (Chapter 4), only then ROM / multi-fidelity (Chapter 5).
