# Chalk River Tritium Experiments | 恰克河氚释放实验资料库

Research-oriented source registry and validation preparation for the **1986, 1987 and 1994 controlled atmospheric HT releases** at Chalk River Laboratories, Canada.

本仓库长期整理加拿大 Chalk River（恰克河）野外 **HT（氚化氢）** 释放实验文献、经核验的实验设置、可追溯观测数据和多介质模型验证流程。目标是为大气扩散、HT 土壤沉积与氧化、HTO 再释放、植物 TFWT/OBT 动态模型提供**可信、可复现的验证依据**，而不是把文献摘要当作完整实验数据集。

> **Data status (2026-10-12):** Literature and source locations identified; one small 1987 meteorological table transcribed with row-level provenance. **No complete raw observation dataset or validated simulation results are claimed.**  
> **物种提醒：** 原始释放主要是 HT，不是 HTO。不能将 HT 沉积、土壤氧化及二次 HTO 直接当作一次 HTO 排放试验。

## Quick navigation / 导航

| Path | Purpose |
|---|---|
| [docs/experiment-overview.md](docs/experiment-overview.md) | 三次实验的物理过程和关键区别 |
| [literature/README.md](literature/README.md) | 原始论文、报告与可访问链接 |
| [literature/references.csv](literature/references.csv) | 机器可读 DOI/文献索引 |
| [experiments/1986/README.md](experiments/1986/README.md) | 1986 短时释放 |
| [experiments/1987/README.md](experiments/1987/README.md) | 1987 30分钟释放及观测 |
| [experiments/1994/README.md](experiments/1994/README.md) | 1994 连续12天释放 |
| [data/derived/1987_meteorology_5min.csv](data/derived/1987_meteorology_5min.csv) | 从1997论文表1人工转录的6行气象记录 |
| [data/README.md](data/README.md) | 数据状态、单位与溯源政策 |
| [validation/plan.md](validation/plan.md) | 与快速模型、CFD 和多介质模块的验证路线 |
| [validation/acceptance.md](validation/acceptance.md) | 不夸大验证结论的分级验收标准 |
| [sources/discrepancy-log.md](sources/discrepancy-log.md) | 冲突、缺失与尚待核对的信息 |
| [sources/acquisition-log.md](sources/acquisition-log.md) | 文献获取及数据可用性台账 |
| [AGENTS.md](AGENTS.md) | 后续研究人员/AI agent 的事实与提交约束 |

## Experiment snapshot / 实验概览

| Event | Emitted species | Release | Availability |
|---|---|---|---|
| **1986-08** | HT | 短时野外试验；具体参数以原文复核为准 | PubMed abstract; 1990 Health Physics paper |
| **1987-06-10** | HT | **3.54 TBq**, **30 min**, **1 m point source** | JAERI-M 88-232; peer-reviewed papers; 5-min meteorology table |
| **1994-07-27 to 08-08** | HT | **12-day chronic release**; line-source report in a secondary study | 1995 papers; total-activity literature conflict (**8.8 vs 13 TBq**) |

1987 release parameters and 1994 dates are supported by original experiment reports; see [source registry](literature/README.md). **The reported 1994 activity must not be hard-coded until reconciled.**

## Intended use / 与博士研究的关系

- **Fast / low-fidelity:** test the HT atmospheric source/plume independently, then HT deposition → soil conversion → HTO reemission → vegetation. Useful for diagnostic-wind/puff and UFOTRI-like compartment interfaces.
- **High-fidelity:** candidate transient scalar and atmosphere–soil interface benchmark (only after adequate boundary conditions and observations are recovered).
- **Cross-model:** compare predictions to observations separately; do **not** call agreement between two codes experimental validation.
- **Not a graduation dependency:** missing experimental input is documented and can be substituted with independently sourced benchmarks.

## First reproducible asset

`data/derived/1987_meteorology_5min.csv` reproduces the **six rows of Table 1** in Murata & Noguchi (1997), *Journal of Nuclear Science and Technology*, 34(2):176–184, using measured wind speed at **0.9 m**, direction, Pasquill class, and reported roughness height in cm. Source PDF: https://www.jstage.jst.go.jp/article/jnst1964/34/2/34_2_176/_pdf .

The CSV is **not** a complete 3-D meteorological forcing dataset, and no plume concentration series is included yet.

## Reuse and rights / 版权与数据伦理

- The repository includes original summaries, source metadata, URLs, and a small factual table with provenance. It does not redistribute journal PDFs, IAEA PDFs, or the JAERI technical report.
- Publicly readable / free-to-read **does not automatically mean free to redistribute**.
- Measurement digitization, images and full texts require rights review; every admitted dataset must have a source, units, transcription/digitization method and uncertainty notes.
- No licensing claim is made for third-party content. Repository-wide reuse permissions are not declared until a license is chosen by the owner.

This is an evolving **research evidence repository**, not an officially released experimental database.
