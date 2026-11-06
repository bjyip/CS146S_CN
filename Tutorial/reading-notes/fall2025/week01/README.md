# Fall 2025 第 1 周：LLM 与提示

[2025 入口](../README.md) | [材料总清单](../../README.md) | [第 01 章](../../../chapters/01-llm-prompting.md)

基础学习直接阅读第 01 章：从会议笔记提取任务的需求出发，依次理解生成、任务约定、错误诊断、具体改进与逐项评测，不按原课件顺序堆术语。分两段、五步完成范围判断、提示与人工预期、假响应检查、具体反馈和评分；有记录框、逐步通过标准及章内答案。基础阅读估计 60–90 分钟、零调用练习约 75 分钟，不按速度验收；复杂机制、参数和进阶小题按需展开，原作业与来源核验选学。本页保留原资料范围与逐份定位；章内深化不证明原视频、Google 概览、课件图像、真实实验或新手阅读效果已验证。

| 材料 | 类型 | 状态 |
| --- | --- | --- |
| [课程导论与 LLM 的构建过程](lecture-intro-to-llms.md) | 本地 PPTX 与备注 | 20 页文字核对及中文解读完成；图片、图片内公式未视觉核验；已融入第 01 章 |
| [LLM 的高效提示](lecture-effective-prompting.md) | 本地 PPTX 与备注 | 31 页中英文文字与备注核对及中文解读完成；第 3、4、21、22、27、28 页图片未视觉核验；技术、案例与证据边界已融入第 01 章自包含样板 |

## 已有指定阅读

| 材料 | 范围与状态 |
| --- | --- |
| [03 提示工程指南](03-prompt-engineering-guide.md) | 六个技术子页的中英文正文完成解读，关联第 01 章；其余技术页、图像、论文与 notebook 未读，不代表全站完成 |
| [05 OpenAI 如何使用 Codex](05-how-openai-uses-codex.md) | 官方 PDF 13 页可提取文字已读，中文解读关联第 06、07 章；第 13 页无提取文字、图像未核验，指定中文仍 403；不证明现行产品或内部收益 |

其余三项指定阅读仍待获取所需正文或字幕，按[总清单](../../README.md#fall-2025)独立维护；2026-11-05 本次逐项重试结果如下，没有据标题或二进制创建笔记。课堂解读不代表指定视频已经取得字幕。

| 编号与获取入口 | 本次实际结果 |
| --- | --- |
| 01 [深入理解 LLM](https://www.youtube.com/watch?v=7xTGNNLPyMI)、[指定中文版](https://www.bilibili.com/video/BV16cNEeXEer) | 两个视频页均传输错误；YouTube 公开 `api/timedtext?v=7xTGNNLPyMI&lang=en` 也传输错误，未取得字幕/转写，不推定无字幕 |
| 02 [Google 提示概览](https://cloud.google.com/discover/what-is-prompt-engineering)、[语雀中文版](https://www.yuque.com/wangjiandong/gwcyhv/uw3b7we9pmdubdig) | 原入口及 `?hl=en`、`?hl=zh-CN` 均传输错误；中文入口仅标题“2提示词工程概述中文版”，未取得正文 |
| 04 [AI Prompt Engineering](https://www.youtube.com/watch?v=T9aRN5JkmL8)、[指定中文版](https://www.bilibili.com/video/BV18ukBYzEQG) | 视频页与 YouTube 公开 `api/timedtext?v=T9aRN5JkmL8&lang=en` 均传输错误，未取得字幕/转写 |
| 05 [Codex 报告 PDF](https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf)、[指定中文版](https://tools.wingzero.tw/article/sn/3533) | 通用读取仍超 5MB；现有 PyMuPDF 成功在内存中提取官方原件 13 页文字，笔记完成；中文 403 与图像缺口保留，未保存 PDF 或安装依赖 |

失败结果仅描述本次可访问范围，不证明永久失效。本次未下载完整视频、安装依赖、调用模型或使用其他课堂转写代替指定视频。

## 中文学习补充

[提示要素、采样设置与失败契约](supplement-prompting-introduction.md)：2026-11-05 实际读取 DAIR.AI 中文简介、要素、设置、技巧四页，给出历史参数边界、温度措辞疑点、停止串/截断反例、原例契约冲突与 35 分钟零调用练习，关联第 01 章。它扩大已有指南的精选范围，不新增指定阅读条目，不冒充 Google 概览译文或视频字幕；本周三项缺口不变。其他主题的本地学习入口见[替代路线](../../../reference/offline-learning.md)。

## 作业导读

[六种提示技术与验证边界](assignment-guide.md)：已静态读取 assignment、README、六个脚本和 API 文档，解释原 60 分要求、答案泄漏、众数/多数、AST 注解、RAG 字符串检查与反思执行风险，关联第 01 章。提供 45 分钟零调用替代；未安装、下载模型或运行原作业，不计入指定阅读完成数。
