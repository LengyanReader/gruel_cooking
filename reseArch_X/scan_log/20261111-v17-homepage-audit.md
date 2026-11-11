# 20261111 · v17 主页直链审计（用户指令：查得到就补，查不到就明说没有）

**触发**：用户「明白，有些学者的主页确实需要进一步查找，没有的话，就注明没有即可」。范围：60 档学者中 homepage 字段非 URL 或直链待补的 13 档，外加 Google Scholar 直链在本网不可达的 Kull 1 档。

**判据**：只落**实测 200 且正文可核实到其人**的页面；403/202 不作「存在」证据（见第三节控制测试）。查不到即写「无个人主页 ◇」并在字段注释里留实证过程，不落未核实链接。

## 一、本轮落库 9 档（实测 200，正文含其人）

| 档案 | 主页 | 核实要点 |
|---|---|---|
| behrendt-frauke | `tue.nl/en/research/researchers/frauke-behrendt` | 标题即其名，32 次命中；`research.tue.nl` 旧路径 000 |
| davidson-richard | `psych.wisc.edu/staff/davidson-richard/` | 系页标题「Davidson, Richard – Department of Psychology」；Center for Healthy Minds 的 leadership 旧路径 404 |
| escobar-arturo | `anthropology.unc.edu/people/arturo-escobar/` | 系页标题含其名，21 次命中；`arturoescobar.net` 000（无个人官网） |
| moretti-franco | `english.stanford.edu/people/franco-moretti` | 标题「Franco Moretti \| Department of English」；`dlcl.stanford.edu` 旧路径 404 |
| sheller-mimi | `wpi.edu/people/faculty/msheller` | 校方教职员页，19 次命中，含 The Global School 职务 |
| tsing-anna | `campusdirectory.ucsc.edu/cd_detail?uid=atsing` | 校方名录条目；系页 `faculty/index.php?uid=atsing` 实为全系名册（其条目另列项目站 Matsutake Worlds，独立域名未取到） |
| wang-xiaoguang | `sim.whu.edu.cn/` | 学院官网 200（32 次命中）；个人简介页未定位：站内 sitemap 与常见栏目路径软 404，教师主页系统 `jszy.whu.edu.cn/wangxiaoguang` 返回 error 页（见第三节，200 不可信） |
| salganik-matthew | `bitbybitbook.com/` | 其《Bit by Bit》书站，标题与正文可核；Princeton 社会系页与 `www.princeton.edu/~msalganik` 均 403 |
| sawin-will | `math.princeton.edu/people/will-sawin` | 标题「Will Sawin \| Math」；**并据此订正 affiliation（见第二节）** |

## 二、substantive 订正一处：Will Sawin 任职机构

- 旧档（2026-11-04）记 `Columbia University · Department of Mathematics`，依据是「Kalai 博客/媒体一致」。
- 本轮实证：① `math.princeton.edu/people/will-sawin` 200；② ORCID `0000-0003-0344-5438` 任职记录「Princeton University · Professor, 2024 → 至今」；③ Columbia 数学系名录（`people/faculty/`、`department-directory/`）已无 Sawin 条目。
- 处置：affiliation 改 Princeton，`entry` 同步；`risk` 由「职级与带生未核」改为「带生与课程未核」（职级已由 ORCID 任职记录落实）。v4 覆盖度台账里的 Columbia 记法为 2026-11-04 时点快照，保留不改，以本档为现行口径。

## 三、控制测试（为什么 202/403 不能当证据）

- `uni.lu` 与 `psych.ox.ac.uk` 对**任意路径**（含虚构人名 `zzz-not-a-person-12345`）均返回 **202 空体**；`jszy.whu.edu.cn` 对任意 slug 返回 **200 + error 页**。故「202/200」须配正文核实才成立，本轮据此拒绝了 Oberbichler 的 uni.lu 个人页直链与王曉光的教师主页直链。
- `sais.jhu.edu`、`sociology.princeton.edu`、`adaptationwithoutborders.org`、`sas.ac.uk` 对无头抓取一律 403（浏览器可开），属反爬误伤，非死链。

## 四、以 ORCID 为页 3 档（200，任职/机构与档案自洽）

| 档案 | ORCID | 依据 |
|---|---|---|
| chandaria-shamil | 0009-0004-9946-4901 | 任职列 University of Oxford · Senior research fellow；该姓名唯一记录（无作品条目，故仅作身份页） |
| fanzo-jessica | 0000-0002-6760-1359 | 任职列 JHU SAIS Europe · The James Anderson Professor of Food Policy and Climate, 2026–；Columbia 2023–2025 已结束，与档案「Director Emeritus」吻合 |
| oberbichler-sarah | 0000-0002-1031-2759 | 任职列 Luxembourg C²DH · Assistant Professor in AI and Data Mining in Digital History, 2026–，61 条作品；与 affiliation 一致 |

## 五、明写「无个人主页」2 档 + 保留机构页 1 档

| 档案 | 处置 | 实证过程 |
|---|---|---|
| norstrom-asa | `无个人主页 ◇` | SRC 站内检索与 sitemap 仅见 Albert Norström（`/meet-our-team/staff/2009-09-28-norstrom.html`）；ORCID 以 Åsa/Asa 两种写法检索均 0 条 |
| kull-kalevi | `无个人主页 ◇` | UT 总站与哲学与符号学研究所（`flfi.ut.ee`，站可达）人名录无其个人页，站内检索为 JS 渲染无服务端结果；ORCID 检索 0 条；Google Scholar 页在本网 000 不可达 |
| wang-xiaoguang | 保留学院官网（非个人页，已注明） | 见第一节 |

## 六、同一缺陷类：括注粘连 URL 3 档（v16 已记的 gobet/boellstorff 同型）

| 档案 | 原状 | 处置 |
|---|---|---|
| sicart-miguel | `en.itu.dk/en/Miguel-Sicart（个人页直补 ◇）` | 剥括注入注释；ITU 该路径 000、`pure.itu.dk` 301，改个人站 `miguelsicart.net`（200，正文自述 ITU 副教授） |
| wang-siming | `icac.edu.cn/  （中华农业文明研究院；…）` | 剥括注入注释；研究院官网 200 保留为机构页 |
| west-geoffrey | `santafe.edu/…/geoffrey-west（个人页待直补 ◇）` | 剥括注入注释；SFI 个人页 200，标题含其名 |

> 该缺陷在 v16 只修了 2 档，本轮补扫全部 60 档又发现 3 档（均属「URL 后紧跟中文括注」），已清零。渲染层守护（`^https?://` 才出 `<a>`）与源头不粘连，二者并用。

## 七、方法学备注

- **全量复扫**（58 条 homepage 逐条 GET，2026-11-11）：54 条 200；1 条 403 反爬（`cbdb.hsites.harvard.edu`，浏览器可开）；4 条本网 000——`digitalhistorian.org`（本日早前实测 200，复测抖动）、`rubenlaukkonen.com`、`stefangossling.de`、`terrytao.wordpress.com`。四条均非本轮改动项，未据此改档，留待下轮复测。

- 环境限制：`websearch` 402、DuckDuckGo HTML 返回空、Bing 结果被区域噪声污染（返回淘宝/百科无关条目），故本轮**未用搜索引擎**，全部走机构站内检索 / sitemap / 名录 / ORCID 公共 API 直证。
- 渲染侧同步：`template.html` 的 homepage 守卫（仅 `^https?://` 出 `<a>`）使「无个人主页 ◇」与机构页说明不再生成坏链，悬停可见原文。
