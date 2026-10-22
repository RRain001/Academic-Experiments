# MUST — Mock Urban Setting Test（2001）

**定位：第四章建筑解析 CFD 首选外部基准。** 2001 年美国 Utah Dugway Proving Ground，**12 × 10 = 120 个集装箱**形成约 200 m × 200 m 的规则模拟城市；单个集装箱约 12.2 × 2.42 × 2.54 m。示踪物为**丙烯（propylene）**，并非氚。

共 68 次试验，其中 63 次连续释放、5 组脉冲试验（每组可能含多个脉冲）。实测含浓度、气象和局地流动信息；高频浓度不应直接与 URANS 的瞬时湍流脉动逐点比较。

## 资料
- [2006 年同行评审研究：MUST 模型对照与试验说明](https://journals.ametsoc.org/view/journals/apme/45/10/jam2410.1.xml)。
- [原试验报告（Biltoft / MUST）](https://my.mech.utah.edu/~pardyjak/documents/MUSTCustReport.pdf)。
- [公开 CFD benchmark 示例：MUST trial 2681829](https://cerfacs.fr/wp-content/uploads/2021/06/Rochoux_2021_Large_eddy_simulation_multi_model_comparison_of_the_MUST_trial_2681829.pdf)。

## 第四章验证
1. 先从单次 trial 获取可复算的容器坐标、源项、气象初边值、观测站与平均窗口。
2. 无示踪被动流动：ABL 入口/壁面与站点风速验证。
3. OpenFOAM URANS + 瞬态丙烯标量：时间窗平均浓度、归一化浓度、峰值到达时刻/尾流滞留。
4. 不将丙烯结果用于论证 HT/HTO 传质、OBT 或人体剂量。

**数据状态**：试验与论文档案已找到；完整原始机器可读试验集及获取许可仍需确认，L0。

## 2026-10-22 权利状态补充

**原 2001 MUST Customer Report 封面写有 `Distribution authorized to U.S. government agencies only; other requests ... Defense Threat Reduction Agency`。** 已公开出现 PDF 不代表允许公开 GitHub 重新分发；当前公开仓库只登记 DOI/直链和实验概要，若要进一步拿到完整试验数据库应联系授权机构。资料获取脚本不自动下载这份受限报告。
