# 第三章/第四章外部实验验证矩阵（2026-10-22）

## 基本准则

- **第三章（快）**：诊断风场 / CALPUFF 风格拉格朗日烟团 → 土壤 HT/HTO → 植物 TFWT/OBT → 食物链/剂量，按观测驱动的长时序工程评价。
- **第四章（精）**：现场实测气象 → OpenFOAM **URANS + HT/HTO 非稳态欧拉输运** → 大气—土壤守恒界面 → 土壤多孔介质 → 植物动力学 → 食物链/剂量；以局地典型时段验证，不要求整个 12 天/全年都连续求解 CFD。
- **验证不是只看浓度拟合**：每个模块分别进行方程/守恒验证、网格时间步收敛、野外独立观测比较；标量与水/活度/植株的单位和采样时间窗不可混用。
- **无氚示踪物只验证大气流动/标量**；不能因 SF₆、SO₂、丙烯浓度吻合就宣称 HT 氧化、HTO 地表交换或植物 OBT 验证通过。
- 以下 P0/P1/P2 表示**研究优先级**，不是资料或模型已经通过验收。

## A. 第三章：快速评价模块

| 模块 | 主验证实验 | 补充实验 | 实测指标 | 方法与失效风险 | 优先级 |
|---|---|---|---|---|---|
| C3-A1 近地面烟团/大气扩散 | [Prairie Grass](../experiments/prairie-grass/README.md) | Hanford Green Glow 子集 | 距离弧线地面浓度、横向分布、气象稳定度 | 检查 SO₂ 沉积与采样窗；不能把不同试验日期拼为一个时序 | P0 |
| C3-A2 高架浮力烟团/抬升 | [Kincaid SF₆](../experiments/kincaid/README.md) | Copenhagen SF₆（无浮力源） | 小时平均/弧线最大浓度、风廓线 | 区分 SF₆ 与 SO₂ 及 buoyant vs nonbuoyant；部分受体超过 5 km | P0 |
| C3-A3 动态浓度、HT→土壤氧化 | [Chalk River 1987](../experiments/chalk-river/1987/README.md) | 1986 | 空气 HT/HTO、土壤 HTO 随时间、后期 HTO | 土壤来源的二次 HTO 不能误当大气中 HT 快速氧化 | P0 |
| C3-A4 土壤—植物 TFWT/OBT | [Chalk River 1994](../experiments/chalk-river/1994/README.md) | 1987 植物 | 土壤水 HTO、植物组织水 TFWT、OBT 时序 | 1994 总源项冲突；鲜重/干重/植物部位基准 | P0 |
| C3-A5 HTO 再释放/界面参数 | [Canada 1992](../experiments/canada-hto-1992/README.md) | Chalk River 1987 | HTO 地气交换通量、浓度梯度、再释放 | 受污染地表自然通量不是已知一次脉冲源 | P1 |
| C3-A6 食物链、剂量 | **未由上述试验独立覆盖** | 需另寻食品活度、畜产品和人体剂量系数证据 | 可食部位活度、摄入率、剂量换算 | 不得凭植物叶片 OBT 直接宣称完整食物链 PASS | 待补 |

## B. 第四章：OpenFOAM 精细评价模块

| 模块 | 主验证实验 | 补充实验 | 实测指标 | 数值验收要点 | 优先级 |
|---|---|---|---|---|---|
| C4-F1 开阔地 ABL + URANS 标量 | [Prairie Grass](../experiments/prairie-grass/README.md) | Copenhagen | 风速/温度廓线、地面与垂向浓度 | 观测气象入口、ABL 壁面一致性、网格/时间步独立、时间窗平均 | P0 |
| C4-F2 建筑绕流、尾流、事故型瞬态 | [MUST](../experiments/must/README.md) | Joint Urban 2003 | 建筑阵列风场、浓度、到达时间与洗出过程 | 首先重建容器坐标，URANS 均值不与未滤波 50Hz 脉动直接比 | P0 |
| C4-F3 高架非浮力/非中性验证 | [Copenhagen](../experiments/copenhagen/README.md) | Kincaid 浮力烟羽（难） | 20 min 平均浓度、气象塔风和湍流 | 非浮力与浮力源区分，外部场范围需覆盖受体 | P1 |
| C4-M1 空气—土壤 HTO 双向传质 | [Canada 1992](../experiments/canada-hto-1992/README.md) | Chalk River 1987 二次 HTO | 地面/近地梯度、HTO 通量、蒸散发、土壤 HTO | 同量纲活度闭合，分清 measured vs derived，边界通量不重记 | **P0** |
| C4-M2 HT 土壤摄取、氧化、二次释放 | [Chalk River 1987](../experiments/chalk-river/1987/README.md) | 1986 | 空气 HT/HTO、土壤 HTO、释放后延迟 | HT 和 HTO 两个组分，土壤氧化为 HTO 不凭空生成活度 | P0 |
| C4-M3 土壤—植物连续动力学 | [Chalk River 1994](../experiments/chalk-river/1994/README.md) | Canada 1992 中合适植物记录 | 土壤含水/HTO、TFWT、OBT/组织部位 | 长时序植物用 ODE/多孔介质模块连续计算；CFD 分段积分气地通量需守恒 | P1 |
| C4-M4 真实城市复杂下垫面 | [Joint Urban 2003](../experiments/joint-urban-2003/README.md) | MUST | 城市街谷浓度、风速及定位 | 需要正确三维几何和独立气象；高成本选做 | P2 |
| C4-M5 系统性跨介质/食物链/剂量 | **多组分阶段拼接验证，不是现成完整独立野外试验** | 另寻长期农业/食品记录 | 组分活度、跨介质通量、剂量 | 全链守恒+数据验证分开披露，缺真实食物链观测不得称全链验证 | 待补 |

## C. 对照设计：避免科学上不可区分的误差

| 对照 | 必须保持一致 | 推荐指标 |
|---|---|---|
| 第三章烟团 vs 野外观测 | 同一释放源、地形/粗糙度、采样坐标、积分区间 | FB、NMSE、FAC2、分位误差、弧线最大值 |
| 第四章 URANS vs 野外观测 | 独立气象驱动、多高度观测、同几何源项与采样窗 | 风 U/V、平均浓度、峰值/到达时间、技能评分 |
| 第三章 vs 第四章 | 同一场址/输入/物种，明确不同时间步与保真度 | 浓度/通量的成本—误差 Pareto，**不是独立实验验证** |
| 大气—土壤界面 | 流入土壤 = 从空气移除的同一活度，源/汇不重复 | 积分通量闭合、不同时间步残差、再释放响应 |
| 土壤—植物 | 统一土壤水、叶水、OBT 的浓度基准与组织 | 时间滞后、积分库存、TFWT/OBT 曲线 |

## D. 观测级数据现状

在提交本版本时，**没有一套实验被标记为 Benchmark Ready**。Kincaid/Prairie Grass 的公开 ZIP 是获取入口；MUST/JU03 的完整数字记录仍需确认；Chalk River 1987 只有六行气象表转录；1994 存在总源项冲突。数据质量和验收门槛见 [data-contract.md](data-contract.md) / [acceptance.md](acceptance.md)。

## E. 精细 CFD 模拟时长不是观测实验的全部长度

- 优先建立稳态 ABL 初始化，再根据事件作 **3–6 h 事故/风向过渡、6–24 h 非稳态交换** 的初始成本评估，具体时长以浓度尾迹和界面通量收敛为准；
- 对 1994 年 **12 天植物 OBT**，可让植物/土壤动力学保持连续积分，而在代表性气象区间运行 URANS；但未模拟 CFD 时段的边界通量需由有依据的模型/观测补足，不可空缺当成零；
- 若研究目标要求完整气象事件，就必须计算充分的时间历程；不能把独立稳态 RANS 的快照拼接当作 URANS。

所有成功标准均须在查看模型预测前冻结，禁止事后改阈值。
