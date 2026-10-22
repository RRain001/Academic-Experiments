# 全库获取台账（2026-10-22）

| 实验 | 已确认入口 | 文件已入库 | 下一步 |
|---|---|---|---|
| Chalk River 1986/87/94 | 原论文、JAERI-M 88-232、JAERI-Data/Code 99-022 | 仅 1987 六行气象表 | 1994 数据库逐表核验；1987 站点和 HT/HTO 浓度 |
| Canada 1992 HTO | JAERI-M 94-065 官方 PDF | 否 | 审核地表交换/再释放通量、测量 vs 推导 |
| Kincaid | EPA Kincaid SF6/SO2 ZIP、HARMO | 否 | 下载后盘点文件、每个 trial 的源项/气象/浓度 |
| Prairie Grass | 原始实验报告、EPA ZIP | 否 | 优先形成大气双模型共同 benchmark |
| MUST | Biltoft 报告、同行评审论文 | 否 | 确认可下载数值观测和选定 trial 的几何 |
| Joint Urban 2003 | NOAA 技术备忘录、PNNL 坐标 | 否 | 确认当前数据库访问方式 |
| Copenhagen | DTU 原始观测汇编 | 否 | 提取 20 min 浓度与气象塔数据 |
| Hanford | 67-Series 数据汇编、EPA 归档 | 否 | 选择单一系列/试验日，不混合异构数据 |

**状态口径**：`LINK_VERIFIED` = 已确认机构或期刊入口；`FILE_ACQUIRED` = 已合法获取文件并校验 hash；`NUMERIC_QC` = 数值化+审计；`BENCHMARK_READY` = 源项/气象/监测完整；`VALIDATED` = 独立观测比较已验收。

当前除 1987 一小段转录外，**所有实验原始浓度数据均未作为本仓可复算的完备基准验收**。Chalk River 旧获取记录见 [历史台账](../experiments/chalk-river/sources/acquisition-log.md)。
