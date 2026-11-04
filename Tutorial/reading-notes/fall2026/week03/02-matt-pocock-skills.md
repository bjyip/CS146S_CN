# Matt Pocock Skills：可组合纪律与测试边界

[上下文与规格](../../../chapters/03-context-spec.md) · [Skills 与自动化](../../../chapters/05-skills-automation.md) · [测试与审查](../../../chapters/07-testing-review.md)

## 来源与范围

- 来源：[mattpocock/skills](https://github.com/mattpocock/skills)，README 标题 *Skills For Real Engineers*，作者 Matt Pocock。
- 核对日期：2026-11-04；固定提交 `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`，未另行核验提交日期或所有技能发布日期。
- API 文件树确认路径后，实际读取 [README](https://raw.githubusercontent.com/mattpocock/skills/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/README.md)、[skills/engineering/to-spec/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-spec/SKILL.md)、[skills/engineering/tdd/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/tdd/SKILL.md)。
- 未读其他 Skill 全文、`tests.md`、`mocking.md`、领域文档、setup 配套说明或依赖脚本；未安装、运行技能、发布 issue、调用模型或执行测试。正文中的跨 Skill 引用是未读依赖，不冒充已掌握其细节。

## 1. 组合工作流不等于让框架接管一切

定位：README 开头、`Why These Skills Exist`、`Reference`。

作者以意图不一致、过度冗长、代码不工作、结构变复杂四类失败解释技能设计。共用领域术语帮助沟通，测试反馈帮助实现，模块设计帮助限制复杂度。作者说这些技能小、可适配、可组合；“支持任何模型”是作者的设计宣称，不是本笔记的跨模型实测。

README 区分 user-invoked 编排入口与 model-invoked 可复用纪律，前者不调用另一个 user-invoked 入口。当前 `to-spec` frontmatter 标了 `disable-model-invocation: true`，`tdd` 没有该字段。这说明作者在组织调用意图，不代表所有客户端都遵循相同加载语义。

教程补充案例：规格输出需要已有对话和领域词表，TDD 需要已确认的测试边界。把它们组合时要传递决定，不应通过新一轮访谈重新推翻已经批准的规格。

## 2. to-spec 是综合，不是重新访谈

定位：`to-spec` 开头、`Process` 和 `spec-template`。

该 Skill 要从现有对话与仓库理解合成规格，明确禁止重新访谈。它仍要求确认测试 seam，也就是观察用户行为的公开边界；这是一项有限的测试决策确认，不等于重新询问整个产品意图。

模板包含 Problem Statement、Solution、User Stories、Implementation Decisions、Testing Decisions、Out of Scope 和 Further Notes。通常避免具体文件路径与代码片段，以免规格过早绑死实现；若原型片段比文字更准确表达决定，可以只保留决定密集的部分并注明出处。

教程补充案例：行动项提取器规格写“从公开提取接口观察负责人、动作、期限，空输入返回空数组”，不是“第 42 行调用内部函数”。与 Superpowers 的实现计划精确记录路径并不矛盾：规格确定用户契约，计划安排具体实施。该 Skill 要发布到 issue tracker，本教程只离线模拟，不执行发布。

## 3. tdd 先约定 seam，再逐个垂直切片

定位：`tdd` 的 `What a good test is`、`Seams: where tests go`、`Anti-patterns`、`Rules of the loop`。

好测试经公开接口断言行为，不与私有方法和内部协作者绑死。seam 要提前约定，并说明捕获什么、遗漏什么。较高边界通常能覆盖完整行为，但不意味着每次只能做端到端测试；具体取决于接口和成本。

该版本警告三类问题：耦合实现的测试、用与实现相同算法重算期望的同义反复、先写全部测试再写全部实现的横向切片。它要求一次一个 seam、一个测试、最小实现，下一轮利用刚获得的反馈。

**版本差异：**此处 `Rules of the loop` 明确把重构放到 `code-review` 阶段，不放在红 → 绿实现循环。README 仍称红绿重构，Superpowers 概览也用 RED-GREEN-REFACTOR。不要把不同层次或不同来源拼成完全一致的规则；此笔记按实际 Skill 正文解释当前循环，并保留差异。

## 4. 30 分钟离线练习

教程扩展。预算 30 分钟、0 模型/网络请求，不运行或安装技能，用假数据写规格和测试设计。

假需求已确认：公开接口 `extractActions(text)` 只抽取明确负责人和动作。输入“李明提交草稿”期望一条；“讨论草稿”期望空；空输入期望空。不决定日期推断、不发送任务到第三方。

1. 0–8 分钟：写半页规格，区分已确认决定、测试决定与范围外事项，不重新访谈。
2. 8–15 分钟：记录 seam 为公开提取接口，说明捕获文本到结果的行为，遗漏模型服务或 UI 交互。
3. 15–23 分钟：写三份字面期望，并排除“调用实现再复制结果作为期望”的同义反复。
4. 23–30 分钟：设计先正常样例、再无负责人、再空输入的三个红绿循环；假设第二轮失败时记录停止与下一步，而非把全部循环填通过。

验收：交付规格、seam 说明、三份独立期望和循环表；没有私有方法断言，没有无依据的完成标记。**本次仅编写练习，未执行测试或模型实验。**

## 局限与自测

公开边界测试不是无盲区保证；未读 `mocking.md` 不能从这里归纳完整 mocking 政策。作者的工程观念和自动更新说明不证明本地插件兼容，发布和认证仍需要单独授权。

1. 为什么期望不能由同一实现计算？答案：实现错误会同时污染期望，测试可能永远无法反驳它。
2. to-spec 是否必须重新访谈？答案：当前正文明确禁止，只综合已有信息，并确认测试 seam。
3. seam 描述为什么要写遗漏？答案：防止把局部接口覆盖说成全系统验证。
4. 当前 tdd 正文把重构放在哪？答案：审查阶段；这与 README 的概览措辞存在层次差异。
