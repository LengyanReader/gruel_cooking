# 20261105 · v16 链接审计 + 目录导航重设计 + 影响力补员（用户三指令）

**触发**：用户指令 ① 内容/显示整理充实 + 主页链接 double check（部分打不开）② 页面目录导航粗疏琐碎 → 重新设计实现 ③ 增补更多相关领域有影响力的学者。

## 一、链接审计（42 个去重 homepage URL 逐个 HTTP 探活）

- **200 正常 15 + 复测后恢复 15**（首测 12s 超时的慢站点：manovich/taniasinger/peterturchin/fil 等，25s 复测均 200）
- **修复 8 档**（含一种真缺陷：中文括注直接粘在 URL 后 → 渲染 href 即坏）：
  | 档案 | 原状 | 处置 |
  |---|---|---|
  | gobet-fernand | `chessprogramming.org/Fernand_Gobet（条目页；LSE` 括注粘 URL | 剥离括注，实测 200 |
  | boellstorff-tom | `anthropology.uci.edu/（系页…` 同上 | 系官网 base（个人条目路径随学期变动） |
  | klein-richard | SEI 个人页 404——**实为已离任 SEI**，现独立执业（RICKLE）+ Adaptation Without Borders | 主页改 AWB 官网（200）；affiliation 行据实改写「前 SEI」 |
  | chun-wendy | sfu.ca `team/` 路径 404 | 改 `people/` 路径 200 |
  | winters-jane | sas.ac.uk 403（反爬非死链） | 主页改个人站 digitalhistorian.org（200），SAS 页保留于 affiliation 并注反爬 |
  | friston-karl | fil.ion.ucl.ac.uk/~karl/ 失联 000 | 改 UCL profiles 官方页（有浏览器门禁 ◐ 注明） |
  | brattland-camilla | UiT 页时段性 500 | 主页暂改 Google Scholar（200），UiT 官方页保留注明 ◐ |
  | liestol-gunnar | mediakom.uio.no 旧系站失联 | 改 IMK 系个人页（200） |
- **反爬误伤清单**（非死链，浏览器可开，已在档案注明）：cbdb.hsites.harvard.edu 403 / sas.ac.uk 403 / profiles.ucl.ac.uk 浏览器门禁。
- **留待观察**：`https://www.sei.org/people?q=Klein` 类搜索页 200 但非个人页；UCL profiles 对无头抓取拒绝。

## 二、目录导航重设计（template.html）

- **病因**：TOC 面板把 56 份学者档案逐人罗列（第二份名册），8 个顶栏链接平铺无组。
- **处置**：TOC 重构为 **总览 / 人与方向 / 工作 / 方法与过程** 四组章节 + **「学者筛选」控制器组**（全部/卓越开明/有潜力 + 9 轴，各带数量徽章，点击直达并设置 SCH_STATE 过滤器——TOC 从「索引」升级为「控制器」）；56 行逐人罗列删除；新增滚动高亮（scroll-spy）；顶栏 8→7 项精简措辞；修「方向轴覆」截断字。
- 重建后 `--check` 绿；面板内 `data-target="sch-"` 逐人项归零。

## 三、影响力补员（5 档，库 55 → 60）

| 学者 | tier | 领域 | 关键锚（✔ 2026-11-05） |
|---|---|---|---|
| N. Katherine Hayles | 卓越开明 | 后人类理论/非意识认知（UCLA/Duke，Guggenheim/AAAS） | Unthought 纲领 × 本仓论说文「数学家之定位」 |
| Safiya Umoja Noble | 卓越开明 | 算法批判（UCLA C2i2） | Algorithms of Oppression × MVP-001 bot-gating 同构对照 |
| Luciano Floridi | 卓越开明 | 信息哲学/AI 政策（Yale DEC/Bologna，引 125k+，EU AI Act） | 真值 vs 共识之结 × 本仓论说文 |
| Melanie Mitchell | 卓越开明 | 复杂系统/AI 实证批判（SFI，Complexity Explorer） | Jagged Intelligence × 五问审计表锯齿标注 |
| Fabio Parasecoli | 卓越开明 | 食物研究/数字食物景观（NYU，前博士项目主任） | 2026-07 柏林 Digital Foodscapes 工作坊 × 走廊数字食物小志 |

**新格局**：ai_hum 轴现具「批评-政策-理论-媒介」四层全谱（Noble/Floridi/Hayles/Mattern）；food 轴四翼再扩（+数字景观）；SFI 双锚（West 规模律/Mitchell AI 边界）；与 Ray 同系（NYU Steinhardt）的 peer bridge 落成。

## 空手而归（下轮）

- 有潜力层仍待扩充（本轮 5 档全为卓越开明——影响力指令使然；下一轮应专做 early-career 扫描）。
- QID 批量 resolve（全库）、tour 轴青年、food 轴非西方学者仍空。
