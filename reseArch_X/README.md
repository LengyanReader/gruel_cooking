# reseArch_X · 科研机会与开放学者检索评估

> 目的：全面检索高校、研究所及同等机构**已发布或即将发布**的研究工作与岗位（PhD / RA / postdoc / professor），
> 并在当前 AI 环境（2026）下回答两个问题——
> ① 哪些项目还值得申请、值得把几年生命投进去，做的是**真正有意义的工作**；
> ② 哪些学者**眼界开放、有真知灼见**，值得主动发起合作交流。
>
> 本模块是「机会层」：把 `academic_research/` 的方向图落到**具体的人、岗位与入口**。

---

## 一、与既有模块的接缝 · Seams

| 模块 | 回答 | 本模块如何承接 |
|---|---|---|
| `discovery_atlas/`（science 域） | 去哪儿**找**（基础设施） | 复用其来源注册与 probe 惯例 |
| `academic_research/` | 什么**值得追**（方向 × 势能 × 可介入性） | frontier_scan 与 scholars 点名的方向/学者，在此展开为职位档案与导师档案 |
| `docs/culture_review/` | 当月文化动态 | 学界人事、重大资助、奖项公告可作线索来源之一 |

本模块补上缺的最后一问：**人往哪里去**（where does a person actually go）。

## 二、抓取范围 · Coverage

- **机构**：高校（含非 G14 的新秀与地区强校）、公立/私立研究所（Max Planck、CNRS、KAIST、中科院各所、艾伦研究所…）、交叉机构与独立实验室（Santa Fe、MATS、Konrad Zuse、Allen AI…）、企业研究院的学术化项目（FAIR、OpenAI Residency 之类）。
- **岗位**：PhD（含结构化博士项目、DTP/LITE 之类）、RA / 研究工程师 / 研究员、postdoc、教授/PI 教职（含 tenability 观察）、以及荣誉性入口（访问学者、fellowship、resident、visiting student）。
- **「可能发布」**：周期性招生项目按上一周期外推，一律标 ◐；未公开但按导师资助到期、组内节奏可合理预期的，记入 watchlist 并标 ◐，**绝不写成已存在的事实**。

## 三、评估标尺 · Six-dimension rubric（★1–5，每分附一句可证由）

| 维度 | 问题 | 证据来源 |
|---|---|---|
| **真问题性** | 去掉 AI 热点词后，这个问题本身还成立吗？产出是理解还是 benchmark 增量？ | 项目页原文、近 3 年组内发表的实际问题 |
| **AI 暴露度** | AI 进步让这个项目**增值**（判断、数据、现场、品味稀缺）还是**贬值**（生产环节可被替代）？ | 工作内容分解、领域自动化文献 |
| **导师质量** | 近 5 年：组内 PhD 中位毕业年限、去向、师生合著生态、独立指导 vs 放养/压榨 | 学术谱系（Mathematics Genealogy / 博士论文致谢页）、 alumni 页 |
| **资源与稳定性** | 资助来源与期限（ERC / DFG / NSF-CORE / 青基…）、计算与数据条件、组规模 | 资助公告、项目页、OSF/GitHub 活跃度 |
| **可及性** | 对「我」的申请画像的匹配与竞争面：签证/语言/经费通道/届期 | 招生页硬条件、往年录取观察（观察≠事实） |
| **眼界开放度** | 跨域接纳、允许失败、真名对话——决定「真正合作交流」是否可能 |  writings、演讲问答、对学生跨域流动的事后支持 |

**判断口径**（只记可核行为，不做人身评价）：
- 绿灯信号：导师支持学生独立署名一作、组内成员跨界后仍被引用合作、对失败实验公开复盘、招生写明"问题优先于方法"。
- 红旗信号：单年批量招生无经费来源、组内 PhD 延期率异常、把 LLM 微调当全部贡献、只回模板邮件、以 group list 替代个人面谈。

## 四、标记与纪律 · Marks & discipline

沿用仓库铁律（`harness/`、memory：zero-fabrication）：

- ✔ **命中** — 官方发布页/公告原文核实，带发布或检索日期；
- ◐ **预告/外推** — 周期推断、资助到期推断、传闻，注明推断依据；
- ◇ **待核** — 事实倾向存在但一手来源未落地，回源后升级；
- 撤回与更正照 ledger 惯例记入 `scan_log/`，不静默删改。

一时性事实（届期、薪酬、名额）随时间漂移：**每条档案带 `asof` 日期**，过期只允许复跑更新，不允许凭记忆续写。

## 五、数据模型 · Schemas

### opportunity（每文件一条，落 `opportunities/<type>/`）

```yaml
id: RX-<type>-<机构slug>-<yyyymm>
type: phd | ra | postdoc | professor | fellowship
institution:
country:
program:
pi:                # 或 hiring-committee
application_url:
deadline:          # ISO 或 "rolling" / ◐外推
funding:           # 薪酬/tuition/经费来源，能写数字才写数字
status: ✔ | ◐ | ◇
asof: YYYY-MM-DD   # 本条最后回源日期
dims: {q: , ai: , m: , r: , a: , o: }   # 六维分值，缺维写 "?"
verdict: 一句话（值得申请 / 值得先建立联系 / 观察 / 不投）
sources: [ url1, url2 ]
```

### scholar（每学者一卡，落 `scholars/`）

```yaml
name:
affiliation:        # asof 有效，机构漂移要重核
field:
homepage:
why_open: 眼界开放的**可证行为**（不是形容词）
what_real: 其"真问题"表述（引用其原文，标明出处）
entry: 合作入口（邮件惯例 / workshop / 访问项目 / 联合申请渠道）
risk: 排队时间、近年指导生态观察
stamps: [ ✔/◐/◇ + asof ]
```

## 六、产物 · Deliverables

- `opportunities/{phd,ra,postdoc,professor}/` — 机会档案（每文件一条，可 grep 可 diff）
- `scholars/` — 开放学者档案
- `indexes/shortlist.md` — 申请候选排序（每次复评更新一版）
- `indexes/contacts.md` — 合作交流名册与入口进展
- `scan_log/` — 检索台账：每轮的 query、命中、来源域、核实记录（可审计）
- 方法论变更须同步修订本 README 并记台账

## 七、启动路线 · Roadmap

1. **v0（本次）**：框架落地——目录、标尺、schema、README。
2. **v1 广扫**：按 `academic_research/frontier_scan.md` 七轴逐条展开，每轴先扫「已发布的博士/博后岗位 + frontier_scan 已点名学者的现组近况」，落 ✔ 档案与 scan_log。
3. **v2 评估**：跨档案比较，产 `indexes/shortlist.md`（含六维分值、verdict、申请成本估计）。
4. **常态**：每月复跑一轮到期与新增；文化月旦的学界人事线索流入本模块。
