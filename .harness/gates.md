# Gates · reseArch_X 科研评估验证门禁

> 基于 M3 (Verification & Gates) 与 M4 (Provenance)。
> 「完成」是证据闭环的状态，不是主观描述的完成。

## 1. 事实主张门禁 (Hard Gates)

- **[G1] 零臆造 (Zero-fabrication)**: `ethos`、`vision`、`what_real` 必须包含引用的原文。禁止使用 AI 总结替代学者本人的表述。
- **[G2] 来源可溯 (Traceability)**: 每个 ✔ 标记的事实必须带有 `(✔ 出处, YYYY-MM-DD)` 格式的指针。出处必须解析为一手来源（官网、论文 DOI、官方社交账号）。
- **[G3] 意群对齐 (Meaning-unit Fidelity)**: 跨语言引用（如英译中）必须保留学者的立场与限定词，关键术语需保留原文括号标注。

## 2. 软性评估准则 (Soft Gates / Rubrics)

- **[S1] 理论实践结合 (Theory-Practice Bridge)**: `theory_practice` 字段必须指明具体的软件、数据集或实验项目，而非空泛的“应用”。
- **[S2] 动向分析深度 (Trend Depth)**: `trends` 必须基于最近 6 个月的具体事件（如 2026 年 10 月的讲座），而非重复其职业生涯的常态。
- **[S3] 对话感 (Dialogue Hook)**: `dialogue_hook` 必须是不带索取请求的、基于 MVP 产物的专业探讨。

## 3. 视觉资产准则 (Visual Assets)

- **[V1] 照片来源**: `photo` 字段优先使用官方主页的 URL。若使用生成的占位图，必须标注为 `[AI Generated Placeholder]` 并提供 prompt 记录。

## 4. 验证流程 (Verification Protocol)

1. **Self-Audit**: Agent 在提交前，按上述 G1-G3 逐条复核，记录在 `.harness/PROVENANCE.md`。
2. **Harness Check**: 运行 `harness check` 确保结构完整。
3. **Human Gate**: “情怀”与“愿景”的解读由用户最终裁定。
