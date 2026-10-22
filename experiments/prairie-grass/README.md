# Project Prairie Grass：开阔地近地面扩散

1956 年美国内布拉斯加州近 O'Neill 的经典野外实验：**70 次约 10 min 的近地面连续示踪释放**，开阔平坦草原、多气象稳定度，最大弧线距离约 800 m。主要用于短距离浓度和垂直廓线检验；通常使用 SO₂ 数据。

## 资料
- [实验报告 Volume I，HARMO 归档](https://harmo.org/jsirwin/PGrassVolumeI.pdf)。
- [HARMO Prairie Grass 讨论及数据入口](https://harmo.org/jsirwin/PrairieGrassDiscussion.html)。
- [EPA 模型评估数据 ZIP：Prairie Grass](https://www.epa.gov/scram/air-quality-dispersion-modeling-preferred-and-recommended-models)。

## 论文安排
- **第三章 P0**：近地面羽流、稳定度差异、地面水平浓度弧线，作为快速烟团基准。
- **第四章 P0**：无建筑 ABL + 瞬态标量输运、近地面浓度以及独立的网格/边界/时间步验证。
- 注意 SO₂ 存在反应和地表吸收的潜在影响；选择数据集时审查有无沉积校正，不能擅自当作严格惰性。

**数据状态**：官方/归档报告和 EPA ZIP 入口已确认；尚未审计原始采样窗与浓度表，L0。

## EPA 官方数据压缩包的直接下载地址

[Prairie Grass ZIP（pgrass.zip）](https://gaftp.epa.gov/Air/aqmg/SCRAM/models/preferred/aermod/eval_databases/pgrass.zip)，为 US EPA SCRAM 模型评估数据集（官方页面 342 KB），包含模型输入/输出，不应未经辨识直接把模型输出认定为现场观测。此处**只有 verified URL，实际 ZIP 和散列值尚未获得**。
