# Joint Urban 2003（JU2003）：真实城市 SF₆ 扩散

2003 年 7 月美国俄克拉荷马城，**10 个 IOP、29 次约 30 min 准连续释放及 40 次瞬时烟团释放**；约 150 处采样点包括街道、楼顶及 1 / 2 / 4 km 的受体弧线。

## 资料
- [NOAA Technical Memorandum OAR ARL-254：SF6 tracer field tests](https://repository.library.noaa.gov/view/noaa/12573)。
- [PNNL：Study Overview and Instrument Locations，含仪器坐标附录](https://www.pnnl.gov/publications/joint-urban-2003-study-overview-and-instrument-locations)。
- [JU03 数据库设计报告（历史访问说明）](https://ams.confex.com/ams/pdfpapers/99952.pdf)。

**数据访问状态**：实验时存在公开数据库，但历史网址不等于当前仍可访问；当前独立下载验证待做。不得把技术报告当作完整数字原始数据库。

## 第四章价值
复杂街谷、风向切换、城市障碍与脉冲扩散；适合作为 MUST 后的真实性扩展。需要高精度建筑三维几何、稳健的大气边界及成本评估，**不列为第四章首个可运行算例**。

## 前置门槛
优先找原始城市建筑/采样坐标及观测时间窗，确认平均浓度与快响应观测分离；URANS 只与时间平均或模型可解析的过渡过程比较。

## NOAA 原始 PDF 与许可核实

NOAA [官方 PDF 直链](https://repository.library.noaa.gov/view/noaa/12573/noaa_12573_DS1.pdf)（馆藏标示约 61.97 MB），[馆藏资料页](https://repository.library.noaa.gov/view/noaa/12573) 明确标注 **CC0 Public Domain**，并公布 SHA-256：`78c32cc66edf3a7dfe5589c68cfee9fd4e1fed7b18f81becef351d5bea742c9e`。此为**馆藏公布的校验值**，不是本仓库实际下载重新计算值。尚未入库，避免 62 MB 普通 Git blob；适合评估 GitHub Release 等大型二进制发布方式。
