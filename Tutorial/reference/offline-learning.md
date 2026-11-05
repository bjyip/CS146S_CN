# 外网受限时的中文学习路线

[教程目录](../README.md) | [原来源缺口](../reading-notes/README.md#剩余获取缺口) | [来源表](sources.md)

2026-11-05 按用户确认采用可追溯中文补充与现有本地资料深化。不要求先恢复外网、安装产品或购买会员才阅读；也不把知识主题相近当原材料已读。以下是学习导航，不是完整课程材料的新完成清单。

## 两种完成状态

**学习目标完成**需要解释机制、给出案例、写出独立预期、识别失败与局限；纸面练习只验收理解，真实功能仍要另行实验。**指定来源完成**需要取得该材料正文并声明版本与实际读取范围。当前指定阅读仍为 42/64，原缺口 22 项独立保留；不能用下面的补充路线把数字写成 64/64。

中文入口可访问不等于官方原版对应已核验；公共镜像不等于可信、完整或获准执行。只保留必要转述，不默认归档全文、整套字幕或课件图片。

## 剩余 22 项的替代入口

| 原来源缺口 | 项数 | 现在可读的中文依据与章节 | 能学什么、不能替代什么 |
| --- | --- | --- | --- |
| 2025 两份 LLM/提示视频、2026 构建 Agent 视频、2025 审查视频、2026 仓库就绪视频 | 5 | [LLM 与提示](../chapters/01-llm-prompting.md)、[Agent 源码解读](../reading-notes/fall2025/week02/lecture-building-a-coding-agent.md)、[Tomas 文字解读](../reading-notes/fall2025/week07/lecture-tomas-reimers.md)、[仓库审计](../chapters/06-repo-parallel.md) | 模型、循环、审查职责、就绪度；没有五份视频的真实字幕、时间戳或现场演示 |
| FAANG、trq212、trybasis、Addy 的 X 原帖 | 4 | [Boris 本地课件文字](../reading-notes/fall2025/week04/lecture-boris-cherny.md)、[2026 system prompt 转写解读](../reading-notes/fall2026/week01/lecture-system-prompt.md)、[仓库与并行](../chapters/06-repo-parallel.md)、[Addy 官方文章补充](../reading-notes/fall2026/week06/01-risk-tiered-review.md) | 规格迭代、约束、就绪和人工责任；其他演讲或同作者文章不证明原帖对应 |
| MCP servers、TypeScript SDK、humanlayer ace-fca、awesome-claude-agents、SuperClaude、o3 prompt | 6 | [本地 MCP 原型解读](../reading-notes/fall2025/week02/lecture-custom-mcp-server.md)、[上下文与规格](../chapters/03-context-spec.md)、[Skills 与分工](../chapters/05-skills-automation.md)、[安全分诊](../chapters/08-security.md) | 工具契约、上下文、角色与权限；不能讲未读仓库安装命令、当前 SDK API 或原漏洞 prompt |
| Google 概览、stockapp、Medium、SRE 导论 | 4 | [中文提示入门四页解读](../reading-notes/fall2025/week01/supplement-prompting-introduction.md)、[上下文机制](../chapters/03-context-spec.md)、[Agent 原型](../chapters/02-agent-loop.md)、[本地事故响应讲义](../reading-notes/fall2025/week09/lecture-incident-response-devops.md)、[SLO 练习](../chapters/09-delivery-operations.md) | 提示、上下文、循环与可靠性；不是四篇原文摘要，SLO 数值练习为教程扩展 |
| Warp University、历史 Warp-vs-Claude、Warp 内部 Notion 文档 | 3 | [当前迁移补充](../reading-notes/fall2025/week05/02-warp-claude-code-current-migration.md)、[本地 Warp 作业静态导读](../reading-notes/fall2025/week05/assignment-guide.md)、[自动化](../chapters/05-skills-automation.md) | 执行者、配置、共享资源和交接；不证明历史课程内容、现行产品兼容或内部流程 |

原课件可提取文字有页码依据，但图片与版式未视觉核验；嘉宾 PDF 与主讲 PPTX 分开。已取得的转写有真实定位，不能给另一视频借用。上述入口优先使用已完成中文正文，不复制一套新章节。

## 如何选择补充材料

1. 有指定中文版：实际取得正文，核对作者、原链接、日期、范围与删减；仅标题或导航不建笔记。
2. 有同作者另一篇文章：单独记对应关系，未证实就作为补充，不消除原来源缺口。
3. 只有同主题中文资料：选择可追溯正文，写支持的具体知识与不足；不借它归属原作者观点、数字或 API。
4. 无可用正文：用本地代码、文字课件与已有章节学习机制，新增推演明确为教程扩展；不生成空原文笔记。

本轮取得 DAIR.AI 中文简介、要素、设置、技巧四页，已生成[补充解读](../reading-notes/fall2025/week01/supplement-prompting-introduction.md)。它扩大已有指南的精选范围，不增加指定阅读总数或完成数，也不证明 Google 原概览已读。

## 离线资料的接入

后续如取得合法本地 PDF、网页导出、仓库快照或字幕，先验证对应关系再解读。仓库至少记录上游 URL、提交 ID（缺失写未知）与实际文件；字幕记录视频 ID、语言、人工/自动类型和真实时间戳；PDF 记录原入口、版次、页数、文字与图片缺口。外部安装脚本不因被收进快照而获得执行授权。

本轮暂停 `gh` 安装与阻塞域名的反复直连；先前官方安装包下载未成功，不标记 CLI 已安装。没有改变系统代理、登录或通过镜像绕过认证。恢复获取后逐项核对，不用主题补充批量关闭原缺口。

## 零执行学习闭环

每次选一个主题，预算 40 分钟、零模型与网络、零安装和应用执行。读对应中文机制 10 分钟，写一个贯穿项目案例 10 分钟，预写正常/失败/未知三路验收 10 分钟，核对来源与权限 10 分钟。使用[材料替代证据卡](templates.md#16-材料替代证据卡)，只写纸面成果与未运行状态。

例子：模型超时后返回规则结果。验收分列 API 响应、实际引擎、业务质量与生产写入批准；HTTP 200 不能把后三项自动填成功。学习证据可用这张表，真实可靠性仍需隔离环境运行与独立评测。这是教程自学改编，不满足有产品、真实调用或提交要求的原作业。
