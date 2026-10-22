# 实验可复算数据契约（适用于所有子实验）

## 1. Case manifest（最小字段）
```yaml
experiment_id: "MUST"
trial_id: null
evidence_level: "SOURCE_IDENTIFIED"
release:
  species: "propylene"
  geometry: null
  rate_series_path: null
  source_units: null
  source_reference: null
time:
  timezone: null
  start: null
  end: null
  sampling_window_definition: null
geospatial:
  crs: null
  source_location: null
  terrain_building_geometry: null
meteorology:
  input_path: null
  measurement_heights: []
  wind_direction_convention: null
  stability_or_flux: null
observations:
  file: null
  value_basis: null
  censor_rule: null
  station_geometry: null
  uncertainty: null
provenance:
  official_source_url: null
  citation_page_or_table: null
  raw_sha256: null
  extraction_method: null
  redistribution_permission: "UNRESOLVED"
split:
  calibration_trials: []
  withheld_validation_trials: []
validation:
  predefined_metrics: []
  predefined_thresholds: []
  status: "NOT_RUN"
```

**空值保持 null，切勿填入看似合理的站点坐标、温度或背景值**。`experiment_id`、`trial_id` 应与源数据中事件身份一一映射。

## 2. 推荐观测 CSV
`experiment_id,trial_id,station_id,time_start,time_end,timezone,x_m,y_m,z_m,species,phase,concentration_basis,value,unit,uncertainty,detection_limit,censor_flag,source_document,page_table,method`

不同介质不可混写单位：空气 `Bq/m3`、水 `Bq/L`，植物 `Bq/kg-dry`、`Bq/kg-fresh` 与 TFWT/OBT 的化学水形态要有明确定义。SF₆/丙烯/SO₂ 也可使用 ppm、g/m³ 等原单位，但要保留转换过程。

## 3. 验证/留出原则
- 代码单元测试及与原版模型互比：**numerical verification**，不等于野外验证。
- 使用测量数据反演源项/湍流参数后，应留出独立站点/日期测试，避免数据泄漏。
- 需要比较同一时间支持范围的积分值：一次 20 min 实测不等于 CFD t=1200s 的单点值。
- 1992 地表研究：明确直接仪器测得通量与根据气象梯度估算通量，后者不能作为完全独立的通量真值。
- 1994 源项冲突、未确认采样坐标和未知降水保持阻塞，不得用虚构输入得到可计算样例。
- 外部数据库许可不明确时只提交原文链接和自建元数据；不分发受限原始文件。

## 4. 计算记录（尤其 CFD）
网格与建筑形状、贴壁 y+ / 粗糙度、地形/坐标、URANS 湍流模型、数值离散、时间步/CFL、初始化 spin-up、模拟与墙钟时间、核数、收敛和守恒、观察时间窗口、实测不确定度、失败模式。

## 5. 验收
满足 [统一分级验收](acceptance.md) 且报告当前案例实际字段证据，才可提升到 L2–L4。
