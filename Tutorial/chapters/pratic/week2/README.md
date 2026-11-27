# 第 2 周自学：行动项提取器

网页把笔记交给 FastAPI，可选择本地规则提取或阿里云百炼的 Qwen 提取。只有勾选「保存原始笔记」且提取成功才会写入本目录的 `data/app.db`；提取出来的行动项不入库。它与 2025 原作业的数据和代码分开，不需要 Ollama。

在上一级 `Tutorial/chapters/pratic` 目录、已有 `cs146s` 环境中运行：

```powershell
poetry run python -m uvicorn week2.app.main:app --reload --port 8001
```

打开 <http://127.0.0.1:8001/>，输入 `- 周三前补齐登录页测试`。先不勾选保存，确认能提取待办；再勾选保存，提取后点「列出笔记」，确认能看到完整原文。接口文档在 <http://127.0.0.1:8001/docs>。

阅读顺序：[网页](frontend/index.html)发请求 → [路由](app/routers/notes.py)处理参数 → [提取函数](app/services/extract.py)识别标记 → 勾选保存时由[数据库模块](app/db.py)写入。FastAPI 应用从[入口文件](app/main.py)加载路由和网页。

在同一个 Poetry 目录运行离线测试。测试使用临时数据库，不会更改网页练习数据：

```powershell
poetry run python -m pytest week2/tests -v
```

## Qwen 提取练习

「LLM 提取」按钮通过 `POST /action-items/extract-llm` 调用 [`extract_action_items_llm(text)`](app/services/extract.py)。「规则提取」继续使用 `POST /action-items/extract`，不联网。后端使用现有 OpenAI SDK 调用[百炼 Function Calling](https://help.aliyun.com/zh/model-studio/qwen-function-calling)，通过 `tools` 传入 JSON Schema，再解析 `tool_calls` 里的参数，不执行外部工具，也不发第二次模型请求。

真实调用前，参照 [`week2/.env.example`](.env.example) 在本地 `week2/.env` 设置 `DASHSCOPE_API_KEY` 和 `DASHSCOPE_MODEL`，旧的 `ZAI_*` 配置不再使用。`qwen-plus` 是示例模型，不代表你的账户对它有免费额度。`DASHSCOPE_BASE_URL` 不填时使用北京公共地址；如果控制台给出地域或业务空间专用的 OpenAI 兼容地址，就用该地址（以 `/compatible-mode/v1` 结尾，不加 `/chat/completions`）。密钥、模型和地址应对应同一地域及业务空间。

从 `Tutorial/chapters/pratic` 启动，修改 `.env` 后需停止并重新启动 Uvicorn：

```powershell
poetry run python -m uvicorn week2.app.main:app --reload --port 8001 --env-file week2/.env
```

`week2/.env` 已被 Git 忽略；不要将真实密钥写入模板或 Git 已跟踪的第 1 周 `.env`。调用前确认模型支持工具调用、账户有权限，并确认免费额度与用完后的扣费设置。

点击「LLM 提取」会发送笔记到百炼，即使不勾选保存也会发送；只使用练习笔记。空白笔记不会发给模型。模型调用失败或输出格式不合法时，页面显示错误，不回退到规则提取，也不保存原笔记。上面的离线测试使用模拟响应，不需要真实密钥或联网。
