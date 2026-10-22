# 全库开放问题 / blockers

| ID | 等级 | 内容 | 解决路径 |
|---|---|---|---|
| CR94-TOTAL | BLOCKER | 1994 HT 总量存在 **8.8 vs 13 TBq** 文献差异 | 审核原始 Davis 1995、JAERI 99-022 与试验记录，未核实前不得使用唯一值 |
| CR87-OBS | HIGH | 1987 只有转录的 6 行气象数据，不含完整采样/浓度/误差 | 从 JAERI-M 88-232 提取，并与许可状态同时审查 |
| CA92-MEAS | HIGH | 1992 报告所列地气通量需分辨直接测量、估算和参数反演 | 逐表建立 observation-vs-derived 标签 |
| KIN-DATA | HIGH | EPA ZIP 中真实观测、预处理及模型评估产物边界未审计 | 下载校验并构建字段字典 |
| PG-DATA | HIGH | 不同归档版本的浓度、稳定度、SO₂ 地表吸收处理待核对 | 选定试验事件与采样窗 |
| MUST-ACCESS | HIGH | 完整原始数据是否可直接下载、具体 trial 权限不明 | 联系原报告数据归档 |
| JU03-ACCESS | HIGH | 公开的历史数据库访问链接可能已失效 | 查 NOAA/PNNL/Dugway 当前可访问渠道 |
| CFD-MET | HIGH | 单站气象是否足以约束复杂厂址 3D URANS 侧边界 | 多高度/多站观测检验及计算域敏感性 |
| CHAIN-DOSE | HIGH | 已列试验不直接构成人体食物链及剂量的独立实验验证 | 补充农产品转移、剂量基准，不凭空宣称全链条 PASS |

[旧 Chalk River 原始矛盾记录](../experiments/chalk-river/sources/discrepancy-log.md)保留，且权威性高于本概览的简写。每次解决问题需给出来源页码与处理前后证据。
