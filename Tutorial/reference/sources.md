# 资料索引与来源边界

[返回目录](../README.md)

本教程根据本地资料重新组织，正文中的解释与实验不是逐页翻译，也不声称复现了完整嘉宾讲座。以下链接可以溯源；完成学习不需要打开视频。

系统教程位于 `chapters/`，共用资料位于 `reference/`。[逐份阅读笔记索引](../reading-notes/README.md)记录指定阅读的范围与进度；本文件记录教程依据与课堂材料状态，两者不等同。已有 2026 年 14 份和 2025 年二十八份声明范围内的指定阅读笔记，共 42/64 份，22 份待补；另有 Warp 当前迁移与 Addy 官方文章两份补充，不计指定阅读完成数。规格按英文预览与删减中文版、提示指南按六个双语技术子页完成，不代表英文全文或全站。三份课堂转写解读和本地全部 11 份作业导读另行统计，未执行模型、OAuth、客户端或安全实验。

增量核对日期为 2026-11-05，以当前根 README、真实资料和本地文件为依据，不以历史 merge 代表覆盖。前一轮新增 Devin、Anthropic 团队与最佳实践、安全五项、AutoCommenter 共九份指定笔记后为 41/64；本次处理剩余 23 项，改用现有 PyMuPDF 在内存中取得 Codex 官方 PDF 8040907 字节、13 页可提取文字，新增一份并关联第 06、07 章。通用读取仍超 5MB，指定中文仍 403；图像及第 13 页无提取文字的视觉内容未核验。其余 22 项缺口见[分类与逐项表](../reading-notes/README.md#剩余获取缺口)：字幕列表传输错误，X 传输错误/超时，Google/stockapp/Medium/SRE 未取得正文，Notion HTML 无正文，Warp 历史两入口仍返回当前概览。SRE 直接 HTTP 请求也超时；本地盘点无所需原文副本，gh 仍不可用，未安装或绕 GitHub 入口。并非本次重新取得全部 64 项外链；旧已读材料按声明范围沿用。在线课件及英文规格全文缺口独立保留，本次未安装、保存 PDF、下载完整视频、登录、执行来源脚本或产品实验。

当前本地全部 11 份作业已有导读：2025 第 1–8 周见[年份入口](../reading-notes/fall2025/README.md#已有作业导读)，2026 第 1–3 周见[学习路线](../reading-notes/fall2026/README.md)。此前盘点所有 assignment、核对既有九份导读并重读 2026 三份说明，补齐[第 7 周](../reading-notes/fall2025/week07/assignment-guide.md)与[第 8 周](../reading-notes/fall2025/week08/assignment-guide.md)，最小关联第 07、09 章。第 7 周实际读说明/报告/配置、八份应用 Python、六份测试（含 fixture）、三个前端与种子；第 8 周读三栈说明、主体源码、配置、迁移与模板，Flask 单行 CSS 仅取得前 2000 字符，尾部不计已读，包初始化仅盘点。各导读列精确范围与限制：源码缺陷是静态推导，Graphite 未运行，Bolt 使用及耗时只有报告自述；功能、数据库和原提交要求未验证。作业不增加指定阅读完成数，外部阅读、视频、在线课件与视觉核验缺口保留。未导入/执行作业 Python、测试、应用、构建、迁移、登录、调用 AI、创建数据库、远程 PR 或推送；本次 Python 仅用于内存 PDF 文字提取，报告外链未读。

### 外网受限后的学习替代

2026-11-05 用户确认采用可追溯中文补充与本地资料深化，详见[22 项学习替代入口](offline-learning.md)。本轮新增 DAIR.AI 中文入门四页的实际阅读与解读，章节最小补采样/截断辨析和 SLO 错误预算假例。补充不消除原文、视频、仓库或视觉缺口，指定阅读仍为 42/64；四页入门属于已有指南的额外范围，不重复计数。预算例和替代路线为教程扩展，不归属未读 SRE 导论。

此前用户另获授权安装官方 gh，但 WinGet 不可用、官方 MSI 下载超时、curl 重试中止，未成功安装、验证或认证；上文“未安装”描述先前轮次。本轮暂停安装、网络配置及受限原入口重试，没有调整代理、下载完整视频、执行课程代码或产品实验。已读旧来源按原声明沿用，不声称本轮重新获取全部外链。

### 第 01 章自包含样板

2026-11-05 按用户确认方案，将已有两份课件解读、六技术双语笔记、四页中文补充与原作业静态依据按知识融入[第 01 章](../chapters/01-llm-prompting.md)。章内提供生成流程、完整提示、参数算例、六类机制与原案例、独立匹配/评测、集中练习和答案；笔记保留逐页与逐文件定位，章末可选溯源。原作业六份脚本及 assignment 本轮重读，未执行；外部材料沿用先前声明范围，未重新请求受限来源。自包含仅指本章基础学习闭环，不指全部原件、矩阵推导、真实实验或其余章节已完成。指定阅读仍为 42/64，22 项获取缺口和全部视觉核验缺口保留。

2026-11-06 经样板审阅后，补充人为分词与术语例、响应结构/语义处理、多路径聚合、反思记录加载，以及完整开放题参考产物；按两段学习调整预算，原作业与来源核验明确选学。随后补齐首次出现的中文与白话定义，拆分训练与评测概念；按“降低负荷、闭合规则、做出成果”反馈，将复杂机制折叠选学，基础改为五步提取设计，提供记录框、逐步通过标准和对应答案。进阶小题独立验收，保留拆分、否定、冲突复核、容量超限及CoT/分解的边界。

本次按整章叙述衔接反馈重排已有内容：以行动项需求引出生成与任务约定，先看具体失败再解释示例、分解与反馈，先比较响应再划分检查职责，先匹配任务再命名TP/FP/FN。其他案例说明切换理由并返回主线；基础练习与答案按同一顺序闭合，具体反馈不再藏在选学部分。基础阅读60–90分钟、练习75分钟仍为估计。章内假例和练习均为教程扩展，不是原课件图示、指南真实轨迹、现行 SDK 接口或模型成绩；沿用既有来源范围，未新增外链获取、视觉核验或实验执行，未做真实新手阅读测试，指定阅读仍为42/64。

### 全章教学重组

2026-11-06 将同一教学要求扩展到00及02–10章，保留编号、主线和原来源边界。00补必要前置与证据判断；02–04把调用关联、上下文冲突、严格候选与应用包装、工具参数、双OAuth边界及批准/幂等连成案例；05–07以诊断、交接、依赖和失败记录讲自动化、并行与诚实评测；08–10以资产/动作、全链路证据、双指标预算和阶段门禁讲安全、运维及团队交付。各章基础假材料、练习、通过标准与详细答案在章内闭合，真实实验和长来源对照独立选学。新增假记录、预算与工程策略为教程扩展，沿用既有已读范围，未重新获取外链、核验图像或运行模型、OAuth、应用、安全、数据库与工厂。指定阅读仍42/64、缺口仍22项；全部视觉核验与新手阅读效果仍待验证，章节重组不等于全部课程资料或真实项目完成。

## 1. 课程定位

- [根 README](../../README.md)：课程目标、前置条件、时间投入及 2025/2026 大纲。
- [Fall 2025 原始资料目录](../../Resource/Fall2025/)：PPTX、课堂代码、设计文档及嘉宾 PDF。
- [Fall 2025 中文课件目录](slides/fall2025/)：13 份配套 PPTX，与原版共用下面的章节映射，不另维护一套教程。
- [2025 作业根目录](../../_assignments/2025%20fall/)：完整练习及依赖配置。
- [2026 本地作业目录](../../_assignments/2026%20fall/modern-software-dev-assignments-master/)：已取得第 1 至 3 周作业。

## 2. 逐章对应

| 教程 | 核心本地来源 | 教程补充 |
| --- | --- | --- |
| 00 环境与方法 | [2025 安装说明](../../_assignments/2025%20fall/README.md)、[2025 pyproject](../../_assignments/2025%20fall/pyproject.toml)、[2026 安装说明](../../_assignments/2026%20fall/modern-software-dev-assignments-master/README.md)、[2026 pyproject](../../_assignments/2026%20fall/modern-software-dev-assignments-master/pyproject.toml)、[Makefile](../../_assignments/2025%20fall/week4/Makefile) | 双年份目录、算法诊断、访问验收与实验设计 |
| 01 LLM 与提示 | [LLM](../../Resource/Fall2025/week01-0922-intro-to-llms.pptx)、[提示](../../Resource/Fall2025/week01-0926-effective-prompting.pptx)、[作业](../../_assignments/2025%20fall/week1/assignment.md) | 自包含样板：完整提示、参数、六类案例、匹配/P/R/F1、离线练习与答案；假例和评测为扩展 |
| 02 Agent | [讲义](../../Resource/Fall2025/week02-0929-building-a-coding-agent.pptx)、[代码](../../Resource/Fall2025/week02-0929-completed-exercise.py)、[2026 trace](../../_assignments/2026%20fall/modern-software-dev-assignments-master/week1/assignment.md) | 执行边界、预算与恢复 |
| 03 上下文与规格 | [AI IDE](../../Resource/Fall2025/week03-1006-ai-ide-setup.pptx)、[设计模板](../../Resource/Fall2025/week03-1006-design-document-template.md)、[行动项作业](../../_assignments/2025%20fall/week2/assignment.md) | RePPIT 编排、示例契约 |
| 04 MCP/OAuth | [MCP](../../Resource/Fall2025/week02-1003-custom-mcp-server.pptx)、[代码](../../Resource/Fall2025/week02-1003-completed-exercise.py)、[2025 作业](../../_assignments/2025%20fall/week3/assignment.md)、[2026 作业](../../_assignments/2026%20fall/modern-software-dev-assignments-master/week2/assignment.md) | 信任边界、幂等和 OAuth 细化 |
| 05 自动化 | [Agent 管理](../../Resource/Fall2025/week04-1013-agent-manager.pptx)、[Claude Code](../../Resource/Fall2025/week04-1017-boris-cherny.pptx)、[2025 作业](../../_assignments/2025%20fall/week4/assignment.md)、[2026 Skill](../../_assignments/2026%20fall/modern-software-dev-assignments-master/week3/assignment.md) | MCP/Skill/CLI 组合、作用域、渐进披露与门禁 |
| 06 仓库与并行 | [产品讲义](../../Resource/Fall2025/week05-1020-ai-developer-product.pptx)、[Warp 作业](../../_assignments/2025%20fall/week5/assignment.md) | 就绪度自评、独立任务、指令漂移、隔离与后台状态 |
| 07 测试与审查 | [测试讲义](../../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[审查讲义](../../Resource/Fall2025/week07-1103-ai-code-review.pptx)、[Tomas PDF](../../Resource/Fall2025/week07-1107-tomas-reimers-slides.pdf)、[审查作业](../../_assignments/2025%20fall/week7/assignment.md) | 测试层次、风险分层、专业审查；Tomas 三项职责与内外循环关联，验收练习为教程扩展 |
| 08 安全 | [安全讲义](../../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[Semgrep 作业](../../_assignments/2025%20fall/week6/assignment.md)、[非官方商业页](../../Resource/Claude-Code%E5%85%85%E5%80%BC/README.md) | 威胁模型、注入防护、凭据披露辨析和回归 |
| 09 交付与运维 | [全栈](../../Resource/Fall2025/week08-1110-end-to-end-app.pptx)、[三栈作业](../../_assignments/2025%20fall/week8/assignment.md)、[事故响应](../../Resource/Fall2025/week09-1117-incident-response-devops.pptx)、[Resolve PDF](../../Resource/Fall2025/week09-1121-resolve-guest-lecture-slides.pdf) | 验收、SLI/SLO；关联 Resolve 系统关系、团队知识与并行调查观点，权限/预算/失败评测练习为教程扩展 |
| 10 团队与工厂 | [README 2026 大纲](../../README.md)、[自动化作业](../../_assignments/2025%20fall/week4/assignment.md)、[交付作业](../../_assignments/2025%20fall/week8/assignment.md) | 网关、受控流水线、开源贡献闭环与独立自学评分 |

## 3. 阅读源代码时的四个提醒

- [自洽性脚本](../../_assignments/2025%20fall/week1/self_consistency_prompting.py) 当前提示含预期答案。它不构成无泄漏的能力评测。
- [RAG 脚本](../../_assignments/2025%20fall/week1/rag.py) 的字符串检查与多次尝试成功不等价于运行正确或首次可靠。
- [提取实现](../../_assignments/2025%20fall/week2/app/services/extract.py) 已有 LLM 与回退逻辑；[测试](../../_assignments/2025%20fall/week2/tests/test_extract.py) 主要使用 mock，需另测真实质量。
- [课堂 MCP 原型](../../Resource/Fall2025/week02-1003-completed-exercise.py) 不应照搬不受限路径与 stdout 日志到生产。

这些提醒针对当前本地快照，不是在指责原课程练习目标。教学简化有价值，但必须解释简化边界。

## 4. 更新教程时

补入新资料时先确认其版本和内容，再调整章节及来源表。不要把仅存在于网页链接中的内容写成已阅读的本地依据。命令、认证流程与 SDK 示例涉及外部实时行为时，核对当前官方文档和实际版本。

经用户明确授权，中文课件已归入 `Tutorial/reference/slides/fall2025/`，Python 工具统一放入 `Tutorial/scripts/`，课件内容不变；英文原件及 `Resource/.translation_work/` 中间数据保留原位。原版用于溯源，正式中文 PPTX 用于辅助阅读；阅读链接直接指向成品，不依赖中间文件。

## Fall 2025 中文课件

2026-11-04 核对本地目录中的 13 个文件并接入下表。此表是配套阅读导航，不是逐份课件解读或翻译质量验收，不计入指定阅读笔记完成数。课程位置按根 README 的 Fall 2025 大纲对应；同名原版与中文版视为同一来源。

| 课程位置与课件 | 中文版 | 原版 | 对应教程 |
| --- | --- | --- | --- |
| 第 1 周：LLM 导论 | [中文 PPTX](slides/fall2025/week01-0922-intro-to-llms.pptx) | [原版](../../Resource/Fall2025/week01-0922-intro-to-llms.pptx) | [01 LLM 与提示](../chapters/01-llm-prompting.md) |
| 第 1 周：高效提示 | [中文 PPTX](slides/fall2025/week01-0926-effective-prompting.pptx) | [原版](../../Resource/Fall2025/week01-0926-effective-prompting.pptx) | [01 LLM 与提示](../chapters/01-llm-prompting.md) |
| 第 2 周：构建 Coding Agent | [中文 PPTX](slides/fall2025/week02-0929-building-a-coding-agent.pptx) | [原版](../../Resource/Fall2025/week02-0929-building-a-coding-agent.pptx) | [02 Agent](../chapters/02-agent-loop.md) |
| 第 2 周：自定义 MCP Server | [中文 PPTX](slides/fall2025/week02-1003-custom-mcp-server.pptx) | [原版](../../Resource/Fall2025/week02-1003-custom-mcp-server.pptx) | [04 MCP/OAuth](../chapters/04-mcp-oauth.md) |
| 第 3 周：AI IDE 配置 | [中文 PPTX](slides/fall2025/week03-1006-ai-ide-setup.pptx) | [原版](../../Resource/Fall2025/week03-1006-ai-ide-setup.pptx) | [03 上下文与规格](../chapters/03-context-spec.md) |
| 第 3 周：Silas Alberti 嘉宾课件 | [中文 PPTX](slides/fall2025/week03-1010-silas-alberti.pptx) | [原版](../../Resource/Fall2025/week03-1010-silas-alberti.pptx) | [03 上下文与规格](../chapters/03-context-spec.md)、[06 仓库与并行](../chapters/06-repo-parallel.md)，已读讲义观点，不泛化效率数字 |
| 第 4 周：Agent 管理 | [中文 PPTX](slides/fall2025/week04-1013-agent-manager.pptx) | [原版](../../Resource/Fall2025/week04-1013-agent-manager.pptx) | [05 Skills 与自动化](../chapters/05-skills-automation.md) |
| 第 4 周：Boris Cherny 嘉宾课件 | [中文 PPTX](slides/fall2025/week04-1017-boris-cherny.pptx) | [原版](../../Resource/Fall2025/week04-1017-boris-cherny.pptx) | [05 Skills 与自动化](../chapters/05-skills-automation.md) |
| 第 5 周：AI 开发者产品 | [中文 PPTX](slides/fall2025/week05-1020-ai-developer-product.pptx) | [原版](../../Resource/Fall2025/week05-1020-ai-developer-product.pptx) | [06 仓库与并行](../chapters/06-repo-parallel.md) |
| 第 6 周：AI QA、SAST 与 DAST | [中文 PPTX](slides/fall2025/week06-1027-ai-qa-sast-dast.pptx) | [原版](../../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx) | [07 测试与审查](../chapters/07-testing-review.md)、[08 安全](../chapters/08-security.md) |
| 第 7 周：AI 代码审查 | [中文 PPTX](slides/fall2025/week07-1103-ai-code-review.pptx) | [原版](../../Resource/Fall2025/week07-1103-ai-code-review.pptx) | [07 测试与审查](../chapters/07-testing-review.md) |
| 第 8 周：端到端应用 | [中文 PPTX](slides/fall2025/week08-1110-end-to-end-app.pptx) | [原版](../../Resource/Fall2025/week08-1110-end-to-end-app.pptx) | [09 交付与运维](../chapters/09-delivery-operations.md) |
| 第 9 周：事故响应与 DevOps | [中文 PPTX](slides/fall2025/week09-1117-incident-response-devops.pptx) | [原版](../../Resource/Fall2025/week09-1117-incident-response-devops.pptx) | [09 交付与运维](../chapters/09-delivery-operations.md) |

使用方法：先学习对应章节，再按需打开中文课件查看图示与课堂结构；遇到术语或论断疑问，记录页码并对照原版，不把翻译当作独立权威来源。第 00 章仍以环境说明和依赖配置为依据，第 10 章仍使用统一综合项目，不为课件增加重复章节。

根据[本地翻译脚本](../scripts/translate_fall2025.py)，生成过程替换幻灯片及备注中的文本，其他资源保持原样。这意味着图片内文字不一定已翻译；已按页核对可提取文字与备注并编写解读，但图片文字、图示关系和排版溢出尚未视觉核验。旧界面、安装命令、产品能力和价格不能作为当前操作保证，实际操作仍需核对当前官方资料。

脚本按自身位置定位路径，不依赖终端当前目录：读取 `Resource/Fall2025/` 原件和 `Resource/.translation_work/` 翻译数据，输出到 `Tutorial/reference/slides/fall2025/`。在仓库根目录可运行 `python Tutorial/scripts/translate_fall2025.py check` 检查已有成果；`extract` 会写入中间数据，`generate` 会覆盖中文课件，维护时应先确认已有修改并备份。

### 课件文字化与融合状态

2026-11-04 在两份样板基础上继续处理剩余 11 份，本地 13 份 PPTX 共 275 页的可提取文字与关联备注已中英文对照，并有逐份中文解读。文字提取不等于视觉核验或官方逐字译文；章节只吸收有教学价值的概念，已覆盖的内容补来源关联。指定阅读的完成数不因课堂课件增加而改变。

2026-11-05 经用户授权安装 PyMuPDF 2.1 及自动依赖，实际读取 Tomas 30 页、Resolve 35 页可提取文字，渲染 8/9 张四页核对图。图像读取仅返回成功提示，没有可检查的内容，因此撤回“页面图已查看、关键截图已核对”的声明及未经核验的细节。页数、署名和能力文字已核对，两份解读仅在文字范围内完成；全部视觉核验仍待完成。产品/原始事故证据未验证；PDF 独立统计，不加入 PPTX 页数，未生成中文版 PDF。

| 原材料 | 文字提取与核对 | 图像与版式 | 中文解读 | 章节融合 |
| --- | --- | --- | --- | --- |
| LLM 导论 | 20 页及关联备注，中英文可提取文字已对照 | 图片未视觉核验；第 16 页表格文字已读但布局未还原 | [已完成，声明缺口](../reading-notes/fall2025/week01/lecture-intro-to-llms.md) | [01](../chapters/01-llm-prompting.md)：训练/推理、数据量/参数、概率辨析离线练习 |
| 构建 Coding Agent | 7 页及关联备注，中英文可提取文字已对照；198 行配套代码静态阅读 | 第 3 页六个图片对象未视觉核验 | [已完成，声明缺口](../reading-notes/fall2025/week02/lecture-building-a-coding-agent.md) | [02](../chapters/02-agent-loop.md)：代码定位、缺参覆盖风险、消息关联与总预算 |
| 高效提示 | 31 页及关联备注，中英文文字已对照 | 未视觉核验，截图与角色效果有缺口 | [中文解读](../reading-notes/fall2025/week01/lecture-effective-prompting.md) | [01](../chapters/01-llm-prompting.md)：提示技术、独立证据与失败辨析 |
| 自定义 MCP Server | 13 页及关联备注，中英文文字已对照；配套代码静态阅读 | 未视觉核验，不复原多接口图 | [中文解读](../reading-notes/fall2025/week02/lecture-custom-mcp-server.md) | [04](../chapters/04-mcp-oauth.md)：连接复用与服务端职责 |
| AI IDE 配置 | 15 页及关联备注，中英文文字已对照 | 未视觉核验，索引图与配置截图有缺口 | [中文解读](../reading-notes/fall2025/week03/lecture-ai-ide-setup.md) | [03](../chapters/03-context-spec.md)：规格与上下文；[06](../chapters/06-repo-parallel.md)：仓库就绪 |
| Silas Alberti | 29 页及关联备注，中英文文字已对照；第 8–11 页表格可提取标签已读 | 图片与表格布局未视觉核验，不推断矩阵产品位置 | [中文解读](../reading-notes/fall2025/week03/lecture-silas-alberti.md) | [03](../chapters/03-context-spec.md)：规格交接；[06](../chapters/06-repo-parallel.md)：同步/异步与交接，不泛化效率数字 |
| Agent 管理 | 14 页及关联备注，中英文文字已对照 | 未视觉核验，不重建历史图片 | [中文解读](../reading-notes/fall2025/week04/lecture-agent-manager.md) | [05](../chapters/05-skills-automation.md)：委派、检查点与门禁 |
| Boris Cherny | 49 页及关联备注，中英文文字已对照 | 未视觉核验，界面迭代截图与纯图片页有缺口 | [中文解读](../reading-notes/fall2025/week04/lecture-boris-cherny.md) | [05](../chapters/05-skills-automation.md)：任务适配流程，不照搬旧 CLI |
| AI 开发者产品 | 14 页及关联备注，中英文文字已对照 | 未视觉核验，采用率图不作实证 | [中文解读](../reading-notes/fall2025/week05/lecture-ai-developer-product.md) | [06](../chapters/06-repo-parallel.md)：可见反馈、操作摩擦与控制 |
| AI QA、SAST、DAST | 22 页及关联备注，中英文文字已对照 | 未视觉核验，不补造攻击截图细节 | [中文解读](../reading-notes/fall2025/week06/lecture-ai-qa-sast-dast.md) | [07](../chapters/07-testing-review.md)、[08](../chapters/08-security.md)：检测覆盖与分诊 |
| AI Code Review | 25 页及关联备注，中英文文字已对照 | 未视觉核验，代码截图案例未复原 | [中文解读](../reading-notes/fall2025/week07/lecture-ai-code-review.md) | [07](../chapters/07-testing-review.md)：可复核评论、噪声与责任 |
| 端到端应用 | 17 页及关联备注，中英文文字已对照 | 未视觉核验，架构图与执行结果有缺口 | [中文解读](../reading-notes/fall2025/week08/lecture-end-to-end-app.md) | [09](../chapters/09-delivery-operations.md)：原型与全链路验收 |
| 事故响应与 DevOps | 19 页及关联备注，中英文文字已对照 | 未视觉核验，产品截图不作执行证据 | [中文解读](../reading-notes/fall2025/week09/lecture-incident-response-devops.md) | [09](../chapters/09-delivery-operations.md)：证据驱动的分诊与受控缓解 |
| [Resolve 嘉宾 PDF](../../Resource/Fall2025/week09-1121-resolve-guest-lecture-slides.pdf) | 35 页可提取文字已读，页数与署名已核对 | 9 张核对图已渲染；内容未完成可检查的视觉核验，全部页面待核验 | [文字范围内完成，截图细节已撤回](../reading-notes/fall2025/week09/lecture-resolve-guest.md) | [09](../chapters/09-delivery-operations.md)：系统关系、知识与并行调查的文字观点；权限/预算和验收为教程扩展 |
| [Tomas Reimers 嘉宾 PDF](../../Resource/Fall2025/week07-1107-tomas-reimers-slides.pdf) | 30 页可提取文字已读，页数与归属已核对 | 8 张核对图已渲染；坐标、节点与截图未视觉核验，全部页面待核验 | [文字范围内完成，图像缺口明确](../reading-notes/fall2025/week07/lecture-tomas-reimers.md) | [07](../chapters/07-testing-review.md)：三项职责、平台/参与者和内外循环文字；端到端算例为教程扩展 |
| Fall 2025 在线嘉宾课件（根 README 的 Warp / Vercel 入口） | Warp 返回 Figma 标题；Vercel 文字导出传输错误，均无正文 | 未核验 | 待获取，不以主讲 PPTX 替代 | 未完成来源特定融合 |

这些笔记没有视频时间戳，不是相应视频的替代转写。LLM 导论第 13 页的历史评分、18–19 页的闭源模型规模与价格不写成当前课程事实；Agent 第 7 页的产品机制与推测不写成通用保证。其余课件的效率、检测率、误报率与产品宣传也不能泛化。本地授课课件中的嘉宾预告不证明嘉宾是本讲作者；运维第 16 页的代码审查文案保留疑似模板残留状态，不转述为运维效果实证。原件、中文版、翻译中间数据均未更改或重新生成。

Resolve 第 1–2 页署名与 Tomas 的课程归属已对照；两份的页数和能力文字有实际原件提取依据。页面渲染与读取成功提示不构成视觉证据，不由既有稿反证来源；未经核验的截图指标、代码和根因输出不纳入原文解读。无现场演示、问答转写或产品运行证据，不公开整套截图与完整原文。

本轮复用工作区已有的只读核对工具 [pptx_text.py](../scripts/pptx_text.py)，仅调整存放目录，未修改工具内容。它按演示关系取页序并关联备注，打印页面位置和图片/表格数量，适合维护时核对文字，不执行 OCR、不恢复图示、不生成正式笔记。仓库根目录示例：

```powershell
python Tutorial/scripts/pptx_text.py "Resource/Fall2025/week01-0922-intro-to-llms.pptx" "Tutorial/reference/slides/fall2025/week01-0922-intro-to-llms.pptx"
```

不另公开归档完整逐页原文底稿；正式产物是可追溯的中文解读及章节增量。后续材料遵循同一三层流程：按页码或真实时间戳读取，编写逐份解读，按概念融合学习必需的内容并更新各阶段状态，不全文堆叠；已读笔记不自动证明章内自包含。视频优先公开转写和字幕；下载完整音视频、安装 OCR/ASR 或付费转写仍需独立授权。

### 本地 PDF 核对工具

[pdf_review.py](../scripts/pdf_review.py)输出原件 SHA256、总页数与按页提取的文字，并把最多四页组成带页码的临时 PNG 核对图。默认处理全部页面，`--pages` 使用从 1 开始的页码；无效页码会在创建临时输出前拒绝。工具不做 OCR、不运行 PDF 中的链接或代码，也不修改原 PDF；终端文字顺序可能受多栏布局影响，截图内文字不保证可提取，渲染成功仍须实际检查图像。

```powershell
python Tutorial/scripts/pdf_review.py "Resource/Fall2025/week07-1107-tomas-reimers-slides.pdf"
python Tutorial/scripts/pdf_review.py "Resource/Fall2025/week09-1121-resolve-guest-lecture-slides.pdf" --pages 29 30 32
```

2026-11-05 经独立授权，以 `python -m pip install --user PyMuPDF` 安装到本机当前用户 Python 3.14 环境，实际版本为 PyMuPDF 2.1；安装自动带入 pymupdf-layout/pymupdf4llm、numpy、onnxruntime 等依赖，不等于仅安装一个包，也未单独执行 OCR/ASR。未改 PATH 或升级 pip，不是隔离虚拟环境。日常文档校验不需要这些依赖；其他机器使用本工具前须独立确认依赖与安装授权，不能把本次版本当永久固定要求。页面图写入系统临时目录，工具不会自动删除；不要将整套图片或逐页原文作为公开教程产物。

## 5. 已读来源与使用边界

“已阅读”指维护期间实际取得声明范围的正文，不表示本次重新读取所有来源、已验证产品运行或复现作者实验。外部页面可能持续更新，下表保留各批读取范围，不保证永久可访问。

| 来源 | 类别与状态 | 用于何处及限制 |
| --- | --- | --- |
| [Prompt Engineering Guide](https://www.promptingguide.ai/techniques)及[中文入口](https://www.promptingguide.ai/zh/techniques) | DAIR.AI，fewshot/cot/consistency/rag/react/reflexion 六页双语正文；其余技术页未读 | [六页精选解读](../reading-notes/fall2025/week01/03-prompt-engineering-guide.md)，01；双语用词/删减差异已说明，图片、论文、notebook、旧 SDK 未验证 |
| [中文提示入门](https://www.promptingguide.ai/zh/introduction)及 settings/elements/tips | DAIR.AI，2026-11-05 四页中文正文与文字示例；无可核验逐页日期/个人署名，英文对应未读 | [补充解读](../reading-notes/fall2025/week01/supplement-prompting-introduction.md)，01；扩大已有指南范围，不增加指定完成数，不替代 Google 原概览；温度措辞、实体与推荐契约疑点保留，API/效果未验证 |
| [Semgrep 漏洞发现研究](https://semgrep.dev/blog/2025/finding-vulnerabilities-in-modern-web-apps-using-claude-code-and-openai-codex/) | Romain Gaucher、Vasilii Ermilov、Clint Gibler，2025-09-02，完整文字、表格与提示模板已取得；同日交付前复核传输错误 | [分母与生命周期](../reading-notes/fall2025/week06/03-ai-vulnerability-evaluation.md)，07、08；依据此前取得正文，原文 TPR/FPR 分母校准，原始数据、图像、应用、成本与实验未复现 |
| [Graphite AI 审查落地指南](https://graphite.dev/guides/ai-code-review-implementation-best-practices) | Greg Foster，完整正文、表格与 FAQ，无可核验绝对发布日期 | [试点与反馈校准](../reading-notes/fall2025/week07/04-ai-review-implementation.md)，07；类型不能代替全部运行时验证，接受率/准确率/收益周期宣传未核验，产品未运行 |
| [OpenAI 如何使用 Codex](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf)及[中文版](https://tools.wingzero.tw/article/sn/3533) | 官方原件 13 页可提取文字，现有 PyMuPDF 内存解析成功；无个人署名/日期元数据，中文仍 403 | [任务、环境与验收](../reading-notes/fall2025/week01/05-how-openai-uses-codex.md)，06、07；第 13 页无提取文字，图像未核验，不把历史 Ask/Code Mode、research preview 或自述收益当现行保证 |
| [Traces & Spans](https://last9.io/blog/traces-spans-observability-basics/) | Anjali Udasi，2025-04-23，完整正文及 FAQ | [操作关系、传播与采样](../reading-notes/fall2025/week09/02-traces-spans.md)，09；图片/规范/SDK 未验证，开销与产品主张不泛化 |
| [SAST vs. DAST vs. RASP](https://www.splunk.com/en_us/blog/learn/sast-vs-dast.html) | Shanika Wickramasinghe，2024-12-18；本轮取得完整文字、比较表及结论，更新此前 403 | [检测时点与覆盖](../reading-notes/fall2025/week06/01-sast-dast.md)，08；RASP 防护不等于根因修复，未运行扫描或防护 |
| [Coding Agents 101](https://devin.ai/agents101)及[指定中文](https://www.vibevibe.cn/Articles/01-core-concepts/coding-agents-101.html) | Cognition Team，June 2025，正文、表和四注释；指定中文对照 | [委派与检查点](../reading-notes/fall2025/week03/03-coding-agents-101.md)，03、06；初级伙伴风险和 MCP beta 注释的中文差异保留，收益经验不泛化 |
| [Anthropic 团队使用报告](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)及[指定中文](https://baoyu.io/translations/how-anthropic-teams-use-claude-code) | 十团队中文译述及官方 news 全文，官方页 2025-07-24；PDF 超 5MB，逐句/版本对应未核验 | [专业子任务与组合验收](../reading-notes/fall2025/week04/01-how-anthropic-teams-use-claude-code.md)，05、06；官方短版与中文详细版不混为 PDF 全文 |
| [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)及[指定中文](https://claude.whaty.org/posts/Claude-code-official-best-practices.html) | 指定中文完整译述，标 2025 年 12 月；原入口返回当前文档，尾部截断，仅已见段落作差异校准 | [规划、权限与验证](../reading-notes/fall2025/week04/02-claude-code-best-practices.md)，05、06；历史英文全文未得，不照搬当前命令或推定运行兼容 |
| [Warp 当前迁移指南](https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-claude-code/) | 当前官方正文，2026-11-03；额外补充，非原 2025 对比课 | [终端、Agent 与恢复边界](../reading-notes/fall2025/week05/02-warp-claude-code-current-migration.md)，05、06；不计指定阅读，规则改名不保证工具/认证/执行兼容，产品未验证 |
| [Copilot prompt injection](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/)及[指定中文](https://cn-sec.com/archives/5301988.html) | 指定中文转载全文，admin，2026-06-28；英文两入口传输错误 | [数据面到策略写入](../reading-notes/fall2025/week06/02-copilot-rce.md)，08；英文作者日期与当前修复未核验，路径作用域冲突保留，不复制可执行攻击 |
| [Unit42 Agentic threats](https://unit42.paloaltonetworks.com/agentic-ai-threats/) | Royce Lu、Jay Chen，2025-05-01，5 月 2 日文案更新；全文文字、九场景/五层防护 | [主体、对象与动作](../reading-notes/fall2025/week06/04-agentic-identity-threats.md)，08；特定应用设计非框架普遍漏洞，图像/仓库/数据未读 |
| [OWASP Top Ten](https://owasp.org/www-project-top-ten/)及[2021 中文正文](https://owasp.org/Top10/2021/zh-Hant/) | 官方 2021 首页、介绍、作为标准、A01–A10 文字及英文方法核对；当前主页最新 2025 | [版本与分母](../reading-notes/fall2025/week06/05-owasp-top-ten-2021.md)，08；原 China/zh_CN 入口 404，导航标签/正文繁简差异保留，2025 类别正文与完整 ASVS 未读 |
| [Context Rot](https://research.trychroma.com/context-rot)及[指定中文](https://research.chroma.org.cn/context-rot) | Hong、Troynikov、Huber，2025-07-14/7 月 16 日附注；双语正文、脚注、附录文字 | [长度、干扰与评测](../reading-notes/fall2025/week06/06-context-rot.md)，03、07；最差/最好翻译差异、人工 oracle 非检索器、输入输出共变保留，图像/代码/数据未验证 |
| [AutoCommenter 论文](https://arxiv.org/html/2405.13565v1) | Vijayvergiya 等，2024-05-22 v1；摘要、1–6/8 节与 Go 例精选，7 节仅核对相关工作 | [标签与服务层校准](../reading-notes/fall2025/week07/03-ai-assisted-coding-practices.md)，07；图像/内部数据未核验，反馈有用率非真实正确率，A/B 未检测到显著审查耗时收益 |
| [Addy Agentic Code Review](https://addyosmani.com/blog/agentic-code-review/) | Addy Osmani，2026-06-15，官方正文及例子精选；额外补充，指定 X 未得 | [风险与人工责任](../reading-notes/fall2026/week06/01-risk-tiered-review.md)，07；原 X 对应未证实，不计指定阅读，转引研究/产品/截图未独立验证 |
| [Code Reviews: Just Do It](https://blog.codinghorror.com/code-reviews-just-do-it/) | Jeff Atwood，2006-01-21，完整正文 | [同行审查与历史收益](../reading-notes/fall2025/week07/01-code-reviews-just-do-it.md)，07；转引书籍/研究未读，检出率和十倍回报不泛化 |
| [Code Review Essentials](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html) | Blake Smith，2015-02-09，完整正文 | [团队理解、说明与反馈](../reading-notes/fall2025/week07/05-code-review-essentials.md)，07；层次图未视觉核验、原例代码/测试未验证 |
| [How to review code effectively](https://github.blog/developer-skills/github/how-to-review-code-effectively-a-github-staff-engineers-philosophy/) | Sarah Vessels，2024-07-23，完整正文 | [清晰及时的审查](../reading-notes/fall2025/week07/02-how-to-review-code-effectively.md)，07；图片、团队自动化、门禁与通知未验证 |
| [Kubernetes Troubleshooting in Resolve AI](https://resolve.ai/blog/kubernetes-troubleshooting-in-resolve-ai) | Resolve 产品文章完整正文，页面无可核验个人署名/发布日期 | [实例身份与证据保存](../reading-notes/fall2025/week09/03-kubernetes-troubleshooting.md)，09；图片、集群与产品未验证，自动修复时态差异已说明 |
| [Your New Autonomous Teammate](https://resolve.ai/blog/product-deep-dive) | Seerut Sidhu，完整产品文章正文，未见可核验发布日期 | [调查到复盘的状态](../reading-notes/fall2025/week09/04-autonomous-teammate.md)，09；图像、执行、客户收益未验证，自动修复时态不与其他文章拼接 |
| [Multi-agent systems and AI-native engineering](https://resolve.ai/blog/role-of-multi-agent-systems-AI-native-engineering) | Spiros Xanthos、Gabor Angeli、Bharat Khandelwal，完整正文及比较表，未见可核验发布日期 | [协调成本与专业分支](../reading-notes/fall2025/week09/05-multi-agent-ai-native.md)，09；链接视频/实现未读，多 Agent 必要性是作者主张，非同预算对照结论 |
| [Top 5 Benefits of Agentic AI](https://resolve.ai/blog/Top-5-Benefits) | Mitch Wakefield，完整正文，未见可核验发布日期或可复现评测数据 | [收益假设与失败计入](../reading-notes/fall2025/week09/06-on-call-benefits.md)，09；供应商宣传不是实测，未验证主动预测、修复或疲劳改善 |
| [The spec is dead, long live the spec!](https://blog.ravi-mehta.com/p/specs-are-the-new-source-code)及[中文版](https://bbs.sangfor.com.cn/forum.php?mod=viewthread&tid=322197) | Ravi Mehta、Danny Martinez，2025-07-31；英文仅公开引言，中文为 Costrict 2026-03-09 公开删减译述 | [意图、原型与实现证据](../reading-notes/fall2025/week03/01-specs-as-source-code.md)，03；英文全文/翻译忠实度/图片/演讲/案例未核验，推广不纳入原观点 |
| [MCP 简介](https://stytch.com/blog/model-context-protocol-introduction/) | 2025 入门文章，全文 | [角色与伪代码边界](../reading-notes/fall2025/week02/01-mcp-introduction.md)，04；不是规范，链接中的 SDK/研究未读 |
| [Cloudflare 远程 MCP 指南](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/) | 当前官方指南全文，更新于 2026-10-27 | [远程身份与版本](../reading-notes/fall2025/week02/03-remote-mcp-authentication.md)，04；非 2025 快照，完整 Authorization/迁移/模板未读 |
| [MCP Registry 公告](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) | 2025 公告全文 | [目录与授权](../reading-notes/fall2025/week02/05-mcp-registry.md)，04；现行 API/政策未读，移除条目不保证撤销执行 |
| [API 不等于好 MCP 工具](https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/) | 作者观点，全文 | [任务粒度与结果预算](../reading-notes/fall2025/week02/06-apis-and-mcp-tools.md)，04；条数不约束长度，格式效率未测 |
| [长上下文如何失效](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html) | 作者文章全文及脚注 | [错误传播与恢复](../reading-notes/fall2025/week03/02-how-contexts-fail.md)，03；底层研究/图像/修复续篇未读，不给通用阈值 |
| [为 Agent 编写有效工具](https://www.anthropic.com/engineering/writing-tools-for-agents) | 英文及根 README 中文入口正文对照 | [任务级评测](../reading-notes/fall2025/week03/06-writing-tools-for-agents.md)，04、07；图片/cookbook/SDK 未读，评测未运行 |
| [Claude Code 架构论文](https://arxiv.org/html/2604.14228v3) | 非官方研究，v3 精选章节 | [范围与方法局限](../reading-notes/fall2026/week01/03-claude-code-design.md)；分析 v2.1.88 不代表现行产品保证 |
| [上下文税](https://langwatch.ai/blog/context-tax-when-to-compact) | 作者观察研究，全文 | [成本与压缩](../reading-notes/fall2026/week02/01-context-tax.md)；个人数据与模型判断不证明因果或通用阈值 |
| [OpenSpec](https://openspec.dev/) | 首页及 [quickstart](https://openspec.dev/docs/quickstart) | [持久规格](../reading-notes/fall2026/week02/02-openspec.md)；非全部文档，流程复核不是测试通过 |
| [Superpowers](https://github.com/obra/superpowers) | 固定提交精选 README/技能 | [文件与提交记录](../reading-notes/fall2026/week02/03-superpowers.md)；未安装或执行脚本 |
| [企业级 MCP](https://blog.cloudflare.com/enterprise-mcp) | 工程与产品文章，全文 | [身份、门户、网关与 Code Mode](../reading-notes/fall2026/week02/04-enterprise-mcp.md)；数字与产品能力按作者报告，不泛化 |
| [pstack](https://github.com/cursor/plugins/tree/main/pstack) | 固定提交子目录精选文件 | [影响范围与证据](../reading-notes/fall2026/week03/01-pstack.md)；未读其他技能或运行实现 |
| [Matt Pocock skills](https://github.com/mattpocock/skills) | 固定提交 README/to-spec/tdd | [版本化解读](../reading-notes/fall2026/week03/02-matt-pocock-skills.md)；不将不同框架的测试流程拼成新规则 |
| [browse.sh](https://browse.sh/) | 首页与一个示例条目 | [实际范围](../reading-notes/fall2026/week03/03-browse.md)；未读全站，不将目录标签当权限 |
| [Claude Code 安装](https://code.claude.com/docs/en/setup) | 官方产品文档，已阅读 | 00、02 安装与访问验收；资格和平台能力仍按当前版本核对，不固定价格 |
| [Claude Code 定制机制](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) | 官方产品说明，重试后已阅读 | 05 加载作用域、Skill、Subagent、Hook 的职责；不泛化版本机制，不将模型 Hook 判断说成确定性 |
| [Factory AGENTS.md](https://docs.factory.com/harness/agents-md) | 产品文档，已阅读 | 05、06 短规则、命令和作用域；Droid 的发现与优先级不是通用标准 |
| [Writing a good CLAUDE.md](https://hlyr.dev/blog/writing-a-good-claude-md) | 行业经验文章，已阅读 | 05 渐进披露、权威引用、确定性检查；行数和指令数经验阈值不是科学定律 |
| [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills) | 作者观点，已阅读 | 05 能力接口与过程知识组合；远程服务不自动保证安全，偏好不是普遍结论 |
| [Cloudflare AI Code Review](https://blog.cloudflare.com/ai-code-review) | 团队工程实践，已阅读 | 07 专业角色、协调、去重、上下文、超时与预算；不照搬成本、准确率、审批或紧急绕过策略 |
| [Greptile Code Review Agent](https://www.greptile.com/blog/how-to-build-a-code-review-agent) | 行业经验文章，已阅读 | 07 diff 之外的上下文、沙箱验证与模型比较；效果数字和模型偏好仅为作者报告 |
| [Codex authentication](https://developers.openai.com/codex/authentication) | 官方链接，本轮读取返回 403 | 仅登记；不据此写入当前套餐资格或认证步骤 |
| [非官方开通补充页](../../Resource/Claude-Code%E5%85%85%E5%80%BC/README.md) | 本地商业页，已阅读 | 08 凭据安全案例；不推荐第三方会话提交，不验证购买与价格，不作为官方资格依据 |

## 6. 2026 课堂资料与未读外链

以下入口逐项来自当前根 README。2026-11-04 已取得三份文字转写，其他材料没有据此自动标记已读。Google Slides 公开文字导出传输错误、Drive 原入口超时的既有状态保留，本次未重新读取全部课堂外链。2026-11-05 指定视频页及英文字幕/列表未取得文字，X 请求传输错误或超时；作者其他文章不证明原帖已读。不证明链接永久失效，不绕认证，未读资料不生成摘要。

| 课程位置 | 新链接 | 本轮状态 |
| --- | --- | --- |
| 2026 第 1 周 9/22 | [幻灯片](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link)、[代码](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link) | 未取得正文；Slides 导出传输错误、Drive 超时 |
| 2026 第 1 周 9/24 | [幻灯片](https://docs.google.com/presentation/d/1RZu-p18Qybbgm8WVP2RH04ESc4Bn377B-T9j5-TBFdQ/edit?usp=drive_link)、[提示词](https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link) | 未取得正文；不把转写当提示词集合已读 |
| 2026 第 1 周 9/24 | [转写](https://themodernsoftware.dev/materials/9-24-26-transcript.txt) | [课堂解读完成](../reading-notes/fall2026/week01/lecture-system-prompt.md)，依据原时间戳与主题，未执行演示 |
| 2026 第 2 周 9/29 | [幻灯片](https://docs.google.com/presentation/d/17brqoQQZHF3K82WgYaV6urAV3Q7iIwyGUBYRvSuY8QY/edit?usp=sharing)、[转写](https://themodernsoftware.dev/materials/9-29-26-transcript.txt) | Slides 未取得；[RePPIT 解读完成](../reading-notes/fall2026/week02/lecture-reppit.md)，不编造缺失时间戳 |
| 2026 第 2 周 10/1 | [幻灯片](https://docs.google.com/presentation/d/1q2cB1a7P4XsR0UJqE0RmtZFeggNOLdPaSnOpbBVewHA/edit?usp=sharing)、[技能文件夹](https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW?usp=drive_link)、[转写](https://themodernsoftware.dev/materials/10-1-26-transcript.txt) | Slides/技能未取得；[MCP 课堂解读完成](../reading-notes/fall2026/week02/lecture-mcp.md) |
| 2026 第 3 周 10/6 | [幻灯片](https://docs.google.com/presentation/d/15bPu5c-i8D8McTh6l7SpUPk2n9M_Y-CdDQLfyzL8RD8/edit?usp=sharing) | 文字导出传输错误，未取得正文 |
| 2026 第 3 周 Lee Robinson | [幻灯片](https://drive.google.com/file/d/1b8WiBk_lcB3ue-jZMLijSUMLj6SDiF6Z/view?usp=drive_link) | 仅登记，未读取正文 |
| 2026 第 4 周定制环境 | [幻灯片](https://docs.google.com/presentation/d/152VaUifBKH4T6hxd6fCKKM9kJTSAuBmkF8zSYwuTYAo/edit?usp=sharing) | 读取发生传输错误，未取得正文 |
| 2026 第 5 周仓库就绪 | [幻灯片](https://docs.google.com/presentation/d/1yCxocmUrGIN7IrC42WB6NW08PtYYFLe1ombDj3Ay6_8/edit?usp=drive_link) | 仅登记，未读取正文 |
| 2026 第 5 周仓库就绪 | [视频](https://www.youtube.com/watch?v=ShuJ_CN6zr4)、[X 帖文](https://x.com/trybasis/status/2056881705269580023) | 视频及字幕传输错误，X 此前传输错误、本次超时；未取得正文，不是无视频学习前提 |
| 2026 第 6 周风险分层 | [X 帖文](https://x.com/addyosmani/status/2114604912520921136) | 此前传输错误、本次超时，原帖未读；[作者官方文章补充](../reading-notes/fall2026/week06/01-risk-tiered-review.md)不证明原帖对应或完成 |
| 2026 第 6 周 Agentic Review | [幻灯片](https://docs.google.com/presentation/d/1u8WYtFj0O9yc4H4JX9D4URYKhDzvrAGKLzn38DXSrak/edit?usp=drive_link) | 仅登记，未读取正文 |

第 4 周 Boris Cherny、第 5 周 Eno Reyes、第 6 周 Silas Alberti、第 7 周 Isaac Evans、第 8 周 Rajesh Bhatia、第 9 周 Elad Gil/Amjad Masad 的嘉宾安排按根 README 登记；尚无取得的对应讲座正文，不推断其主张。第 7–10 周系统学习环依据当前主题与保留工程资料编写，明确为教程扩展。原课程评分与自学评分分别维护，广告、二维码、访问统计不纳入知识材料。
