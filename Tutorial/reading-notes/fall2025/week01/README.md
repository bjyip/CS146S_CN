# Fall 2025 第 1 周：LLM 与提示

[2025 入口](../README.md) | [材料总清单](../../README.md) | [第 01 章](../../../chapters/01-llm-prompting.md)

| 材料 | 类型 | 状态 |
| --- | --- | --- |
| [课程导论与 LLM 的构建过程](lecture-intro-to-llms.md) | 本地 PPTX 与备注 | 20 页文字核对及中文解读完成；图片、图片内公式未视觉核验；已融入第 01 章 |
| [LLM 的高效提示](lecture-effective-prompting.md) | 本地 PPTX 与备注 | 31 页中英文文字与备注核对及中文解读完成；第 3、4、21、22、27、28 页图片未视觉核验；已关联并最小融入第 01 章 |

## 已有指定阅读

| 材料 | 范围与状态 |
| --- | --- |
| [03 提示工程指南](03-prompt-engineering-guide.md) | 六个技术子页的中英文正文完成解读，关联第 01 章；其余技术页、图像、论文与 notebook 未读，不代表全站完成 |

其余四项指定阅读仍待获取所需正文或字幕，按[总清单](../../README.md#fall-2025)独立维护；2026-11-05 本次逐项重试结果如下，没有据标题或二进制创建笔记。课堂解读不代表指定视频已经取得字幕。

| 编号与获取入口 | 本次实际结果 |
| --- | --- |
| 01 [深入理解 LLM](https://www.youtube.com/watch?v=7xTGNNLPyMI)、[指定中文版](https://www.bilibili.com/video/BV16cNEeXEer) | 两个视频页均传输错误；YouTube 公开 `api/timedtext?v=7xTGNNLPyMI&lang=en` 也传输错误，未取得字幕/转写，不推定无字幕 |
| 02 [Google 提示概览](https://cloud.google.com/discover/what-is-prompt-engineering)、[语雀中文版](https://www.yuque.com/wangjiandong/gwcyhv/uw3b7we9pmdubdig) | 原入口及 `?hl=en`、`?hl=zh-CN` 均传输错误；中文入口仅标题“2提示词工程概述中文版”，未取得正文 |
| 04 [AI Prompt Engineering](https://www.youtube.com/watch?v=T9aRN5JkmL8)、[指定中文版](https://www.bilibili.com/video/BV18ukBYzEQG) | 视频页与 YouTube 公开 `api/timedtext?v=T9aRN5JkmL8&lang=en` 均传输错误，未取得字幕/转写 |
| 05 [Codex 报告 PDF](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf)、[指定中文版](https://tools.wingzero.tw/article/sn/3533) | PDF 响应超过读取工具 5MB 限制；中文入口 403；尝试官方文字候选 `https://openai.com/index/how-openai-uses-codex/` 返回 404，候选并非已确认替代正文 |

失败结果仅描述本次可访问范围，不证明永久失效。本次未下载完整视频、安装依赖、调用模型或使用其他课堂转写代替指定视频。

## 作业导读

[六种提示技术与验证边界](assignment-guide.md)：已静态读取 assignment、README、六个脚本和 API 文档，解释原 60 分要求、答案泄漏、众数/多数、AST 注解、RAG 字符串检查与反思执行风险，关联第 01 章。提供 45 分钟零调用替代；未安装、下载模型或运行原作业，不计入指定阅读完成数。
