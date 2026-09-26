# articles — 文章书架 (The article shelf)

正式文章每篇一个 Markdown 文件，直接放在本目录下；网页查看器（`web/parser.py`）自动扫描 `articles/*.md` 并在首页列出，无需其他登记。

## 文章索引

- [证明不再稀缺：AI 时代的数学边界与数学家之定位 / When proofs are no longer scarce](proofs_no_longer_scarce.md) *(长稿：七章全景 + L0 导读与目录压缩版；约 1.9 万汉字，双语逐段并列)*
- [数学真理不由共识决定 / Mathematical truth is not a matter of consensus](ai_and_math.md) *(压缩版双语综述：前言 + 十节，三问为纲；其投稿包（提要、闸门、重建脚本）在 [`../essays/submission/`](../essays/submission/))*

## 写作规范

- 体例（论点→论据→论证→反诘→来源）、双语标注、来源四级标注（harness R-B）、AI 起草标注（§I.6）见 [`../essays/README.md`](../essays/README.md)；论说工作区（参考稿 `ref1/`、投稿包 `submission/`）也留在 `essays/` 下，不入渲染。
- 新增一篇：写 `articles/<slug>.md`（H1 首行为标题，`中文 / English` 双语格式），在本文索引加一行（MC-W4）。
- 与 `ai_and_math.md` 相关的手册式流程：`python essays/submission/build_reader.py` 重建生成视图，`python essays/submission/checks/refcheck.py` 与 `checks/review_scope.py` 为引用与范围闸门。
