# Fall 2025 第 9 周：事故响应与 AI DevOps

[2025 入口](../README.md) | [材料总清单](../../README.md) | [第 09 章](../../../chapters/09-delivery-operations.md)

| 材料 | 类型 | 状态 |
| --- | --- | --- |
| [AI DevOps、事故分诊与证据驱动恢复](lecture-incident-response-devops.md) | 本地双语 PPTX 与备注 | 19 页文字及关联备注完整核对，详细解读完成；图片页 2、5、10、14、15 未视觉核验；最小融入第 09 章 |
| [Resolve：生产环境中的 Agentic AI](lecture-resolve-guest.md) | 独立嘉宾 PDF | 35 页可提取文字已读，文字范围内解读完成并关联第 09 章；页面图已生成但全部视觉核验未完成，未经核验的截图细节已撤回，底层代码/日志和产品效果未验证 |

主讲 PPTX 归档署名 Mihail Eric，11/21 Resolve 嘉宾为该课预告；独立 PDF 第 1–2 页已核对 Mayank Agarwal 与 Milind Ganjoo 的署名，不与主讲材料互相替代。主讲第 11 页 SLA 正文/备注冲突与第 16 页疑似审查模板残留已保留。第 09 章关联嘉宾的系统关系、知识与并行调查观点，权限、预算和验收练习仍为教程扩展。现场演示未复现；练习零网络，不访问生产系统或执行运维动作。

## 已有指定阅读

| 材料 | 实际范围 | 章节关联 |
| --- | --- | --- |
| [Traces 与 Spans](02-traces-spans.md) | Last9 完整正文及 FAQ，2026-11-05 复核；图片、链接规范与 SDK 未验证 | 09：操作关系、时长重叠、传播、采样与降级证据 |
| [03 Kubernetes 排障](03-kubernetes-troubleshooting.md) | Resolve 产品文章完整正文；图片、集群与产品未验证，页面无可核验作者/日期 | 09：实例身份、证据保存与修复权限 |
| [04 自主值班伙伴](04-autonomous-teammate.md) | Seerut Sidhu，完整产品文章正文；图片、动作与收益未验证 | 09：调查、建议、批准、执行与复盘状态 |
| [05 多 Agent 与 AI-native 工程](05-multi-agent-ai-native.md) | Spiros Xanthos、Gabor Angeli、Bharat Khandelwal，完整正文及比较表；关联视频与实现未读 | 09：专业分支、同源证据、冲突与协调成本 |
| [06 Agentic AI 的五项值班收益](06-on-call-benefits.md) | Mitch Wakefield，完整正文；无可复现效果数据 | 09：收益假设、错误预警、遗漏与人工负担 |

假 span 表、采样、实例身份及收益验证练习为教程扩展，没有接入遥测服务或集群。六份指定阅读已有五份解读，[SRE 导论](https://sre.google/sre-book/introduction/)仍待获取。2026-11-05 原入口、`index.html`、语言参数、www 主机、旧 landing 官方入口均传输错误；官方目录与 workbook introduction 也未取得，O'Reilly `ch01.html` 返回 403。未取得指定章或可用官方替代正文，不以摘要建立空笔记，不推断永久失效，见[总清单](../../README.md#fall-2025)。四篇 Resolve 文章独立解读，不互相充当产品效果证据，不填补嘉宾 PDF 视觉缺口。
