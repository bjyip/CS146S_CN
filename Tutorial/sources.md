# 资料索引与来源边界

[返回目录](README.md)

本教程根据本地资料重新组织，正文中的解释与实验不是逐页翻译，也不声称复现了完整嘉宾讲座。以下链接可以溯源；完成学习不需要打开视频。

## 1. 课程定位

- [根 README](../README.md)：课程目标、前置条件、时间投入及 2025/2026 大纲。
- [Fall 2025 原始资料目录](../Resource/Fall2025/)：PPTX、课堂代码、设计文档及嘉宾 PDF。
- [2025 作业根目录](../_assignments/2025%20fall/)：完整练习及依赖配置。
- [2026 本地作业目录](../_assignments/2026%20fall/modern-software-dev-assignments-master/)：已取得第 1 至 3 周作业。

## 2. 逐章对应

| 教程 | 核心本地来源 | 教程补充 |
| --- | --- | --- |
| 00 环境与方法 | [安装说明](../_assignments/2025%20fall/README.md)、[pyproject](../_assignments/2025%20fall/pyproject.toml)、[Makefile](../_assignments/2025%20fall/week4/Makefile) | Windows 目录解释、实验设计 |
| 01 LLM 与提示 | [LLM](../Resource/Fall2025/week01-0922-intro-to-llms.pptx)、[提示](../Resource/Fall2025/week01-0926-effective-prompting.pptx)、[作业](../_assignments/2025%20fall/week1/assignment.md) | 泄漏辨析、精确率/召回率 |
| 02 Agent | [讲义](../Resource/Fall2025/week02-0929-building-a-coding-agent.pptx)、[代码](../Resource/Fall2025/week02-0929-completed-exercise.py)、[2026 trace](../_assignments/2026%20fall/modern-software-dev-assignments-master/week1/assignment.md) | 执行边界、预算与恢复 |
| 03 上下文与规格 | [AI IDE](../Resource/Fall2025/week03-1006-ai-ide-setup.pptx)、[设计模板](../Resource/Fall2025/week03-1006-design-document-template.md)、[行动项作业](../_assignments/2025%20fall/week2/assignment.md) | RePPIT 编排、示例契约 |
| 04 MCP/OAuth | [MCP](../Resource/Fall2025/week02-1003-custom-mcp-server.pptx)、[代码](../Resource/Fall2025/week02-1003-completed-exercise.py)、[2025 作业](../_assignments/2025%20fall/week3/assignment.md)、[2026 作业](../_assignments/2026%20fall/modern-software-dev-assignments-master/week2/assignment.md) | 信任边界、幂等和 OAuth 细化 |
| 05 自动化 | [Agent 管理](../Resource/Fall2025/week04-1013-agent-manager.pptx)、[Claude Code](../Resource/Fall2025/week04-1017-boris-cherny.pptx)、[2025 作业](../_assignments/2025%20fall/week4/assignment.md)、[2026 Skill](../_assignments/2026%20fall/modern-software-dev-assignments-master/week3/assignment.md) | 机制职责、失败门禁 |
| 06 仓库与并行 | [产品讲义](../Resource/Fall2025/week05-1020-ai-developer-product.pptx)、[Warp 作业](../_assignments/2025%20fall/week5/assignment.md) | 就绪度自评、任务隔离、后台状态 |
| 07 测试与审查 | [测试讲义](../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[审查讲义](../Resource/Fall2025/week07-1103-ai-code-review.pptx)、[审查作业](../_assignments/2025%20fall/week7/assignment.md) | 测试层次、变异练习、评测边界 |
| 08 安全 | [安全讲义](../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[Semgrep 作业](../_assignments/2025%20fall/week6/assignment.md) | 威胁模型、注入防护和回归 |
| 09 交付与运维 | [全栈](../Resource/Fall2025/week08-1110-end-to-end-app.pptx)、[三栈作业](../_assignments/2025%20fall/week8/assignment.md)、[事故响应](../Resource/Fall2025/week09-1117-incident-response-devops.pptx) | 验收、SLI/SLO 与演练 |
| 10 团队与工厂 | [README 2026 大纲](../README.md)、[自动化作业](../_assignments/2025%20fall/week4/assignment.md)、[交付作业](../_assignments/2025%20fall/week8/assignment.md) | 网关、受控流水线与自学评分 |

## 3. 阅读源代码时的四个提醒

- [自洽性脚本](../_assignments/2025%20fall/week1/self_consistency_prompting.py) 当前提示含预期答案。它不构成无泄漏的能力评测。
- [RAG 脚本](../_assignments/2025%20fall/week1/rag.py) 的字符串检查与多次尝试成功不等价于运行正确或首次可靠。
- [提取实现](../_assignments/2025%20fall/week2/app/services/extract.py) 已有 LLM 与回退逻辑；[测试](../_assignments/2025%20fall/week2/tests/test_extract.py) 主要使用 mock，需另测真实质量。
- [课堂 MCP 原型](../Resource/Fall2025/week02-1003-completed-exercise.py) 不应照搬不受限路径与 stdout 日志到生产。

这些提醒针对当前本地快照，不是在指责原课程练习目标。教学简化有价值，但必须解释简化边界。

## 4. 更新教程时

补入新资料时先确认其版本和内容，再调整章节及来源表。不要把仅存在于网页链接中的内容写成已阅读的本地依据。命令、认证流程与 SDK 示例涉及外部实时行为时，核对当前官方文档和实际版本。

本地翻译目录与中间提取文件属于已有工作，本教程没有修改它们；正式引用优先指向稳定原始资料，避免依赖翻译工作目录才能阅读。
