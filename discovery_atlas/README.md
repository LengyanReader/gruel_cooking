# Discovery Atlas · 发现源总库

> 状态：**P0 规划已确认，种子库已落盘**。四域（书 / 乐 / 影 / 艺）· 五层 · 全文明圈的发现源登记库，服务「下一步读什么 / 听什么 / 看什么」。
> Status: **plan confirmed at R4, seed registered.** A registry of discovery sources across four media domains, five source layers and the world's civilizational circles.

**用法一句话**：想读书时按 `域 → 层 → 文明圈` 三维翻 `sources/*.json`——①层找人气与同好，②层找专业评价与奖项书单调性，③层追有品味的出版者，④层用国家书目/开放书目对元数据，⑤层解决"去哪儿拿到"。

---

## 五层分类法 · The five layers

聚合器只供**发现**，不供**背书**——一切事实与引用回一手文本本体（harness 之 outlet-map 原则的反向应用）。

| 层 | 名称 | 它回答的问题 | 典型误用（NOT for） |
|---|---|---|---|
| ① `discovery` | 社区发现 | 有什么？谁在读？热度与口味相似的人在推什么？ | 评分是大众情绪与刷量场，不是质量判决 |
| ② `criticism` | 专业评价与奖项 | 哪个更好？谁在把关？奖项书目即免费书单 | 评审也是意见；一个奖不是终审 |
| ③ `publishing` | 出版机构 | 谁的品味值得持续追随？（出版社/厂牌/公司/画廊） | 名社也有庸作；按条评估 |
| ④ `infrastructure` | 书目与元数据基础设施 | 版本、ISBN/ISMN、国家书目、权威控制 | 身份与著录而已，不含质量信号 |
| ⑤ `access` | 获取渠道 | 图书馆借阅 / 公版 / 购买 / **影子库** | 能拿到 ≠ 该读；获取与评价严格分离 |

**影子库立场（如实登记）**：Anna's Archive、Z-Library 等按用户既往决定作为⑤层正常条目登记，`note` 中标注版权争议状态；本库**只登记信息，不代为获取**。Z-Library 域名流变频繁，规范锚定其维基百科条目，具体镜像以条目内当期说明为准。

## 文明圈 · Civilizational circles

`circle` 枚举：**已启动** `zh` `en` `ja` `fr` `de` `es`；**待补批次（用户明令全部覆盖）** `ar`（阿拉伯）、`fa`（波斯）、`he`（希伯来/犹太）、`zh-Hant`（港澳台，随 zh 圈深入）、`sa`（梵语/印度古典）、`hi` 等现代印度语言、`tr`（突厥）、`ko`（朝鲜半岛）、`pt`（葡语）、`am`（阿姆哈拉/非洲之角）、`sw`（斯瓦希里）、`yo`（约鲁巴）、`qu`（克丘亚）、`nai`（原住民北美）、`ber`（柏柏尔）、`ku`（库尔德）、`ur`（乌尔都）、`ta`（泰米尔）、`mn`（蒙古）、`bo`（藏）及东南亚诸圈（`vi` `th` `id`）。每圈补齐前，总数即标注为**未穷尽**——「完整」是方向不是状态，各批次在 `PROGRESS.md` 报覆盖率。

## 条目 schema · Entry schema（SSOT 为 `sources/*.json`）

每条源 = 一个 JSON 对象，必填 13 字段：

```
id, domain, layer, circle, name, url,        # 标识与归属
langs[], regions[], kind,                     # 语言/地域/细型
why, not_for,                                 # 一句话评估：何所长·何所长不对
verified, access_date,                        # ✔=本次实测 HTTP 状态；○=规范域名未本次确认
status, note                                  # active|bot-gated|moved|contested|pending + 备注
```

可选：`wikidata_qid`（查重主键，P1 起逐条补）、`language`（登记条目自身双语）。

**查重与实体之辨（`entity-resolution`）**：同名站点、一地多站、站与奖同名同实之辨，以 Wikidata QID 为主键去重；无 QID 时以 `domain` 去点小写为次键。

## 闸门 · Gate

`python gate.py` 检查：字段完整 · 枚举合法 · `id`/`domain`/QID 唯一 · `✔` 必配 `access_date`。FAIL 即退出码 1（结构闸门只机器可判者；「是否高质量」永远是人的判断）。

## 核验规程 · Verification protocol

- 可达性 = 对 `url` 的实测（HEAD/GET，PowerShell 探针），当日写入 `access_date`；**403/429 反爬不判死**，标 `bot-gated` + `○`。
- 域名可疑者**回源核实**（搜索→官网互证），不凭记忆写 URL——本库落盘前已纠两处记忆偏差（Goncourt、芥川/直木赏官网）。
- 批量推进：每批 25–40 条，按 域×圈 推进；每批走 草拟→实测→闸门→commit（不 push），可中断续接。

## 路线图 · Roadmap

| 期 | 内容 | 状态 |
|---|---|---|
| P0 | schema · 五层 · 圈枚举 · 书域种子（中·英·日·法·德·西·阿·波·希·非洲）· 闸门 | ✅ 本次落盘 |
| P1 | 书域全量：主要文明圈已铺（15 圈 · 88 条） | ✅ 收束 |
| P2 | 乐、影、艺三域同构推进（各先补层定义+种子） | 🔄 进行中（乐 19 · 影 19 已开账，艺待启） |
| P3 | 接 Reading_IA 图谱/站点视图（发现源↔书卡边） | 未纳入 MVP |
| P4 | 存活定期 refresh（harvest 式） | 未纳入 MVP |

**P1 已知待办（本批诚实缺口）**：阿拉伯出版商协会（IPWA/BAF）与阿联酋作协正典域名待回源；中文评奖官网入口（鲁迅文学奖等）统一以中国作家网为锚待逐奖固化路径；国家書目（JRDC 追手門）正确 URL 待重测；理想国/世纪文景官网待补；`wikidata_qid` 全空待回填。

---

*Generated with harness_factory 常驻引用（规划经 R0–R5 收敛）；铁律：M0.1/M0.2 真实可溯 · M0.4 不编造 · 双语 parity。*
