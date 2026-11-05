# Fall 2025 第 6 周：AI 测试与安全

[2025 入口](../README.md) | [材料总清单](../../README.md) | [第 07 章](../../../chapters/07-testing-review.md) | [第 08 章](../../../chapters/08-security.md)

| 材料 | 类型 | 状态 |
| --- | --- | --- |
| [AI 测试、安全检测与 Agent 攻击面](lecture-ai-qa-sast-dast.md) | 本地双语 PPTX 与备注 | 22 页文字及关联备注完整核对，详细中文解读完成；图片页 2、4、12、13、15、17 未视觉核验；最小融入第 08 章并关联第 07 章 |
| [Semgrep 作业导读](assignment-guide.md) | 本地说明、应用、配置、测试与报告 | 静态阅读完成，关联第 08 章；区分报告自述与实际证据、SQL/DOM/CORS、启动隔离与依赖公告；50 分钟零调用替代，七个测试和扫描未运行 |

归档讲者署名 Mihail Eric，10/31 Isaac Evans 为嘉宾预告，不视为嘉宾讲座正文。指定阅读与原作业另见总清单；笔记的离线练习为教程扩展，没有运行扫描、攻击或模型实验。

## 指定阅读

| 材料 | 范围与状态 |
| --- | --- |
| [01 SAST、DAST 与 RASP](01-sast-dast.md) | Splunk 2024-12-18 原文文字本轮获取成功，比较表与结论已读；区分 SAST/SCA、运行覆盖与 RASP；图片和工具未验证 |
| [02 Copilot 提示注入与策略控制面](02-copilot-rce.md) | 英文两次传输错误；指定 CN-SEC 中文转载正文已读，转载日期 2026-06-28；路径作用域不一致保留，英文作者/日期与当前修复状态未核实，未复现 |
| [03 Claude Code 与 Codex 漏洞发现评测](03-ai-vulnerability-evaluation.md) | 2025-09-02 文章全文、结果表与提示模板；第 07、08 章关联分母、误报、非确定性与修复证据；图片/原始报告/应用未验证 |
| [04 Agentic AI 威胁与身份](04-agentic-identity-threats.md) | Unit42 2025-05-01 原文文字、九场景与五层防护已读；补读截断后段；区分身份、BOLA、SSRF 与网络外传，仓库/图片/产品未验证 |
| [05 OWASP Top Ten 2021](05-owasp-top-ten-2021.md) | 原 China 中文入口及官方 zh_CN 路径 404；官方语言导航的 zh-Hant 中文入口、介绍、标准说明与 A01–A10 文字已读；当前主页最新为 2025，本文锁定 2021，未读 2025 类别/完整 ASVS |
| [06 Context Rot](06-context-rot.md) | 英文及指定中文版正文、脚注、附录文字已读；指出 worst 误译、人工证据与实际检索差别、裁判校准及拒绝分母；图表/代码/数据/模型未验证 |
| [07 o3 系统提示词](https://github.com/SeanHeelan/o3_finds_cve-2025-37899/blob/master/system_prompt_uafs.prompt) | 2026-11-05 尝试 gh api 读取 master 文件，本机 gh 未识别（CommandNotFoundException，退出码 1）；正文与提交未取得，不安装、不换入口绕过、不建空笔记 |

本轮新增五篇详细中文笔记，周内指定阅读为 **6/7 篇笔记完成、1 项来源受限**；Copilot 仅在指定中文转载范围内完成，不代表英文全文已读。原版与中文版共用一篇，不重复计数。

2026-11-05 主代理已完成主要章节最小融合与反向链接：SAST、Copilot、Unit42、OWASP 对应第 08 章；Context Rot 对应第 03、07 章。其他章节链接是知识延伸，不声明全部新增反向链接。全局导航与来源状态由主代理统一维护，阅读范围以本周表格和各篇说明为准；章节融合不等于产品验证或实验复现。

o3 使用只读命令 `gh api repos/SeanHeelan/o3_finds_cve-2025-37899/contents/system_prompt_uafs.prompt?ref=master -H "Accept: application/vnd.github.raw+json"` 获取失败；待具备 gh 的合法环境取得正文并固定版本后再编写。不根据文件名推测漏洞分析流程。

五篇练习均为零执行教程扩展，只设计证据、权限或评测表，不安装、不调用模型、不访问真实目标、不运行安全 payload。没有执行扫描、攻击、跳过权限确认、自动修复或 Context Rot 实验；来源文字已读不等于产品和实验通过。
