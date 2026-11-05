# 资料索引与来源边界

[返回目录](../README.md)

本教程根据本地资料重新组织，正文中的解释与实验不是逐页翻译，也不声称复现了完整嘉宾讲座。以下链接可以溯源；完成学习不需要打开视频。

系统教程位于 `chapters/`，共用资料位于 `reference/`。[逐份阅读笔记索引](../reading-notes/README.md)记录指定阅读的范围与进度；本文件记录教程依据与课堂材料状态，两者不等同。保留已有第 4 周四份笔记，补入十份限定范围阅读笔记、三份课堂转写解读和三周作业导读，未执行模型、OAuth、客户端或安全实验。

本次核对日期为 2026-11-04，以当前根 README、真实资料和本地文件为依据，不以历史 merge 代表覆盖。已核对真实 2026 第 1–3 周 assignment 与 writeup，未发现本地后续周作业；没有修改原作业。

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
| 01 LLM 与提示 | [LLM](../../Resource/Fall2025/week01-0922-intro-to-llms.pptx)、[提示](../../Resource/Fall2025/week01-0926-effective-prompting.pptx)、[作业](../../_assignments/2025%20fall/week1/assignment.md) | 泄漏辨析、精确率/召回率 |
| 02 Agent | [讲义](../../Resource/Fall2025/week02-0929-building-a-coding-agent.pptx)、[代码](../../Resource/Fall2025/week02-0929-completed-exercise.py)、[2026 trace](../../_assignments/2026%20fall/modern-software-dev-assignments-master/week1/assignment.md) | 执行边界、预算与恢复 |
| 03 上下文与规格 | [AI IDE](../../Resource/Fall2025/week03-1006-ai-ide-setup.pptx)、[设计模板](../../Resource/Fall2025/week03-1006-design-document-template.md)、[行动项作业](../../_assignments/2025%20fall/week2/assignment.md) | RePPIT 编排、示例契约 |
| 04 MCP/OAuth | [MCP](../../Resource/Fall2025/week02-1003-custom-mcp-server.pptx)、[代码](../../Resource/Fall2025/week02-1003-completed-exercise.py)、[2025 作业](../../_assignments/2025%20fall/week3/assignment.md)、[2026 作业](../../_assignments/2026%20fall/modern-software-dev-assignments-master/week2/assignment.md) | 信任边界、幂等和 OAuth 细化 |
| 05 自动化 | [Agent 管理](../../Resource/Fall2025/week04-1013-agent-manager.pptx)、[Claude Code](../../Resource/Fall2025/week04-1017-boris-cherny.pptx)、[2025 作业](../../_assignments/2025%20fall/week4/assignment.md)、[2026 Skill](../../_assignments/2026%20fall/modern-software-dev-assignments-master/week3/assignment.md) | MCP/Skill/CLI 组合、作用域、渐进披露与门禁 |
| 06 仓库与并行 | [产品讲义](../../Resource/Fall2025/week05-1020-ai-developer-product.pptx)、[Warp 作业](../../_assignments/2025%20fall/week5/assignment.md) | 就绪度自评、独立任务、指令漂移、隔离与后台状态 |
| 07 测试与审查 | [测试讲义](../../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[审查讲义](../../Resource/Fall2025/week07-1103-ai-code-review.pptx)、[审查作业](../../_assignments/2025%20fall/week7/assignment.md) | 测试层次、风险分层、专业审查、沙箱与评测 |
| 08 安全 | [安全讲义](../../Resource/Fall2025/week06-1027-ai-qa-sast-dast.pptx)、[Semgrep 作业](../../_assignments/2025%20fall/week6/assignment.md)、[非官方商业页](../../Resource/Claude-Code%E5%85%85%E5%80%BC/README.md) | 威胁模型、注入防护、凭据披露辨析和回归 |
| 09 交付与运维 | [全栈](../../Resource/Fall2025/week08-1110-end-to-end-app.pptx)、[三栈作业](../../_assignments/2025%20fall/week8/assignment.md)、[事故响应](../../Resource/Fall2025/week09-1117-incident-response-devops.pptx)、[Resolve 嘉宾 PDF](../../Resource/Fall2025/week09-1121-resolve-guest-lecture-slides.pdf) | 验收、SLI/SLO、图导航、知识更新、并行调查与失败评测 |
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

另外，Resolve 嘉宾 PDF 的 35 页解析文字及所附 34 张页面图已读，独立中文解读和第 09 章融合完成；第 33 页仅解析文字。PDF 单独统计，不加入 PPTX 的 275 页或 13 份中文版数量，未生成中文版 PDF。所附页面图用于核对可辨认内容，不表示细小截图全部文字或图中引用的底层证据已取得。

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
| [Resolve 嘉宾 PDF](../../Resource/Fall2025/week09-1121-resolve-guest-lecture-slides.pdf) | 35 页解析文字已读并与所附图核对；无中文版 PDF | 所附 34 张页面图已查看；第 33 页仅文字，密集节点/细小截图与底层证据有缺口 | [独立中文解读](../reading-notes/fall2025/week09/lecture-resolve-guest.md) | [09](../chapters/09-delivery-operations.md)：依赖图与有限查询、知识来源/失效、并行假设及失败评测 |
| [Tomas Reimers 嘉宾 PDF](../../Resource/Fall2025/week07-1107-tomas-reimers-slides.pdf) | 待读取 | 未核验 | 待编写，不建空笔记 | 未完成来源特定融合 |
| Fall 2025 在线嘉宾课件（根 README 的 Warp / Vercel 入口） | 未取得正文 | 未核验 | 待获取，不以主讲 PPTX 替代 | 未完成来源特定融合 |

这些笔记没有视频时间戳，不是相应视频的替代转写。LLM 导论第 13 页的历史评分、18–19 页的闭源模型规模与价格不写成当前课程事实；Agent 第 7 页的产品机制与推测不写成通用保证。其余课件的效率、检测率、误报率与产品宣传也不能泛化。本地授课课件中的嘉宾预告不证明嘉宾是本讲作者；运维第 16 页的代码审查文案保留疑似模板残留状态，不转述为运维效果实证。原件、中文版、翻译中间数据均未更改或重新生成。

Resolve 讲者署名依据 PDF 第 1–2 页，35 页解析文字与页面图来自本次本地 PDF 读取结果附送的内容，未安装解析/OCR 依赖。第 5、12 页的劳动占比、人数及入职耗时是讲者叙述；第 29 页 Redis 工作假设与第 30 页数据库时间线分别解读，截图置信度不是根因验证；第 33 页是 2025 年的未来预测。无现场演示、问答转写或产品运行证据，不公开整套截图与完整原文。

本轮复用工作区已有的只读核对工具 [pptx_text.py](../scripts/pptx_text.py)，仅调整存放目录，未修改工具内容。它按演示关系取页序并关联备注，打印页面位置和图片/表格数量，适合维护时核对文字，不执行 OCR、不恢复图示、不生成正式笔记。仓库根目录示例：

```powershell
python Tutorial/scripts/pptx_text.py "Resource/Fall2025/week01-0922-intro-to-llms.pptx" "Tutorial/reference/slides/fall2025/week01-0922-intro-to-llms.pptx"
```

不另公开归档完整逐页原文底稿；正式产物是可追溯的中文解读及章节增量。后续材料遵循同一三层流程：按页码或真实时间戳读取，编写逐份解读，按概念最小融合并更新各阶段状态。视频优先公开转写和字幕；下载完整音视频、安装 OCR/ASR 或付费转写仍需独立授权。

## 5. 已读来源与使用边界

“已阅读”指本次增量工作期间取得正文，不表示已验证产品运行或复现作者实验。外部页面可能持续更新，下表记录本轮读取状态，不保证永久可访问。

| 来源 | 类别与状态 | 用于何处及限制 |
| --- | --- | --- |
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

以下入口逐项来自当前根 README。2026-11-04 已取得三份文字转写，其他材料没有据此自动标记已读。Google Slides 尝试公开文字导出遇到传输错误，Drive 原入口请求超时；这些是本轮获取结果，不证明原链接不存在或永久失效，不绕过认证。视频页面及字幕入口未取得文字，X 请求遇到传输错误。未读资料不生成摘要。

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
| 2026 第 5 周仓库就绪 | [视频](https://www.youtube.com/watch?v=ShuJ_CN6zr4)、[X 帖文](https://x.com/trybasis/status/2056881705269580023) | 仅登记，未观看或读取；不是无视频学习前提 |
| 2026 第 6 周风险分层 | [X 帖文](https://x.com/addyosmani/status/2114604912520921136) | 读取发生传输错误，未取得正文 |
| 2026 第 6 周 Agentic Review | [幻灯片](https://docs.google.com/presentation/d/1u8WYtFj0O9yc4H4JX9D4URYKhDzvrAGKLzn38DXSrak/edit?usp=drive_link) | 仅登记，未读取正文 |

第 4 周 Boris Cherny、第 5 周 Eno Reyes、第 6 周 Silas Alberti、第 7 周 Isaac Evans、第 8 周 Rajesh Bhatia、第 9 周 Elad Gil/Amjad Masad 的嘉宾安排按根 README 登记；尚无取得的对应讲座正文，不推断其主张。第 7–10 周系统学习环依据当前主题与保留工程资料编写，明确为教程扩展。原课程评分与自学评分分别维护，广告、二维码、访问统计不纳入知识材料。
