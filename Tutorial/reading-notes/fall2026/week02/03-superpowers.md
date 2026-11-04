# Superpowers：规格、计划与证据门禁

[上下文与规格](../../../chapters/03-context-spec.md) · [Skills 与自动化](../../../chapters/05-skills-automation.md) · [测试与审查](../../../chapters/07-testing-review.md)

## 来源与范围

- 来源：[obra/superpowers](https://github.com/obra/superpowers)，README 署名 Jesse Vincent 与 Prime Radiant 团队。
- 核对日期：2026-11-04；固定提交 `22f0b463e7a5e579904dd6211a520321035526f7`，不把核对日当发布日期。
- 通过该提交的 API 文件树确认路径，实际读取 [README](https://raw.githubusercontent.com/obra/superpowers/22f0b463e7a5e579904dd6211a520321035526f7/README.md)、[writing-plans/SKILL.md](https://raw.githubusercontent.com/obra/superpowers/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md)、[verification-before-completion/SKILL.md](https://raw.githubusercontent.com/obra/superpowers/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md)。
- 未逐份读取其他 Skill、平台安装说明、Hooks、依赖脚本和测试仓库，未安装插件、运行来源命令、创建 worktree 或执行模型实验。下文不声称读完技能库，也不验证 README 的自动触发与长时自主运行宣称。

## 1. 总体方法与具体规则要分开读

定位：README 的 `How it works`、`The Basic Workflow`、`Philosophy`。

README 提倡先澄清意图和规格、批准设计、编写计划，再进入实现与审查。其基本工作流介绍 brainstorming、worktree、writing-plans、执行、TDD、审查与分支收尾。这里只是概览；没有读取某个 Skill 正文就不能推测它的准确权限、任务分配机制和失败恢复流程。

README 把这些称为强制工作流。但“Skill 写着必须”不等于客户端一定会触发，也不是操作系统级门禁。工程上仍要保留权限检查、测试和人工批准不可逆动作。来源里的提交、合并、删除或安装步骤不是本教程的授权。

## 2. 好计划记录执行者不能自行猜出的决定

定位：`writing-plans` 的 `Overview`、`Task Right-Sizing`、`What a Step Contains`、`Self-Review`。

计划的读者是没看过仓库或规格的工程师。需要写清文件职责、接口签名、规格中的具体值和证明该任务的测试，不是复制实现的全部函数体。

当前版本把任务边界定义为“值得独立审查、具有自己的测试循环的最小交付单元”。README 仍用 2–5 分钟任务的概览说法；正文更重要的是独立验收边界，不能为了时间数字机械拆出没有功能意义的脚手架任务。

计划头部包含 Goal、Architecture、Tech Stack、Spec、Global Constraints 和 Review Focus。各任务注明输入输出接口，防止上一任务产出 `parseItems()`，下一任务却调用 `extractActions()`。Review Focus 是规格未显式列出但用户实际会遇到的输入或失败条件，不是空泛的“处理边界情况”。

教程补充案例：行动项提取器的一项任务可以定义 `extractActions(text)`，返回负责人、动作与期限；固定样例“李明周五提交草稿”应有独立期望值。若规格没有规定无负责人时的处理，就必须决策或记录缺口，不能由实现者偷偷补成“未知”。任务应包含实现该行为与测试，而不是把“建文件”“写类型”“写测试”拆成三个无法独立验收的交付。

## 3. 验证门禁约束的是声明

定位：`verification-before-completion` 的 `The Gate Function` 和 `Common Failures`。

规则是：识别能证明声明的命令，完整运行，读取输出和退出码，判断证据是否支持，再报告。测试通过不等于 build 成功；lint 通过不等于原缺陷被修复；子 Agent 自报完成不等于实际 diff 存在并满足规格。

回归测试必须证明对原缺陷敏感。仅看到新测试通过一次，可能是测试从不触达缺陷。红阶段应显示预期缺陷导致失败，绿阶段才说明修复改变了结果。真实项目中的回退或重放必须在隔离副本进行，不能照抄来源示例去回退用户工作区。

## 4. 30 分钟离线练习

教程扩展。预算 30 分钟、0 API 调用、不安装或执行插件，用假数据设计计划与审查证据。

假需求：“从会议文本提取明确负责人和动作；无负责人返回空结果；不访问网络。”样例 A“李明提交草稿”应有一条，B“下周讨论”应为空，C 空字符串应为空。假测试报告写着“A 通过，B 失败，C 未运行”。

1. 0–10 分钟：写一项独立任务，列文件职责、接口、三份字面期望和全局限制。
2. 10–18 分钟：补 Review Focus：空输入、无负责人、重复行动项；重复规则未决定时明确写待确认，不自行扩规格。
3. 18–25 分钟：审查计划的接口一致性，并删掉“完善处理”等无法验收的步骤。
4. 25–30 分钟：根据假报告写状态说明，只能声明 A 已通过、B 失败、C 未测，不能写“功能完成”。

验收：计划每个决定有规格依据，每个已确定行为有独立期望，状态说明不超出报告证据。交付一页计划和一段验证声明。**本次未执行该练习或来源测试。**

## 局限与自测

重流程对小改动可能带来上下文、审查和调用成本；README 的平台兼容与自动触发仍需在具体客户端版本验证。规划质量不能消除错误规格；Fresh evidence 也只能证明覆盖的检查，不证明所有潜在输入正确。

1. 为什么计划不应写满函数体？答案：应保留实现者可合理决定的部分，重点传递无法猜出的规格值、接口和验收决定。
2. 子 Agent 说完成能直接宣布完成吗？答案：不能，应检查实际产物并独立验证。
3. 测试全部通过是否代表需求全部满足？答案：不一定，还要逐项核对规格覆盖和遗漏。
4. README 写了自动触发，本笔记是否验证了？答案：没有，仅完成文档读取。
