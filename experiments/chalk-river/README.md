# Chalk River：1986 / 1987 / 1994 受控 HT 释放实验

**定位**：HT 大气扩散 → 土壤摄取、氧化为 HTO → HTO 再释放 → 植物 TFWT / OBT 动态。该系列实验的**一次释放物为 HT**，不能直接充当 HTO 蒸汽释放实验。

## 导航
- [1986 短时释放](1986/README.md)；[1987 年 30 min 释放](1987/README.md)；[1994 年约 12 天持续释放](1994/README.md)
- [物理过程总览](overview.md) · [主要原始论文与报告](literature/README.md) · [文献 CSV](literature/references.csv)
- [1987 年 5 min 气象表及溯源](data/derived/1987_meteorology_5min.provenance.md)
- [历史获取记录](sources/acquisition-log.md) · [关键矛盾](sources/discrepancy-log.md)
- [原有阶段验证计划](validation-plan.md) · [原有验收口径](acceptance.md)

## 现有证据与阻塞
- 已有：1987 年论文表 1 的六行 5 分钟气象记录（人工转录、有页码溯源），不是原始完整风场。
- 尚无：1986/87/94 全量监测站坐标、逐点 HT/HTO/土壤/植物浓度、误差与完整数字源项文件。
- **1994 总释放量存在 8.8 TBq 与 13 TBq 的二手文献冲突**；解决前不得对总活度归一化数据宣称验收。
- 原始 JAEA 报告以官方链接提供，尚未获得再分发许可，故本仓库不镜像 PDF。

## 特别关注的 1994 数据报告
[JAEA JAERI-Data/Code 99-022（官方 PDF）](https://jopss.jaea.go.jp/pdfdata/JAERI-Data-Code-99-022.pdf)，1999 年，125 页。官方摘要列明气象、土壤、空气 HT/HTO、土壤水 HTO、水表面沉积、蒸散及湍流扩散估算。**报告 PDF 可定位，不代表表格已抽取为机器可读原始观测集**。

与 1992 年加拿大地表 HTO 现场研究不同：后者在 [../canada-hto-1992/](../canada-hto-1992/README.md)，属于另一独立数据来源。

## 模型使用
- 第三章：拉格朗日烟团 + HT 土壤氧化 / 再释放 + 植物箱体动力学；
- 第四章：对已具备几何与气象资料的短时段，验证 URANS 标量输运、双向界面通量；植物和食物链用守恒的动力学耦合模块。
- 不把 CFD 与快速模型的一致性当成野外观测验证。
