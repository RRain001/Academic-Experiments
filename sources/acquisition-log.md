# 全库获取台账（2026-10-22）

| 实验 | 已确认入口 | 文件已入库 | 下一步 |
|---|---|---|---|
| Chalk River 1986/87/94 | 原论文、JAERI-M 88-232、JAERI-Data/Code 99-022 | 仅 1987 六行气象表 | 1994 数据库逐表核验；1987 站点和 HT/HTO 浓度 |
| Canada 1992 HTO | JAERI-M 94-065 官方 PDF | 否 | 审核地表交换/再释放通量、测量 vs 推导 |
| Kincaid | EPA Kincaid SF6/SO2 ZIP、HARMO | **是：SF6 与 SO2 两 ZIP；SHA256 + CRC** | 区分真实观测与 AERMOD 模型输出，挑选可复算 trial |
| Prairie Grass | 原始实验报告、EPA ZIP | **是：pgrass.zip；SHA256 + CRC** | 抽取并核对真实观测、气象与源项；报告 PDF 仍未入库 |
| MUST | Biltoft 报告、同行评审论文 | 否 | 确认可下载数值观测和选定 trial 的几何 |
| Joint Urban 2003 | NOAA 技术备忘录、PNNL 坐标 | 否 | 确认当前数据库访问方式 |
| Copenhagen | DTU 原始观测汇编 | 否 | 提取 20 min 浓度与气象塔数据 |
| Hanford | 67-Series 数据汇编、EPA 归档 | 否 | 选择单一系列/试验日，不混合异构数据 |

**状态口径**：`LINK_VERIFIED` = 已确认机构或期刊入口；`FILE_ACQUIRED` = 已合法获取文件并校验 hash；`NUMERIC_QC` = 数值化+审计；`BENCHMARK_READY` = 源项/气象/监测完整；`VALIDATED` = 独立观测比较已验收。

当前除 1987 一小段转录外，**所有实验原始浓度数据均未作为本仓可复算的完备基准验收**。Chalk River 旧获取记录见 [历史台账](../experiments/chalk-river/sources/acquisition-log.md)。

## 2026-10-22 外部二进制资料再核实

本仓库经 GitHub API 确认为 **PUBLIC**。通过公开资料核实 EPA Prairie Grass/Kincaid 的确切 ZIP 文件、NOAA JU2003 PDF 官方 SHA-256（见 `binary_sources.json`）。JAEA 1994 和 1992 PDF 直链已登记但获取失败；MUST 2001 官方报告封面标注仅限美国政府机构分发，不自动下载镜像。**所有新 PDF/ZIP 的实际入库状态仍为 NO；也没有计算新 SHA256。** 下载脚本见 `scripts/fetch_reference_materials.py`，下载后再逐项更新台账，禁止将报告目录当作数值数据验收。

## 2026-10-22 GitHub Actions 实际文件入库结果

三个 EPA ZIP 已在 `docs/source-download-verification-20261022` 分支真正保存：`pgrass.zip`、`kinsf6.zip`、`kinso2.zip`；校验报告见 [binary-acquisition-results.md](binary-acquisition-results.md)。NOAA JU2003 返回 HTTP 403，未获得 PDF。**报告入库不等于观测数据分析可用**。
