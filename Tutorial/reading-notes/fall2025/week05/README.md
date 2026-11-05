# Fall 2025 第 5 周：现代终端与 AI 开发者产品

[2025 入口](../README.md) | [第 06 章](../../../chapters/06-repo-parallel.md)

核对日期：2026-11-05。本周产品材料用于理解交互、反馈与自治程度；仓库就绪、任务租约和并行隔离仍是系统教程的工程扩展。

## 已读取课堂材料

| 材料 | 真实范围与状态 | 中文解读 |
| --- | --- | --- |
| Mihail Eric，AI 开发者产品，2025-10-20 | 双语各 14 页可提取文字与第 3、6–13 页备注已读；第 2、4 页图片未核验；所有产品与 MCP 演示未执行 | [七项产品原则](lecture-ai-developer-product.md) |

第 2 页是 2025-10-24 Zach Lloyd（Warp CEO）嘉宾公告，不是本份课件的作者信息。根 README 单列的 Zach Lloyd Figma 讲义未在本轮读取，不由这份笔记替代；视频与逐字稿未取得。

## 阅读与作业边界

2026-11-05 对三项指定阅读分别取得实际响应，不把备注、产品概览或 Notion 页面壳等同原课程正文。

| 指定材料 | 实际获取与合理替代 | 状态 |
| --- | --- | --- |
| [Warp University](https://www.warp.dev/university?slug=university) | 原入口与无 query 的 `/university/` 均返回 2026-11-03 更新的 Warp products overview，不是原课程集合；只见概览不能代表各课程已读 | 原集合待获取，不建空笔记 |
| [Warp vs Claude Code](https://www.warp.dev/university/getting-started/warp-vs-claude-code) | 返回与 University 相同概览；进一步取得其链接的[当前官方迁移指南](https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-claude-code/)完整正文，更新于 2026-11-03 | [当前替代笔记完成](02-warp-claude-code-current-migration.md)，历史对比原文仍待获取，不称 2025 原课程完成 |
| [How Warp uses Warp](https://notion.warp.dev/How-Warp-uses-Warp-to-build-Warp-21643263616d81a6b9e3e63fd8a7380c) | 原链接及同域裸页面 ID 两次都仅返回需启用 JavaScript 的 Notion 页面壳，无团队实践正文；未登录、调用私有 API 或绕过访问限制 | 待获取，不从标题/作业报告补造团队案例 |

本周有一份当前官方替代资料解读，但三项历史指定原文均未取得，不能因此增加“原课程全文完成”数量。当前迁移指南用于理解终端与 Agent 身份、规则迁移、布局/进程恢复和共享资源边界，不代表 University 全站、历史对比或 Warp 内部实践已读。年份与总索引由统一汇总维护，本页保留最精确的本次状态。

[第 5 周作业导读](assignment-guide.md)已静态核对原要求、四份 Warp 定义、应用、12 个测试与报告，说明打印清单/交接不等于执行、启动数据库隔离、串行去重和乐观回滚边界，并提供 50 分钟零调用替代。原说明要求至少两项任务、A 类 Warp Drive 自动化与 B 类真实并发，MCP 非必选，没有数值评分。当前原生前端不满足任务 2 原文的 React 部分，报告自述不当实测证据。

建议先读[第 06 章](../../../chapters/06-repo-parallel.md)，再读产品原则、[当前迁移指南解读](02-warp-claude-code-current-migration.md)与作业导读，最后在获准独立环境决定是否复现[原作业](../../../../_assignments/2025%20fall/week5/assignment.md)。通用审计、worktree 和纸面替代不自动满足 Warp 产品要求；本批未安装、登录、导入定义、运行 Agent/测试/Hook/服务、创建数据库或真实账号写入。三项历史指定正文与在线嘉宾课件仍待取得，当前替代笔记不消除这些缺口，也不增加指定阅读完成数。统一汇总已在第 05 章补规则名/技能发现不等于执行兼容、在第 06 章补布局恢复不等于进程恢复的反向来源关联，保留未运行边界。
