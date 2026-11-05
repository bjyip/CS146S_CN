# MCP 简介：统一连接，不自动统一权限

[本周入口](README.md) | [第 04 章](../../../chapters/04-mcp-oauth.md)

## 1. 来源与范围

- 原文：[Model Context Protocol (MCP): A comprehensive introduction for developers](https://stytch.com/blog/model-context-protocol-introduction/)，Reed McGinley-Stempel，Stytch，2025-03-28。
- 核对日期：2026-11-05。读取文章正文，从 Executive summary 到 Conclusion，包括示例代码、历史认证讨论与调试建议；未独立读取链接中的论文、SDK、产品文档或图像。
- 定位：供应商撰写的入门文章，不是协议规范或已验证 SDK 教程。以下是中文解读，不是官方译文；未安装、连接或执行 MCP。

阅读目标：能画出 Host、Client、Server、模型和第三方服务的位置，解释为什么模型输出一个调用意图仍不等于操作已经发生。

## 2. What is MCP / Why MCP is Valuable：适配器统一哪一层

作者用通用适配器类比 MCP。过去每个 AI 应用分别适配不同服务；统一协议后，一个支持 MCP 的应用可以复用不同 Server 暴露的能力。统一的是发现和通信边界，不是所有服务的业务语义。

Host 是承载用户任务的应用；它运行 Client 组件，由 Client 维护与 Server 的协议连接。Server 实现外部能力，可以调用 API、查数据库或访问文件。模型通常看到工具说明并提出调用，Host 将意图转换为实际协议请求，然后把结果放回模型可使用的上下文。

三个能力不能混称：Tool 是可调用动作，Resource 是可读取上下文，Prompt 是可复用提示模板。Claude Desktop、Cursor 这类产品在此是 Host 示例，不是等同于 `get_weather` 的协议 Tool。原文 “MCP clients and tools” 小节在这点上用词宽泛，学习时应按角色区分。

原文 CRM → 邮件 → 数据库的组合例子说明可组合性，不证明跨服务事务、安全审批或失败恢复已经实现。邮件发出后数据库写入失败，简单重跑可能重复发信；这些责任仍在工具与执行系统。

## 3. Architecture / Technical deep dive：发现与执行分开

文章按连接、发现、模型选择、协议调用、结果返回五步解释链路。初始化用于协商版本与能力；`tools/list` 取得说明；`tools/call` 才要求执行。列出一个工具不代表当前用户获准访问其所有资源。

原文天气工具的 JSON-RPC 请求演示了 `jsonrpc`、请求 `id` 和 `method`。但列工具响应把 `result` 直接写成数组，并把输入约束写成简化 `schema`；不能拿这段作为互通测试夹具。MCP 工具列表的关键结构是 `result.tools`，工具输入使用 `inputSchema`。具体版本的完整字段、初始化顺序及错误语义仍须核对规范和 SDK。

其 Anthropic 示例明确属于伪代码：`complete`、`send`、模型名称和消息结构不能当成当前 SDK 可运行接口。尤其不应把任意工具结果提升为 system 指令；结果应按真实模型 API 的工具消息契约关联调用，并保持不可信数据边界。

## 4. Comparing approaches：协议与框架互补

原文比较手写 API 集成、历史 ChatGPT Plugins 和 LangChain。可以保留的区别是：MCP 规定跨进程的通信和发现方式，框架组织 Agent loop，模型的 function calling 表达调用意图，三者可以协作。

不能把比较表中的“即插即用”“持续上下文”“安全”等标签当成保证。自定义集成也可采用 OAuth 和多步循环；支持协议的 Client 仍可能不支持某个 transport、能力或版本。Server 也仍要处理供应商响应、错误和限流，不因 JSON-RPC 就消除 XML 或业务格式转换。

## 5. Early limitations / OAuth / Debugging：认证的历史与现在

文章回顾早期远程认证不足，再介绍 OAuth、发现与动态客户端注册。这是 2025 年文章的历史脉络，不能推出所有当前部署都必须使用 DCR，或旧 SSE 示例适用于所有现行客户端。

OAuth 主要解决委派授权，不等于证明用户身份的所有机制，更不等于细粒度资源授权自动成立。Client → MCP Server 与 Server → 第三方 API 是两条边界。即使 token 有效，用户 B 读取用户 A 的笔记仍应被拒绝。本地运行也不自动可信：启动的进程可能拥有文件和网络权限。

Inspector 可观察协议与工具调用，但“能列工具”只能验证部分通信。应分别记录初始化、参数校验、授权拒绝、供应商错误与结果关联，且日志不能包含真实 token。当前远程指南另见[Cloudflare 解读](03-remote-mcp-authentication.md)。

## 6. 教程补充练习与验收

预算 25 分钟、零网络、零模型调用。为“查询 note_17 并预览行动项”画五方链路，给每个箭头标明消息或数据；分别走查列工具成功、参数错误、跨用户拒绝、第三方超时四种情况。使用假身份，不运行 Server。

验收交付一张链路图和四行失败表，每行说明哪层有证据、哪层尚未验证、是否允许重试。必须能指出工具返回文本不是新授权，列工具不算业务调用成功。这是纸面契约演练，不是协议互通或 OAuth 实验。

## 7. 自测与答案

**问：换模型后可以原样使用所有 Server 吗？** 协议边界可复用，但 Host 的能力、transport、消息转换和版本仍需核验。

**问：MCP 是否代替 function calling？** 不代替。模型表达调用意图，MCP 负责能力通信，Host 和执行层组织实际操作。

**问：有效 token 是否允许访问任意 note_id？** 不允许，仍需验证主体、scope、资源归属及副作用。

第 04 章使用本篇校准角色与历史示例，协议响应不是本笔记验证通过的实现；原文产品宣传和生态前景不作为选型保证。
