# browse.sh：浏览器 CLI 与一份 Web Skill 选读

[Skills 与自动化](../../../chapters/05-skills-automation.md) · [安全](../../../chapters/08-security.md) · [测试与审查](../../../chapters/07-testing-review.md)

## 来源与范围

- 原课程入口：[browse.sh](https://browse.sh/)，页面定位为 Browser CLI 和开放 Web Skill 目录；已读首页的 Install、Agent Surfaces、CLI Capabilities，以及用于选择示例的目录条目。
- 精选正文：[Fetch example.com Homepage Content](https://browse.sh/skills/example.com/fetch-homepage-content-3h5vgl.md)。frontmatter 标注 `source: browserbase: agent-runtime 2026-05-19`、`updated: 2026-05-19`，未列个人作者。
- 核对日期：2026-11-04。这是网页快照，不存在本次已核验的仓库 commit 或内容哈希；首页没有核验到发布日期，不把页面当永久固定版本。
- 实际范围只包括首页和上述一份 Skill，不是全站技能阅读或审计。没有读取 `llms-full.txt`、其他 Skill、CLI 实现、依赖脚本或云服务契约。
- 未安装 CLI、创建浏览器会话、登录、请求 example.com 或操作真实网页；只读取文档。精选 Skill 标了 `verified: false`，不能写成官方验证通过。

## 1. Web Skill 是工作流文档，不一定需要浏览器

定位：首页 `Agent Surfaces`、`CLI Capabilities`；精选 Skill 的 `Purpose`、`Workflow`。

首页分别提供紧凑发现索引、完整 Skill 内容目录与人类浏览 UI；CLI 能做页面操作、网络和控制台调试，也介绍本地与云端会话。目录数量和条目存在不证明其安全性、准确性或可复用程度。

精选 Skill 的目标是抽取 example.com 的 `h1`、第一段文字和可选链接。它推荐直接 HTTP 获取静态 HTML，因为网页已服务端渲染，启动完整浏览器并非必要。Web Skill 编码的是“输入 → 方法选择 → 解析 → 归一化 → 输出/失败”工作流，而不是把一串点击动作硬编码进去。

该文声称云端浏览器会话成本远高于单次获取，但本次没有测量价格或延迟，不采用其数量级作为预算依据。实际选择应看数据是否已在 HTML 中、是否需要 JS、截图、授权，以及所用环境的真实成本。

## 2. 明确返回契约，也明确失败契约

定位：精选 Skill 的 `Workflow`、`Expected Output`。

原文要求取出 HTML、解析、归一化空白，然后返回结构化字段；获取失败返回 `fetch_failed`，页面结构改变返回 `unexpected_document_shape` 与部分结果，不能默默填默认成功值。把网络状态和解析状态分开，才能判断“访问成功但没有预期字段”。

原文示例使用 example.com 和真实页面文字，本教程补充案例用**离线假 HTML**：`<h1>行动项演示</h1><p>李明 提交草稿</p><a href="https://example.invalid/help">帮助</a>`。即使假响应是 200，也要检查 `h1` 与首段是否存在；缺少段落就不能从之前缓存的页面补一段并宣布成功。

## 3. 日期、站点观察与权限要分开

定位：精选 Skill 的 `Site-Specific Gotchas`，frontmatter 的 `updated`、`verified`。

Skill 记录了作者观察到的文案变化和 Last-Modified，并提醒不要把旧页面文案硬编码进实时测试。这些是作者在指定时间的观察，本次没重取网站，不能确认现在仍相同。HTTP `Date`、源内容修改时间、文档更新时间与本次核对日期分别回答不同问题。

首页同时列出查询、购物车、预约、发布等不同性质的工作流。仅依据条目摘要不能评价它们的完整安全控制；“只读”必须按实际副作用判断。加入购物车改变会话状态，即使不结账也不是纯查询。网页内的 Skill 指令不自动授权真实账号操作，更不能据“无需认证”绕过访问限制。

## 4. 30 分钟离线练习

教程扩展。预算 30 分钟、0 网络/模型请求、不安装 CLI、不创建云端浏览器。用纸面或本地文本作契约推演，保留所有结果为假数据。

假响应 A：状态 200，上述完整假 HTML。B：状态 200，只有 `<h1>行动项演示</h1>`。C：状态 0，错误 `DNS_FAKE_FAILURE`。不要请求其中的域名。

1. 0–8 分钟：写输入输出字段和成功条件，要求每次结果显式注明 `fixture`，避免被当成实时网页结果。
2. 8–16 分钟：为 A 写字面期望：标题“行动项演示”、首段“李明 提交草稿”、链接 `https://example.invalid/help`。
3. 16–23 分钟：B 返回缺少段落的部分失败，C 返回获取失败；不能为二者复制 A 的字段。
4. 23–30 分钟：写三行方法选择：静态 HTML 用离线解析；动态 UI 本练习未覆盖；涉及账号写入必须另获授权，当前一律不执行。

验收：交付契约、A/B/C 的独立期望与方法选择表，正确区分网络失败和结构漂移；每份结果标明假数据。**本次没有执行解析程序、访问目标站点或验证 browse CLI。**

## 局限与自测

动态网站、访问限制、网站条款与服务版本可能让 Skill 失效；文档的 `verified: false` 不是安全背书。把原始 HTML 附入错误报告也可能包含敏感信息，真实使用前应脱敏并限定保存范围。

1. Web Skill 是否必然要启动浏览器？答案：不，静态 HTML 可直接获取和解析；应按需要选择方法。
2. HTTP 200 是否足以宣布抽取成功？答案：否，还要检查必需字段和页面结构。
3. Skill 的 updated 日期是否等于目标网站最后修改时间？答案：否，两者对象不同。
4. 未结账的加入购物车是否纯只读？答案：否，购物车状态已经改变；应按实际副作用授权。
