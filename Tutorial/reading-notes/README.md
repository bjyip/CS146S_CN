# 逐份中文阅读笔记

[返回教程](../README.md) | [教程依据](../reference/sources.md)

## 范围与使用方法

本清单依据根 README 的“阅读材料”建立，增量核对日期为 2026-11-05。原版及其中文版算同一材料，不重复计数，但中文版对应与差异需另核对。课堂讲义、转写、代码和嘉宾主页是补充来源，不算指定阅读条目；它们的状态独立维护。广告和购买说明不纳入阅读笔记。

当前登记 2025 阅读材料 45 份、2026 阅读材料 19 份，共 64 份；完成 32 份声明范围内的指定阅读中文笔记（2025 十八份、2026 十四份），32 份待补。其中“规格作为源代码”按英文公开预览与删减中文版完成解读，提示指南按六个双语技术子页完成，不是英文全文或全站已读。另有 3 份课堂转写解读、13 份 2025 PPTX 文字解读、两份嘉宾 PDF 文字范围内的解读及 2026 第 1–3 周作业导读；课堂 PDF 不计指定阅读数量，视觉核验未完成。网站、论文与仓库的精选范围见笔记，不能视为全站、全篇或所有技能已读。没有阅读材料的周次不建立空目录；笔记完成不表示运行案例、验证产品或复现论文结果。

| 状态 | 含义 |
| --- | --- |
| 待获取 | 本轮未取得所需正文或字幕，不编写摘要；不代表链接失效 |
| 待编写 | 历史教程工作取得过正文，但尚无逐份笔记；编写前需重新核对 |
| 笔记完成 | 已有本地中文笔记，阅读范围以笔记说明为准 |
| 需复核 | 来源或产品行为变化，已有笔记需要更新 |

优先读系统教程，再按问题选择笔记。视频优先取得官方转写或字幕；自动字幕须标注可能的识别错误。另一场课堂转写不能冒充指定视频。未获取材料只登记，不生成空笔记。索引未列中文版链接时，可从[根 README](../../README.md)查找对应入口；中文版仍需实际核对。

## Fall 2026

| 周次 | 材料与原始入口 | 类型 | 状态与中文笔记 |
| --- | --- | --- | --- |
| 01 | [构建编程智能体](https://www.youtube.com/watch?v=s7ZzkdvCMDY) | 视频 | 待获取字幕或转写 |
| 01 | [构建 Claude Code 的经验与启示](https://x.com/trq212/status/2027463795355095314?s=20) | 社交媒体帖文 | 待获取 |
| 01 | [深入剖析 Claude Code](https://arxiv.org/pdf/2604.14228) | 论文 | [笔记完成：v3 精选章节](fall2026/week01/03-claude-code-design.md) |
| 02 | [上下文税：何时压缩上下文](https://langwatch.ai/blog/context-tax-when-to-compact) | 文章 | [笔记完成：全文](fall2026/week02/01-context-tax.md) |
| 02 | [OpenSpec](https://openspec.dev/) | 产品网站/文档入口 | [笔记完成：首页及 quickstart](fall2026/week02/02-openspec.md) |
| 02 | [Superpowers](https://github.com/obra/superpowers) | 代码仓库 | [笔记完成：固定提交精选文件](fall2026/week02/03-superpowers.md) |
| 02 | [企业级 MCP](https://blog.cloudflare.com/enterprise-mcp) | 工程文章 | [笔记完成：全文](fall2026/week02/04-enterprise-mcp.md) |
| 03 | [pstack 技能集](https://github.com/cursor/plugins/tree/main/pstack) | 仓库子目录 | [笔记完成：固定提交精选文件](fall2026/week03/01-pstack.md) |
| 03 | [Matt Pocock 的技能集](https://github.com/mattpocock/skills) | 代码仓库 | [笔记完成：固定提交精选文件](fall2026/week03/02-matt-pocock-skills.md) |
| 03 | [browse.sh](https://browse.sh/) | 产品网站 | [笔记完成：首页与一个示例](fall2026/week03/03-browse.md) |
| 04 | [我仍然更偏好 MCP 而非 Skills](https://david.coffee/i-still-prefer-mcp-over-skills) | 作者观点文章 | [笔记完成](fall2026/week04/01-mcp-over-skills.md) |
| 04 | [AGENTS.md](https://docs.factory.com/harness/agents-md) | Factory 产品文档 | [笔记完成](fall2026/week04/02-factory-agents-md.md) |
| 04 | [引导 Claude Code](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) | 官方产品文章 | [笔记完成](fall2026/week04/03-steering-claude-code.md) |
| 04 | [编写高质量 CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md) | 行业经验文章 | [笔记完成](fall2026/week04/04-writing-a-good-claude-md.md) |
| 05 | [让代码库为 Agent 做好准备](https://www.youtube.com/watch?v=ShuJ_CN6zr4) | 视频 | 待获取字幕或转写 |
| 05 | [构建便于 Agent 使用的仓库](https://x.com/trybasis/status/2056881705269580023) | 社交媒体帖文 | 待获取 |
| 06 | [分层代码审查与基于风险的人工监督](https://x.com/addyosmani/status/2114604912520921136) | 社交媒体帖文 | 待获取；读取遇到传输错误 |
| 06 | [大规模协调专业审查 Agent](https://blog.cloudflare.com/ai-code-review) | 工程文章 | [笔记完成：全文](fall2026/week06/02-specialist-review.md) |
| 06 | [超越 Diff：上下文、测试与模型选择](https://www.greptile.com/blog/how-to-build-a-code-review-agent) | 行业经验文章 | [笔记完成：全文](fall2026/week06/03-beyond-diff.md) |

第 7–10 周当前未列专门阅读材料，不能从课程主题或嘉宾姓名生成“原文笔记”。周次学习路线、课堂解读和三周作业入口见 [Fall 2026 入口](fall2026/README.md)，课堂原链接与未读状态见[来源表](../reference/sources.md)。指定阅读尚缺 5 份：第 1、5 周两份视频和第 1、5、6 周三份 X 帖文。其他 14 份的笔记完成按声明范围计算，不表示全部仓库或多页网站覆盖。

## Fall 2025

下表已有十八份声明范围内的指定阅读解读，剩余 27 份尚无完成笔记；各项状态与实际范围分别记录，删减中文版不代表英文全文，提示指南精选六页不代表全站。系统教程引用本地讲义不代表已完整读过外部材料。[Fall 2025 课堂解读入口](fall2025/README.md)已有 13 份本地 PPTX 的文字解读，共 275 页可提取文字及关联备注，按概念融入第 01–09 章或关联已有覆盖；图片仍待视觉核验。[本地中文课件](../reference/sources.md#fall-2025-中文课件)的导航与[分阶段状态](../reference/sources.md#课件文字化与融合状态)独立维护，不把文字提取、视觉核验、解读和章节融合混为一项。

2026-11-05 经授权安装本地解析依赖后，读取 [Tomas 30 页](fall2025/week07/lecture-tomas-reimers.md)与 [Resolve 35 页](fall2025/week09/lecture-resolve-guest.md)的可提取文字，完成文字范围内的解读并关联第 07、09 章。页面图已生成，但读取仅返回成功提示，没有可检查的内容，全部视觉核验仍待完成；未经核验的坐标、代码、日志与事故截图细节已撤回。底层运行证据和产品效果未验证。在线嘉宾课件与视频仍未完成，下表 Resolve 指定文章独立登记。

| 周次 | 材料与原始入口 | 类型 | 状态 |
| --- | --- | --- | --- |
| 01 | [深入理解 LLM](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 视频 | 待获取；原视频、指定中文版及公开字幕入口均传输错误 |
| 01 | [Prompt Engineering 概览](https://cloud.google.com/discover/what-is-prompt-engineering) | 文章 | 待获取；原入口及语言参数重试均传输错误，中文版仅标题 |
| 01 | [Prompt Engineering 指南](https://www.promptingguide.ai/techniques) | 多页指南 | [笔记完成：六个技术子页双语正文，非全站](fall2025/week01/03-prompt-engineering-guide.md) |
| 01 | [AI Prompt Engineering：深入解析](https://www.youtube.com/watch?v=T9aRN5JkmL8) | 视频 | 待获取；原视频、指定中文版及公开字幕入口均传输错误 |
| 01 | [OpenAI 如何使用 Codex](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf) | PDF 报告 | 待获取；PDF 超工具 5MB 限制，中文版 403，官方文字候选 404，无正文 |
| 02 | [MCP 简介](https://stytch.com/blog/model-context-protocol-introduction/) | 文章 | [笔记完成：全文，示例边界已校准](fall2025/week02/01-mcp-introduction.md) |
| 02 | [MCP Server 示例实现](https://github.com/modelcontextprotocol/servers) | 代码仓库 | 待获取；当前 PATH 无 gh，未取得文件或版本，不安装或绕行 |
| 02 | [MCP Server 身份验证](https://developers.cloudflare.com/agents/guides/remote-mcp-server/#add-authentication) | 产品文档 | [笔记完成：当前对应指南全文，非 2025 快照](fall2025/week02/03-remote-mcp-authentication.md) |
| 02 | [MCP Server SDK](https://github.com/modelcontextprotocol/typescript-sdk/tree/main?tab=readme-ov-file#server) | SDK 仓库 | 待获取；gh 不可用，无固定版本或正文 |
| 02 | [MCP Registry](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) | 官方文章 | [笔记完成：历史公告全文](fall2025/week02/05-mcp-registry.md) |
| 02 | [关于 MCP 的思考](https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/) | 作者观点文章 | [笔记完成：全文](fall2025/week02/06-apis-and-mcp-tools.md) |
| 03 | [规格即新的源代码](https://blog.ravi-mehta.com/p/specs-are-the-new-source-code) | 文章 | [笔记完成：英文预览与删减中文版，英文全文待核验](fall2025/week03/01-specs-as-source-code.md) |
| 03 | [长上下文如何失效](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) | 文章 | [笔记完成：全文及脚注，底层研究未读](fall2025/week03/02-how-contexts-fail.md) |
| 03 | [Devin：Coding Agents 101](https://devin.ai/agents101#introduction) | 指南文章 | [笔记完成：英文与指定中文正文/注释，非全站](fall2025/week03/03-coding-agents-101.md) |
| 03 | [让 AI 在复杂代码库中工作](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) | 仓库文档 | 待获取；gh 不可用，无文件或版本 |
| 03 | [FAANG 如何 Vibe Code](https://x.com/rohanpaul_ai/status/1959414096589422619) | 社交媒体帖文 | 待获取；X 传输错误，另取得的 Reddit 译述对应未证实，不计此项 |
| 03 | [为 Agent 编写有效工具](https://www.anthropic.com/engineering/writing-tools-for-agents) | 工程文章 | [笔记完成：英文/中文正文对照，图片未核验](fall2025/week03/06-writing-tools-for-agents.md) |
| 04 | [Anthropic 如何使用 Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf) | PDF 报告 | [笔记完成：官方网页替代与指定中文译述](fall2025/week04/01-how-anthropic-teams-use-claude-code.md)；PDF 超工具限制、版本对应未核验 |
| 04 | [Claude 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices) | 官方文章 | [笔记完成：指定中文译述及当前文档部分差异](fall2025/week04/02-claude-code-best-practices.md)；历史英文全文未取得 |
| 04 | [Awesome Claude Agents](https://github.com/vijaythecoder/awesome-claude-agents) | 代码仓库 | 待获取；gh 不可用，无正文或版本 |
| 04 | [Super Claude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 代码仓库 | 待获取；gh 不可用，无正文或版本 |
| 04 | [好的上下文，好的代码](https://blog.stockapp.com/good-context-good-code/) | 文章 | 待获取；Markdown/text 两次均传输错误 |
| 04 | [窥探 Claude Code 的内部机制](https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62) | 文章 | 待获取；Markdown/text 两次均传输错误，不以其他论文替代 |
| 05 | [Warp University](https://www.warp.dev/university?slug=university) | 课程集合入口 | 待获取；返回当前产品概览，未取得原课程集合正文 |
| 05 | [Warp 与 Claude Code 对比](https://www.warp.dev/university/getting-started/warp-vs-claude-code) | 产品课程页 | 原文待获取；返回同一概览；另有[当前迁移补充笔记](fall2025/week05/02-warp-claude-code-current-migration.md)，不计本项完成 |
| 05 | [Warp 如何用 Warp 构建 Warp](https://notion.warp.dev/How-Warp-uses-Warp-to-build-Warp-21643263616d81a6b9e3e63fd8a7380c) | 文档页面 | 待获取；仅 JavaScript 页面壳 |
| 06 | [SAST 与 DAST](https://www.splunk.com/en_us/blog/learn/sast-vs-dast.html) | 文章 | [笔记完成：本轮取得完整文字与比较表](fall2025/week06/01-sast-dast.md)；更新此前 403 状态，未运行扫描 |
| 06 | [通过 Prompt Injection 实现 Copilot RCE](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) | 安全案例 | [笔记完成：指定中文转载](fall2025/week06/02-copilot-rce.md)；英文传输错误，路径冲突/当前修复未知，不提供可执行攻击 |
| 06 | [使用 Claude Code 与 Codex 发现漏洞](https://semgrep.dev/blog/2025/finding-vulnerabilities-in-modern-web-apps-using-claude-code-and-openai-codex/) | 工程文章 | [笔记完成：全文、结果表与提示模板；原始数据/实验未验证](fall2025/week06/03-ai-vulnerability-evaluation.md) |
| 06 | [Agentic AI 威胁：身份欺骗与冒充](https://unit42.paloaltonetworks.com/agentic-ai-threats/) | 安全研究文章 | [笔记完成：全文文字、九场景与五层防护](fall2025/week06/04-agentic-identity-threats.md)；特定演示非框架通用漏洞，图像/实现未读 |
| 06 | [OWASP Top Ten](https://owasp.org/www-project-top-ten/) | 多版本指南 | [笔记完成：官方 2021 中文 A01–A10 及方法](fall2025/week06/05-owasp-top-ten-2021.md)；当前主页最新 2025，其类别正文/完整 ASVS 未读 |
| 06 | [Context Rot](https://research.trychroma.com/context-rot) | 研究报告 | [笔记完成：双语正文、脚注与附录文字](fall2025/week06/06-context-rot.md)；图表视觉/数据/代码/实验未验证 |
| 06 | [使用 O3 进行漏洞 prompt 分析](https://github.com/SeanHeelan/o3_finds_cve-2025-37899/blob/master/system_prompt_uafs.prompt) | 提示词源文件 | 待获取；gh 调用失败，不安装或绕行；未复现漏洞 |
| 07 | [Code Review：做就对了](https://blog.codinghorror.com/code-reviews-just-do-it/) | 文章 | [笔记完成：完整正文，转引原始研究未读](fall2025/week07/01-code-reviews-just-do-it.md) |
| 07 | [如何有效进行 Code Review](https://github.blog/developer-skills/github/how-to-review-code-effectively-a-github-staff-engineers-philosophy/) | 工程经验文章 | [笔记完成：完整正文，产品门禁/通知未验证](fall2025/week07/02-how-to-review-code-effectively.md) |
| 07 | [现代 Code Review 中 AI 辅助 Coding 实践评估](https://arxiv.org/pdf/2405.13565) | 论文 | 待获取 |
| 07 | [AI Code Review 落地最佳实践](https://graphite.dev/guides/ai-code-review-implementation-best-practices) | 产品指南 | [笔记完成：全文、表格与 FAQ；产品与宣传数字未验证](fall2025/week07/04-ai-review-implementation.md) |
| 07 | [软件团队的 Code Review 要点](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html) | 文章 | [笔记完成：完整正文，图片未视觉核验](fall2025/week07/05-code-review-essentials.md) |
| 07 | [来自数百万次 AI Code Review 的经验](https://www.youtube.com/watch?v=TswQeKftnaw) | 视频 | 待获取字幕或转写 |
| 09 | [SRE 导论](https://sre.google/sre-book/introduction/) | 书籍章节 | 待获取；原入口及 index.html 重试均传输错误，其他官方章节也未取得，未用替代摘要编写 |
| 09 | [需要了解的可观测性基础](https://last9.io/blog/traces-spans-observability-basics/) | 文章 | [笔记完成：完整正文与 FAQ，图片/SDK 未验证](fall2025/week09/02-traces-spans.md) |
| 09 | [使用 AI 排查 Kubernetes 故障](https://resolve.ai/blog/kubernetes-troubleshooting-in-resolve-ai) | 产品文章 | [笔记完成：完整正文，图片/产品未验证](fall2025/week09/03-kubernetes-troubleshooting.md) |
| 09 | [你的新 Autonomous Teammate](https://resolve.ai/blog/product-deep-dive) | 产品文章 | [笔记完成：完整正文，图片/产品/收益未验证](fall2025/week09/04-autonomous-teammate.md) |
| 09 | [多 Agent 系统如何使工程师 AI-native](https://resolve.ai/blog/role-of-multi-agent-systems-AI-native-engineering) | 产品文章 | [笔记完成：完整正文及比较表，视频/实现/对照未验证](fall2025/week09/05-multi-agent-ai-native.md) |
| 09 | [Agentic AI 在 On-call 工程中的益处](https://resolve.ai/blog/Top-5-Benefits) | 产品文章 | [笔记完成：完整正文，收益主张未验证](fall2025/week09/06-on-call-benefits.md) |

第 8、10 周阅读材料栏为空，未建立虚构材料条目。

## 作业材料

作业与上述 64 项指定阅读独立统计。已盘点当前本地全部 11 份 assignment，并核对 11 份导读：2026 第 1–3 周见[2026 学习路线](fall2026/README.md)，2025 第 1–8 周见[2025 作业入口](fall2025/README.md#已有作业导读)。本批补齐[第 7 周审查证据](fall2025/week07/assignment-guide.md)与[第 8 周三栈交付](fall2025/week08/assignment-guide.md)，各含原 100 分评分、源码机制、证据缺口、50 分钟零执行替代与自测，关联第 07、09 章。第 7 周 15 项业务操作、14 个测试函数均属静态盘点，未定义 li、Unicode 标签和弱 AND 数据集不当作实测；第 8 周 Bolt 来源与耗时仅报告自述，三栈契约/CSRF/导入写库边界另列。未运行原作业、客户端、Agent、测试、Hook、扫描、攻击、数据库、构建、认证或外部写入；导读完成不代表作业完成，本地未取得的后续 2026 作业不补造。

## 笔记编写约定

文件按 `fallYYYY/weekNN/序号-主题.md` 放置，序号对应该周阅读材料顺序，不因本轮先完成后面的条目而重新编号。每周开始编写时建立周索引，链接回本页与相应章节。

每份笔记包括来源与阅读范围、阅读目标、原作者核心观点、按原文小节定位的详细解读、案例与术语、局限、自测答案和教程关联。引用只保留必要短句，主要用中文转述；保留作者归属，不复制整篇受版权保护的正文。仓库类材料必须声明实际读取文件和版本，多页网站不得声称完整阅读。

默认不下载完整视频、不安装转写依赖、不调用付费转写服务。需要这些操作时另行确认。索引条目的外部链接未由文档校验器检查；状态以实际获取证据为准。
