# 第 4 周作业导读：自动化工作流与可核验交付

[本周入口](README.md) | [第 05 章](../../../chapters/05-skills-automation.md) | [第 07 章](../../../chapters/07-testing-review.md)

## 来源与状态

- 归属：CS146S Fall 2025 本地作业快照；说明与报告已有中文，本文是实现与验证边界的教学解读，不是初始英文 starter 的逐字翻译。
- 核对日期：2026-11-05；已读 assignment、README、writeup、CLAUDE.md、Makefile、pre-commit 配置、三份命令、七份应用源码、四份测试文件、两份 docs、seed.sql 与三个前端文件全文；包初始化文件不在实质分析范围。另核对 2025 根安装说明与 pyproject。
- 仅静态阅读，未安装依赖或客户端、加载命令、运行 pytest/覆盖率/Hook、导入应用、创建数据库、启动服务、调用模型或执行提交与推送。
- 原材料：[week4 目录](../../../../_assignments/2025%20fall/week4/)。作业独立统计，不增加指定阅读完成数；报告引用的外部文章不因此视为本批已取得正文。

## 1. 原要求、评分与交付

[assignment.md](../../../../_assignments/2025%20fall/week4/assignment.md)要求用 Claude Code 功能构建至少两个自动化工作流，再实际用它们改进开发者指挥中心。可组合自定义斜杠命令、CLAUDE.md、子智能体或 MCP；不是必须每类都做，也不是有两个配置文件就完成两个有效流程。若选择子智能体方向，说明要求设计两个或更多角色协作。

提交包括工作流文件/配置与 week4/writeup.md：设计来源、目标、输入输出、步骤、准确运行方式、预期结果、安全与回滚、手动/自动化对比，以及如何增强应用。本地 assignment **没有列数值评分表**，不要借用其他周的 100 分或自学 rubric。原提交说明涉及远程推送、课程协作者及 Gradescope，只描述历史课程要求，不授予本轮账户操作权限，也不要求非课程自学者添加陌生协作者。

当前目录已有三个命令、规则、CRUD 与测试，不能清空重做。[writeup.md](../../../../_assignments/2025%20fall/week4/writeup.md)中的约 8 小时、工作流使用与最终功能是报告自述；姓名/SUNet ID 仍未填写。它没有附足以复核的完整调用记录、退出码或覆盖率数值，不能用它证明本次运行通过。第三个流程描述的是使用重构清单审视扩展，并未真的完成模块改名；这与一次完整重构执行证据不同。

## 2. 环境与命令的实际边界

依赖安装根是 [_assignments/2025 fall/](../../../../_assignments/2025%20fall/README.md)，运行目录是 `_assignments/2025 fall/week4/`。原安装说明建议 Python 3.12；[pyproject](../../../../_assignments/2025%20fall/pyproject.toml)允许 `>=3.10,<4.0`，声明 FastAPI、SQLAlchemy、Pydantic、pytest、Black、Ruff、pre-commit 等，但**未直接声明 pytest-cov**。安装范围不锁定实际版本，本批未验证兼容性。

[Makefile](../../../../_assignments/2025%20fall/week4/Makefile)的 run/test/seed 使用 POSIX 风格 `PYTHONPATH=.`；run 还使用 `${HOST:-127.0.0.1}` 和 `${PORT:-8000}`。这些是原命令，不保证 Windows PowerShell 原样执行；复现时须记录 Make 的 recipe shell 和目录，不能静默换命令仍声称原样复现。默认服务地址为 loopback 8000，前端由 FastAPI 提供，没有 Node 构建工具链。

`make format` 会运行 Black 与 `ruff --fix`，可改文件，不是只读检查；`make lint` 只运行 Ruff，不同时证明 Black 格式通过。[pre-commit-config.yaml](../../../../_assignments/2025%20fall/week4/pre-commit-config.yaml)固定 Black 24.4.2、Ruff v0.4.8 及基础 Hook v4.6.0，含自动修复。该文件名没有默认的前导点；本次目录检索未发现 `.pre-commit-config.yaml`，原文直接 `pre-commit install/run` 的默认配置发现不能视为已接通，实际复现须确认配置路径或显式选择此配置。这里不安装 Hook、不改原文件，也不把本地 Hook 当分支保护或 Claude 事件 Hook。

## 3. 三份命令：提示模板不是执行门禁

| 文件 | 指定流程 | 核验重点 |
| --- | --- | --- |
| [tests.md](../../../../_assignments/2025%20fall/week4/.claude/commands/tests.md) | 空参数用 backend/tests，选项参数前补目录；快速失败，通过后重跑覆盖率 | 首段失败必须停止；选中范围、两次退出码与覆盖率缺口分别记录 |
| [docs-sync.md](../../../../_assignments/2025%20fall/week4/.claude/commands/docs-sync.md) | 读路由/schema/文档，取得 OpenAPI，只改 API.md，再比较 | 服务身份、同一代码版本、人工错误说明、无变化时零差异 |
| [refactor-module.md](../../../../_assignments/2025%20fall/week4/.claude/commands/refactor-module.md) | 参数不全拒绝猜；查引用、窄基线、移动更新、全量检查与残留扫描 | 修改范围、公开行为、数据保留、失败停留与仅撤销自身改动 |

三份文件是自然语言工作流，没有内置执行器验证参数、退出码或批准。`$ARGUMENTS` 是否发现、如何展开及工具权限取决于实际 Claude Code 客户端；本批没有测其加载。流程命名为“安全”不构成沙箱。任意测试路径可能执行有副作用的测试，任意 base URL 可能指向不可信服务；教程扩展应限制允许的范围/地址，不把自由参数直接拼成获准 shell 操作。

`/tests` 快速阶段与覆盖率阶段是两次执行；第二次还需 pytest-cov。前段通过不保证后段可用，也没有 `--cov-fail-under` 阈值，打印覆盖率不等于覆盖率门禁。命令称“只读、确定性”，但测试、导入和插件可以写文件，重复执行也可能不同；实际副作用必须沿调用链检查。

`/docs-sync` 以服务 OpenAPI 核对声明的路径、参数与 schema 很有价值，但运行中的服务可能是旧版本或错误目录。OpenAPI 不是实际业务行为全集：未显式声明的 404、空白查询 400、数据库失败、鉴权与 UI 行为仍需源码和测试依据。第二次 fetch 是复核机会，不自动证明幂等；需保存两次同版本输入与差异，保留人工安全说明。不可达时停留在静态核对，不伪填 `remaining drift: none`。

重构先查 import、字符串引用与基线，再改最小范围；不为展示流程制造无用改名。不保留兼容壳的建议只适用于确认没有持久化数据或外部消费者的情况；一旦存在公开接口/迁移需求，先确认契约。失败时保留工作区证据，不能使用破坏性 Git 命令或回退他人并发修改。

[CLAUDE.md](../../../../_assignments/2025%20fall/week4/CLAUDE.md)提供架构、命令、错误约定、先读再改与保留用户修改的规则。它是 week4 局部指导文件，不证明从整个课程仓库启动就已生效；也不能授权启动服务、安装依赖或真实数据库写入。

## 4. 应用链路：功能存在与端到端接通分开

后端由 [main.py](../../../../_assignments/2025%20fall/week4/backend/app/main.py)、[db.py](../../../../_assignments/2025%20fall/week4/backend/app/db.py)、[models.py](../../../../_assignments/2025%20fall/week4/backend/app/models.py)组织。导入 main 会建立 data 目录并配置静态目录；启动先 `create_all`，再 `apply_seed_if_needed`。后者只在数据库文件此前不存在时导入 seed，但正常 `create_all` 已可创建默认文件，因此不能保证首次正常启动会导入欢迎记录；直接 seed 与正常启动也不是同一路径。自定义 DATABASE_PATH 的父目录若不存在，建表可能先失败。这里只给静态控制流风险，未运行验证。

请求依赖 yield 一个 Session，成功后 commit、异常 rollback，路由在返回前 flush/refresh。flush 不是最终 commit；正常 HTTP 返回与提交/响应时序仍须按实际 FastAPI 版本验证。默认 `./data/app.db`、seed 与 frontend 均依赖工作目录，不是第 2 周数据库的迁移版。[模型](../../../../_assignments/2025%20fall/week4/backend/app/models.py)中 Note 与 ActionItem 没有 note_id 关联；删除笔记不会按模型关系删除其行动项。

[notes.py](../../../../_assignments/2025%20fall/week4/backend/app/routers/notes.py)提供六个笔记路由，[action_items.py](../../../../_assignments/2025%20fall/week4/backend/app/routers/action_items.py)提供三个行动项路由，共九个业务端点，另有根页面。固定 search 在动态 ID 前；查询使用 SQLAlchemy 参数绑定，不拼接原始 SQL，但 `%` 与 `_` 仍是 LIKE 通配符，并未转义为字面搜索。测试只覆盖 ASCII 大小写，不证明 SQLite 的全部 Unicode 大小写语义。列表没有分页或输出总量限制。

[schemas.py](../../../../_assignments/2025%20fall/week4/backend/app/schemas.py)声明标题/content/description 长度与必填，after validator 去首尾空白并拒绝空串。长度约束先于该 validator，并非先 strip 再校验最大长度；超长外部空白不能假定会被裁剪后接受。PUT 完整替换标题与正文；删除成功为 204 空体；资源不存在为 404；空白 search 为 400，其他输入校验由框架处理。代码未配置完整身份/资源授权，不能直接作为多用户公开服务。

[extract.py](../../../../_assignments/2025%20fall/week4/backend/app/services/extract.py)是规则纯函数，不调用 LLM：清理行前导字符后，保留不区分大小写以 `TODO:` 开头或以 `!` 结尾的行；标签按正则、出现顺序、大小写敏感去重。`extract_note` 聚合两种结果，却未接入当前九个路由或前端；[TASKS.md](../../../../_assignments/2025%20fall/week4/docs/TASKS.md)的 `/notes/{id}/extract` 是可选任务，不是已实现接口。有服务函数不能写成用户已能一键从笔记生成行动项。

具体静态矛盾：[test_extract.py](../../../../_assignments/2025%20fall/week4/backend/tests/test_extract.py)期望 `Ship it! #release` 被收进 action_items，但它既不以 TODO: 开头，也不以 `!` 结尾，按当前函数会被排除。这是源码支持的预期冲突，不是本批实际 pytest 失败日志。应先决定“标签后缀是否改变行动判定”，再在独立练习修实现或测试，不能为绿灯随意删断言。

前端 [app.js](../../../../_assignments/2025%20fall/week4/frontend/app.js)通过 fetchJSON 统一处理非 2xx 与 204；显示数据使用 textContent，清空列表的空字符串 innerHTML 不等于插入用户 HTML。仍需注意：请求前清列表，失败会留空；没有按钮锁或请求代次，重复提交可能重复创建，迟到搜索结果可能混入当前列表；编辑/删除后刷新会丢失当前搜索条件。验证错误的 detail 可能是数组，直接构造 Error 不保证友好字段说明；错误状态也未在后续成功时统一清除。页面与 CSS 尚未浏览器或移动端验收，不把存在 viewport 当完整可用性证明。

## 5. 测试隔离与证据不足

[四份测试文件](../../../../_assignments/2025%20fall/week4/backend/tests/)包含 fixture 和 11 个测试函数：笔记 5 个、行动项 3 个、提取 3 个。它们静态覆盖 CRUD/search、若干 400/404/422、重复完成与标签聚合；数量不代表本批通过，也不代表完整安全/边界覆盖。

[conftest.py](../../../../_assignments/2025%20fall/week4/backend/tests/conftest.py)为每例创建临时 SQLite 并覆盖 get_db，但先导入真实 app，TestClient 上下文还会执行 startup。该 startup 使用原模块 engine，依赖覆盖并不替换它；因此可能建立默认 data/app.db，不能认定 `/tests` 只接触临时数据库。fixture 尾部只 unlink 临时文件，未显式恢复 override、dispose engine 或以 finally 保证清理；Windows 文件句柄与异常清理行为需另测。测试隔离是调用链属性，不是夹具名字或报告中的承诺。

尚无本批实测：启动/seed、真实磁盘提交失败、完整长度/额外字段、搜索通配符/Unicode、浏览器并发、认证、命令发现、覆盖率插件、Hook 安装与文档二次同步。应分别保存命令、工作目录、版本、退出码、实际数据库路径与未覆盖项，不用报告自述或 OpenAPI 清单替代。

## 6. 建议实施顺序与离线替代

原作业复现仅在另获授权的个人练习副本中进行：先核对客户端/依赖/recipe shell 与临时数据库边界，再建立窄基线，运行两个真实工作流，改一项有验收的应用功能，并保留改前失败、改后结果与文档差异。自动化前后比较固定任务和输入，同时记录人工纠错、失败时间和副作用；不要只比较命令字数。提交与推送另行确认。

教程扩展提供 **50 分钟、零网络、零安装、零模型、零测试/服务执行、零数据库写入** 的纸面替代，不修改原作业：

1. 10 分钟为 `/tests` 与 `/docs-sync` 各填目标、输入范围、两阶段输出、停止条件与修改边界。
2. 10 分钟画测试调用链：导入 app、临时 engine、依赖覆盖、原 startup、请求与清理，标出仍使用原 engine 的节点；另画 create_all 到 seed 的文件存在判断。
3. 10 分钟分析假输入 `TODO: docs #docs`、`Ship it!`、`Ship it! #release`、`Note #docs #Docs #docs`；手算行动与标签，再解释测试预期冲突。
4. 10 分钟对四份虚构记录判定：快速测试失败却继续覆盖率；快速通过但插件缺失；拿旧服务 OpenAPI 宣称同步完成；同版本双次核对无变化且保留人工错误说明。区分阻塞、待证据与声明范围内文档完成。
5. 10 分钟用[交接模板](../../../reference/templates.md#9-最终交接)写最小修复方案与验收矩阵，单列数据库隔离、命令配置、提取语义和浏览器并发，不预填运行成功。

验收交付是两份流程合同、两条副作用链、手算结果、四路状态与待运行矩阵。第 3 步行动结果依次是包含该 TODO 行、包含 Ship it!、空、空；标签依次是 docs、空、release、按顺序 docs/Docs。第 4 步前三项不得宣称端到端成功，末项只支持同版本输入下文档核对结果，不支持业务测试或模型有效性。纸面分析只证明理解，不能证明真实权限阻断、幂等或性能收益。

## 7. 自测与章节关联

**问：三个命令文件就证明三个工作流完成吗？** 不证明。还要核验发现、输入、实际执行分支与应用增强证据；清单审视不等于完整模块迁移。

**问：覆盖率阶段打印结果就有门禁吗？** 没有数值阈值不能称覆盖率门禁；首段/次段退出码、选择范围与业务覆盖要分别记录。

**问：覆盖 get_db 是否阻止全部原数据库访问？** 不阻止原 startup 的 engine 与导入副作用；必须沿调用链确认隔离。

**问：OpenAPI 一致是否证明 404、事务与 UI 正确？** 不证明。声明契约、实际失败行为与浏览器状态需要不同证据。

[第 05 章](../../../chapters/05-skills-automation.md)统一解释规则、流程与门禁；[第 06 章](../../../chapters/06-repo-parallel.md)负责仓库就绪与隔离，[第 07 章](../../../chapters/07-testing-review.md)负责独立测试，[第 09 章](../../../chapters/09-delivery-operations.md)负责持久化与交付。本页定位真实文件与本周冲突，不把全部实现复制到章节，也不与 2026 Skill 作业的提交要求混用。
