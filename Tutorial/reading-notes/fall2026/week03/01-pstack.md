# pstack：变更影响范围与直接证据

[Skills 与自动化](../../../chapters/05-skills-automation.md) · [仓库与并行](../../../chapters/06-repo-parallel.md) · [测试与审查](../../../chapters/07-testing-review.md)

## 来源与范围

- 原入口：[cursor/plugins 的 pstack](https://github.com/cursor/plugins/tree/main/pstack)。`pstack/README.md` 作者自称 poteto，介绍其 Meta、Netflix、Cursor 和 React Compiler 工程背景；这是作者自述，不作履历独立核验。
- 核对日期：2026-11-04；固定提交 `bb68f2365eceafa0cb2d253112f675acf5f144cc`，发布日期未另行核验。
- API 文件树确认路径后，实际读取 [pstack/README.md](https://raw.githubusercontent.com/cursor/plugins/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/README.md)、[blast-radius/SKILL.md](https://raw.githubusercontent.com/cursor/plugins/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/blast-radius/SKILL.md)、[principle-prove-it-works/SKILL.md](https://raw.githubusercontent.com/cursor/plugins/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/principle-prove-it-works/SKILL.md)。
- 未读全部 Skill、`poteto-mode` 正文、playbook、子 Agent 模板、harness 生成代码、自动化包或依赖脚本。未安装、运行、开 PR、合并或调用模型。README 的技能表只是入口，不代表已读所有技能。

## 1. “写得少但更可靠”是一种工程目标

定位：README 开头、`usage`、`principles`、`not shipped here`。

作者反对只用代码吞吐量衡量 Agent，强调先做深、验证产物，再放心并行。README 把 `poteto-mode` 描述为按任务匹配 playbook 并调用相关技能的路由入口；并不是每个任务都先产出详细书面计划。

这个概览与 Superpowers 强调先规格和计划的工作流不同，不必强行合成一条“所有优秀 Agent 都相同”的流程。可以学习共同的验证纪律，任务路由、规划成本与人类控制方式则按风险选择。

README 还说明若干能力来自其他插件或 Cursor 内置功能。因此“目录里有 pstack”不等于其所有依赖都存在；模型偏好和平台加载说明是此快照的陈述，不是本教程通用配置建议。

## 2. Blast Radius 不是调用者名单

定位：`blast-radius` 的 `Don't trust your own writeup`、`How sure are you`、`Steps`。

影响范围分析要找“这个改动安全所依赖的关键事实”，然后验证，而不是堆出一长串可能风险。原文举例：若某调用仅删除已经失效的缓存项且无其他副作用，那么验证这一个事实可能排除大部分担忧。

作者给出逐级证据：自述、真实源码位置、沿失败路径证明无法发生、运行调用真实代码的测试、在运行应用中复现。报告要说停在哪一级；本教程的假数据推演只能算练习，不升级为应用运行证据。

搜索函数引用会漏掉 API JSON、数据库列、序列化格式、其他语言消费者、feature flag、微任务时序、组件卸载等边界。教程补充案例：把行动项字段 `owner` 改成 `assignee`，本地调用者搜索全部改完，但导出的 JSON 仍被旧报表读取。真正需要验证的是外部消费者契约，而不只是函数列表。

正文 frontmatter 的 `disable-model-invocation: true` 表达禁用模型自动调用的意图；本笔记不据此推测其他客户端如何实现这一字段。加载正文后仍应服从用户权限，来源的多模型审查、执行与合并步骤不是新授权。

## 3. 直接检查产物而非代理信号

定位：`principle-prove-it-works` 的 `Check the real thing`、`Script the check when you can`。

文件修改时间、缓存截图、子 Agent 自报、编译成功都是容易误用的代理。检查任务实际产物，例如解析结果的真实字段、应用内的真实交互、变更 diff。可以脚本化时保存可重跑的检查；这能降低审查者重新理解环境和相信口头结论的成本。

但“必须证明”也不授权访问真实账号或运行破坏性测试。安全环境不足时，标明关键事实未证实，比模拟结果并宣称真实可用更正确。

## 4. 30 分钟离线练习

教程扩展，预算 30 分钟、0 网络/模型调用、不运行 pstack。使用假接口与假消费者，不接触真实仓库业务。

假变更：导出 `{ "owner": "李明", "action": "提交草稿" }` 改成 `{ "assignee": "李明", "action": "提交草稿" }`。消费者一在同仓库已改，消费者二是纸面旧报表，只读取 `owner`；假 CI 仅检查内部编译。

1. 0–8 分钟：列两个消费者和跨边界数据格式，解释为什么符号搜索漏掉旧报表。
2. 8–16 分钟：写关键安全事实：“所有消费方已经接受新字段”；根据假输入判定该事实不成立。
3. 16–23 分钟：写一份字面契约检查，旧报表读取新 JSON 应得到缺失字段错误，而不是默默显示空负责人。
4. 23–30 分钟：交付“已确认风险 / 已排除项 / 尚未验证项 / 最便宜下一步验证”的报告，标明只有纸面推演，真实运行未证实。

验收：必须识别外部消费者风险，不能凭编译通过清除它；每个清除项有证据，每个未证实项明确标注。不默认新增兼容层，真实方案取决于外部契约和迁移授权。**本次未执行练习或应用实验。**

## 局限与自测

只选读两份 Skill，不评价整个多模型系统；作者的模型默认值、并行可靠性与夜间合并示例没有复现。直接运行仍可能只覆盖少数条件，关键事实必须与实际风险对应。

1. 为什么列调用者不等于影响范围分析？答案：序列化、外部消费者与时序边界可能不在符号调用图中。
2. “编译通过”能证明导出字段兼容吗？答案：不能，需要消费者契约检查。
3. 纸面模拟能列为运行证据吗？答案：不能，只能写推演及其限制。
4. 多模型多数赞成能替代证据吗？答案：不能，仍需检查真实产物和关键安全事实。
