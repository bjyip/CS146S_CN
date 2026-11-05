# 远程 MCP 身份验证：版本、授权服务器与资源边界

[本周入口](README.md) | [第 04 章](../../../chapters/04-mcp-oauth.md)

## 1. 来源与范围

- 原课程入口：[Cloudflare Remote MCP Server / Add authentication](https://developers.cloudflare.com/agents/guides/remote-mcp-server/#add-authentication)。
- 当前对应正文：[Build a Remote MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/)，Cloudflare 官方文档，页面更新日期 2026-10-27，核对日期 2026-11-05。
- 已读当前指南全文，包括无认证演示、CLI、客户端连接及 Add authentication；不是恢复了 2025 年快照。未读完整 Authorization、迁移指南、模板实现或锁定依赖版本，未部署、安装、登录或启动 Inspector。

阅读目标：解释公网无认证演示与受控远程服务的差别，防止把旧 `McpAgent` 与当前 handler 流程拼成未经验证的配置。

## 2. How the server works：请求级状态与持久化

当前指南采用 Streamable HTTP 和 Agents SDK 的 `createMcpHandler`。工厂为每个请求提供新的 `McpServer`，handler 无状态，不要求每个 Server 都有 Durable Object 或会话。需要跨请求保留的数据放在 KV、D1 或 Durable Object 等 binding。

这是当前模板架构，不是 MCP 的唯一合法实现。不能从“无状态 handler”推出“业务没有状态”：预览、审批、幂等记录或授权缓存仍可能必须持久化，且要绑定用户。页面将 `McpAgent` 标为废弃并链接迁移文档；没有读取迁移细节，不发布机械替换代码。

## 3. Deploy / Connect：教程说明不是执行授权

无认证示例意味着任何能够连接的人都可使用暴露的能力。它适合受控假数据演示，不适合直接挂接真实日志、数据库或写入能力。

指南提供 dashboard 和 CLI 两条部署路线；dashboard 路线可创建远程仓库并建立自动部署。这些都是外部副作用，阅读并不授权创建仓库或上线。CLI 的 `latest` 也是浮动版本，本篇不把安装命令作为已锁定的实验环境。

浏览器直接打开 `/mcp` 不等于协议客户端。需要支持 Streamable HTTP 的 Client 发送初始化及工具消息。指南中的 8788、5173 是示例端口，应以实际启动输出为准。Inspector 的代理认证参数属于敏感信息，不写进公开报告。

## 4. Add authentication：两类 Worker 的分工

指南概述以下结构：授权服务器 Worker 使用 `OAuthAuthorizationServer`，其 `/authorize` 页面直接登录或接入身份供应商；资源服务器把 `createMcpHandler` 包在 `OAuthResourceServer` 中，通过 Service Binding 向授权服务器检查每个请求的 token。

Client 从 MCP Server 的 `401` 响应找到授权入口，用户完成授权后携 token 重试；工具使用 `getMcpAuthContext()` 取得登录主体。这里只解释指南给出的角色，不补造完整 token 验证、metadata 或注册实现。

身份取得后仍需检查工具和对象权限。例如登录用户 A 只可读取自己的笔记；工具名字可见不等于获准访问 B 的记录。远程 Client 的 token 也不能直接透传给任意上游 API，当作其授权凭据。第三方 API OAuth 是第 04 章另一条独立边界。

## 5. 教程补充练习与验收

预算 30 分钟、零云费用、零网络部署，用假主体和假 token 标签画 Client、授权 Worker、资源 Worker、上游笔记服务四方图。走查缺 token、过期 token、有效 token 但跨用户、写入无审批四种情况，标拒绝位置和脱敏日志字段。

验收保留版本来源、状态持久化位置、每步证据需求和权限矩阵。缺失实现写“待读官方 Authorization 与测试”，不把纸面 `401` 流程写成实际拦截成功。若以后运行，须另行授权安装、登录和部署，再锁定版本并验证拒绝路径。

## 6. 自测与答案

**问：handler 无状态，是否可把所有审批放在内存变量？** 不可据此保证跨请求有效；审批需持久化、绑定主体与具体差异，并处理失效。

**问：登录成功是否允许所有写工具？** 不允许，还需要 scopes、资源归属和写入门禁。

**问：这篇是否证明 2025 作业的部署方式？** 不证明，取得的是 2026-10-27 当前指南，不是历史版本或已运行作业。

第 04 章关联本篇作为当前官方指南的限定范围解读，不替代完整 SDK、协议及供应商核对。
