# extraction/ · 读物内容提取管线 · Lossless Intake Pipeline

Domain: Reading & IA. The **decode half** of intake: from a text in hand to a complete, accurate,
deep card — with no information, content, or depth lost. One pipeline per *kind* of material.

本目录是 reading → 卡片的「解码侧」：确保信息无损、内容无损、深度无损、证据无损、结构无损。
不同读物走不同透镜（kind-route），每层有最低捕获阈值（lossless ledger），由 `audit.py` 验账。

> Register 注册表：本目录接入根 harness 的 `Reading_IA/docs/workflows.md` **W1·Reading intake**。

---

## 结构 Structure

| 文件 | 作用 |
|---|---|
| `framework.md` | 无损原则 + 读物分型路由 + 分层透镜堆栈（唯一权威） |
| `prompts/novel.md` | 小说/虚构透镜提示词（literary fiction · sci-fi · crime） |
| `prompts/memoir.md` | 回忆录/证词透镜（life-writing · testimony） |
| `prompts/essay.md` | 论说/非虚构透镜（argument · medicine · social science） |
| `prompts/generic.md` | 通用兜底透镜（film · poetry · paper · 其他） |
| `audit.py` | 无损账本校验脚本（测试即文档） |

---

## 怎么用 How to use

1. **分型 kind-route**：读前先按 `framework.md` §2 给读物定 kind（novel / memoir / essay / generic）。
2. **加载透镜**：打开对应 `prompts/<kind>.md`，按其 10–12 层堆栈逐层提取。
3. **写账本 ledger**：卡片末尾填 `提取账本` 块（`framework.md` §4 的最小捕获阈值）。
4. **验账 audit**：`py -X utf8 Reading_IA/readings/extraction/audit.py` —— 任一阈值不达标 = 卡片未完成，补足而非删除。

> 原则（`framework.md` §8）：样本不足时宁可标 `◐` 进「未核」，绝不为了凑数编造；无损 = 完整 + 诚实，不是长。