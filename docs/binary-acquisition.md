# 二进制原件获取和授权核查（2026-10-22）

**重要发现：** GitHub API 复核 `RRain001/Academic-Experiments` 当前为 **PUBLIC**。此前误认为私有仓库的说法不成立。公开仓库不应直接复制没有再分发许可的第三方原文。

**本次已完成的工作**：对外部来源重新核实、明确直链、将 NOAA 档案官方 SHA-256 与许可状态登记至 [binary_sources.json](../sources/binary_sources.json)，建立可在有互联网的本机或 CI 环境运行的 [下载+校验脚本](../scripts/fetch_reference_materials.py)。**结果更新（2026-10-22）**：本地工作容器对外部服务器下载失败，但 GitHub Actions 已通过官方 EPA 站点获取并验证 **3 份 ZIP**，且将实际文件与计算出的 SHA-256 提交到 GitHub 分支。NOAA JU2003 下载返回 HTTP 403；JAEA、MUST 和 Copenhagen 未向公开仓库镜像。参见 [验收清单](../sources/binary-acquisition-results.md)。

## 各来源的访问与授权

| 资料 | 核实结果 | 公共仓库存档 |
|---|---|---|
| Chalk River 1994 `JAERI-Data/Code 99-022` | JAEA 目录可检索，PDF 正式直链明确，下载出现连接错误 | **否**：JAEA 条款保留版权并限制复制 |
| Canada 1992 `JAERI-M 94-065` | PDF 直链明确，下载出现连接错误 | **否**：JAEA 同上 |
| Prairie Grass `pgrass.zip` | 美国 EPA 官方页面的 **ZIP 直链**已确认，不是只有入口页 | 检查包内第三方资料与元数据后可考虑 |
| Kincaid SF₆ `kinsf6.zip`、SO₂ `kinso2.zip` | 美国 EPA 官方 ZIP 直链已确认 | 同上 |
| Prairie Grass Volume I | HARMO 提供美国空军原始实验报告 PDF | 原报告与附图权属需确认 |
| MUST 2001 `MUSTCustReport.pdf` | 可在线阅读 55 页，但**首页写明仅限美国政府机构分发，其他请求联系 DTRA** | **绝不自动上传/分发** |
| Joint Urban 2003 NOAA ARL-254 | 直接 PDF 61.97 MB，NOAA 官网标注 **CC0 公共领域**，并列官方 SHA256 | **可以公开再分发**；建议避免直接将 62 MB 文件写入普通 Git 历史，可采用 Release asset 或大型文件策略 |
| Copenhagen `Risø-R-1054 rev.1` | 已核实 2002 修订版 75 页直接 PDF，DTU 目录可检索 | 版权归属未确认，暂不公开镜像 |

### 官方许可依据
- [JAEA JOPSS terms](https://jopss.jaea.go.jp/search/common/inter/ereading.html)：报告版权归 JAEA，除法律规定外复制需获许可。
- [EPA Standard Open Data License](https://edg.epa.gov/EPA_Data_License.htm)：EPA 制作数据一般为美国公共领域，但需检查第三方数据与元数据说明。
- [NOAA JU03 资料记录](https://repository.library.noaa.gov/view/noaa/12573)：标记 `CC0 Public Domain`，发布 SHA-256。
- MUST 限制见原报告封面，不能仅以互联网可打开为由当作无版权/无分发限制。

## 在有网络环境下载与验证

```bash
python3 scripts/fetch_reference_materials.py --list
python3 scripts/fetch_reference_materials.py --default
# 只取一个来源：
python3 scripts/fetch_reference_materials.py --id prairie-grass-epa

# 本地合法的个人研究副本（不执行公开仓库上传）：
python3 scripts/fetch_reference_materials.py --id chalk-river-1994-database --acknowledge-rights
```

下载内容会放在被 `.gitignore` 忽略的 `.cache/reference_materials/<experiment>/`。会检查 PDF 头、ZIP 完整性、SHA256；NOAA 报告额外与原始馆藏公布值比较。运行结果存在相邻 `*.acquisition.json`。脚本**不会自动提交、推送或分发**。

这次 EPA 三份 ZIP 已经从 `LINK_VERIFIED` 升级为 `FILE_ACQUIRED_WITH_SHA256`；其他资料保持相应状态。下载报告 != 已得到机器可读观测数据；仍需数值提取、时空和单位核对后才可用于 CFD 校验。

如果需要将 JAEA / Copenhagen 正文上传 **GitHub 私有仓库**，应先将当前仓库设置为 Private，并核实许可与使用范围；本次不自动修改用户仓库隐私设置。
