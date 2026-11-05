# Fall 2025 第 3 周：AI IDE 与上下文

[2025 入口](../README.md) | [第 03 章](../../../chapters/03-context-spec.md) | [第 06 章](../../../chapters/06-repo-parallel.md)

核对日期：2026-11-04。原版与中文版共用笔记，不把已有中文 PPTX 当成视觉或演示验证。

## 已读取课堂材料

| 材料 | 真实范围与状态 | 中文解读 |
| --- | --- | --- |
| Mihail Eric，AI IDE，2025-10-06 | 双语各 15 页文字及关联备注已读；第 2、5、8、14 页图片未核验；第 7、11、15 页演示未执行 | [AI IDE、上下文与规格](lecture-ai-ide-setup.md) |
| Silas Alberti，2025-10-10 | 双语各 29 页文字及第 12 页备注已读；第 2、4、5、9–12、21–22 页图片、第 8–11 页表格布局未核验；无视频转写或产品执行 | [同步 IDE 与异步 Agent](lecture-silas-alberti.md) |
| [设计文档模板](../../../../Resource/Fall2025/week03-1006-design-document-template.md) | 全部 137 行静态读取；占位代码和发布步骤未执行 | 融入 AI IDE 笔记，不另建重复笔记 |

文字读取、中文解读及章节融合已完成，不表示视觉核验、外链正文、模型或产品实验完成。Silas 的效率倍率是讲者的商业经验主张，不是本教程测量结果；本地/云端与同步/异步是不同维度。

## 阅读与作业边界

根 README 本周指定文章另见[总阅读清单](../../README.md)，不将未读取外链计作完成。2025 第 3 周 MCP 原作业与笔记中的规格/委派练习不同；[第 04 章](../../../chapters/04-mcp-oauth.md)提供工具契约与受控写入学习路径，不由原作业完成标记推定复现实验。

先读 AI IDE 的规格和数据路径，再读 Silas 的交接与局限；练习均有零网络、零模型预算和明确验收，不需要购买或下载产品。

## 已有指定阅读解读

2026-11-05 已接入四份声明范围内的笔记，原编号与总清单一致；本次新增 Devin 指南的双语全文解读，其余两项未取得指定正文。

| 材料 | 实际范围与章节关联 |
| --- | --- |
| [01 规格作为源代码](01-specs-as-source-code.md) | 英文公开引言与根 README 删减中文版；英文全文/图片/案例未核验；第 03 章关联持久意图、原型反馈和实现证据 |
| [02 长上下文如何失效](02-how-contexts-fail.md) | 文章全文及脚注；底层研究、图像与修复续篇未读；第 03 章补分类区别和旧假设撤销 |
| [03 Coding Agents 101](03-coding-agents-101.md) | Cognition Team，2025 年 6 月；英文与指定 VibeVibe 中文版对应正文、原例和注释已读，区分译文弱化、遗漏 MCP beta 限定、80% 经验目标与未实测产品；第 03、06 章最小融合并双向关联，原案例未复现 |
| [06 为 Agent 编写有效工具](06-writing-tools-for-agents.md) | 英文及中文正文对照；图片、cookbook、SDK 未读；第 04、07 章关联工具粒度与任务级评测 |

正文解读完成不代表工具或模型评测完成；验收集未参与优化的独立性必须另行保持。

本次受限项与替代核对：第 04 项 [humanlayer ace-fca.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)因 `gh --version` 命令不可识别，未取得固定版本文档；不安装或绕用 webfetch 读 GitHub。第 05 项 [Rohan Paul 的 FAANG X 帖文](https://x.com/rohanpaul_ai/status/1959414096589422619)传输错误。另从 Devin 指定中文版的导航取得[VibeVibe 同题中文文章](https://www.vibevibe.cn/Articles/01-core-concepts/how-we-vibe-code-at-faang.html)全文，但其署名为 Anonymous FAANG Engineer、原链接指向 Reddit，不指向指定 X；对应关系未证实，不能冒充 Rohan Paul 帖文或增加指定阅读完成数，本次不为其另建笔记。来源失败不等于永久失效。

## 作业导读

[GitHub MCP 与执行边界](assignment-guide.md)：2026-11-05 已静态读取 assignment、README、requirements 与四份服务源码，保留 90 分基础及两项 5 分加分，解释工具/资源/提示词、部分失败、写入重试、JWT 与资源授权边界，关联第 04 章。提供 50 分钟零调用练习；本周目录未发现测试或独立 writeup，未启动、认证、写入或部署，不计指定阅读完成数。
