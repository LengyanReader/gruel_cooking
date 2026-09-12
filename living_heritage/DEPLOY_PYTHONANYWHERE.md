# 部署到 PythonAnywhere(免费,完整持久化)

站点是一个纯 Python + SQLite 的自建 HTTP 服务(`app/router.py` 原生的
`socket/http.server`)。PythonAnywhere 不运行裸 socket,只执行 WSGI → 适配层在
`app/wsgi_app.py`(`application`)。放上去后**数据(含笔记、计划编辑)持久保存**;
免费版限 100 CPU 秒/天,个人浏览够用,超限会临时下线、次日恢复。

## 1. 注册 (免费)
- 打开 https://www.pythonanywhere.com → Sign up → **Beginner (Free)**。
- 记住你的用户名(下文 `<username>`),例如 `lengyanreader`。

## 2. 拉代码 + 建环境 (Bash console)
登录后 **Consoles → Bash**,依次执行:

```bash
git clone https://github.com/LengyanReader/gruel_cooking.git
cd gruel_cooking/living_heritage
python3.12 -m venv ~/.venvs/lh
source ~/.venvs/lh/bin/activate
pip install -r requirements.txt
python -m app.seed       # 生成 data/living_heritage.db 并灌入种子
```

> 若控制台没有 `python3.12`,用 `python3.11`(代码要求 3.10+)。

## 3. 添加 Web 应用
**Web → Add a new web app**:
- Python web app → Manual configuration → Python 3.12。
- **Source code:** `/home/<username>/gruel_cooking/living_heritage`
- **Virtualenv:** `/home/<username>/.venvs/lh`
- 点「WSGI configuration file」的链接,把内容**全部替换**为下面模板
  (把 `<username>` 换成你的用户名,`<token>` 换成你的管理员令牌):

```python
import sys
sys.path.insert(0, '/home/<username>/gruel_cooking/living_heritage')   # ← 换成你的用户名
import os

os.environ['LH_ADMIN_TOKEN'] = '<token>'              # 管理员口令,留空则 admin 关闭
os.environ['LH_BASE_URL'] = 'https://<username>.pythonanywhere.com'   # OG/SEO 绝对链接,可留空

from app.wsgi_app import application as application
```

## 4. 生效
回到 **Web** 页点 **Reload** → 打开 `https://<username>.pythonanywhere.com/`
应看到站点首页;`/plan`、`/admin`(用上一步 token 登录)均可用。
后台写的数据写入 `/home/<username>/gruel_cooking/living_heritage/data/living_heritage.db`,
**不会因重启丢失**。

## 5. 更新代码
1. Bash console: `cd ~/gruel_cooking && git pull`
2. 若 `data/seeds/` 有更新:`cd living_heritage && python -m app.seed`
3. **Web → Reload**。

## 已知限制(免费版)
- 100 CPU 秒/天;超限站点当天暂停、次日恢复(个人使用通常不会触发)。
- 代码内**出站** HTTP 受限(白名单);本站所有资源(含 KaTeX)均为本地,不受影响。
- 免费版绑定 `<username>.pythonanywhere.com` 子域;自定义域名需付费版。
- 静态文件经由 WSGI 由应用自己服务(与本地一致);若日后想省 CPU,可在
  Web 页 **Static files** 里把 `/css`、`/js`、`/img`、`/vendor` 映射到
  `app/static/` 下对应目录(需调整 `templates/base.html` 的引用前缀)。