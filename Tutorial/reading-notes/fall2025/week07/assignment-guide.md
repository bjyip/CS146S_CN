# 第 7 周作业导读：四项实现与人工、AI 审查证据

[本周入口](README.md) | [第 07 章](../../../chapters/07-testing-review.md) | [第 09 章](../../../chapters/09-delivery-operations.md)

## 来源与状态

- 归属：CS146S Fall 2025 本地作业，说明未单独署名。本页分析当前实现快照，不冒充初始 starter、官方译文或 Graphite 审查结果。
- 核对日期：2026-11-05。读取 assignment、README、writeup、TASKS、Makefile、pre-commit 配置、seed.sql、八份实质应用 Python 文件、六份测试文件（含 conftest）、三个前端文件，以及作业根 README 与 pyproject；包初始化仅盘点，Poetry 锁文件未逐项分析。
- 实际状态：仅静态阅读；未安装依赖、运行 Python/pytest/浏览器/应用、创建数据库、调用 AI、登录 Graphite、创建分支或远程 PR、提交或推送。报告引用的框架外链本批未读。
- 原材料：[week7 目录](../../../../_assignments/2025%20fall/week7/)。本页不增加指定阅读数量，不代表本周论文、指定视频或课件视觉核验完成。

## 1. 原目标、评分与环境

[assignment.md](../../../../_assignments/2025%20fall/week7/assignment.md)要求对[四项任务](../../../../_assignments/2025%20fall/week7/docs/TASKS.md)分别创建独立分支，以一次性提示实现，逐行人工审查并修正，再提交独立 PR，取得可见的 Graphite Diamond 审查。PR 要写问题、方案、真实测试命令及结果、新增测试、取舍和后续工作；writeup 对每个 PR 比较人工与 Graphite 的具体发现，并反思信任边界。

| 原任务 | 应留证据 | 原评分 |
| --- | --- | --- |
| 更多端点、验证与错误处理 | 首次生成、人工修正、契约与边界回归、独立 PR 和 Diamond 评论 | 20 分 |
| 更复杂的行动项提取 | 选择规则、结构化结果、语义反例、独立 PR 和 Diamond 评论 | 20 分 |
| 新模型与关系 | 模型、关联生命周期、应用支持及测试、独立 PR 和 Diamond 评论 | 20 分 |
| 分页与排序测试 | 可区分错误实现的数据、边界与组合断言、独立 PR 和 Diamond 评论 | 20 分 |
| 简短反思 | 各 PR 的真实人工/AI 对照、确认发现、误报、遗漏与信任经验 | 20 分 |

总计 100 分；每项 20 分同时考察正确完整、代码质量、人工审查深度和 Graphite 审查，不把“实现文件存在”视为自动得分。原说明的 30 天试用、教育码和协作者/Gradescope 是历史课程要求，不证明当前资格，也不授权本次登录、加协作者或远程写入。

[作业根 README](../../../../_assignments/2025%20fall/README.md)建议 Python 3.12，[pyproject](../../../../_assignments/2025%20fall/pyproject.toml)允许 `>=3.10,<4.0`，采用 Poetry dev 依赖组且 `package-mode=false`。本周 README 的 `pip install -e .[dev]`不能据此视为已验证的根环境安装方法；其中 `assignments/week7`也不是本地真实目录。依赖根为 `_assignments/2025 fall/`，应用与 Make 工作目录为其 `week7/`，不能混用中文仓库根和另一个年份。

[Makefile](../../../../_assignments/2025%20fall/week7/Makefile)启动 loopback 8000、运行 backend/tests，format 会写文件，lint 是 Ruff 而非完整测试或远程门禁。POSIX 环境前缀与 shell 默认值未验证原生 PowerShell 兼容。[pre-commit-config.yaml](../../../../_assignments/2025%20fall/week7/pre-commit-config.yaml)没有常规前导点，默认发现未证明；Black 24.4.2、Ruff v0.4.8 与基础 Hook 的配置不证明 Hook 已安装或执行，也不授权下载其环境。

## 2. 当前实现与报告声明

[writeup.md](../../../../_assignments/2025%20fall/week7/writeup.md)明确未创建远程 PR、Issue 或提交哈希，未运行 Graphite 服务及 Python/pytest；“Diamond 风格本地审查”不是 Graphite 输出。未保留 one-shot 提示和首次产物、实现前基线、独立审查日志、实测命令结果、身份或时间记录。因此可读代码是机制证据，报告的“无阻断问题”不能当审查通过，尤其不能覆盖下文的静态缺陷。

当前后端有笔记五项、行动项六项、标签四项，共 **15 项业务 HTTP 操作**，另有主页/静态页面。没有提取 HTTP 端点，没有用户身份与资源归属；不要把其他周的批量 apply、幂等或 Note→Action 关系带入本周。

### 端点、验证与查询

[schemas.py](../../../../_assignments/2025%20fall/week7/backend/app/schemas.py)的 ApiModel 禁额外字段并 trim 字符串；标题 1–200、正文 1–20,000、描述 1–2,000。行动项请求体 completed 使用 StrictBool；查询参数解析不是同一条验证路径，不能自动赋予同等严格性。PATCH 拒绝空对象/全 null，非 null 字段才更新，`tags: []`用于清空标签。

[notes.py](../../../../_assignments/2025%20fall/week7/backend/app/routers/notes.py)对 q 的标题/正文匹配取 OR，再与 tag 条件组合成 AND；[action_items.py](../../../../_assignments/2025%20fall/week7/backend/app/routers/action_items.py)的 completed 与 q 同时限制。SQLAlchemy 绑定参数使输入保持数据角色，但 LIKE 中 `%`、`_`仍可通配，不等于字面搜索，也不等于 SQL 结构注入。SQLite 与 Python 的 Unicode 大小写处理不能假定完全一致。

skip 非负、limit 为 1–200（默认 50），q/tag 有长度限制。排序参数正则与固定属性集合限制列名及最多一个前导 `-`，ID 次序与主排序同方向，可减少主排序值相同时的歧义；offset 分页遇到并发增删仍可能漏读/重复，条数上限不保证响应字节、关联总行数或查询时长预算。

[main.py](../../../../_assignments/2025%20fall/week7/backend/app/main.py)将无效 JSON 请求归为 400，其他请求验证归为 422，并处理 StarletteHTTPException 的错误信封。验证错误有 details，不证明任意数据库/未处理异常也走同一 JSON 契约。路由 flush/refresh 不是最终 commit；响应与依赖提交时序需要按真实版本另验。

### 跨文件标签契约

标签与笔记通过[models.py](../../../../_assignments/2025%20fall/week7/backend/app/models.py)中的关联表建立多对多。两侧 `lazy="selectin"`支持批量关联读取，但可能同时预取反向集合，不能仅凭选项名字宣称所有 N+1 或规模问题解决。`ondelete="CASCADE"`是声明；[db.py](../../../../_assignments/2025%20fall/week7/backend/app/db.py)未启用 SQLite `PRAGMA foreign_keys`，ORM 清理不能证明数据库级级联已经生效。

源码支持的契约不一致：schemas 10–11 行的 TagCreate/TagRead 只接受 ASCII 名称，而 22–32 行的 normalize_tags 使用 Python `isalnum()`，接受 Unicode 字母。合法长度的笔记请求含 `tags: ["中文"]`可通过 NoteCreate，并进入标签创建路径；构造 NoteRead 时嵌套 TagRead 的 ASCII 约束可能失败。该结论来自跨文件静态推导，未观察 HTTP 状态或最终持久化；异常路径有 rollback，不能断言失败响应必然留下数据。

标签还会 trim、移除前导 `#`，每篇最多 20 个，并拒绝忽略大小写的重复名称。路由的大小写查重与数据库字符串唯一索引不等于并发下的完全大小写一致性。ActionItem 仅存描述、完成状态和时间，提取器的负责人、日期、优先级与标签不是自动持久化字段。

### 前端路径是独立验收层

[frontend/app.js](../../../../_assignments/2025%20fall/week7/frontend/app.js)的 loadNotes 在 29–30 行使用 `li`，但该函数未创建或定义它。正常页面收到至少一条笔记时，静态预期为 ReferenceError，笔记渲染无法完成；空列表不进入该分支，因此“空首页打开”不能覆盖它。这是当前源码问题，不是本次已执行的浏览器故障，也没有修改原作业来修复。

空搜索仍发送 `q=""`，与后端 q 最小长度 1 冲突，静态预期为 422；省略 q 才表达无搜索条件。fetchJSON 能显示部分 HTTP 错误，但网络异常和上述 ReferenceError 不经过该显示逻辑；多个回调未等待重新加载，没有写入按钮锁或请求代次控制。加载前清空和交叠响应可能造成空状态或旧结果，创建后的无条件 reload 会重置筛选。

界面提供创建、删除、搜索、状态切换，不是完整标题/正文编辑 UI。用户数据使用 textContent，常量 `innerHTML=''`只是清空，不据此报告用户 HTML 注入。浏览器、窄屏、键盘和可访问性未运行；占位文字也不替代正确表单标签。

## 3. 提取器机制与语义边界

[extract.py](../../../../_assignments/2025%20fall/week7/backend/app/services/extract.py)是纯英文规则解析，没有模型和跨行去重。非空 checkbox、TODO/ACTION 前缀、末尾 `!`、首词动作动词，或任意负责人/标签/有效日期元数据，都可使一行入选。普通历史叙述含 `@alice`也会入选，否定不是独立排除条件；这是规则局限，是否违反作业应结合具体业务规格，不能给宽泛任务清单补造唯一语义标准。

描述保留 TODO 与元数据，移除识别到的 checkbox 或单个列表前缀。优先级取首次 high/low，负责人取首个非 high/low mention，标签按精确大小写去重，因此 `#work #Work`保留两个。日期优先首个 ISO，再首个斜杠日期，再 today/tonight、tomorrow、next week（+7）、by/before/on 星期；无效首个 ISO 不会继续遍历后续 ISO，仍可能走其他日期类别。

固定参考日 2026-08-28（星期五）时，`Review plan before Friday`映射到当天，不表达“严格早于星期五”；`next week`也不是下一周周一。默认 date.today 的时区未约定。保留旧函数返回 list[str] 只证明返回形状，扩展选择规则可能改变既有调用行为；纯函数的日期测试不证明 HTTP 提取、保存或实际业务期限正确。

## 4. 测试能区分错误吗

六份测试文件含 conftest，其余五个模块共有 **14 个测试函数**：笔记 1、行动项 1、提取 3、CRUD/验证/标签 4、分页/排序 5。本次均未运行，没有覆盖率或变异结果。

[test_pagination_sorting.py](../../../../_assignments/2025%20fall/week7/backend/tests/test_pagination_sorting.py)的笔记组合测试只有同时命中 q+tag 的记录和同时不命中的记录，缺 q-only/tag-only。把实现误改成 OR，也可能返回相同预期；报告“防住 OR 错误”不能由该数据集证明。行动项组合包含单条件记录，更能区分 AND/OR。没有排序同值的专门断言，不能据 ID 次序代码就说 tie 已实测；标签分页/排序、全部边界、null/空 patch、Unicode 标签、统一错误和浏览器路径仍有缺口。

[conftest.py](../../../../_assignments/2025%20fall/week7/backend/tests/conftest.py)先导入真实 app，再建立临时请求库和 get_db override；TestClient 的 startup 仍使用原全局 engine。请求隔离不等于启动隔离，默认数据库可能被创建。原 startup 先 create_all 再按文件是否存在决定 seed，默认文件已创建时通常跳过种子；自定义父目录创建顺序也需复核。固定 seed.sql 只有 notes/actions，不是完整标签初始化或迁移。

fixture 未用 finally 保证清理，也没有显式恢复 override 或 dispose 临时 engine，Windows 文件句柄释放未验。不要先运行测试再确认是否写原库；获准复现时应先在个人副本隔离导入配置、启动 engine、请求会话、存储目录与清理路径。

## 5. 原作业执行顺序与离线替代

1. 在获准的独立练习仓库冻结基线、四项契约、工具/数据政策和预算。每项保留独立 one-shot 提示及原始产物，人工逐行检查后单独留修正 diff，不反复生成后伪装首次输出。
2. 为发现写位置、触发条件、影响、预期与确认方法，补正常/失败/组合回归。真实运行另需依赖与双数据库隔离授权；记录命令、退出码和完整结果，不填未运行通过。
3. 经明确远程授权才创建四个 PR 并取得真实 Diamond 评论。按根因去重后比较人工与 AI，分确认、误报、待验证与遗漏；没有已知缺陷全集，不声称真实召回率。缺平台条件时如实标为自学改编，不冒充原作业完成。

教程扩展：50 分钟，零网络、安装、AI/Agent、Graphite、测试、浏览器、服务、数据库和远程写入，只做纸面假数据，不改原作业。

1. 10 分钟填写四张任务证据卡，分别列现有实现、one-shot/人工修正/PR/Diamond/实测缺口；把报告“本地 Diamond 风格”标为自述而非产品输出。
2. 10 分钟写两条静态发现：非空笔记的未定义 li、Unicode 笔记标签与 TagRead 不一致。区分代码确定事实、条件预测、尚未观察的 HTTP/数据库结果。
3. 15 分钟画 AND 矩阵：同时命中、q-only、tag-only、皆不命中四种记录；加两条主排序值相同的不同 ID，写双向次序预期，不执行变异。
4. 15 分钟手算固定星期五下的三行：`Review plan before Friday`、`A note about @alice`、`TODO: Ship #work #Work`；再画真实 startup 与临时请求 override 的两条数据库路径，写运行前隔离条件。

验收为四卡、两发现、过滤/tie 矩阵、三条手算和双库图。AND 只保留双命中，OR 会加入两种单命中；同主值按排序方向排列 ID。三行均入选，第一期限为 2026-08-28，第二负责人 alice，第三保留两个大小写不同标签；均不是实测。纸面成果不替代四个 PR、Graphite 对照及技术正确性验收。

## 6. 自测与关联

**问：后端 14 个测试即使通过，能排除 li 缺陷吗？** 不能，这些 API/纯函数断言不执行正常页面的非空笔记渲染链路，本次也未实际通过测试。

**问：同时命中与皆不命中两类数据足以验证 AND 吗？** 不足，必须包含只命中一个条件的反例，才能与 OR 区分。

**问：模型字段和响应 schema 各自合法就没有跨层问题吗？** 不是；Unicode 名称能过 normalize_tags，却不符合嵌套 TagRead 的 ASCII 约束，需沿完整创建与返回链路审查。

**问：本地 Diamond 风格评论可填原评分中的 Graphite 审查吗？** 不可，来源、平台执行和 PR 可见性是不同证据；只能如实作为自学材料。

[第 07 章](../../../chapters/07-testing-review.md)统一讲测试分层与审查质量，本页提供原作业任务、实际代码和证据缺口；[第 09 章](../../../chapters/09-delivery-operations.md)连接 UI、失败恢复与持久化，[第 08 章](../../../chapters/08-security.md)补数据库/身份边界。复用[测试矩阵与审查模板](../../../reference/templates.md)，不新增重复模板；本周其他材料状态见[周索引](README.md)。
