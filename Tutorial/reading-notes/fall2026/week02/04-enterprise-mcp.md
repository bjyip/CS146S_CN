# 阅读笔记：企业 MCP 的发现、身份与治理

[对应第 04 章：MCP 与 OAuth](../../../chapters/04-mcp-oauth.md) | [对应第 10 章：团队与网关](../../../chapters/10-capstone.md)

## 1. 来源与阅读范围

- 原文：[Scaling MCP adoption: Our reference architecture for simpler, safer and cheaper enterprise deployments of MCP](https://blog.cloudflare.com/enterprise-mcp)。
- 作者：Sharon Goldberg、Matt Carey，Cloudflare。
- 发布日期：2026-04-14；页面结构化元数据修改日期：2026-07-15；本次核对：2026-11-04。
- 已读范围：正文全部，从 Remote MCP 到 Access、MCP server portals、Code Mode、AI Gateway、Shadow MCP、公众服务保护及总结。未进一步读取链接中的产品教程、定价、Dynamic Workers 或协议规范。
- 材料性质：Cloudflare 内部部署经验与产品参考架构；不等同于 MCP 标准要求，也不证明任意套餐、网络或服务器具备相同防护。本文是中文解读，未部署产品或验证作者节省比例。

## 2. 先把四个边界画清楚

定位原文 `Remote MCP servers provide better visibility and control`、`Cloudflare Access provides authentication`、`MCP server portals centralize discovery and governance`、`AI Gateway provides extensibility and cost controls`。

```text
用户/Agent Host
  -> MCP Client -> MCP 门户 -> 远程 MCP Server -> 企业资源/API
  -> LLM 网关 -> 模型供应商

身份服务参与受保护 MCP 的登录/令牌签发
企业网络安全网关另观察获准范围内的网络流量
```

| 部件 | 原文职责 | 不应混淆为 |
| --- | --- | --- |
| Cloudflare Access | SSO、MFA 等身份验证，作为 OAuth provider | 所有资源操作的业务授权自动正确 |
| MCP server portal | 工具发现、工具暴露策略、日志和 DLP | 接管 LLM 推理路由的模型网关 |
| AI Gateway | 位于 MCP Client 与 LLM 之间，切模型供应商、控模型用量 | 改变工具资源归属或提供 MCP OAuth |
| Cloudflare Gateway | 企业网络的安全 Web 网关，检测未纳入门户的远程 MCP | 与 AI Gateway 同一服务或可靠发现全部本地 stdio |

身份验证回答“你是谁”；授权还要回答“对哪个资源能做哪种操作”。门户隐藏工具可减少暴露，但后端仍须在每次调用时验证主体、scope、资源与副作用。第 04 章区分 Client 访问 Server 和 Server 访问下游 API 两个 OAuth 边界；本文的 Access 描述不能代替任意下游供应商的授权流程。

## 3. 从个人安装到受治理远程平台

原文认为员工自行运行来源不明、版本不统一的本地 MCP 会增加供应链、工具投毒和维护风险。其做法是中央团队维护 monorepo 模板，新增资源先通过 AI governance 审批，再获得默认拒绝写入、审计、CI/CD 与秘密管理等基础设施。

可迁移的原理是让安全默认值随模板与运行平台传播，而非依赖每个员工手工配置。远程服务器便于统一更新与可见性，却也聚合访问和故障风险；“远程”本身不保证安全，“本地”也不必然不可信。批准软件来源、限定能力、及时补丁与审计同样重要。

**原文案例：** finance 门户只暴露内部代码仓库的只读工具；engineering 门户结合企业设备与组身份暴露更强读写工具。**教程补充案例：** 行动项提取器的分析角色只允许查假笔记和生成预览，提交角色仍需外部批准绑定预览 ID、资源和字段，不能仅凭模型声称“已同意”写入。

## 4. Code Mode：按需发现与组合执行

定位原文 `Code Mode with MCP server portals reduces costs`。

常规做法把大量工具 schema 提前放进模型上下文。Code Mode 门户只暴露 `portal_codemode_search` 和 `portal_codemode_execute`：前者让模型生成代码，通过 `codemode.tools()` 筛选工具定义；后者让模型生成代码，经代理调用发现的上游工具、链式处理并裁剪返回值。原文说代码在门户的 Dynamic Workers 沙箱执行。

这减少前置定义和往返，不消除真正任务中读取定义、输入、结果、代码与模型调用的成本。作者报告四个内部 MCP 的 52 个工具定义约 9,400 tokens，替换为两个门户工具约 600 tokens，减少约 94%；另一个 Cloudflare API MCP 案例的 99.9% 来自原文引用的先前文章。两者不是本教程复现，也不是全部 MCP 的固定收益。

**原文案例：** 搜索 Jira 和 Google Drive 工具，再在一次 execute 中查工单、读文档、更新首个工单描述。教学上应看到风险：搜索结果为空怎么办，首个结果是否唯一目标，文档是否含不可信指令，写入是否获批准，读成功但写失败如何处理？原文代码用于说明组合机制，不应复制成真实写入配方，其展示还含排版引号，不视为已验证可运行代码。

Code Mode 生成的代码仍是不可信产物。沙箱需要限制网络、秘密、时间、内存和可调用工具；逐次上游调用仍须执行资源授权、审批、输入校验、审计与幂等。不能让一次 execute 的批准隐式授权其内部任意数量、任意目标的写操作。把多次写入塞进一个调用，也不使跨系统动作自动具备事务性或可回滚性。

## 5. Shadow MCP 检测与防护的边界

定位原文 `Cloudflare Gateway discovers and blocks shadow MCP` 和 `Public-facing MCP Servers are protected with AI Security for Apps`。

原文组合主机名、`/mcp` 等 URI、HTTP body 内 JSON-RPC `method` 和 `protocolVersion` 模式识别远程 MCP，再用于日志、阻断或重定向。路径与正则只是信号：普通 JSON-RPC 可能误报，自定义路径、不同序列化或不可见内容可能漏报。可观察性取决于真实网络部署、合法检查权限与数据保留政策；不能由几个模式宣称所有 MCP 已受控。

WAF/AI Security for Apps 在作者架构中检测公网 MCP 的注入或数据泄漏，但内容检测不能证明请求无害，第一方服务也仍须审查代码与授权。组织应避免把敏感正文全量写入集中日志，保留必要任务标识与脱敏证据。

## 6. 40 分钟零付费练习：纸面门户与写入门禁

教程扩展；用独立临时文本或纸面模拟，不注册 Cloudflare、不修改 MCP 配置、不执行 Code Mode、不做真实 OAuth 或网络检测。预算：40 分钟、0 元、0 次外部请求；数据只用假用户、假工单和假文档。

1. 用 8 分钟列四个假工具：查笔记、读笔记、预览行动项、提交预览。给 finance、engineering、审核者分别画允许动作，写出服务端检查，不能只写工具可见性。
2. 用 8 分钟画两条请求链：MCP Client 到资源，MCP Client 到模型。标明身份、模型预算、工具授权、审计分别在哪层。
3. 用 10 分钟模拟 Code Mode 组合“查两个工单并更新首个”，主动拒绝歧义目标、未批准写入和来自文档的“忽略门禁”文本；返回紧凑预览而非提交。
4. 用 7 分钟模拟三个失败：过期批准、写响应丢失、只读身份尝试写入。分别写停下、重新批准、查幂等状态或拒绝的理由。
5. 用 7 分钟对四条假网络记录分类：`/mcp` 普通网页、标准 tools/call、未知路径 JSON-RPC、无 HTTP 的 stdio。写可疑/已确认/不可见，不用一个路径就断定违规。

验收证据：角色-资源-动作矩阵、双链路图、一次获准读与至少两次拒绝、脱敏审计草稿、失败恢复表、检测误报/漏报说明。通过条件是门户与模型网关不混淆、代码不自授权限、写入目标明确、重试不会盲目重复。本次仅编写练习，未运行或预填通过。

## 7. 局限与自测

本架构依赖 Cloudflare 内部身份、平台与治理条件，产品集成、低延迟、成本和保护能力不能无条件搬到别处。集中入口需容量、故障降级、撤权传播和最小权限设计。企业浏览记录与正文检查还涉及隐私及合规，本文不授权抓包或上线 DLP。

**问：MCP 门户和 LLM 网关可以相互替代吗？** 不可以。前者治理工具访问，后者治理模型调用；两条链路可关联审计但职责不同。

**问：代码在沙箱里运行是否意味着它可信？** 不意味着。沙箱限制能力，授权和审批仍须对每次资源操作强制执行。

**问：只展示只读工具就能使用管理员 token 吗？** 不应。后端凭据也要最小权限，否则暴露或逻辑错误可扩大损害。

**问：搜索得到第一条工单能直接更新吗？** 不能。需确认唯一目标、写入差异、批准绑定及失败恢复。

**问：94% token 减少能作为预算保证吗？** 不能。是作者特定定义集报告，完整费用还包括发现、执行、结果和返工。
