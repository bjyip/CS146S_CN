# Fall 2025 第 2 周：Coding Agent 与 MCP

[2025 入口](../README.md) | [材料总清单](../../README.md) | [第 02 章](../../../chapters/02-agent-loop.md) | [第 04 章](../../../chapters/04-mcp-oauth.md)

| 材料 | 类型 | 状态 |
| --- | --- | --- |
| [从零构建 Coding Agent](lecture-building-a-coding-agent.md) | 本地 PPTX、备注与课堂代码 | 7 页文字核对及中文解读完成；第 3 页图片未视觉核验；已融入第 02 章 |
| [构建自定义 MCP Server](lecture-custom-mcp-server.md) | 本地 PPTX、备注与课堂代码 | 13 页中英文文字与备注、84 行代码静态核对及中文解读完成；第 5–7、10 页图片未视觉核验；已关联并最小融入第 04 章 |

配套代码只做静态阅读，没有运行云端模型、文件编辑工具或原课堂演示。指定 MCP 阅读材料另见[总清单](../../README.md#fall-2025)。

## 指定阅读

2026-11-05 接入以下四份正文解读，已关联并最小融入第 04 章；原编号保留，未读 SDK 和示例仓库不补空笔记。

| 材料 | 实际范围与状态 |
| --- | --- |
| [01 MCP 简介](01-mcp-introduction.md) | 文章全文；校准角色、简化协议响应与伪代码，不视为规范 |
| [03 远程 MCP 身份验证](03-remote-mcp-authentication.md) | 当前指南全文，更新于 2026-10-27；不是 2025 快照，完整 Authorization/迁移/模板未读 |
| [05 MCP Registry](05-mcp-registry.md) | 2025-09-08 公告全文；现行 API、政策及实现未读 |
| [06 API 与 MCP 工具](06-apis-and-mcp-tools.md) | 文章全文；工具粒度与结果预算，未验证 tokenizer 或沙箱 |

第 02 项 [Server 示例仓库](https://github.com/modelcontextprotocol/servers)与第 04 项 [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk/tree/main?tab=readme-ov-file#server)仍待读取固定版本的实际文件。2026-11-05 本次 `gh --version` 返回命令不可识别，未取得仓库正文或版本；按 GitHub 仅使用 gh 的限制，没有安装 CLI、克隆、改用 webfetch 或其他 GitHub 入口绕读，不建空笔记。工具不可用不证明仓库不存在，也不能将已读 MCP 文章算作 SDK 已读。以上笔记不是安装、登录或部署授权，纸面练习未执行。

## 作业导读

[行动项提取器与端到端契约](assignment-guide.md)：已静态阅读本地说明、README、writeup、入口、服务、数据库、两份路由、测试及前端，保留原五部分 100 分要求，解释写入、宽松解析、回退与 mock 边界，并关联第 03 章。提供 50 分钟零调用替代；未运行作业，不计指定阅读完成数。
