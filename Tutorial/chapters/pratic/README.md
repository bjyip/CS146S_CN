# 教程自学实验

这里是中文教程的自学改编，不是 2025 或 2026 原作业目录。只想读原理时回到[教程首页](../../README.md)。

## 离线实验

从仓库根目录运行，需要 Python 3.10+，建议使用已配置的 3.12。不需要 Poetry、API Key 或 Ollama。

```powershell
python Tutorial/chapters/pratic/agent_lab.py
python -B -m unittest discover -s Tutorial/chapters/pratic -p test_labs.py -v
```

第一条显示三条排序轨迹，第二条运行确定性测试。这些结果验证本地模拟程序，不代表真实模型会做出同样的决策。参见[第 02 章](../02-coding-agent.md)。

## 远程 API 练习

在 PowerShell 中，从仓库根目录进入自学目录。已有可用的 Conda 环境时先激活，不必重复新建。

```powershell
Set-Location Tutorial/chapters/pratic
python --version
poetry install --no-interaction
```

在运行脚本的终端环境中设置 `ZAI_API_KEY` 和 `ZAI_MODEL`，模型可用时例如 `glm-5.2`。不要把真实密钥填进 Git 已跟踪的 `week1/.env`。联网前先确认账户权限、调用预算与数据政策；不上传真实笔记或提交密钥。依赖表中的 Python `ollama` 包不等于安装或启动 Ollama 服务，这组脚本不需要服务或本地模型。

```powershell
poetry run python week1/k_shot_prompting.py
```

它会实际请求智谱，成功匹配时输出 `SUCCESS`，不匹配可能重试，当前最多五次尝试。如果预算不足以覆盖五次，不运行这条命令，改做离线实验。随后可按需运行同目录的 `chain_of_thought.py`、`tool_calling.py`、`rag.py` 或 `reflexion.py`。单题通过只说明这次结果符合对应判据。

## 贯穿项目：行动项提取器

这是[第 10 章](../10-capstone.md)的起步检查点，不是完整项目。为避免把演示候选当成通用算法，`preview` 只读取固定假会议的候选，**不写数据库**；`save` 保存的是人亲自确认并传入的文字，不会自动接收候选。下面的例子把候选中的「日志」修订为「登录日志」。从仓库根目录运行，把数据库路径换成专用的空练习路径，不使用业务库。

```powershell
python -X utf8 Tutorial/chapters/pratic/action_items.py preview
python -X utf8 Tutorial/chapters/pratic/action_items.py --db "$env:TEMP/cs146s-action-items.sqlite3" save --confirm "明天检查登录日志"
python -X utf8 Tutorial/chapters/pratic/action_items.py --db "$env:TEMP/cs146s-action-items.sqlite3" list
```

预期：第一条只显示候选；第二条返回新记录 ID；第三条启动新进程，仍能读取同一个 ID 和修订后的文本。省略 `--confirm` 应报错，不能写入；同一库重复保存会产生新记录，目前没有幂等保证。测试还演示了候选生成失败时保留错误、使用固定规则降级，两者不会自动保存。

| 接下来做什么 | 对应章节与证据 |
| --- | --- |
| 用可核对规则替换固定假数据，补上无任务和拒绝条件 | [01](../01-llm-prompting.md)、[03](../03-context-spec.md)：先写预期，再看输出与规则是否一致 |
| 将模型限制在生成候选，保留确认和保存边界 | [02](../02-coding-agent.md)、[04](../04-mcp-oauth.md)：记录调用和拒绝，不把模型回复当授权 |
| 加入真实评测、失败回归和恢复记录 | [07](../07-testing-review.md)、[09](../09-delivery-operations.md)：区分模型失败、规则降级与已保存结果 |

这个起点不包含完整 CRUD、真实模型评测、OAuth 或生产级回滚，不能据此勾选综合项目的全部里程碑。
