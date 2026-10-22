# 2026-10-22 EPA 原始评价 ZIP 实际入库验收

执行系统：[GitHub Actions：Acquire open field-study references](https://github.com/RRain001/Academic-Experiments/actions/workflows/acquire-open-references.yml)；本次实际下载目录为 `experiments/<experiment>/data/raw/open/`，每份同名 `*.source.json` 内有来源、计算 SHA-256、时间和 ZIP 成员样例。

| 文件 | bytes | ZIP 条目 | SHA-256（GitHub Actions 实际计算） | 归档 |
|---|---:|---:|---|---|
| [pgrass.zip](../experiments/prairie-grass/data/raw/open/pgrass.zip) | 350105 | 26 | `0f97645619b8fe6a54e27f1b8671817b2eb42040323e2165ceab4e5ac89535db` | **FILE_ACQUIRED_WITH_SHA256** |
| [kinsf6.zip](../experiments/kincaid/data/raw/open/kinsf6.zip) | 3129058 | 375 | `8b645ac7c4dbbc126a315124d4bf7bb8863077b25f06155bca17bc00d2445470` | **FILE_ACQUIRED_WITH_SHA256** |
| [kinso2.zip](../experiments/kincaid/data/raw/open/kinso2.zip) | 5652319 | 39 | `5ad6ed75891da9b6751b20e54652ae6026ac4131092ef2aee56aa91bcf7afe36` | **FILE_ACQUIRED_WITH_SHA256** |

三 ZIP 源自 [US EPA 官方 AERMOD 评估数据库](https://www.epa.gov/scram/air-quality-dispersion-modeling-preferred-and-recommended-models)。脚本对整个 ZIP 的每个成员执行 CRC 验证，校验记录见各 `*.source.json`。这里的 SHA-256 是**下载字节的实际散列**，并非来自 EPA 另行公布的标准哈希。

**注意**：EPA 发布的是 *model evaluation input/output package*；包内含 AERMET/AERMOD 气象输入、模型输出、评价文件等。文件存在和 ZIP 完整，**不等于其中每项都是现场实测观测，也不等于能立即作为论文独立验证数据集**。

## 尚未入库
- **NOAA JU2003 官方 PDF**：馆藏 [CC0 + SHA-256](https://repository.library.noaa.gov/view/noaa/12573) 已核实，下载实际返回 `HTTP 403`，故未计算新的散列或存入库。
- **Chalk River 1994 / Canada 1992 JAEA**：官方 PDF 可定位，但 JAEA 网站保留版权，本公开仓库不镜像；本地工作环境也未取得原件。
- **MUST 2001**：报告封面明确限制分发对象，不自动下载或上传。
- **Copenhagen**：观测汇编可在线核实但再分发许可未确认，未入库。
- **Prairie Grass Volume I**：报告 PDF 已核实可在线访问但暂未镜像，EPA ZIP 已入库。

其余来源与权限说明参见 [docs/binary-acquisition.md](../docs/binary-acquisition.md)。本页反映实际 GitHub 提交和下载日志，不宣称独立数值验证 PASS。
