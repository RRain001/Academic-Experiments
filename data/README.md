# 全库实验数据与模型产物管理

**当前数据实物**：唯一明确转录的小数据集为 [Chalk River 1987 六行 5 分钟气象表](../experiments/chalk-river/data/derived/1987_meteorology_5min.csv)（[逐行/原文溯源](../experiments/chalk-river/data/derived/1987_meteorology_5min.provenance.md)）。不是完整原始观测或三维风场。

每个新实验应使用 `experiments/<id>/data/raw/` 存放经授权取得的不可变观测原件，`data/derived/` 存放合法转录/转换结果，`results/` 存放模拟/验证结果（不得写成观测）。本库不承诺、也不预先镜像所有官方 PDF/ZIP。

建模机器可读表建议列：
`experiment_id,trial_id,station_id,time_start,time_end,time_zone,x_m,y_m,z_m,species,phase,basis,value,unit,uncertainty,detection_limit,censor_flag,source_id,page_or_table,method`。

统一要求：缺测不填 0；原浓度单位不擅自转换；源/受体坐标系、时间区间、采样积分窗口、风从向与风去向、量测高度、土壤含水率/植物鲜干质量基准一并记录；保留原文件 SHA-256 与转换日志。

更多见 [验证数据契约](../validation/data-contract.md)。
