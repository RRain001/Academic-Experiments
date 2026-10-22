# Academic Experiments｜大气扩散与氚多介质迁移野外实验验证资料库

用于博士论文第三章（**快速评价：诊断风场—拉格朗日烟团—土壤—植物—食物链—剂量**）和第四章（**精细评价：现场气象驱动 OpenFOAM URANS—HT/HTO 输运—土壤—植物—食物链—剂量**）的**可追溯外部实验资料、数据获取台账、验证矩阵和执行计划**。

> **2026-10-22 资料状态**：已整理 8 组主要野外试验系列 + 1992 年加拿大 HTO 现场研究；**不代表已下载或数字化全部原始实验数据，更没有宣称任何模型实验验证 PASS**。唯一目前仓内明确转录的小型观测文件是 Chalk River 1987 论文中的六行 5 min 气象表，保留逐行溯源和审查限制。所列 JAEA、EPA、NOAA、DTU 等链接为外部资料入口，非仓内副本。

## 实验导航

| 实验 | 主要示踪/介质 | 第三章快速评价 | 第四章 CFD / 多介质 | 档案 |
|---|---|---|---|---|
| Chalk River 1986/87/94 | HT → 土壤 HTO → TFWT/OBT | **P0** HT 氧化与二次释放 | **P0** 土壤/植物时序耦合 | [资料](experiments/chalk-river/README.md) |
| Canada 1992 地表 HTO | 污染地表 HTO、蒸散/界面通量 | P1 双向交换参数 | **P0** 地气 HTO 通量 | [资料](experiments/canada-hto-1992/README.md) |
| Kincaid | SF₆，SO₂（两类数据） | **P0** 高架浮力烟团 | P2 选做高架对照 | [资料](experiments/kincaid/README.md) |
| Prairie Grass | SO₂，近地面释放 | **P0** 近场扩散 | **P0** 开阔地 ABL/标量基线 | [资料](experiments/prairie-grass/README.md) |
| MUST | 丙烯，120 容器阵列 | P2 | **P0** 建筑解析 URANS | [资料](experiments/must/README.md) |
| Joint Urban 2003 | SF₆，城市脉冲/连续释放 | P2 | P1 真实城市扩展 | [资料](experiments/joint-urban-2003/README.md) |
| Copenhagen | SF₆，无浮力高架源 | P1 烟团/稳定度 | P1 ABL 验证 | [资料](experiments/copenhagen/README.md) |
| Hanford | ZnS 等，不同试验系列 | P2 独立附加案例 | P2 多高度扩散 | [资料](experiments/hanford/README.md) |

## 研究方案入口
- **[第三章/第四章验证矩阵](validation/matrix.md)**：实验—模型模块—独立观测量—关键误用风险。
- **[分阶段计划及验收门槛](validation/roadmap.md)**：先拿到可复算数据，再做大气、界面、植物和集成验证。
- [全库统一的验收等级](validation/acceptance.md) · [数据契约与验证规范](validation/data-contract.md)。
- [数据源总台账](sources/catalog.csv) · [获取进度日志](sources/acquisition-log.md) · [未解问题](sources/discrepancy-log.md)。
- [文献总导航](literature/README.md) · [仓库数据说明](data/README.md)。

## 目录
```text
experiments/
  chalk-river/{1986,1987,1994,data,literature,sources,...}
  canada-hto-1992/   kincaid/   prairie-grass/
  must/              joint-urban-2003/
  copenhagen/        hanford/
validation/{matrix,roadmap,acceptance,data-contract}.md
sources/{catalog.csv,acquisition-log,discrepancy-log}.*
literature/README.md
data/{README.md,raw/README.md}
```

旧路径 `experiments/1986` 等保留迁移指引；原有 Chalk River 论文索引、源数据六行表和冲突台账保留在新目录，Git 历史不丢失。**实测数据与模拟结果严格分离**；论文摘要不等于观测数据库，模型之间吻合不等于野外独立验证。

## 第三章与第四章的边界
1. 第三章负责长时序低成本评价，重点用 Kincaid、Prairie Grass 验证大气烟团，再用 Chalk River 验证 HT/HTO 环境过程。
2. 第四章使用 **现场实测气象构造 OpenFOAM URANS 动态边界**，重点用 Prairie Grass 验证开阔地输运、MUST 验证建筑绕流、1992 HTO 与 Chalk River 验证双向界面—土壤—植物。WRF 与诊断风场对 OpenFOAM 的替代驱动研究不作为必需验证项目。
3. 非氚示踪物仅验证空气动力学和被动标量输运，不可以直接证明 HT/HTO 特有化学或生物机制。
4. 高成本 CFD 优先运行可复算的典型时段；跨天至 12 天的土壤—植物动力学可由独立时域求解，但分段耦合须保持积分通量与物质守恒。

## 版权与研究诚信
外部实验原始 PDF/受限数据只登记官方页面；获许可方可入库，记录 SHA256、版本、坐标、单位、时间区间、检测限与来源页码。**公开可读 ≠ 可再分发**。不得捏造观测、时间、源项或 PASS。更多约束见 [AGENTS.md](AGENTS.md)。

## 外部原始资料的实际下载状态

[逐份直链核实、版权风险和下载校验脚本](docs/binary-acquisition.md) · [来源机器清单](sources/binary_sources.json) · [Python 获取脚本](scripts/fetch_reference_materials.py)。**本库当前是公开仓库；不能将仅有官方直链误写成文件已经归档。**
