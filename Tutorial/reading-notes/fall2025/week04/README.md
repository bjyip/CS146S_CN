# Fall 2025 第 4 周：Coding Agent 模式

[2025 入口](../README.md) | [阅读总清单](../../README.md) | [第 05 章](../../../chapters/05-skills-automation.md)

本周围绕 Agent 自主性、人机分工、定制与工作流展开。以下两份是 2025 归档课件的中文解读，不是 Fall 2026 第 4 周的新课件，也不是视频转写或实际演示复现。

## 已读课堂资料

| 日期与材料 | 中文笔记 | 实际读取与保留缺口 |
| --- | --- | --- |
| 2025-10-13，Mihail Eric：如何成为 Agent 管理者 | [Agent 管理解读](lecture-agent-manager.md) | 2026-11-04 核对英文与中文全部 14 页文字及关联备注；第 2、5、6 页图片未视觉核验，示例/工作流演示缺实际输出 |
| 2025-10-17，Boris Cherny：Claude Code | [Boris 嘉宾解读](lecture-boris-cherny.md) | 2026-11-04 核对英文与中文全部 49 页文字及关联备注；第 1、5–13、20–23、34–43、48 页图片未视觉核验，第 43 页无正文；未执行 CLI、SDK 或原型 |

原件和中文对照共用一份笔记，各笔记保留资源链接、真实页码、备注范围、图像缺口与历史版本限制。“已读文字”不等于“完整复现讲座”；原件和中文 PPTX 均保持不变。

## 建议阅读顺序

1. 先读 Agent 管理，理解任务责任、定制层次与可审计交接。
2. 再读 Boris 的第 30–43 页解读，比较工作流选择和需求撤销/替换的原型案例。
3. 回到第 05 章的[自主性与交接证据](../../../chapters/05-skills-automation.md#自主性与交接证据)和[原型迭代中的有效规格](../../../chapters/05-skills-automation.md#原型迭代中的有效规格)，完成离线验收。

## 指定阅读与作业边界

2026-11-05 逐项核对六份指定阅读，完成两份声明范围内的笔记；原版与指定中文入口共用一项，不把课堂课件或作业引用算作外部正文已读。

| 指定材料 | 实际获取与失败方式 | 中文笔记/状态 |
| --- | --- | --- |
| [Anthropic 团队经验 PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)与[宝玉译述](https://baoyu.io/translations/how-anthropic-teams-use-claude-code) | PDF 响应超过工具 5MB 限制；取得[官方网页](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)完整正文与宝玉十团队译述；当前英文比中文简略，PDF 对应未核验 | [笔记完成：官方文字替代与指定译述](01-how-anthropic-teams-use-claude-code.md)，不是 PDF 全文/逐页复原 |
| [Claude 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)与[Whaty 中文页](https://claude.whaty.org/posts/Claude-code-official-best-practices.html) | 历史入口返回当前产品文档，当前输出末尾截断；Whaty 完整中文正文取得，标记 2025 年 12 月社区译述，历史英文全文未取得 | [笔记完成：指定中文译述与当前差异](02-claude-code-best-practices.md)，不称历史英文全文已读 |
| [Awesome Claude Agents](https://github.com/vijaythecoder/awesome-claude-agents) | `gh --version` 返回 CommandNotFoundException，当前 PATH 无 GitHub CLI；未安装、未用 webfetch/raw 绕行，无仓库正文或固定版本 | 待获取，不建空笔记 |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 同一 GitHub CLI 前置检查失败，未请求仓库正文、未安装或绕行 | 待获取，不建空笔记 |
| [好的上下文，好的代码](https://blog.stockapp.com/good-context-good-code/) | 原 URL 两次获取分别采用 Markdown/text 均返回 GET 传输错误，未取得正文 | 待获取，不从标题补摘要 |
| [Claude Code 内部机制](https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62) | 原 URL Markdown/text 两次均传输错误；未绕认证或付费，也没有合理官方同篇副本 | 待获取，不将其他架构论文冒充原文 |

两份完成按明确声明的替代/译述范围统计，仍有四份无正文；图片、产品、命令、原实验与 PDF/历史英文全文均保留缺口。本周编辑保留旧材料；统一汇总已在第 05、06 章补两份笔记的反向来源关联，强调任务风险分类、组合验收及历史/当前机制分层，不添加未经验证的产品参数。

[2025 第 4 周本地作业](../../../../_assignments/2025%20fall/week4/assignment.md)已核对；[自动化工作流导读](assignment-guide.md)覆盖说明、三个命令、规则、应用、测试与报告，解释覆盖率依赖、Hook 配置发现、启动数据库副作用与提取测试冲突，并关联第 05 章。原说明没有数值评分表，报告自述不当本批运行证据。根 README 的 `Assignments/week4/assignment.md` 与实际 `_assignments/2025 fall/week4/` 路径不同，本页使用已核对本地材料，不改根链接或据完成标记宣称实验通过。

## 作业学习顺序

先读[作业导读](assignment-guide.md)，为测试诊断与文档同步各建流程合同，再完成其中 50 分钟纸面替代。两份课件笔记与作业的零网络练习都是教程扩展，不等价于 Claude Code 功能交付；安装、服务、数据库、提交和推送均未执行，也不自动获得授权。

## 本周验收

读者应能给出七步责任表、委派合同、证据不足/失败的阻塞规则，以及原型的有效需求账本。练习限制与预算详见逐份笔记；当前完成的是资料核对与文档解读，视觉、模型、客户端、MCP/SDK 与实际应用实验均未执行。
