# 资料索引与来源边界

[返回目录](README.md)

本教程根据本地资料重新组织，正文中的解释与实验不是逐页翻译，也不声称复现了完整嘉宾讲座。以下链接可以溯源；完成学习不需要打开视频。

本次核对日期为 2026-11-04，增量基于 `a1add0e` 相对第一父提交的合并差异。README 新增作业入口不代表作业文件新增；本次 `_assignments/` 没有变化，2026 仍为本地第 1 至 3 周。

## 1. 课程定位

- [根 README](../README.md)：课程目标、前置条件、时间投入及 2025/2026 大纲。
- [Fall 2025 原始资料目录](../Resource/Fall2025/)：PPTX、课堂代码、设计文档及嘉宾 PDF。
- [2025 作业根目录](../_assignments/2025%20fall/)：完整练习及依赖配置。
- [2026 本地作业目录](../_assignments/2026%20fall/modern-software-dev-assignments-master/)：已取得第 1 至 3 周作业。

## 2. 逐章对应

| 教程 | 核心本地来源 | 教程补充 |
| --- | --- | --- |
| 00 环境与方法 | [2025 安装说明](../_assignments/2025%20fall/README.md)、[2025 pyproject](../_assignments/2025%20fall/pyproject.toml)、[2026 安装说明](../_assignments/2026%20fall/modern-software-dev-assignments-master/README.md)、[2026 pyproject](../_assignments/2026%20fall/modern-software-dev-assignments-master/pyproject.toml)、[Makefile](../_assignments/2025%20fall/week4/Makefile) | 双年份目录、算法诊断、访问验收与实验设计 |
| 01 LLM 与提示 | [LLM](../Resource/Fall2025/week01-0922-intro-to-llms.pptx)、[提示](../Resource/Fall2025/week01-0926-effective-prompting.pptx)、[作业](../_assignments/2025%20fall/week1/assignment.md) | 泄漏辨析、精确率/召回率 |
| 02 Agent | [讲义](../Resource/Fall2025/week02-0929-building-a-coding-agent.pptx)、[代码](../Resource/Fall2025/week02-0929-completed-exercise.py)、[2026 trace](../_assignments/2026%20fall/modern-software-dev-assignments-master/week1/assignment.md) | 执行边界、预算与恢复 |
| 03 上下文与规格 | [AI IDE](../Resource/Fall2025/week03-1006-ai-ide-setup.pptx)、[设计模板](../Resource/Fall2025/week03-1006-design-document-template.md)、[行动项作业](../_assignments/2025%20fall/week2/assignment.md) | RePPIT 编排、示例契约 |
| 04 MCP/OAuth | [MCP](../Resource/Fall2025/week02-1003-custom-mcp-server.pptx)、[代码](../Resource/Fall2025/week02-1003-completed-exercise.py)、[2025 作业](../_assignments/2025%20fall/week3/assignment.md)、[2026 作业](../_assignments/2026%20fall/modern-software-dev-assignments-master/week2/assignment.md) | 信任边界、幂等和 OAuth 细化 |
| 05 自动化 | [Agent 管理](../Resource/Fall2025/week04-1013-agent-manager.pptx)、[Claude Code](../Resource/Fall2025/week04-1017-boris-cherny.pptx)、[2025 作业](../_assignments/2025%20fall/week4/assignment.md)、[2026 Skill](../_assignments/2026%20fall/modern-software-dev-assignments-master/week3/assignment.md) | MCP/Skill/CLI 组合、作用域、渐进披露与门禁 |
| 06 仓库与并行 | [产品讲义](../Resource/Fall2025/week05-1020-ai-developer-product.pptx)、[Warp 作业](../_assignments/2025%20fall/week5/assignment.md) | 就绪度自评、独立任务、指令漂移、隔离与后台状态 |
| 07 测试与审查 | [测试讲义](../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[审查讲义](../Resource/Fall2025/week07-1103-ai-code-review.pptx)、[审查作业](../_assignments/2025%20fall/week7/assignment.md) | 测试层次、风险分层、专业审查、沙箱与评测 |
| 08 安全 | [安全讲义](../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[Semgrep 作业](../_assignments/2025%20fall/week6/assignment.md)、[非官方商业页](../Resource/Claude-Code%E5%85%85%E5%80%BC/README.md) | 威胁模型、注入防护、凭据披露辨析和回归 |
| 09 交付与运维 | [全栈](../Resource/Fall2025/week08-1110-end-to-end-app.pptx)、[三栈作业](../_assignments/2025%20fall/week8/assignment.md)、[事故响应](../Resource/Fall2025/week09-1117-incident-response-devops.pptx) | 验收、SLI/SLO 与演练 |
| 10 团队与工厂 | [README 2026 大纲](../README.md)、[自动化作业](../_assignments/2025%20fall/week4/assignment.md)、[交付作业](../_assignments/2025%20fall/week8/assignment.md) | 网关、受控流水线、开源贡献闭环与独立自学评分 |

## 3. 阅读源代码时的四个提醒

- [自洽性脚本](../_assignments/2025%20fall/week1/self_consistency_prompting.py) 当前提示含预期答案。它不构成无泄漏的能力评测。
- [RAG 脚本](../_assignments/2025%20fall/week1/rag.py) 的字符串检查与多次尝试成功不等价于运行正确或首次可靠。
- [提取实现](../_assignments/2025%20fall/week2/app/services/extract.py) 已有 LLM 与回退逻辑；[测试](../_assignments/2025%20fall/week2/tests/test_extract.py) 主要使用 mock，需另测真实质量。
- [课堂 MCP 原型](../Resource/Fall2025/week02-1003-completed-exercise.py) 不应照搬不受限路径与 stdout 日志到生产。

这些提醒针对当前本地快照，不是在指责原课程练习目标。教学简化有价值，但必须解释简化边界。

## 4. 更新教程时

补入新资料时先确认其版本和内容，再调整章节及来源表。不要把仅存在于网页链接中的内容写成已阅读的本地依据。命令、认证流程与 SDK 示例涉及外部实时行为时，核对当前官方文档和实际版本。

本地翻译目录与中间提取文件属于已有工作，本教程没有修改它们；正式引用优先指向稳定原始资料，避免依赖翻译工作目录才能阅读。

## 5. 本次新增阅读与使用边界

“已阅读”指本次增量工作期间取得正文，不表示已验证产品运行或复现作者实验。外部页面可能持续更新，下表记录本轮读取状态，不保证永久可访问。

| 来源 | 类别与状态 | 用于何处及限制 |
| --- | --- | --- |
| [Claude Code 安装](https://code.claude.com/docs/en/setup) | 官方产品文档，已阅读 | 00、02 安装与访问验收；资格和平台能力仍按当前版本核对，不固定价格 |
| [Claude Code 定制机制](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) | 官方产品说明，重试后已阅读 | 05 加载作用域、Skill、Subagent、Hook 的职责；不泛化版本机制，不将模型 Hook 判断说成确定性 |
| [Factory AGENTS.md](https://docs.factory.com/harness/agents-md) | 产品文档，已阅读 | 05、06 短规则、命令和作用域；Droid 的发现与优先级不是通用标准 |
| [Writing a good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md) | 行业经验文章，已阅读 | 05 渐进披露、权威引用、确定性检查；行数和指令数经验阈值不是科学定律 |
| [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills) | 作者观点，已阅读 | 05 能力接口与过程知识组合；远程服务不自动保证安全，偏好不是普遍结论 |
| [Cloudflare AI Code Review](https://blog.cloudflare.com/ai-code-review) | 团队工程实践，已阅读 | 07 专业角色、协调、去重、上下文、超时与预算；不照搬成本、准确率、审批或紧急绕过策略 |
| [Greptile Code Review Agent](https://www.greptile.com/blog/how-to-build-a-code-review-agent) | 行业经验文章，已阅读 | 07 diff 之外的上下文、沙箱验证与模型比较；效果数字和模型偏好仅为作者报告 |
| [Codex authentication](https://developers.openai.com/codex/authentication) | 官方链接，本轮读取返回 403 | 仅登记；不据此写入当前套餐资格或认证步骤 |
| [非官方开通补充页](../Resource/Claude-Code%E5%85%85%E5%80%BC/README.md) | 本地商业页，已阅读 | 08 凭据安全案例；不推荐第三方会话提交，不验证购买与价格，不作为官方资格依据 |

## 6. 仅登记的讲义与外链

以下链接来自本次 README 合并增量，仅作导航。未取得正文时不生成讲义摘要；教程相关解释来自已读资料或明确标注的扩展，不要求观看视频。未读取与不存在是不同状态。

| 课程位置 | 新链接 | 本轮状态 |
| --- | --- | --- |
| 2026 第 3 周 Lee Robinson | [幻灯片](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link) | 仅登记，未读取正文 |
| 2026 第 4 周定制环境 | [幻灯片](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit?usp=sharing) | 读取发生传输错误，未取得正文 |
| 2026 第 5 周仓库就绪 | [幻灯片](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit?usp=drive_link) | 仅登记，未读取正文 |
| 2026 第 5 周仓库就绪 | [视频](https://www.youtube.com/watch?v=ShuJ_CN6zr4)、[X 帖文](https://x.com/trybasis/status/2056881705269580023) | 仅登记，未观看或读取；不是无视频学习前提 |
| 2026 第 6 周风险分层 | [X 帖文](https://x.com/addyosmani/status/2114604912520921136) | 读取发生传输错误，未取得正文 |
| 2026 第 6 周 Agentic Review | [幻灯片](https://docs.google.com/presentation/d/1u8WYtFj0O9yc4H4JX9D4URYKhDzvrAGKLzn38DXSrak/edit?usp=drive_link) | 仅登记，未读取正文 |

第 8 周 Rajesh Bhatia、第 9 周 Elad Gil 与 Amjad Masad 的新增嘉宾安排，以及第 10 周团队 Coding Agent/Software Factory 调整，按根 README 登记课程安排；未读取相应讲座，不推断嘉宾主张。群二维码更新不影响教程知识内容。原课程评分与本教程自学评分分别维护，不由新增宣传页改变学习验收。
