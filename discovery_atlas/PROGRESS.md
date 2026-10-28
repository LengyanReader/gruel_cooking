# Discovery Atlas · PROGRESS

## 2026-10-27 · P0 种子批（经 R0–R5 确认后执行）

**需求确认记录（R4 锁定）**：新建顶层模块 · MVP 登记库（不做 web 视图/图谱） · 语言圈首批 中/英/日/法/德/西，用户明令扩展覆盖阿拉伯、中东、非洲等各文明圈 · 影子库按既往决定单列⑤层登记（仅登记信息，不代为获取）。

**落盘产物**：
- `README.md` —— 五层分类法 · 文明圈枚举 · schema · 核验规程 · 路线图
- `sources/books.json` —— 书域种子 **33 条**
- `gate.py` —— 结构闸门（字段/枚举/查重/标记-日期一致性）
- `scripts/probe.ps1` —— URL 可达性探针（HEAD+GET 回退），P1 起每批复用

**本批统计**（截至 2026-10-27 实测）：

| 维度 | 覆盖 |
|---|---|
| 层 | discovery 5 · criticism 13 · publishing 4 · infrastructure 7 · access 4 |
| 圈 | zh 4 · en 8 · ja 3 · fr 3 · de 2 · es 2 · ar 1 · fa 1 · he 1 · afr 1 · global 9（多归属） |
| 核验 | ✔ 实测通过 24 · ○ 已知未本次确认 9（其中 bot-gated 6 / 网络失败 1 / 待补 2） |

**回源纠偏记录**（不凭记忆写 URL，M0.1）：
1. Goncourt 官网 ≠ 记忆中的 `gongur.fr` → 确认为 `academiegoncourt.com`
2. 芥川/直木赏主办官网 ≠ 岩手大学页面 → 确认 `bungakushinko.or.jp`
3. Gutenberg / Ganjoor 首探针 HEAD 误报，GET 复测 200 → 升 ✔
4. Z-Library 域名流变 → 以维基条目为规范锚，不写死镜像域
5. 自查剔除两条凭记忆生成的可疑条目（原 id `heidrich`/`pritz`），改为回源确认的 Deutscher Buchpreis 与 Ganjoor

**闸门结论**：`gate.py` exit=0，33/33 PASS（一次抓到真问题：双维基锚 host 重复 → 以 Ganjoor 升级官网解决；锚点主机豁免规则入闸门）。

**已知缺口（诚实标注，P1 处理）**：
- IPWA/阿拉伯出版商协会、阿联酋作协正典域名待回源
- 中文其余评奖（鲁奖/冯牧等）稳定路径待固化；理想国/世纪文景官网待补
- Anna's Archive 本环境双探针失败（网络性），待换网络复测
- `wikidata_qid` 全空 → P1 起逐条回填（查重主键）
- 乐/影/艺三域尚未开账（P2）；`zh-Hant`、印、突厥、佛教圈、东南亚圈未启动

## 2026-10-27 · P1 书域·批 1（zh + en 圈加密，铺满五层）

**流程**：候选 27 URL → 内联探针（修正 `pwsh -File` 传数组字面量的绑定报错：改为清单文件 + `Select-Object -Unique` 循环 HEAD→GET 回退）→ 可疑域名 WebSearch 回源 → 只把核实过的入库。

**落盘产物**：`sources/books.json` 33 → **57 条**（+24）。

**本批统计**：

| 维度 | 本批新增 |
|---|---|
| 圈 | zh +5（微信读书·中华读书报·国家图书馆·三联·译林）· en +14 · global +5（IA/Standard Ebooks/Wikisource/LibriVox/ISBN Agency） |
| 层 | discovery +1 · criticism +10 · publishing +7 · infrastructure +2 · access +4 |
| 核验 | ✔ 实测 21 · ○ bot-gated 2（pulitzer/faber 403）· ○ pending 1（yilin 网络失败） |

**回源纠偏（M0.1，本批 3 处凭记忆域名全为错）**：
1. `sanlianbook.com`（臆造）→ 三联书店正典官网 **`www.sdxjpc.com`**（GET 200）
2. `yilin.net`（错）→ 译林出版社正典 **`www.yilin.com`**（维基/豆瓣官方俱乐部互证；本环境双探针网络失败→标 pending）
3. `bkweekly.com`（臆造）→ 新周刊正典 `neweekly.com.cn` 属时事生活类杂志、非书域发现主干 → **诚实剔除不硬凑**（中华读书报已在批内更贴切）

**闸门结论**：`gate.py` exit=0，57/57 PASS（id/host/qid 全唯一，无冲突）。

**本批未动（诚实缺口）**：nyrb.com 与 nybooks.com 实体未完全区分 → 只入 `nybooks.com`（NYRB 书评刊），nyrb.com 待下次回源再定；ja/fr/de/es 圈未加密；`wikidata_qid` 全空未回填。

## 2026-10-27 · P1 书域·批 2（ja/fr/de 成圈加密）

**流程**：候选 8 URL 探针 + 4 个不确定域名并行 WebSearch 回源 → 再测回源确认域名。全部核实才入库。

**落盘产物**：`sources/books.json` 57 → **67 条**（+10，均 ✔ 200）。

| 维度 | 本批新增 |
|---|---|
| 圈 | ja +5（NDL·岩波·集英社·早川·読書メーター）· fr +2（Gallimard·Seuil）· de +3（Suhrkamp·Rowohlt·Fischer） |
| 层 | infrastructure +1 · discovery +1 · publishing +8 |

**回源纠偏（M0.1）**：岩波書店 → 候选 iwanami-shoten.co.jp 测错误，正典 **`www.iwanami.co.jp`**；Le Seuil 确认 **`seuil.com`**；読書メーター 确认 **`bookmeter.com`**。诚实剔除：`tokuma-shoten.co.jp`（德间，猜域+双探针失败）不硬凑。

**闸门结论**：exit=0，67/67 PASS。

## 2026-10-27 · P1 书域·批 3（ar/he/非洲/fa/es/zh-Hant 成圈，新开 zh-Hant）

**流程**：候选 13 URL 探针 + Cassava/Brittle Paper 回源→再测。**13 条全入库**（10 ✔ 200 + 3 ○ bot-gated）。

**落盘产物**：`sources/books.json` 67 → **80 条**（+13）。

| 维度 | 本批新增 |
|---|---|
| 圈 | ar +2（Jarir·Abjjad）· he +1（Steimatzky）· afr +3（Jacana·Cassava·Brittle Paper）· es +2（Planeta·BNE）· zh-Hant +3（国家图书馆·誠品·博客来）**新圈启动** · fa +2（Fidibo·Taqsim） |
| 层 | discovery +4 · access +3 · publishing +3 · criticism +1 · infrastructure +2 |
| 核验 | ✔ 实测 10 · ○ bot-gated 3（BNE/誠品/博客来 403） |

**回源纠偏（M0.1）**：Cassava Republic 候选 `.org` 失败 → 正典 **`cassavarepublic.biz`**（维基/官方）；Brittle Paper 确认裸域 **`brittlepaper.com`**（www 变体失败）；Abjjad 确认 **`abjjad.com`**。

**闸门结论**：exit=0，80/80 PASS。

## 2026-10-27 · P1 书域·批 4（ko/ru/tr/hi 成圈，新开四圈）

**流程**：候选 7 URL 探针 + Sahitya Akademi / Can Yayınları 回源→再测。**8 条全入库**（7 ✔ 200 + 1 ○ bot-gated）。

**落盘产物**：`sources/books.json` 80 → **88 条**（+8）。

| 维度 | 本批新增 |
|---|---|
| 圈 | ko +2（Aladdin·Yes24）· ru +3（Lib.ru·LitRes·RGB）**新圈** · tr +2（İletişim·Can）**新圈** · hi +1（Sahitya Akademi）**新圈** |
| 层 | discovery +2 · access +2 · infrastructure +1 · publishing +2 · criticism +1 |
| 核验 | ✔ 实测 7 · ○ bot-gated 1（Can Yayınları 403） |

**回源纠偏（M0.1）**：Sahitya Akademi 确认 **`sahitya-akademi.gov.in`**；Can Yayınları 确认 **`canyayinlari.com`**（回源后探针 403→标 bot-gated）。诚实剔除：`sahapedia.org`（双探针失败且偏艺术非书域主干）。

## P1 书域 收束（主要文明圈已成图）

累计 **88 条**，15 个文明圈已开账：zh · zh-Hant · en · ja · fr · de · es · ar · fa · he · afr · ko · ru · tr · hi（+ global 多归属）。

**尚未启动（诚实缺口，待方向调整）**：
- 东南亚（vi/th/id）、梵语/南亚其他语（sa/ta/ur/bn）、柏柏尔/库尔德/蒙古/藏等中小文明圈——这些圈 registry 级发现源稀疏、域名回源成本高，建议优先用维基锚或降优先级
- `wikidata_qid` 全 88 条未回填（查重主键）
- 乐/影/艺三域尚未开账（P2）
- Anna's Archive、JRDC 等国家/影子层网络失败项待换网络复测

## 方向调整（用户 2026-10-27 确认）

用户选定：**开 P2 音乐/影视/艺术三域（尽可能穷尽，含各影响力社区）+ 回填 wikidata_qid**；东南亚/南亚其他语/中小文明圈 **暂不做、保留缺口**。

## 2026-10-27 · P2 音乐域·首批（`sources/music.json` 开账）

**流程**：候选 19 URL 探针。15 ✔ 200 + 4 ○ bot-gated（RYM/Album of the Year/AllMusic/Discogs 域名皆公认正典，403=反爬，无需回源）。

**落盘产物**：新建 `sources/music.json` **19 条**（书 88 + 乐 19 = **全库 107**）。

| 维度 | 首批 |
|---|---|
| 层 | discovery 4（RYM·AOTY·Billboard·网易云）· criticism 10（Pitchfork·Stereogum·AllMusic·NME·Rolling Stone·Grammy·Mercury·Consequence·Slant·Paste）· infrastructure 2（Discogs·MusicBrainz）· access 3（Spotify·Bandcamp·QQ音乐） |
| 圈 | en 主 · global（Discogs/MusicBrainz）· zh 2（网易云·QQ音乐）**新域开账** |

**待加密（音乐批 2）**：③「厂牌/唱片公司」层尚空（Sub Pop、Warp、ECM、4AD、XL、Blue Note 等）；日/韩/法/德/巴西等各圈音乐发现与奖项（日本唱片大赏、韩国 Melon、巴西、印度）待成圈。

## 2026-10-27 · P2 影视域·首批（`sources/film.json` 开账）

**流程**：候选 17 URL 探针 + Sight&Sound/Cahiers 回源→再测。**19 条全入库**（12 ✔ 可达 + 7 ○ bot-gated）。

**落盘产物**：新建 `sources/film.json` **19 条**（书 88 + 乐 19 + 影 19 = **全库 126**）。

| 维度 | 首批 |
|---|---|
| 层 | discovery 6（Letterboxd·AlloCiné·Filmaffinity·豆瓣电影·时光网·Filmarks）· criticism 9（RogerEbert·Metacritic·RT·Sight&Sound·Cahiers·Oscars·Cannes·Berlinale·Sundance）· infrastructure 2（IMDb·TMDB）· publishing 1（Criterion）· access 1（MUBI）——**五层齐备** |
| 圈 | en 主 · fr 4（Cahiers·Cannes·AlloCiné·+）· de 1（Berlinale）· es 1（Filmaffinity）· zh 2（豆瓣电影·时光网）· ja 1（Filmarks）· global（TMDB） |
| 核验 | ✔ 可达 12（含 IMDb 202）· ○ bot-gated 7（Letterboxd/TMDB/RogerEbert/Criterion/Oscars/Cannes/Filmaffinity 403/400） |

**回源纠偏（M0.1）**：Sight&Sound 现归 BFI → **`bfi.org.uk/sight-and-sound`**（非旧 sightandSound 独立域）；Cahiers du cinéma 确认 **`cahiersducinema.com`**。bot-gated 七条皆公认正典，403=反爬非错域，未回源。

**待加密（影视批 2）**：各圈电影节/发行商加密（威尼斯/多伦多/鹿特丹、日韩印发行）；中文专业批评与选片人待补。

## 2026-10-27 · P2 艺术域·首批（`sources/art.json` 开账）

**流程**：候选 19 URL 探针 + Wikimedia Commons 补测。无一凭记忆错域（皆知名机构）。

**落盘产物**：新建 `sources/art.json` **20 条**（书 88 + 乐 19 + 影 19 + 艺 20 = **全库 146**）。

| 维度 | 首批 |
|---|---|
| 层 | discovery 8（Google Arts&Culture·Met·Louvre·MoMA·Rijks·British Museum·Uffizi·Tate）· criticism 6（Hyperallergic·The Art Newspaper·Frieze·Artforum·e-flux·La Biennale）· publishing 3（Gagosian·Hauser&Wirth·White Cube）· infrastructure 2（WikiArt·Artnet）· access 1（Wikimedia Commons）——**五层齐备** |
| 核验 | ✔ 200 共 11 · ○ bot-gated 共 8（Artnet/Frieze/Gagosian/BM 403、H&W/Met 429、Google…）· ○ pending 1（WikiArt 网络失败） |

## P2 三域开账 收束

全库 **146 条 = 书 88 + 乐 19 + 影 19 + 艺 20**，四域五层均已成图。

## 下一步（连批推进中）

三域各批 2 加密（音乐厂牌层、影视各圈节/印发行、艺术非英语圈）→ wikidata_qid 全库回填（查重主键，146 条）。

## 2026-10-27 · QID 回填（entity-resolution，经 P856 官网核验，绝不臆造）

**能力**：harness_factory entity-resolution + M0.4 no-fabrication。

**脚本**：`scripts/resolve_qid.py` —— Wiki 锚定条目走 enwiki sitelink 精确解；其余 `wbsearchentities` 按名检索 → 批量 `wbgetentities` 取候选 **P856 官网声明**，仅当候选 P856 可注册域名与本条 url 域名一致才采纳；无法确认→留空（不猜 QID）。支持 429/5xx `Retry-After` 退避、逐条 try/except、实时 checkpoint、按文件名断点续跑。

**排障（本环境）**：首轮持续 HTTP 429 —— 根因是一个**前次未退出的 `resolve_qid.py` 进程在并发打同一 API、互抢限流额度**；结束僵尸进程 + 加节流（每请求间隔 ≥1s）后吞吐恢复正常。

**结果**（146 条）：

| 域 | 采纳 QID | 留空（无 P856 匹配/瞬时网络） |
|---|---|---|
| art | 20/20 | 0 |
| music | 18/19 | consequence |
| film | 17/19 | sundance · douban-movie |
| books | 69/88 | 评奖/门户类无官网声明者（douban-book·booker·maodun·goncourt·bungakushinko·ganjoor·deutscher-buecherpreis·elpais-babelia·jrdc·libby·graywolf·shueisha*·hayakawa*·jarir·abjjad·planeta·taqsim·aladin·lib-ru）*为瞬时 URLError |
| **合计** | **124/146** | **22（诚实留空，可复跑）** |

**闸门复验**：`gate.py` exit=0，146/146 PASS（ids/hosts/**qids 全局唯一**）。

## 2026-10-27 · 社区专项批 1（四域高影响力社区，+13）

**能力**：verification-gate + traceable-sources + M0.4。**schema 演进**：闸门 `ANCHOR_HOSTS` 新增 `reddit.com`/`old.reddit.com`——一域承载多个各自独立的子社区，豁免 host 去重、改由 `id`(+QID) 守护唯一（与现有 en.wikipedia.org 锚点同构）；README 同步。

**流程**：候选 21 → 探针（reddit 全域 403 反爬、deviantart 403、anobii 网络 ERR）→ 探针无法定存在，逐条**检索回源**确认存在与规模 → 只把核实过的入库。

**入库 13**：书 r/books·r/Fantasy·r/RomanceBooks(~541k)；乐 r/hiphopheads·r/indieheads(~1.9M)·r/listentothis(最大音乐发现)·r/metal；影 r/movies·r/TrueFilm(~504k)；艺 r/Art(~22.5M、有独立维基条目)·r/ArtHistory·r/ContemporaryArt·DeviantArt。均 `○` bot-gated + 今日 access_date（反爬非死，浏览器可读）。

**诚实剔除（未回源到存在证据→不录入）**：r/Mystery·r/writing·r/scifi·r/jazz（本轮检索未直接命中）；aNobii（网络 ERR 且域名未回源）。留作后续候选。

**全库迄今 159 条**（书 91 + 乐 23 + 影 21 + 艺 24），gate 159/159 PASS。

## 2026-10-27 · P2 加密批 2（音乐厂牌层补齐 + 影/艺非英语圈，+15）

**能力**：verification-gate + traceable-sources/outlet-map + M0.1/M0.4。

**音乐③厂牌/集团层（原空→ 8）**：Blue Note✔ · ECM✔(de) · Sub Pop✔ · Warp○403 · 4AD○403 · XL✔ · 摩登天空✔(zh) · Beggars Group✔——**音乐域五层至此齐备**。

**影②/③（+3）**：TIFF✔202 · IFFR 鹿特丹✔(新开 nl 圈) · Janus Films✔(distributor，首轮 ERR 复测 200)。

**艺①/②（+4）**：Centre Pompidou○pending(fr) · Reina Sofía✔(es) · MALBA✔(es/拉美 AR) · artpress○pending(fr)。

**回源纠偏（M0.1·再抓一个凭记忆错域）**：Beggars Group 候选 `beggarsgroup.co.uk` 错→正典 **`beggars.com`**（官网/维基互证，复测 200）。Centre Pompidou/artpress/Janus 本环境 ERR 但域名经回源确认：Janus 复测 200 入库✔；Pompidou/artpress 仍网络失败→诚实标 `pending`。Warp/4AD 403=bot-gated（正典域名未本次确认）。

**全库迄今 174 条**（书 91 + 乐 31 + 影 24 + 艺 28），gate 174/174 PASS。

## 2026-10-27 · QID 攻坚复跑（+15 → 139/174）

**方法**：全库复跑 `resolve_qid.py`（断点续跑，自动跳过已有 QID）；新增条 + 上轮瞬时 URLError 均重解，仍经 P856 核验。

**新采纳 15**：艺 Centre Pompidou·Reina Sofía·MALBA·artpress·DeviantArt；书 集英社(上轮 URLError 本轮解)；影 TIFF·IFFR·Janus；乐 Blue Note·ECM·Sub Pop·Warp·4AD·XL。**139/174，gate PASS、QID 全局唯一。**

**诚实下限（35 留空）**：① 12 个 reddit 子社区——为 Reddit 分区、非独立实体，无自身 P856，方法学上应留空；② 评奖/门户/机构无匹配官网声明者（douban·booker·maodun·goncourt·ganjoor·libby·graywolf·planeta·sundance·consequence 等）；③ 2 条 CJK 混名检索未命中（modern-sky/beggars-group，可人工补）。留空≠错误，为不臆造的必然结果。

## 2026-10-27 · Web 视图（发现星图静态站）

**产物**：`scripts/build_view.py` 从 `sources/*.json` 生成自包含双语可筛静态页 → `docs/discovery_atlas/index.html`（104KB·离线双击可开）；不硬编码数据，随批次可重跑。已接入仓库主目录 `docs/index.html`（第四组新 pillar “发现星图”）。

**功能**：域/层/圈/核验四维筛选 + 搜索 + 中英切换；卡片显示 name(链)/层/圈/kind/why/not_for/实测状态（✔绿·○黄）+ QID 外链。

**浏览器实测验收**（本地 http.server）：页面非空、统计 174/139/123/17 圈、域与层叠加筛选生效（乐→10、书→91）、搜 reddit 命中 12 条社区、EN 切换正常、**控制台 0 报错**。卡片正文保留中文（why/not_for 为登记员按条撰写，设计如此）。

## 2026-10-27 · QID 诚实缺口清欠（+11 → 150/174）

**方法**：对上轮 35 留空做人工实体消解。先 `wbsearchentities` 出候选，再 `wbgetentities&props=claims` 取候选的 P856 官网声明——**严守 M0.4：只在 ①P856 可注域与条目 URL 完全一致，或 ②候选带 en.wikipedia 站点链接且标签与条目实体一致时采纳，绝不凭标签近似臆造。**

**采纳 11**（gate PASS、QID 全局唯一、150/174）：书 茅盾文学奖 Q451809·Académie Goncourt Q621737·Deutscher Buchpreis Q700236·Graywolf Press Q5598450·早川书房 Q11511323·Jarir Q6160243·Abjjad Q19903167·Lib.ru Q2371298；影 Sundance Institute Q1764307；乐 摩登天空 Q112967075·Beggars Group Q814309（后两条即上轮标注「可人工补」的 CJK 混名，经 P856 精确命中官网域补齐）。

**仍诚实留空 24**：① 12 个 reddit 分区（非独立实体）；② douban 读书/电影（同属 Douban Q5299559 一个实体，两条分面若同赋会破 QID 唯一性，留空）；③ 检索命中的是同名异实或无官网声明者：ganjoor/aladin（命中为书卷/迪士尼地名等错实）、jrdc·libby·consequence·booker·planeta·taqsim·elpais-babelia·bungakushinko（无 P856 匹配或不唯一）。留空均为不臆造的必然结果。

## 2026-10-27 · 数据导出（CSV / NDJSON / JSON）

**产物**：`scripts/export_data.py`——纯变换（不新增数据），从 `sources/*.json` 归并 174 条 → `docs/discovery_atlas/atlas.csv`（含 BOM、全列引用、langs/regions 以 `;` 拼接）、`atlas.ndjson`（逐行完整条目）、`atlas.json`（单对象 indent=2）。静态页页脚新增下载栏（CSV/NDJSON/JSON），重建后视图同步 150 QID。（导出与视图随每个登记批次重跑，最新态见下条。)

## 2026-10-27 · 社区专项批 2 + 稀疏圈加密（+15 → 189）

**目标**：继续「尽可能穷尽」——登记非 Reddit 的各媒介重量级社区，并新开稀疏文明圈。候选 16 → 探针 → 逐条回源。

**方法**：候选先探针（浏览器 UA），**7 条 200**（lubimyczytac·storyweaver·melon·oricon·kinopoisk·justwatch·artsy）直接入库；**9 条 403/418/ERR** 逐条 WebSearch 回源确认官方域名与重要性后以 ○ 入库（babelio·anobii·naver-book·soundcloud·genius·mydramalist·behance·artstation）。**诚实剔除 1**：eksisozluk（Sözlük）——虽回源确认为土耳其重量级社区，但属综合向而非媒介发现专用，不合五域分类，不登。所有新条域名均为记忆域，均经回源；未臆造。

**新条 15**（书 5：babelio(fr)、anobii(it)、naver-book(ko)、lubimyczytac(pl)、storyweaver(hi)；乐 4：soundcloud、genius、melon(ko)、oricon(ja)；影 3：kinopoisk(ru)、justwatch、mydramalist(sea)；艺 3：artsy、behance、artstation）。新开 **it / pl / sea 三圈→ 共 20 圈**。

**现况**：**189 条**（书 96 · 乐 35 · 影 27 · 艺 31），150 QID·130 实测 ✔；gate 189/189 PASS、id/host/qid 全局唯一。视图与导出已重跑同步 189/150/130。

## 2026-10-27 · 图谱深化（QID 关系边 + 星图视图）

**产物**：`scripts/build_graph.py`——仅从 Wikidata 声明派生实体星座（不臆造）：① 机构直连边（某登记实体 P127/P176/P355/P361/P527 的指向命中另一登记 QID）；② 类簇节点（P31/P279 共享值，取连接 ≥ 3 实体者、按度取前 30）。输出 `docs/discovery_atlas/graph.json`。

**图结构**：150 实体 + 30 类簇 = 180 节点、227 边。直连 3 条（Kirkus→NYRB 拥有·Open Library→Internet Archive 隶属·Janus→Criterion 子公司）；类簇如 website(27)·publishing house(26)·magazine(15)·record label(8)·art museum(8)·national library(8)·social cataloging(8)。批量 `wbgetentities` 拉取，尊重 Retry-After。

**Web 视图**：`build_view.py` 新增「列表/星图」切换（graph.json 内联进页，保持离线），自带零依赖的 canvas 力导向图（按域着色·类簇灰菱形·金线=直连）。修复画布尺寸 bug（backing store = CSS×devicePixelRatio，否则仅 300×150 默认→约 81% 节点不可见）。**浏览器实测验收**：180/180 节点全铺满画布、标签正常、悬停命中对齐、拖拽重布局、EN/中切换、控制台 0 报错。

**全库迄今**：189 条·150 QID·20 圈·gate PASS。本次四方向（社区批 2·加密·导出·图谱·QID 清欠）均已入库。

## 2026-10-28 · 新兴潜力批（下一代发现平台，+10 → 199）

**目标**：应需聚焦「新兴且有潜力」的下一代发现源（上升中的平台/社区，非已固化巨头），四媒介各取若干。候选 12 → 内联探针（浏览器 UA）→ 逐条回源（M0.4，记忆域一律核实）→ 只把可达且重要性经确认者入库。

**探针**：**8 条 200**（ream·substack·everynoise·audius·shortoftheweek·foundation·dailyartmagazine·are.na）直接采 ✔；**2 条 403**（bookshop·rhizome）经回源确认官方域名与重要性后以 ○ 入库；**诚实剔除 2**：① talefy——记忆把它当作 BookTok 书目发现，回源发现现为 **AI 角色陪聊应用**（名实漂移，又一记 M0.1 教训），不登；② omeleto——`omeleto.com` 探针 ERR，其真正落点是 YouTube 频道而非独立站点，无稳定规范域，不臆造，不登。

**新条 10**（书 3：bookshop.org(伦理独立书店荐书)、ream(作者—读者直连社区)、substack(长文/批评通讯枢纽)；乐 2：everynoise(算法微流派地图)、audius(去中心化流媒体)；影 1：shortoftheweek(短片策展)；艺 4：rhizome(网络艺术档案机构)、foundation(数字艺术策展市场)、dailyart(艺术史普及)、are.na(连接式研究/灵感板，跨媒介登记于 art 主域)）。本批为平台现代化，未新开文明圈（仍 20 圈）。

**QID 实体消解**：对新条及既有留空重跑 `resolve_qid.py`（严守 P856 官网精确一致或 en-wiki 站点链接 + 标签一致方采）。本会话新条命中 **6**（bookshop·substack·everynoise·audius Q108934318·rhizome·are.na），**4 诚实留空**（ream·shortoftheweek·foundation·dailyart——无匹配维基项，不臆造）；顺带补齐上轮留空的旧条 **soundcloud·genius·melon·oricon·kinopoisk·justwatch·mydramalist** 等。全库 **168 QID / 199**。

**重建同步**：`gate.py` 199/199 PASS（id/host/qid 全局唯一）；`build_view.py` → 视图、`export_data.py` → CSV/NDJSON/JSON、`build_graph.py` → 图谱，均刷新至 **199 条 · 168 QID · 138 实测 ✔**。

## 2026-10-28 · 新兴潜力批 2（下一代发现平台加密，+10 → 209）

**目标**：沿「新兴且有潜力」继续——先拉全库 184 个已存主机去重，避开已登记的巨头（Letterboxd/MUBI/RYM/StoryGraph/Hyperallergic/e-flux/Artsy…），另选 12 个新站候选 → 探针 → 逐条回源。

**探针**：**7 条 live**（wordswithborders·gnoosic·musicmap(202)·lwlies·reverseshot·thisiscolossal·objkt）采 ✔；**5 条 ERR** 中四个经回源发现是记忆域名错写（thebookriot→**bookriot.com**、getfable→**fable.co**、arselectronica.net→**ars.electronica.art**、fxhash.io→**fxhash.xyz**）。**诚实剔除 2**：① chosic——探针 ERR 且回源无确证结果，无法核实→不登；② fxhash——回源发现已于 **2026-08-17 关停**（非“潜力”，属已没），不登。objkt 鉴于 fxhash 前车之鉴额外回源，确认 2026 仍在运营。

**新条 10**（书 3：bookriot(最大独立书单媒体)、fable(BookTok 读书会社交应用)、wordswithborders(世界文学英译管道)；乐 2：gnoosic(Gnod 自学习口味推荐)、musicmap(信息之美奖流派谱系图)；影 2：lwlies(小白色影评志)、reverseshot(深度艺术电影批评)；艺 3：colossal(视觉艺术策展博客)、objkt(Tezos 生成/数字艺术市场)、arselectronica(新媒体艺术机构/Prix)）。未新开文明圈（仍 20 圈）。

**闸门小修**：fable 初填 `status=app-shell` 非枚举→改为 `bot-gated`（JS 外壳需浏览器），gate 209/209 PASS。

**QID 实体消解**：本会话新条命中 **3**（colossal Q16988507·arselectronica Q678361·bookriot Q135003540），**7 诚实留空**（fable·wwb·gnoosic·musicmap·lwlies·reverseshot·objkt——无 P856 精确匹配或不唯一，不臆造）。全库 **171 QID / 209**。

**重建同步**（graph→view→export 依序）：`build_graph.py` 171 实体/257 边、`build_view.py` 视图内联新图、`export_data.py` CSV/NDJSON/JSON、`gate.py` 209/209 PASS；统一态 **209 条 · 171 QID · 145 实测 ✔**。

## 2026-10-28 · 新兴潜力批 3（全方位扫荡，+13 → 222）

**目标**：四媒介全方位加密新兴发现源。先拉全库 198 主机去重，取 16 个新站候选 → 探针 → 逐条回源。

**探针**：**9 条 200**（catapult·booktrib·sofarsounds·thefilmstage·filmcomment·nonfiction·juxtapoz·artblocks·superrare）；**3 条 403**（asymptote·screenslate·ocula）经回源（前两者维基在案）确认后以 ○ 入库；**4 条 ERR** 逐一回源。**诚实剔除 4**：① emptymirror——记忆混淆，`emptymirror.co` 不存、真正的 Empty Mirror（emptymirrorbooks.com）系美 avant 诗刊而非我意图的日本翻译→不登，改用同位的 **Monkey**（`monkeymagazine.org`，日本文学英译，探针 200）；② hypemachine→修正为官方域 **hypem.com**（维基在案，本会话 ERR 但回源确证）→○ 入库；③ musicfy——回源无确证→不登；④ utopiamusic——搜索空→不登；⑤ nonfiction.org——虽 200 但用途无法回源确认→不登。

**新条 13**（书 4：asymptote(世界文学翻译旗舰)、catapult(叙事非虚构杂志)、monkey(日本文学英译)、booktrib(全类型书评)；乐 2：hypem(乐评博客聚合器)、sofarsounds(神秘现场发现网络)；影 3：screenslate(arthouse 片单聚合)、thefilmstage(影展/新片发现)、filmcomment(资深影评刊)；艺 4：ocula(画廊聚合平台)、juxtapoz(街头/低眉艺术刊)、artblocks(链上生成艺术)、superrare(策展加密数字艺术)。artblocks 鉴于 fxhash 前车之鉴以 200 实测确认仍在运营。未新开文明圈（仍 20 圈）。

**QID 实体消解**：本会话新条命中 **6**（juxtapoz Q6319143·superrare Q113995966·catapult Q110908984·filmcomment Q4038736·hypem Q3521346·sofarsounds Q22313035），顺带补齐上轮留空的 **wwb Q4020822**；**7 诚实留空**（asymptote·monkey·booktrib·screenslate·thefilmstage·ocula·artblocks——无 P856 精确匹配/不唯一，thefilmstage 另因瞬时 URLError）。全库 **178 QID / 222**。

**重建同步**（graph→view→export 依序）：`build_graph.py` 178 实体/262 边、`build_view.py` 视图内联新图、`export_data.py` CSV/NDJSON/JSON、`gate.py` 222/222 PASS；统一态 **222 条 · 178 QID · 154 实测 ✔**。





