# reseArch_X 审计脚本

可复跑的证据工具。**不是**面板构建的一部分（那是 `reseArch_X/web/build_reseArch_X.py`），也不受 `check_all.py` 门禁约束——这里放的是「下次再审一遍」用的探针。

## audit_homepages.py — 学者主页三查

```bash
python scripts/scratch/reseArch_X/audit_homepages.py            # 只做结构检查
python scripts/scratch/reseArch_X/audit_homepages.py --probe    # 再加 HTTP 探活
python scripts/scratch/reseArch_X/audit_homepages.py --probe --delay 3 --timeout 40
```

三查按「出过事的频率」排序：

1. **占位字段**：`homepage` 是散文而不是 URL（`(UNC)`、`无个人主页 ◇`）。渲染层会把它变成「暂无稳定主页 ◇」的 span，不会产生坏链，但仍需定期回看：这个人后来有没有主页了。
2. **URL 后紧跟中文括注**：真缺陷。`https://x.org（个人页）` 会保留 `<a>`，但 href 被括注污染。v16 修了 2 档、v17 又补扫出 3 档（Sicart / 王思明 / West）。**命中此项时退出码为 1**，可接进 CI。
3. **可达性**：非 200 逐条列出，供人工分诊。

### 怎么读探活结果

- `200` — 通过。但注意：**200 不等于「这页是这个人」**。`jszy.whu.edu.cn` 对任意 slug 都返回 200 的 error 页；`uni.lu`、`psych.ox.ac.uk` 对虚构路径返回 202 空体。新落一条主页前，必须拉正文确认人名/机构（v17 的教训）。
- `403` — 多为反爬（CBDB、SAIS、Princeton 社会系、SAS、AWB）。浏览器能开，**不是**死链，不要据此改档。
- `000` — 本网不可达。**先复测再下结论**：连续探 40+ 条之后本机会成批返回 000（抖动），间隔 6–8 秒再测往往恢复（v17 复扫时 Davidson 就从 000 回到 200）。连续多轮仍 000 才算线索。

### 与审计台账的对应

| 台账 | 范围 |
|---|---|
| `reseArch_X/scan_log/20261105-v16-links-nav-influence.md` | 42 个去重 URL 首轮探活，修 8 档 |
| `reseArch_X/scan_log/20261111-v17-homepage-audit.md` | 16 档逐条实查：9 档落官方页、3 档改 ORCID、2 档明写无页；并订正 Sawin 任职 |
