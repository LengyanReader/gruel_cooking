# 进度记录 / Work Log

> 日期: 2026-03 (本周) · 项目: Language Stacking-Linguistic Weaving (语言叠置·语言织造)

## 本轮完成 (2026-03-xx, 首次入库 + 推送)

1. **LICENSE（MIT）** 加入项目根 `LICENSE`（Copyright (c) 2026 yunan），随仓库首次入库。
2. **修复 CI 红灯根因**：`web\build_learning.py` 的 `module_data_blocks` → `gojuon_views` 返回的是 **5 条 HTML 字符串**（螺旋五视图：引导 + 四旋 形/词/义/源 + 回望收束，`<section id="spiral-guide"/"ring-shape"/"ring-word"/"ring-sense"/"ring-root">`），而测试原按 dict 断言（`b.get(...)`）导致 `AttributeError: 'str' object has no attribute 'get'`。测试已改为**字符串 marker + 内容断言**，与实现对齐。
3. **全量测试**：`hy_py312` 环境 pytest 全绿（40 passed）。注意：base/miniconda 缺 `markdown`，必须在 `conda activate hy_py312`（CI 同）下运行。
4. **git 提交 + 推送** 至 `origin/main`（`https://github.com/LengyanReader/gruel_cooking.git`），含 `.github/workflows/learning-ci.yml`（pytest + 生成产物同步校验 `git diff --exit-code -- web/产物`）。
5. 移除不踞库杂物：`docs/language_stacking/index.html.bak`、`web/_tmp_classes.py`、`extract_classes.py`、`contemplative science/`（独立项目）。机密扫描 0 命中。

## 后续计划 (Next Steps)

- [ ] 帧图/产物同步口径抽查：CI 强制 `docs/language_stacking/learning` 与源码同步——验证 CI 首跑绿。
- [ ] 观察 `learning-ci.yml` 首跑结果：pytest + `git diff --exit-code` 双关卡。
- [ ] 数据增长触发点（~100 视频）：特征重评 + TimesNet/CTR-GCN 接口 —— 本 cookbook 分支「远程 GPU 主战场」启用时机。
- [ ] 双环境纪律：本地 base（备份/文档）vs `hy_py312`（跑测试/构建）；任何涉及 `build_learning` 的测试都要 `conda activate hy_py312`。

## 纪律提醒

- LICENSE 一旦加入不可回滚为私有；后续新增文件默认含 copyright 声明。
- 机密扫描结论（0 hits）已前置 commit；后续 push 前自动重扫。
```
