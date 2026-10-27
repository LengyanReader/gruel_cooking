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

