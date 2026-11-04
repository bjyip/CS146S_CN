# 课堂解读：MCP、工具设计与 Code Mode

[教程目录](../../../README.md) | [MCP 与 OAuth](../../../chapters/04-mcp-oauth.md) | [Skills 与自动化](../../../chapters/05-skills-automation.md) | [本周作业](assignment-guide.md)

## 来源与定位

- 讲者：Mihail Eric；课堂日期：2026-10-01。
- 原文：[10-1-26-transcript.txt](https://themodernsoftware.dev/materials/10-1-26-transcript.txt)；2026-11-04 已读取可获取全文。
- 本页为中文解读，不是官方译文。转写只有开篇 `00:45` 时间戳，后文使用主题句定位，不捏造逐段时间。
- 范围到交给 Factory 团队为止；正文没有其完整 workshop，不总结未取得的培训内容。不将课务评分口头提醒替代原第 2 周作业 rubric。
- 未运行 MCP、OAuth、原 code-mode 示例或供应商 API；token 缩减与延迟没有本页复现结果。

## 1. 主题定位表

| 顺序 | 原文短句 | 主题 |
| --- | --- | --- |
| 1 | “Today we're focusing on MCP, tool calling, and beyond” | 从静态模型权重扩展到动态能力 |
| 2 | “The value is going from M × N to M + N” | 协议标准化减少重复连接器 |
| 3 | “The host is what we mean when we say Cursor” | Host、Client、Server、Tool 的角色 |
| 4 | “The client typically starts with discovery” | tools/list、定义入上下文、调用与结果返回 |
| 5 | “Great question about tool bloat” | 一对一包装 API 产生工具/上下文膨胀 |
| 6 | “design tool definitions around outcomes” | 以结果设计能力、明确参数和错误 |
| 7 | “It exposes just two tools: search and execute” | meta server、动态检索与代码执行 |

## 2. 标准化与完整协议不是同一层

讲者用三种 Agent 对三个服务的九条连接，说明统一协议后可抽象成三端加三端的六个适配。`M × N → M + N` 是集成复用的示意，不意味着业务授权、分页、限流或错误适配从此无需实现。

Host 承载 AI 应用，Client 在 Host 内维护与 Server 的会话，Server 提供能力，Tool 是可调用操作。原文用 Gmail、S3、DoorDash 和“总结 Jack 邮件”作概念示例，不代表本页确认这些具体官方 MCP Server 可用或已授权。

讲者从 `tools/list` 开始描述发现→定义入上下文→模型选择→Server 执行→返回循环。教程补充：这是简化流程，不是忽略初始化、版本/能力协商的实现指南。MCP 还可暴露资源和提示模板，不能把协议整体等同 tools/list 与 JSON 工具调用。

## 3. 工具数量少不是唯一目标

原文指出早期按每个 API endpoint 导出一个工具，导致数十到上百定义挤占上下文。讲者建议围绕结果而非内部小操作设计。

原付款比喻对比“按用户邮箱付款”与“取邮箱→查账户→按账户付款”。重点是把稳定业务编排放到实现里，减少模型必须正确串联的回合，并非授权模型自动支付。教程安全边界：真实支付不用于本页练习；合并工具不能省掉收款人、金额核验与人工审批。

讲者进一步要求明确参数、类型、docstrings 与错误。无类型的大字典或 `*args/**kwargs` 让模型难判断输入；具体错误提供诊断线索。教程补充：内部错误类型需转换为当前 SDK 兼容且不泄露秘密的工具错误，不能把完整堆栈当作可行动输出。

原问答提到从会议、转写和 Slack 三种搜索工具合并成带资源类型的 search_resource。这是基于 trace 观察后重构的思路，不要求先预测所有未来功能。合并后仍需枚举资源、稳定返回 ID 和验证真实组合，不是创建一个任意请求万能工具。

## 4. Search/Execute 与 Code Mode

讲者第二种方案是 meta MCP Server 只暴露 search 和 execute：先检索相关工具定义，再由动态生成代码串联调用，通常在 VM 等执行环境运行。原 Jira/Google Drive 示例搜索工单、读 Drive 内容并更新工单；检索可用关键词，也可语义搜索。

所谓代码“确定性执行”不代表模型生成的代码正确、安全或无副作用。运行时需要沙箱、网络与资源白名单、时间预算、参数验证和写入审批；结果裁剪也要保留失败与关键证据。两个元工具若拥有无限 execute 能力，安全风险可能比多个受限工具更大。

转写提到一些研究报告超过 90% token reduction，但没有完整实验方法、基线与任务分布；本页不把它当已复现比例或当前产品保证。上下文减少也可能来自过滤输出或任务简化，应以相同任务比较成功率、错误、调用次数、token 与时延。

## 5. OAuth 的讲解边界

讲者讨论第三方连接通常要认证、token 有寿命，失效后重新认证。它是概念讲解，不足以实现原作业要求的授权码交换、缓存、静默刷新和调用中失效处理。

不得把 token 放入模型上下文让它自行 HTTP 调用；秘密属于受控运行时。第 04 章与本周作业导读区分供应商刷新能力、最小 scopes、预览/提交以及长期 Server 的认证错误。课堂提及 OAuth 不代表所有 Server 都必须远程或使用同一种 OAuth。

## 6. 30 分钟隔离练习

教程案例是“从假会议笔记生成任务预览”，不是原 Jira/Drive 实验。预算零付费、30 分钟；仅本地文本和人工推演，不安装、不 OAuth、不调用模型、不执行动态代码、不写任何真实服务。

1. 0–10 分钟：列三个细工具 `search_notes`、`get_note`、`preview_tasks` 的 ID 流转与输出，标注只读和预览均不改变业务状态。
2. 10–20 分钟：对比一个结果导向工具与 search/execute 方案，统计纸面 schema 字段及所需步骤，说明删掉哪些无关信息与保留哪些权限检查。
3. 20–30 分钟：设计坏 ID、限流和认证撤销三种错误及下一行动；列 execute 所需沙箱、网络白名单、预算和禁止写入规则。

验收证据：三方案对照、ID 契约图、错误表和安全边界。纸面字符数不是 token 计费实测；人工步骤数不是模型实际调用次数。此练习不能证明 code mode 性能，也不等价于第 2 周真实 OAuth MCP 作业。

## 7. 局限与自测答案

来源是课堂概念图与口头实践总结，没有完整版本化实现；历史 Cursor 工具上限和 GitHub 工具数量不作为当前配置事实。MCP 不自动免除鉴权、限流、业务校验；tools 全量入上下文是讲者所述朴素实现，不是每个 Host 的必然行为。

**问：MCP Server 是否就是第三方 REST API？** 不是。它是协议能力提供端，可以包装 API，也可以提供本地能力；一对一映射不是设计要求。

**问：search/execute 只有两个工具是否天然安全？** 不是。实际权限取决于 execute 能做什么，必须限制运行环境、资源与写入。

**问：把三次调用合为一次必然更好？** 不一定。可以减少编排负担，但可能隐藏权限检查、错误与中间证据；应按具体任务及风险比较。
