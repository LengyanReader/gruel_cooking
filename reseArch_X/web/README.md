# reseArch_X/web · 面板构建

`build_reseArch_X.py` 把 `scholars/`、`opportunities/`、`mvp/`、`indexes/dialogue_map.md`、`scan_log/` 里的人写内容，重新组装为一份**只读面板**：`docs/reseArch_X/index.html`。

面板是「视图」，不是「源」——所有事实仍在 `.md` 里；页面每次由脚本重生，改动只需提交 `.md`。

## 用法

```powershell
# 在项目根
python -X utf8 reseArch_X/web/build_reseArch_X.py
# → [ok] wrote docs/reseArch_X/index.html (76,2xx chars) · scholars=14 · opportunities=9 · scans=3

# 本地预览（file:// 亦可直用，数据已内联）
python -X utf8 -m http.server 8765 --directory docs
# → http://localhost:8765/reseArch_X/
```

依赖：Python 3.10+，PyYAML 未必需（自带解析器；schema 里出现 `?` 与「冒号在字符串里」都能吃下）。

## 什么进面板，什么不进

| 面板段 | 数据来源 | 更新方式 |
|---|---|---|
| 盘面速览（tiles） | 各目录文件计数 + 最大 `asof` | 自动派生 |
| 对话名册（主视图） | `indexes/dialogue_map.md` 表格行 + 排序逻辑 | 直接在 `dialogue_map.md` 里改行/改序 |
| 学者卡片 | `scholars/<slug>.md` yaml-in-fence | 编辑档案即可 |
| 方向轴覆盖 | `scholars/` × `AXES` × `SCHOLAR_AXES` | 新增轴：改 `build_reseArch_X.py` 三处常量 |
| MVP 轨道 | `mvp/README.md` 表格 + `MVP-*.md` 单件 | 状态改在 `mvp/README.md` |
| 机会档案 | `opportunities/<type>/RX-*.md` | 编辑即可 |
| 六维标尺 | `README.md` 第三节 | 硬编码在 template 里；改文案改 template |
| 调研日志 | `scan_log/YYYYMMDD-vX-slug.md` | 文件名即时间线；正文首段=摘要 |

## Schema 契约

学者 yaml-in-fence 必备字段（缺失即卡片对应处留空，不崩）：
```yaml
name:          # 卡片标题
tier:          # 卓越开明 | 有潜力  —— 决定卡片顶栏色
affiliation:
field:
current_work:  # list of strings，回源带日期
  - 「…」 ✔ <source> YYYY-MM-DD
why_open:      # 眼界开放的可证行为
mvp:           # 可造之 MVP 一句话
dialogue_hook: # 一句不带索取的真实话柄
mode:          # 合作 | 受教 | 两者 —— 参与筛选
stamps:
  - {mark: ✔, asof: YYYY-MM-DD}
```

机会 yaml-in-fence 必备字段：
```yaml
id:            # RX-<type>-<slug>-<yyyymm>
type:          # phd | ra | postdoc | professor | fellowship
institution:
country:
deadline:
status:        # ✔ | ◐ | ◇
asof:
dims: {q, ai, m, r, a, o}   # 允许 "?" 值
verdict:
sources: [...]
```

## 添加新方向轴（策展判断，不入 .md）

编辑 `build_reseArch_X.py` 三处：

1. `AXES` 列表加一条 `(zh, key, desc)`；
2. `SCHOLAR_AXES` 里给命中的学者 slug 补上该 `key`；
3. `OPP_AXES` 里给命中的机会 id 补上该 `key`；

重跑 build。面板「方向轴覆盖」段会即时把新轴加进 heat grid；若学者数为 0，格子自动挂「空缺」标。

## 已知不做

- 不做「增量重建」——全扫全建，规模 <100 文件时不必要；
- 不接 GitHub Actions——`.md` 改完手动 build 提交 `docs/reseArch_X/index.html` 即可；若要接，参照 `.github/workflows/reading-ci.yml` 起一份 `research-ci.yml`；
- 不做多语正文——`.md` 源是中文一手，页面 chrome 双语，卡片内容不 EN 化。
