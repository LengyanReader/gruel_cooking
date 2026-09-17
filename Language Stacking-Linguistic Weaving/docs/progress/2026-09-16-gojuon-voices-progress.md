# 2026-09-16 进度 · 義環溯源 + 例句朗读盘

> 项目：Language Stacking-Linguistic Weaving（语言叠织）
> 本文件记录"五十音義環"当前磁盘真实状态与下一步。所有断言均基于磁盘真字节（git status / git diff / pytest 输出），非记忆。

## 已完成（已提交并推送）

- **commit `a7cf3b4`（已 push origin/main）**：主提交内容 = 義環一手出处溯源脚注可点击核验：
  - 季語 · 歳時記（ja.wikipedia.org/wiki/季語）
  - 美学 · 九鬼周造『「いき」の構造』（ja.wikisource + 青空文庫 cards/000065/files/393_1765.html）
  - 典故 · 本居宣長 · もののあはれ（ja.wikipedia.org/wiki/もののあはれ）
  - **注意**：美学的一手出处经网页核验修正为 `393_1765.html`（含正确 `5`；早前 `393_176.html` 为 404 死链，已修）。
- 文化坐标标注此前 commit 已挂名家一手出处（铃虫/芭蕉枯枝鸦/九鬼/本居宣长/白隐·松竹梅·万叶集）。

## 已实现（磁盘工作树，pytest 绿，但【未提交】）

- **例句朗读盘（sent-voices）**：`web/build_learning.py` 例句单元格现含
  `<span class="kana-voices sent-voices" data-h="{sent}" data-r="{sent_rom}">`，
  复用已有 `kanaSpeak / fillKanaVoices / jaVoices / fillKanaVoices` 引擎（浏览器 TTS 多声线，
  data-h=例句原文、data-r=例句罗马音，点击即合成音朗读）。
- 对应测试断言已随例（test_build_learning.py M 状态）。
- **pytest 全绿**：最近一次完整运行 `38 passed`（PYTEST_EXIT=0）。

## 【未提交】—— 下一步从这两行 git 状态开始

```
 M "Language Stacking-Linguistic Weaving/web/build_learning.py"
 M "Language Stacking-Linguistic Weaving/web/tests/test_build_learning.py"
```

下次继续的动作清单（按顺序）：
1. `git status --short` 复核仅上述 2 个文件。
2. `pytest`（web/tests）确认仍 38 绿。
3. `git add` 该两文件 → `git commit`（消息含「例句朗读盘 sent-voices，复用浏览器TTS多声线」）→ `git push origin main`。
4. 推送后复核 `git ls-remote origin main` 与本地 HEAD 一致。

## 纪律提醒（不可违反）

- 五十音表朗读按钮计数断言 = 46，勿与例句盘混淆（例句盘用独立 `sent-voices` 类）。
- 浏览器 TTS = 合成音，如实标注「合成音 · 浏览器TTS」；绝非真人/声优录音，不冒充。
- 一手出处 URL 必须可核验（网络实际存在），Kuki 青空链接规范形 = 393_1765（带5）。
