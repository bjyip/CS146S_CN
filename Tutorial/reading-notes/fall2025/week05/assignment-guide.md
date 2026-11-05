# 第 5 周作业导读：Warp 自动化、并发交接与集成证据

[本周入口](README.md) | [第 06 章](../../../chapters/06-repo-parallel.md) | [第 05 章](../../../chapters/05-skills-automation.md)

## 来源与状态

- 归属：CS146S Fall 2025 本地作业快照；原说明未单列个人作者，工作流 author 字段为 CS146S，不据此推定全部实现的作者。
- 核对日期：2026-11-05；已读 assignment、README、writeup、Makefile、pre-commit 配置、四份 `.warp` 定义、八份应用 Python 源码、五份测试文件、TASKS.md、seed.sql、三个前端文件及 2025 作业根 README、pyproject.toml 全文。包初始化文件只做目录盘点，不纳入实质解读。
- 实际状态：仅静态阅读，未安装或登录 Warp、导入工作流、启动 Agent/服务、运行测试或 Hook、创建数据库、调用模型、提交或推送。报告用法是提交者自述，不是本批执行证据。
- 原资料：[week5](../../../../_assignments/2025%20fall/week5/)。作业与指定阅读分别统计；本页不代表 Warp University、产品对比、团队实践、Figma 嘉宾课件或视频已取得正文。

## 1. 原要求与当前快照

[assignment.md](../../../../_assignments/2025%20fall/week5/assignment.md)要求从 [TASKS.md](../../../../_assignments/2025%20fall/week5/docs/TASKS.md)选至少两项任务并注明难度，同时必须使用 A、B 两类 Warp 工作方式：至少一项可共享的 Warp Drive 提示词、规则或 MCP 集成，以及至少一次不同 Warp 标签页中的独立 Agent 并发处理独立任务。再实际使用自动化改进工作流，交付两个或更多自动化的分享链接和/或导出定义、辅助材料及 writeup。MCP 不是必选，通用 worktree 或两份提示词本身不能替代真实 Warp 多 Agent 会话。

报告须说明目标、输入/输出、步骤、手动与自动化比较、每项任务的自主性及监督，以及并发的角色、协调、收益、风险和失败。原说明没有数值评分，也没有强制完成全部十一项任务；本页不新增官方 rubric。范围主要限于 week5，原文对其他周修改留有“自动化明确需要且记录原因”的例外，不应当作一般跨目录写权限。推送、协作者和 Gradescope 是历史课程提交要求，不是本批远程操作授权。

[当前 README](../../../../_assignments/2025%20fall/week5/README.md)宣称完成任务 2–8，但应分解核对，而不是重复完成标签：

| 任务与原难度 | 当前静态可见内容 | 尚缺或未验证 |
| --- | --- | --- |
| 2 搜索，中等；8 集合分页，简单 | 同条件计数、筛选、稳定排序、页码与页大小限制、静态界面分页 | 任务 2 原文要求更新 React 界面，当前仍是原生 JS；不能称严格完成 React 要求 |
| 3 CRUD，中等；4 筛选/批量完成，中等 | 笔记 PUT/DELETE、前端局部乐观修改、先核对所有 ID 再批量更新 | 并发回滚、分页刷新、事务故障窗口和浏览器行为未测 |
| 5 标签，复杂；6 提取，中等；7 错误封装，简单至中等 | 多对多表、标签关联、提取预览/写入、异常处理 | 全部失败路径、并发唯一冲突、提取长度边界仍需独立测试 |
| 1 React，复杂；11 Vercel，中等至复杂 | README 明确未迁移/未部署 | 本地无相关构建与部署配置，不因写了解题思路视为完成 |
| 9 索引，简单至中等；10 测试，简单 | 模型有索引，四份测试正文 | 未取得大数据查询计划、性能对照、并发或前端集成测试证据 |

[writeup.md](../../../../_assignments/2025%20fall/week5/writeup.md)未单独计时，姓名与 SUNet ID 未提供；A 为 API 审查入口，B 为交接与角色分工，C 复用 A 检查批量原子性。C 不自动构成独立第三套自动化。报告没有可核验的标签页时间线、模型版本、运行日志或量化前后耗时；不能由“使用了”叙述得出真实并发加速或完整验收。

## 2. 环境入口先消除歧义

依赖根是 `_assignments/2025 fall/`，应用与 Makefile 的工作目录是其 `week5/`，不是课程中文仓库根。[根 README](../../../../_assignments/2025%20fall/README.md)建议 Python 3.12 和 Poetry；[pyproject](../../../../_assignments/2025%20fall/pyproject.toml)允许 `>=3.10,<4.0`、使用 Poetry dev group 并设 `package-mode=false`。week5 README 的 `pip install -e .[dev]` 与这份非包模式、开发依赖组配置不一致，未声明同名 dev extra；不要视为已验证替代安装命令。本批不安装或验证环境兼容性。

[Makefile](../../../../_assignments/2025%20fall/week5/Makefile)使用 POSIX 环境变量前缀及 HOST/PORT shell 默认值，不能直接保证 PowerShell 原生兼容。默认 loopback 8000，前端由 FastAPI 提供，无 Node 构建链；`make format` 会运行 Black 与 Ruff 自动修复，`make lint` 只运行 Ruff，`make test` 运行 backend/tests。配置叫 [pre-commit-config.yaml](../../../../_assignments/2025%20fall/week5/pre-commit-config.yaml)，不是通常自动发现的 `.pre-commit-config.yaml`；须核验选中的配置及执行根目录，不能由 `pre-commit install` 推断此文件已加载。配置固定 Black 24.4.2、Ruff v0.4.8 和基础 hooks v4.6.0，安装/首次执行可能需要网络，自动修复不是只读审查，也不是 Agent 事件 Hook 或远程合并门禁。

## 3. 四份 Warp 定义实际做了什么

[工程规则](../../../../_assignments/2025%20fall/week5/.warp/rules/week5-engineering.md)规定先读任务与受影响代码、明确所有权、统一响应与分页、先核对批量 ID、乐观失败恢复及集成后完整检查。这是提示层的协作约定，不是文件写权限或事务执行器。规则、README 与真实代码不一致时保留差异，由协调者确认契约，不静默以某一份覆盖其他来源。

[API review YAML](../../../../_assignments/2025%20fall/week5/.warp/workflows/week5-api-review.yaml)声明 bash/zsh，接受 endpoint、criteria，实际只打印输入、执行后端/测试的 `git diff`、打印检查清单。它没有调用 pytest、自动读取规则文件或逐项验证端点；工作流末尾的 printf 也不是 Git 成功或审查通过的门禁。普通 diff 不包含未跟踪文件，且不覆盖 frontend、配置和文档，不能称完整变更审查。运行目录决定 pathspec 范围；应显式记录 cwd、基线、未跟踪文件和每项证据。

[handoff YAML](../../../../_assignments/2025%20fall/week5/.warp/workflows/week5-agent-handoff.yaml)用带引号的 heredoc 打印角色、文件范围、契约、任务、限制与交付要求；它不启动 Agent、创建 worktree、合并分支或强制权限。role/scope/task 没有本地 schema 白名单。两个 YAML 中 `{{...}}` 的现行导入、替换与转义机制未验证；尤其不能仅凭单引号/heredoc 就宣称任意不可信参数都安全，需另核验客户端版本和插值边界，本页不执行攻击输入。

[多 Agent 手册](../../../../_assignments/2025%20fall/week5/.warp/prompts/multi-agent-playbook.md)给协调者、后端、前端、测试和只读审查角色。按目录不重叠只是第一步：测试仍依赖后端契约，规则称集成者拥有共享 schema，手册却将模型/schema/路由都交后端，须在每次分派前明确唯一所有者。共享代码正在变动时“局部测试”也可能读到别人的半成品；独立工作区、相同基线、环境隔离和集成顺序比增加标签页更重要。

可复现的报告应保留各任务开始/结束时间、分配文件、共同契约版本、实际差异、检查与退出码、失败与集成耗时。没有这些证据只写“交接模板已准备”，不能写“多 Agent 会话已成功”。规则禁止提交秘密不等于工具没有远程凭据，报告中的低/中自主性也不自动落实为运行时权限。

## 4. 应用链路与关键边界

### 启动、事务与模型

[main.py](../../../../_assignments/2025%20fall/week5/backend/app/main.py)导入时创建相对 `data` 目录并挂载相对 frontend；startup 先 create_all，再调用 [db.py](../../../../_assignments/2025%20fall/week5/backend/app/db.py)的种子逻辑。与第 4 周按文件存在判断不同，本周查询 notes/actions 行数，仅当两者都为空才执行整个 seed.sql，所以清空这两表后重启可能重新加入示例数据；标签是否为空不参与判断。自定义数据库父目录是在 seed helper 中才创建，前面的 create_all 可能先失败；直接 `make seed` 在无表数据库上先 SELECT，也不能当初始化保证。未实际启动或建库。

请求依赖是 yield 后成功 commit、异常 rollback、最终 close；路由 flush 不等于最终持久化，依赖收尾与响应发送的时机仍需按实际 FastAPI 版本核验。[模型](../../../../_assignments/2025%20fall/week5/backend/app/models.py)有 Note/Tag 双向多对多及连接表联合主键；ActionItem 没有 note_id，不能承诺删除笔记级联删除所属待办。SQLite 未显式开启 foreign_keys，ORM 清关系与数据库级 CASCADE 是不同证据；create_all 也不是既有库迁移或新增索引的验收。

### 契约、分页与批量写入

[notes.py](../../../../_assignments/2025%20fall/week5/backend/app/routers/notes.py)、[action_items.py](../../../../_assignments/2025%20fall/week5/backend/app/routers/action_items.py)、[tags.py](../../../../_assignments/2025%20fall/week5/backend/app/routers/tags.py)共 16 项业务操作，另有隐藏于 OpenAPI 的尾斜杠别名。固定 search 路由先于动态 ID；笔记删除返回成功 JSON 而非第 4 周的 204，不能直接复用旧客户端契约。

分页限制 page≥1、page_size 为 1–100，超最后一页返回空 items；搜索空白串返回全部笔记而非第 4 周的 400。排序有 ID 次级键，有助同值稳定，但 offset 分页遇到期间插入/删除仍可能漏项或重复。SQLAlchemy 参数绑定避免直接拼 SQL，LIKE 的 `%`/`_` 仍是通配符而非字面搜索；SQLite 全部 Unicode 大小写语义未验证。页大小限制只约束记录数，不约束整条 content、标签总量或完整响应字节数。

[schema](../../../../_assignments/2025%20fall/week5/backend/app/schemas.py)先执行 Field 长度约束，再运行默认 after-validator 去空白/规范标签；不是先清洗后检查最大长度。标签去首部 `#` 并转小写，但不限制为 hashtag 正则字符集，例如 `# API` 可留下前导空格。bulk IDs 长度最多 100、正数且按首次出现去重；路由先查询全部 ID、发现缺失即 404，全部存在才改 completed。此顺序避免已知缺失 ID 导致部分更新，但不证明并发写入、提交失败与全局原子性都已测。

成功路由用 SuccessEnvelope，但 data 是 Any，不是逐端点强类型契约。main 中自定义 HTTPException、请求验证及未知异常封装，未知异常只回安全通用消息；它没有覆盖所有框架路径的统一错误保证，例如不存在的 URL/不支持的方法由 Starlette 异常路径处理，不能由业务 404 推断全部 404/405 都遵守 envelope。标签创建的预查可给串行重复 409，并发预查后唯一约束失败不一定映射相同 409。没有多用户身份/资源授权，不适合不加防护直接公开部署。

### 提取：预览、去重与幂等不能混用

[extract.py](../../../../_assignments/2025%20fall/week5/backend/app/services/extract.py)是纯规则，无模型：hashtag 支持 Unicode 单词字符/连字符，要求 `#` 前不紧邻单词字符，转小写后按首次出现去重；待办识别 `- [ ] 文本`，并保留 case-insensitive TODO 前缀或行末 `!` 的旧语法，行动文本精确去重。`- [x] done` 不匹配空 checkbox，但 `- [x] done!` 可从旧语法分支成为行动项；不能笼统宣称所有已完成 checkbox 都排除。

本周真的接入 `/notes/{id}/extract`：默认 apply=false 只计算结果，不增加标签/待办业务记录，但仍走 DB 请求依赖，不是零数据库访问。apply=true 创建/关联标签，并用整个 ActionItem 表的 description 去重，已完成的同描述待办也会抑制新待办，不区分笔记。串行重复应用在当前状态下可不增加重复项；两个并发请求仍可能共同未查到再插入，description 没有唯一约束，不能承诺并发幂等。返回 applied=true 是请求分支，不证明新增了多少项。

提取写入直接构造 ORM 对象，没有经过 TagCreate/ActionItemCreate：从合法的最长 20,000 字符笔记可得到超过 50 字符的 hashtag 或超过 500 字符的 checkbox 文本。SQLite 的 VARCHAR 长度声明也不是相同的请求校验；需在独立练习决定拒绝/截断规则并测试，不能把正常例通过当作入口一致性保证。

### 前端：局部恢复不是并发一致性

[app.js](../../../../_assignments/2025%20fall/week5/frontend/app.js)消费 envelope，以 textContent 显示用户内容，避免把笔记作为 HTML 插入。编辑、删除、完成和批量完成都有局部旧状态恢复，但没有请求代次或提交锁：迟到的搜索结果可覆盖新查询，旧失败恢复可覆盖较新操作或把笔记插回当前另一页。后端已写入但响应丢失时，前端回滚不能撤销服务器写入，需重新对账而非直接重试创建。

完成后只改当前记录，未重新计算完成状态筛选与 total；删除不补满页面或调整空末页。搜索非空时忽略 tag，空搜索时 sort 不参与列表查询；点击标签徽章没有清空搜索，可能显示选中标签却仍搜索。loadTags 只取默认第一页最多 100 个标签，无翻页。loadNotes/loadActions 自己 catch 后不再抛出，调用者 await 成功不表示刷新成功；旧 error 也不自动清除。index 的单行内容输入不适合多行 checkbox 编辑；CSS 有窄屏布局但无浏览器、手机、键盘或无障碍实测证据。

## 5. 测试证明的范围

[五份测试文件](../../../../_assignments/2025%20fall/week5/backend/tests/)包含 fixture 加 12 个 test 函数：notes 4、action_items 3、tags 3、extract 2。静态断言涉及 CRUD、422/404 封装、ASCII 搜索/排序/分页、缺失 ID 后仍未完成、串行标签冲突/重复关联、内存双向关系及提取串行重复应用；不是覆盖率测量或实际通过结果。

关键隔离缺口：[conftest.py](../../../../_assignments/2025%20fall/week5/backend/tests/conftest.py)先导入真实 app，之后只覆盖 get_db。TestClient 上下文仍调用真实 startup/engine，可能创建并植入默认应用数据库；README“不会修改应用数据库”的承诺不能由临时请求库推导。清理也未在 finally 中保证、未恢复 dependency_overrides 或显式 dispose engine，Windows 文件句柄和异常路径未测。修补隔离前不直接执行原测试。

新增测试需求应包括：预览后实际零业务行变化、超长提取与已完成 checkbox、不同笔记同描述语义、并发提取/标签唯一冲突、提交异常、框架 404/405、旧响应/回滚与分页筛选一致性、索引查询计划。原测试没有前端/真实 Warp 会话、权限、性能对照或并发故障注入；不能填写“全部任务验收通过”。

## 6. 离线替代与验收

教程扩展：50 分钟、零网络/安装/模型/Agent/服务/测试/数据库写入，仅纸面走查假数据，不修改原作业，也不声称满足 Warp 实操要求。

1. 10 分钟写 A、B 两张自动化契约卡，列目录、基线、参数、允许权限、实际输出、检查与停止条件；把 API review 标成“打印清单”，handoff 标成“生成交接”，不是运行测试或启动并发。
2. 10 分钟分派前端和测试设计两项任务，先冻结 envelope/分页与 schema 所有者。加入“测试依据旧契约”事件，记录暂停、重新同步与集成复核；不虚构标签页或加速数字。
3. 10 分钟手算四例：`#Release #release` 得标签 release；`abc#tag` 不得标签；`- [ ] Add tests` 得行动 Add tests；`- [x] done!` 从旧语法得行动 `[x] done!`。另列同描述已完成待办会抑制新项的规格争议。
4. 10 分钟走查 bulk IDs `[1, 99999]`，假设仅 1 存在，应在修改前 404，1 保持原状态；再让两个 apply 同时读取“无同描述待办”，标出重复写窗口，不写“已实测并发安全”。
5. 10 分钟记录“新查询先返回、旧查询后返回”和“服务器成功、响应丢失、客户端恢复”两条时间线，提出请求代次与重新对账的验收需求，并盘点 TestClient startup 与临时请求库的两条数据路径。

交付物是任务/权限卡、依赖图、四例预期、并发窗口及失败时间线。验收每个结论能定位实际来源，交接与并发、flush 与 commit、预览与零数据库访问、客户端回滚与服务端撤销均分开。只形成测试计划，没有运行结果、性能或平台资格保证；复现必须另在获准独立环境核验版本、输入转义、数据库/端口隔离，并保留基线与集成证据。

## 7. 自测与章节关联

**问：两份 YAML 能证明完成多 Agent 原作业吗？** 不能。当前定义打印审查/交接材料，还需真实 Warp 独立标签页并发、任务成果、监督与集成记录。

**问：12 个测试有临时数据库就安全了吗？** 不能。请求 dependency override 不覆盖真实 startup engine；先核验导入、启动、写入与清理所有路径。

**问：重复 apply 没有增加行，就能称幂等吗？** 只能说明给定串行状态下的去重；全局同描述规则会抑制另一笔记任务，并发窗口仍可能产生重复。

**问：前端失败回滚等于撤销服务器事务吗？** 不等于。响应丢失可能发生在服务器提交之后，需要对账；还应避免旧请求恢复污染新状态。

[第 06 章](../../../chapters/06-repo-parallel.md)集中解释基线、依赖、所有权及隔离，[第 05 章](../../../chapters/05-skills-automation.md)解释定义与执行门禁，[第 07 章](../../../chapters/07-testing-review.md)解释独立行为证据，[第 09 章](../../../chapters/09-delivery-operations.md)解释全链路恢复。本页只解读本周具体实现，不把十二个测试或 Warp 操作说明堆入章节。
