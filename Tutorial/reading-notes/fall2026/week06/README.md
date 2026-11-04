# 第 6 周：Agentic Code Review

[2026 入口](../README.md) | [材料总表](../../README.md) | [测试与审查章节](../../../chapters/07-testing-review.md)

核对日期：2026-11-04。先辨风险与确认缺陷，再讨论角色、上下文、模型和成本；不以多模型一致代替证据。

| 指定阅读 | 状态与范围 |
| --- | --- |
| [风险分层与人工监督](https://x.com/addyosmani/status/2114604912520921136) | 获取遇到传输错误，未取得正文，不生成摘要 |
| [协调专业审查 Agent](https://blog.cloudflare.com/ai-code-review) | [02 协调、边界与去重](02-specialist-review.md)，全文，作者部署策略不是教程安全政策 |
| [超越 diff](https://www.greptile.com/blog/how-to-build-a-code-review-agent) | [03 上下文、测试与模型比较](03-beyond-diff.md)，全文，演讲改编文章不是视频转写 |

10/27 Slides 尚未取得正文；Silas Alberti 的嘉宾安排只登记，不推断发言，见[来源表](../../../reference/sources.md)。原本地 2026 作业目前止于第 3 周，本周实验是章节 07 的教程改编，可参考保留的 2025 第 7 周原要求，不冒充 2026 官方作业。

验收保留原始发现、根因去重、确认测试、误报和未确认项；没有已知缺陷全集不声称计算真实召回率。本轮未调用模型或运行沙箱、PR、客户端实验。
