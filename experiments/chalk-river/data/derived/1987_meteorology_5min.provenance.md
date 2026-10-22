# 1987 five-minute meteorology provenance (VERIFIED_PRIMARY table)

**Source**: Murata, M. & Noguchi, H. (1997), *Dose Delivered by Unit Amount of Tritium Released into the Environment*, *J. Nuclear Science and Technology* **34(2):176–184**, **Table 1 on printed p.177 (PDF page 2 of 9)**. [J-STAGE official PDF](https://www.jstage.jst.go.jp/article/jnst1964/34/2/34_2_176/_pdf); [original DOI 10.3327/jnst.34.176](https://doi.org/10.3327/jnst.34.176); [alternate publisher DOI for same article](https://doi.org/10.1080/18811248.1997.9733644).

**Extraction**: 2026-10-12, visually read and manually transcribed six rows from published table; no OCR interpolation. Independent second-person double check is still pending.

**Column notes**: time strings are as reported, **time zone not verified**; wind direction labelled **bearing from true north** in table (wind **towards/from** interpretation must be resolved before trajectory simulation); speed measured at **0.9 m** height; `roughness_height_cm` uses **centimetres**, with any code conversion `z0[m]=z0[cm]/100`. The original records B, B, C, C, C, C Pasquill classes. The table contains no precipitation, vertical wind profiles, complete source wind field, temperature, sampler geometry, instrument uncertainty or station-level tritium concentration.

**QA**: 6 contiguous 5-minute rows cover **15:20–15:50**; direction 0–360, speeds and roughness strictly positive. Reported instrumental uncertainty remains **unknown**, not zero. This CSV is a small source table, **not a complete experimental forcing field**.
