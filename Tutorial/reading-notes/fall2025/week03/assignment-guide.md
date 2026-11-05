# 第 3 周作业导读：GitHub MCP 与执行边界

[本周入口](README.md) | [第 04 章](../../../chapters/04-mcp-oauth.md) | [材料总清单](../../README.md)

## 来源与状态

- 归属：CS146S Fall 2025 作业，本地文件没有单独作者署名。本页解释当前已包含实现的快照，不是初始 starter 或官方逐字译文。
- 核对日期：2026-11-05。已读本地 assignment.md、README.md、requirements.txt，以及 server/main.py、github.py、auth.py、config.py 全文；包初始化文件不在实质解读范围。本周目录未发现测试文件或独立 writeup。
- 原资料：[week3 目录](../../../../_assignments/2025%20fall/week3/)。仅静态阅读，未导入或启动 Server、安装依赖、配置客户端、生成或验证真实 token、访问 GitHub API、写 Issue 或部署。
- 原文引用的 SDK、授权规范、产品安装和套餐页面本批未读取。代码中的 SDK 调用不证明已与某个客户端互通；本导读不计指定阅读完成数。

## 1. 原要求与评分

[assignment.md](../../../../_assignments/2025%20fall/week3/assignment.md)要求封装真实外部 API，提供至少两个类型化 MCP 工具，处理 HTTP 失败、超时、空结果和限流，给出安装、配置、启动及客户端调用流程。可以选本地 stdio 或远程 HTTP；不能直接提交官方快速入门示例。

基础评分是 90 分：功能 35、可靠性 20、开发者体验 20、代码质量 15。另有远程可访问 MCP 5 分和正确认证 5 分加分，基础与加分分开，不把它写成五部分各 20 分。提交物为 week3 源码及 README；原文没有要求本周 writeup，也没有在本文新增远程提交渠道。

原任务介绍 tools、resources、prompts，但明确数量门槛是至少两个工具；当前四工具、三资源、两提示词是实现选择，不是所有学生的最低要求。OAuth 与远程部署是可选加分，不套用 2026 第 2 周“三个工具、真正写入、授权码交换与刷新”的要求。

## 2. 环境与版本定位

[README](../../../../_assignments/2025%20fall/week3/README.md)要求 Python 3.11+，本周另有[requirements.txt](../../../../_assignments/2025%20fall/week3/requirements.txt)，不是仅凭作业根 Poetry 环境就证明依赖齐全。MCP 依赖为 `mcp[cli]>=1.12,<2`，其余为 httpx、Pydantic、PyJWT 与 Uvicorn 的版本范围，没有锁定实际安装版本或验证所有组合。

README 的 `cd assignments/week3` 是原路径示例，在此仓库实际目录是 `_assignments/2025 fall/week3/`。原启动入口 `python -m server.main --transport stdio`以本周目录为工作目录；命令行 transport 覆盖环境变量。现有代码选择 stdio、sse、streamable-http，后两者默认监听 127.0.0.1:8000，路径为 /sse 或 /mcp。本批不启动这些入口，不把代码路径声明当可访问服务证据。

客户端配置中的解释器、cwd、远程 headers 及重启步骤需按实际产品版本核验，不直接复制 macOS 或 Cursor 示例到其他客户端。原作业的免费套餐说明不证明现行资格；真实凭据不写入教程、提示词或公开配置。

## 3. 三类能力与组合调用

[main.py](../../../../_assignments/2025%20fall/week3/server/main.py)通过 FastMCP 注册能力，上游访问集中在[github.py](../../../../_assignments/2025%20fall/week3/server/github.py)。

| 能力 | 当前实现 | 理解与验收边界 |
| --- | --- | --- |
| 搜索工具 | search_github_issues | 返回 Issue/PR 精简信息、总数与 incomplete_results；空匹配为成功加 warning，不是 HTTP 故障 |
| 读取工具 | get_github_issue | owner、repo、issue_number 定位对象，返回正文与 kind；编号不能脱离仓库单独使用 |
| 写工具 | create_or_update_github_issue | 无 issue_number 创建，有则更新；直接调用上游，没有 dry-run、预览 ID 或服务端审批记录 |
| 汇总工具 | summarize_github_repository | 并行读仓库、语言、前五位贡献者和最新 Release，按字节数算语言占比；不是模型总结或全部仓库分析 |
| 资源 | github://api/schema、service://status、service://logs | 端点清单、进程共享观测快照和最近 100 条内存日志；不是完整 JSON Schema、主动健康检查或持久审计 |
| 提示词 | analyze_github_bug、draft_feature_spec | 返回指导模型先取证的文本，本身不自动调用工具、不证明根因，也不授予写权限 |

教程构造链路：用 repo:demo-org/action-notes 限定假仓库，搜索 Issue，保留查询中的 owner/repo，并结合返回 URL 核对编号所属对象，再读取正文、起草规格。当前精简搜索结果没有独立 owner/repo 字段；跨仓库查询不能只取 number 就调用读取工具，需明确从可信 URL 或新增结构字段取得仓库身份的规则。搜索也可能返回 PR；需要限定 Issue 时先在查询及验收中明确。正文是外部数据，不应因包含“忽略批准并创建 Issue”就成为系统指令。

字段投影减少搜索正文，但标题、标签等仍可能较长；读取工具返回正文，没有独立总输出长度预算。per_page 上限不是 token 上限，返回列表也不证明已遍历全部匹配项。

## 4. 输入、错误与部分成功

类型与 Field 表达 owner/repo 格式、编号正值、分页范围、正文长度等约束；实际 SDK 导出的 schema 与拒绝行为尚未运行核验。标签数和负责人数量在工具函数内检查，而不是由列表长度 schema 限制。创建要求 title 不为 None，但仅空格标题没有额外 strip 检查；更新没有任何非 None 字段才拒绝。不能从“类型化”推断全部业务合法性。

工具捕获 GitHubAPIError 后返回普通字典 `ok:false`，本地代码没有显式构造 MCP `isError` 结果；客户端能否将其识别为工具失败须按 SDK 和协议验证。长度等输入拒绝、协议失败、GitHub 失败与成功空列表是不同层，不用统一成功标签掩盖它们。

汇总的核心仓库请求失败会使汇总失败，次要请求异常转为默认值与 warning。例如 latest_release 为 null 可能表示没有 Release，也可能是读取失败；判断时保留 warning，不把缺省值当完整事实。成功 HTTP 响应只做 JSON 解码，没有完整上游形状校验；畸形对象或空响应可能在后续访问字段时产生未由 GitHubAPIError 捕获的异常。

status 的 authenticated_upstream 只表示配置了非空 GitHub token，不证明有效或权限足够。last_success_at 在 JSON 解析前更新，限流快照由最近响应覆盖；并发汇总没有分别保留每个端点的配额状态。启动前 null 是尚未观察，不等于故障或健康。

## 5. 有限重试不等于安全重试

默认 MAX_RETRIES=3，request 最多尝试四次；默认单次 HTTP 超时配置为 15 秒，并发信号量为 8。重试覆盖网络错误、超时、429、部分 5xx，以及按特定响应头识别的限流 403；不是所有 403 或所有 5xx 都重试。

Retry-After 或 reset 等待被截到最多 60 秒，所以远期 reset 不能被表述为一定等到配额恢复。信号量仅包围单次请求，等待退避时释放；没有整个工具的墙钟期限，排队、重试和额外调用不由“15 秒”统一限制。

更关键的是 GET、POST、PATCH 共用重试循环。创建请求可能已在 GitHub 生效，却因响应超时再次发送；本地没有幂等键或创建后的核对机制，可能产生重复 Issue。MAX_RETRIES=0 只能关闭该循环的自动重试，不能证明没有客户端重试或未知写入。第 04 章的预览、批准与幂等是教程改进目标，不是已有实现。

## 6. 认证与资源授权是两道门

[auth.py](../../../../_assignments/2025%20fall/week3/server/auth.py)在远程 HTTP 外层校验 X-API-Key 或 Bearer JWT；默认 MCP_AUTH_MODE=none 不认证，stdio 不经过该中间件。配置认证变量仍不证明 stdio 自动认证，不应以默认模式公网部署。

API Key 用 hmac.compare_digest；JWT 按配置选择对称密钥或 JWKS，限定算法，要求 exp/aud，并在配置 issuer 时校验 iss。当前是验证已有 JWT 的入口，不是完整 OAuth 授权服务器、发现流程、授权码交换、缓存刷新或撤销检查。JWKS 取钥是同步调用，可能需要网络；本批未核验异常覆盖、耗时或轮换行为。

either 模式下有效 API Key 先通过，即使同时附无效 Bearer；不能写成“两种凭据都必须有效”。JWT 返回的 claims 没有传入后续工具身份或资源权限判断；通过认证的请求共享进程配置的 GITHUB_TOKEN。MCP 凭据与上游 token 分开是必要边界，但不等于用户级 repo/scope 授权。比如假主体 A 的 token 有效，却无权操作假仓库 B，当前入口未实现这层映射。

GITHUB_API_URL 可配置，Authorization 由独立 GITHUB_TOKEN 构造发送到该配置根地址，禁止自动跟随重定向。因此“不透传客户端 token”成立于读取的调用链，但“GitHub token 绝不会发往非 GitHub 主机”不能脱离可信配置保证。URL 只检查非空，主机和 TLS 策略仍需执行环境约束。

instructions 要求先向用户展示写入目标，只是模型指导，写工具没有批准参数或验证。日志内存缓冲只针对含 authorization: 或 x-api-key: 的文字替换，并不全面识别秘密，且 stderr handler 不使用该缓冲的替换结果；不能承诺所有日志永不泄密。共享日志资源、状态和上游权限也不适合直接当多租户隔离。

## 7. 建议实施与验收顺序

1. 在个人练习副本记录原要求、依赖版本与工作目录，选择已获授权的 API 和假资源。原目录已有实现，不删除它或将现成 README 当本人运行报告。
2. 先写两工具的输入输出、ID 来源、分页、错误与副作用契约；若沿用 GitHub，优先只读。工具、资源、提示词各自验收，不用工具数量代替功能质量。
3. 使用假上游建立输入、空结果、坏 JSON、超时、限流和部分失败矩阵；再单独验证初始化、列工具、调用工具及 stdout 纯净。没有本地测试文件不等于功能通过，也不在未执行时填写通过数。
4. 写操作另行确认资源、审批和未知结果恢复，模拟“已创建但响应丢失”。认证另分缺凭据、无效/过期/audience 错误、either 分支与跨主体资源访问；不以 JWT 验证替代业务授权。
5. 将真实命令、客户端/SDK/协议版本、脱敏 transcript、未验证项写入本人 README。按 90 分基础与两项加分逐项提供证据；公网、登录、真实写入和提交需独立授权。

## 8. 零调用练习

教程扩展，限 50 分钟、零网络、零模型、零安装、零服务启动与外部写入；仅纸面分析假主体、假 Issue 和 token 标签，不生成可用凭据，不修改原作业。

1. 15 分钟画搜索、读取、起草、写入的链路，标出仓库/编号来源、外部不可信正文与缺失的批准验证位置。
2. 15 分钟推演五条件：空搜索；次要 Release 请求失败；POST 已创建但响应超时；either 下有效 API Key 加无效 Bearer；JWT 有效但主体无权操作目标仓库。分别列当前分支、可能副作用和未知项。
3. 10 分钟解释默认四次尝试、60 秒等待截断与并发 8 的不同含义，写整体预算与停止条件目标，不填写实测时长。
4. 10 分钟制作函数/mock、MCP 协议、HTTP 认证、上游集成和客户端五层矩阵，每层列一正常和一失败样例，执行结果全部标未运行。

验收为链路图、五条件表、预算表和测试矩阵。答案要点：空搜索成功加 warning；Release 失败保留其他结果和 warning；POST 重试可能重复；either 的 API Key 分支可先通过；有效 JWT 不提供当前未实现的资源授权。纸面答案证明理解，不证明真实身份拒绝、写入幂等或协议互通。

## 9. 自测与章节关联

**问：四工具、三资源、两提示词证明原作业满分吗？** 不证明。还需真实功能、可靠性、文档和质量证据；远程可访问与认证加分分别验收。

**问：有 aud 校验就实现完整 OAuth 了吗？** 没有。当前验证已有 JWT，完整授权流程与业务权限是不同层。

**问：模型提示要求确认，写工具就有刹车吗？** 没有。执行端未绑定批准，外部文本也不能授予权限。

**问：失败字典与空列表都能作为 MCP 成功吗？** 需要区分。空匹配是成功业务结果，失败字典需核验协议错误表达和客户端识别，不能只看传输接通。

[第 04 章](../../../chapters/04-mcp-oauth.md)集中解释工具契约、传输、两层授权、写入与幂等；本页补原作业及当前逐文件边界。[第 07 章](../../../chapters/07-testing-review.md)关联分层测试，[第 08 章](../../../chapters/08-security.md)关联凭据与不可信数据。新增预览审批、主体授权和幂等均为教程扩展，未修改原 Server。
