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

## 下一步（待启动确认）

**P1 书域全量**：按 圈×层 分批（每批 25–40 条：草拟→探针→闸门→commit 不 push，批间心跳续接），顺序建议 zh/en 加密 → ja/fr/de/es 成圈 → ar/fa/he/非洲成圈 → 印/突厥/东南亚/原住民圈。
