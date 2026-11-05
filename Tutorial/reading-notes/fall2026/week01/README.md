# 第 1 周：Coding Agent 内部原理

[2026 入口](../README.md) | [材料总表](../../README.md) | [Agent 章节](../../../chapters/02-agent-loop.md)

先分清模型决策与运行时执行，再分析系统说明、工具契约和失败恢复。既有笔记范围于 2026-11-04 核对；下列视频与 X 缺口于 2026-11-05 再核对。

| 指定阅读 | 状态与范围 |
| --- | --- |
| [构建编程智能体](https://www.youtube.com/watch?v=s7ZzkdvCMDY) | 视频页面、英文公开 timedtext 与字幕列表均传输错误，无正文或时间戳，不以课堂转写替代 |
| [构建 Claude Code 的经验](https://x.com/trq212/status/2027463795355095314?s=20) | 确切 URL 与作者 profile 传输错误；Google 按 ID 搜索超时，Bing 结果不对应原帖；两个 Anthropic 候选文字路径 404，未取得原帖或可确认替代，不生成摘要 |
| [深入剖析 Claude Code](https://arxiv.org/pdf/2604.14228) | [论文精选章节笔记](03-claude-code-design.md)，非官方版本化架构研究，范围以正文说明为准 |

课堂：[9/24 system prompt 转写解读](lecture-system-prompt.md)。9/22 Slides/代码、9/24 Slides/提示词文件夹均未取得正文，原入口见[来源表](../../../reference/sources.md)。取得一份转写不代表读完提示词集合或另一场课程。

作业：[真实会话追踪导读](assignment-guide.md)。先做章节 02 的离线循环分析，具备合法访问、数据政策许可和预算后再决定原作业 trace。验收每项行为有请求或调用定位，不用论文描述替代自己的观察。所有实际抓包、模型与恢复实验本轮未执行。
