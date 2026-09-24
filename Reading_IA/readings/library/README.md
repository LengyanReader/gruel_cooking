# library/ 书目卡片

One Markdown file per book you have read, are reading, or seriously intend to read. Naming: `YYYY-slug.md` (reading year + short key).

每本已读、在读或认真计划读的书一个 Markdown 文件。命名：`YYYY-slug.md`（阅读年份 + 简短关键词）。

## Template 模板

Copy `_template.md` and fill it. Keep one card per book, no matter how brief.

**戴透镜提取**：先按 `../extraction/framework.md` 定型（novel / memoir / essay / generic），
用对应 `../extraction/prompts/<kind>.md` 逐层提取，最后填 `extract_ledger` 验账
（`py -X utf8 ../extraction/audit.py`）——深度无损由账本保证，不只靠手感。

复制 `_template.md` 填写。每书一卡，无论多短。

## Status conventions 状态约定

- `unread` — queued, not started 排队未读
- `reading` — in progress 在读
- `done` — finished 读完
- `re-reading` — returning 重读
- `dnf` — did not finish; record why 未读完（记录原因）

## Index 索引

*Cards will be indexed here as they accumulate. A `data/books.json` machine index may be generated in phase 1 (see `web/README.md`).*

*卡片积累后在此建立索引。阶段一可能由脚本生成 `data/books.json`（见 `web/README.md`）。*