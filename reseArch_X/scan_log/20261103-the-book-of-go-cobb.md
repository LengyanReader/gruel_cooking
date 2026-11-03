# 20261103 · 作品与作者调研：《The Book of Go》— William S. Cobb

**触发**：用户指定「看一下这个作品和作者，The book of go / Cobb, William S.，请进行相关探索、调研和梳理」。此非学者 scouting 对象，而是一件**作品—作者**考订，故只落台账、不建 scholar 档、不入 dialogue_map。

**方法**：延续 zero-fabrication 铁律——每条带 ✔ 命中 / ◐ 外推 / ◇ 待核 + asof；先立书目事实，再做**同名消歧**（本案要害），最后定位其同类谱系。

---

## 一、书目事实（均 ✔，asof 2026-11-03）

| 字段 | 值 | 来源 |
|---|---|---|
| 书名 | *The Book of Go*（部分馆藏副题 *Portable Go Set Included*） | Open Library / 馆藏 |
| 著者 | William S. Cobb | 题名页、Wikipedia "Go (game)" 引文 |
| 出版 | Sterling Publishing Co., New York，2002 年初版（full number line） | Biblio / eBay 初版著录 |
| ISBN | 0-8069-2729-1 / 978-0-8069-2729-9 | ✔ Open Library OL8451810W、Wikipedia |
| LCCN | 2001049835 | Open Library |
| 形态 | 125 页，22 cm；**螺旋装、附塑料封套纸盒便携围棋具**；棋盘硬纸板先于题名页；有索引 | Internet Archive 元数据 |
| 类别 | 少儿/零基础入门图谱，架上归 "Crafts and Hobbies · Games" | Sterling 书目分类 |
| 受评 | Goodreads ≈3.69 / 32 评价（样本极薄）；被 Wikipedia "Go (game)" 条目引为参考；◐ 英式围棋刊 British Go Journal #127 有 Matthew Macfadyen 书评（本轮未能取回全文） | Goodreads / Wikipedia / ◐ BGJ |

**定性**：一本**带玩具棋具的少儿启蒙图画书**，属礼品/兴趣产品，非严肃教程。英国围棋协会现行入门推荐书单（*Go: A Complete Introduction*(Matthews)、*Graded Go Problems* 等）**未收此书**——可作其学术分量偏低的旁证。

## 二、同名消歧（本案要害）✔

Open Library 把**至少四位互不相干的真人**并到同一作者键 `OL2819505A`「William S. Cobb」名下（`search.json?q=author:"William S. Cobb"` 返回 4 条，`author_key` 均含 OL2819505A）：

| 作品 | 年 / 出版社 | 实际领域 | 与围棋书关系 |
|---|---|---|---|
| **The Book of Go** | 2002 / Sterling | 少儿围棋启蒙 | **本案对象** |
| Plato's Sophist（译注） | 1990 / Rowman & Littlefield | 古希腊哲学·语文学者 | 异人 |
| Fire in the Islands of Spice Vol. 1 | 2023 / Helion | 军事史 | 异人 |
| Textbook of Hernia | 2016 / Springer（合著 W.W. Hope、G.L. Adrales） | 外科学 | 异人 |

四者领域互斥（古哲学／少儿桌游／军事史／外科），绝无同一人可能——**此为 Open Library 按姓名字符串自动并档的数据缺陷**（作者记录 OL2819505A 系 revision 1、2008 建、无任何 bio/personal_name，从未经人工梳理，佐证「机械并名」而非「确为一人」）。**结论：凡引《The Book of Go》，只可锚定「Sterling 2002 围棋书」这一身份，不得把另外三位的履历嫁接过来。**

## 三、围棋书 Cobb 本人：查无实据 ◇

- 多轮检索（出版记录、馆藏、Authority、Goodreads 作者页、二手书目）**均未浮现其个人传记**：无围棋段位/会籍、无作者小传、无其他 Sterling 同领域 titles 可系于其名下。
- LC 名字规范检索仅命中同名历史人物（1963 在校学生、1918 通讯兵、1899 共济会、马萨诸塞团兵员等噪声），**无对应现代规范条目**。
- **诚实判定**：就本仓目的而言，围棋书的 William S. Cobb 是一位**匿名/无传的 Sterling 兴趣书写手**（◇ 出身未确立）。「查无此人」本身即结论，不以猜测填充。

## 四、同类谱系定位（✔）

与西方同期入门书并列：Iwamoto《Go for Beginners》(1977, Pantheon)、Matthews《Go: A Complete Introduction》、*Teach Yourself Go*。Cobb 因**附便携棋具、装帧少儿化**，是其中**最偏低龄/礼品**的一本，教学深度与权威性居末；其在学术文献中的被引（如 ResearchGate "Games as cultural practice: postcolonial imaginations"）多属**随手列作通俗参考**，非方法依赖。

## 五、来源与动机追读

- **信息源**：Sterling（大众/礼品出版社，非专业围棋或学术社）委托编写，随书附玩具棋具——出版动机是**零售货架上的入门礼品**，而非围棋教育传承。这解释了为何文本浅、无段位背书、无作者生平沉淀。
- **对本仓的意义**：本案与 reseArch_X 的「学者发现」目标正交，是一例**作品—作者考订 + 数据库同名污染**的方法演练——与 `mvp/MVP-001`（discovery_atlas 登记层的 Wikidata 解析、bot-gating 梯度）同属「语料/元数据可信度」问题域，可作为「元数据同名合并会造成虚假作者连续性」的一个具体标本备查。

**空手而归 / 下一轮（若用户要深化）**：
- British Go Journal #127 Macfadyen 书评全文未取回（◐）。
- 围棋书 Cobb 身份未确立（◇）——除非 Sterling 内部稿件记录或初版版权页署名地址可查，否则大概率永久匿名。
- Goodreads「11 books」徽标疑亦为同名并档产物，未逐条核（◇）。
