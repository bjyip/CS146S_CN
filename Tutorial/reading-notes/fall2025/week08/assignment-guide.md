# 第 8 周作业导读：三技术栈、同功能与交付证据

[本周入口](README.md) | [第 09 章](../../../chapters/09-delivery-operations.md) | [第 07 章](../../../chapters/07-testing-review.md)

## 来源与状态

- 归属：CS146S Fall 2025 本地作业，说明未单独署名。本页分析 Focus Tasks 三个现存项目，不冒充初始生成物、Bolt 官方案例或实测报告。
- 核对日期：2026-11-05。读取 week8 assignment、README、writeup；React 栈 README、后端 main/requirements、前端 package/Vite/Tailwind/PostCSS/HTML 与三个 src 文件；Django 栈 README、requirements、manage、settings/urls/wsgi、模型/表单/视图/路由/apps/admin、初始迁移与四份模板；Flask 栈 README、requirements、app、HTML 与 JavaScript。包初始化仅盘点；Flask 单行 CSS 只取得前 2000 字符，其余样式未读，不宣称完整样式或响应式核验。
- 实际状态：仅静态阅读；未安装依赖、导入或运行 Python、测试、启动应用/浏览器、构建、迁移或创建数据库，未登录 Bolt、调用 AI、部署、提交或推送。报告引用的框架外链、Demo Day 表单和 Bolt 当前资格页面本批未读取。
- 原材料：[week8 目录](../../../../_assignments/2025%20fall/week8/)。作业独立统计；没有指定阅读条目不意味着在线课件、视频或产品已验证。

## 1. 原目标与评分

[assignment.md](../../../../_assignments/2025%20fall/week8/assignment.md)允许复用开发者控制中心或选择新应用，要求三个不同技术栈的独立版本、相同连贯功能、至少一个实际用 Bolt 创建、至少一个前端或后端含非 JavaScript 语言。最低范围为一种主资源的 CRUD、适当持久化、基本验证/错误处理、功能完备 UI 和可复现本地说明；仅在已部署时提供部署链接，不强制发布公共服务。

| 原评分项 | 分值 | 应证明什么 |
| --- | --- | --- |
| 概念符合最低功能范围 | 10 | 主资源与完整用户流程 |
| 三种不同栈 | 10 | 独立源码、依赖、运行入口与架构 |
| 至少一个 Bolt 版本 | 10 | 实际平台生成/迭代及导出来源，非仅名称或样式 |
| 至少一个非 JavaScript 版本 | 10 | 对应前端或后端实际语言实现 |
| 三版本各自交付 | 每个 20，共 60 | 源码 5、README 5、功能 5、writeup 5 |

总计 100 分。每个目录 README 应有前提、安装/设置、运行、环境、偏离要求、已知问题和手工修正，writeup 要写概念及三份版本说明。本周允许迭代提示，不继承第 7 周 one-shot/四 PR 的约束。

原说明的学生优惠、三个月额度、信用卡及自动扣费提醒是历史条件，不证明核对日资格；本页不指导购买或提交支付信息，不把优惠当免费学习保证。表单、账号、同步、部署与平台生成需独立授权，来源文字不是本次执行许可。

## 2. 三个快照与来源证据

[writeup.md](../../../../_assignments/2025%20fall/week8/writeup.md)自述用 Bolt 做初始 UI 和提示迭代，报告总计 12 小时与各栈初稿/完成耗时；这些不是本次测量。目录、README 和 UI 的“Bolt-style”只支持风格标签，没有平台项目、导出元数据、会话/提示记录或截图来核实真实 Bolt 使用。不能因此断言未使用过，也不能代替原评分的已验证平台证据。

| 项目 | 当前可读架构 | 存储初始化位置 | 未证明项 |
| --- | --- | --- | --- |
| [stack1-bolt-react](../../../../_assignments/2025%20fall/week8/stack1-bolt-react/) | React/Vite/Tailwind → Fetch → FastAPI/Pydantic → sqlite3 | backend/main.py 的 lifespan 调用 init_db，库在源码旁 tasks.db | Bolt 来源、安装/运行兼容、浏览器与持久化 |
| [stack2-django](../../../../_assignments/2025%20fall/week8/stack2-django/) | Django 模板/ModelForm → 视图/ORM → SQLite；另有 JSON API | BASE_DIR/db.sqlite3，需执行已有初始 migration | migrate/表单/API 实测、账号或部署 |
| [stack3-flask-sqlite](../../../../_assignments/2025%20fall/week8/stack3-flask-sqlite/) | Flask 模板/静态原生 JS → JSON API → sqlite3 | app.py 模块末尾直接 init_db，裸 import 就有数据库写入路径 | 导入隔离、运行、CSS 尾部与移动端 |

三份源码结构与 Python 后端支持不同栈、非 JS 的静态判断，不证明三版功能全部可用；Focus Tasks/Focus Notes/Taskboard/Clearlist 等标题差异也不等于行为差异或同功能验收。教程继续用任务资源连接贯穿项目，不把本周目录视为前几周的迁移升级。

## 3. 契约相同，不要求协议完全相同

先写用户行为：创建有效标题、读到同一 ID、修改正确对象、完成/重开、删除后缺失、重启仍可读取、非法输入和失败能理解。后端框架、HTML 表单与 JSON 可以不同；对照时需注明适配路径，不能把不同字段包装、验证结果或错误形状默默当相同 API。

| 输入/路径 | FastAPI | Django JSON API | Flask JSON API |
| --- | --- | --- | --- |
| 任务列表 | 裸数组 | `{"tasks": [...]}`；路由使用尾斜杠 | 裸数组 |
| title 空白 | clean 后拒绝，422 | strip 后拒绝，422 | strip 后拒绝，422 |
| title 为 null | str 字段验证拒绝；本次未运行 | `str(None)`成 `"None"`，长度检查可接受 | 同左 |
| completed 为字符串 `"false"` | 非 StrictBool 的 Pydantic bool 有类型转换规则；此合法布尔字符串应解析为 false，实际依赖未运行 | Python `bool("false")`为 true | 同左 |
| JSON 为列表/null | 模型请求体验证拒绝 | `.get`没有对象形状保护，静态预期未处理异常 | 显式 dict 检查，422 |
| 畸形 JSON | 框架请求验证路径，通常 422，精确响应待实测 | 解码捕获，400 | silent 解析得到 None，再对象检查，422 |
| PUT 缺 notes/completed | 默认值参与整对象更新，可能清空/重置 | 默认空备注/false，整对象更新 | 同左 |
| 错误响应 | detail 可为字符串或验证数组 | 自定义 error 与框架 HTML 错误可能混合 | 自定义 error；未知框架异常未统一保证 |

Django JSON 写入仍受默认 CSRF middleware 保护，表格中的 parse_body 推导以已通过 CSRF 等前置检查为条件；无令牌的正常跨站/客户端请求可能先得到 403，不能跳过中间件假装已观察业务结果。ORM create/save 不自动替代完整 ModelForm 或 full_clean 验证；页面表单比手写 JSON parser 更严格，两条路径需分别验收。

对于 completed 与 null，不要把“JSON 可解码”当合法业务类型。Python str/bool 的通用转换不是任务 schema；若规格要求真实字符串与布尔值，应先固定该契约，再在个人副本统一边界与回归。以上列出源码推导和框架预期，不是 HTTP 实测，不自动要求所有栈相同状态码。

## 4. 各栈机制与风险

### React + FastAPI

[backend/main.py](../../../../_assignments/2025%20fall/week8/stack1-bolt-react/backend/main.py)的五项 API 使用绑定 SQL，按 created_at DESC、id DESC 排序，未分页、无身份/资源归属。TaskInput 标题 1–120、备注最多 2000，初步验证后 strip 标题并拒绝全空白；额外字段默认忽略，completed 不是 StrictBool。PUT 是整对象更新，不是局部 PATCH。

connection 每次新建 sqlite3 连接，`with connection() as db`负责事务提交/回滚，**不负责 close**；当前 helper 没有显式关闭，不能把上下文退出当连接已释放，也未测量句柄或泄漏。更新前查存在、随后写、再读取跨多个连接/事务，并发删除或更新的结果未验证。lifespan 初始化只证明源码路径，不等于裸 import 创建表或已有迁移方案。

[App.jsx](../../../../_assignments/2025%20fall/week8/stack1-bolt-react/frontend/src/App.jsx)使用 VITE_API_URL（默认 localhost:8000/api），React 文本输出没有危险 HTML sink。toggle 发送展开的旧 task 全对象，额外 id/时间被忽略，但旧标题/备注仍可覆盖另一窗口的新值。没有写入锁、取消或请求代次；重复点击、旧列表覆盖和提交成功但响应丢失后的重试都需要单独验证。load 自行 catch，因此 await load 不证明刷新成功；detail 为验证数组时错误文字也未保证易懂。开发 StrictMode 行为本次未运行。

前端多数依赖写 latest、Tailwind 为 `^3.4.17`，未发现 package lock；后端直接固定 FastAPI 0.115.6/Uvicorn 0.34.0，Pydantic 传递版本未完整锁定。README 的 Node 18+/Python 3.10+不证明未来解析 latest 的兼容性或完整可复现。Vite 指定 5173 但未 strictPort，端口占用后换端口可能不符固定 CORS 的 localhost/127.0.0.1:5173 来源；CORS 不等于认证。VITE 环境变量会用于前端构建，不是秘密保险箱；部署 HTTPS 页面配 HTTP API 还需另验。

### Django 全栈

[views.py](../../../../_assignments/2025%20fall/week8/stack2-django/taskboard/views.py)用 ModelForm 完成页面创建/编辑，toggle POST-only，删除 GET 展示确认、POST 写入；四份模板含必要 POST 的 csrf_token。JSON API 没有 csrf_exempt，普通外部写客户端需合法 cookie/token/header 流程，不把 API 等同于无 CSRF 的 Flask 接口。

parse_body 59–70 行只捕获解码错误，不检查对象类型，且 str/bool 强制转换带来表格中的差异；这不是框架表单验证自动覆盖的路径。get_object_or_404 与方法/CSRF 失败可能返回 HTML，JsonResponse({},204) 的实际网络响应体未验。模型只按 `-created_at`排序，没有 ID tie 次序；Asia/Shanghai、USE_TZ 与 ISO 时间需比较时间语义，不要求与另两栈的 UTC 文本逐字符相同。

[settings.py](../../../../_assignments/2025%20fall/week8/stack2-django/taskboard_project/settings.py)有固定开发 SECRET_KEY、DEBUG=true、localhost/127.0.0.1 ALLOWED_HOSTS；Host 限制不是监听地址/网络隔离，更不是身份授权。安装 auth middleware/Admin 不让任务视图自动变成每用户私有；当前视图访问全局任务。Django 5.1.4 直接版本、Python 3.10+说明与迁移是否正常均未运行，不能把开发配置直接公开部署。

### Flask + 原生 JavaScript

[app.py](../../../../_assignments/2025%20fall/week8/stack3-flask-sqlite/app.py)通过 g 保留当前 app context 的连接，teardown 显式 close，写入显式 commit，SQL 参数绑定。124 行顶层 init_db 意味着模块 import 就可能创建/写入源码旁 tasks.db；测试前仅改请求配置太晚，需先隔离副本和导入路径。CREATE TABLE IF NOT EXISTS 不等于结构迁移。

validate 有 dict 保护但保留 str/bool 转换问题；列表无界、整对象 PUT 无版本冲突检查、无用户归属。没有显式 CSRF 机制，缺 CORS 头也不是完全 CSRF 防护证明；JSON/content-type 对某些浏览器路径的约束需要按真实请求链路检查。本页不提供真实攻击，也不将 debug 启动用于公开环境。Flask 3.1.0 固定直接版本不是完整传递依赖锁。

[static/app.js](../../../../_assignments/2025%20fall/week8/stack3-flask-sqlite/static/app.js)使用模板克隆和 textContent，提供筛选、计数、编辑、完成切换与删除确认。SQLite 时间附加 Z 按其 UTC 文本约定解释，不代表所有来源时间都可如此处理。初始计数 0 不区分尚未加载/真空，写入未锁定，load 捕获失败后仍可能留下旧状态；浏览器、移动端、键盘、完整 CSS 与失败恢复均未实测。

## 5. 公平比较与获准复现

未找到本周测试文件，React package 只有 dev/build/preview 等脚本，没有测试入口；这不证明不存在任何手工验证，但没有可据此引用的运行日志。报告的各栈速度、已完成勾选和 UI 风格不能当对照结果；需同一需求、数据、机器/平台、工具版本与验收范围，分别记录首次生成、人工修正、运行、失败和成本，不能用不同产品规模解释框架优劣。

1. 在授权的独立副本固定三个行为契约与假数据，核对各 README 的真实目录、依赖方案、端口、环境与数据初始化副作用。安装/导入/运行前隔离三个库，Django migration 与 Flask 顶层写入单独留计划。
2. 真实平台生成获准后保留 Bolt 项目/导出关联、提示迭代和手工 diff，脱敏凭据与支付信息。没有来源证据就写待核验，不用 Bolt-style 标签凑平台要求。
3. 经授权运行后逐版保留 CRUD、重启、非法输入、错误展示、重复提交/响应丢失、并发旧更新和窄屏/键盘证据。部署是独立阶段，需要关闭调试、审查身份/秘密/网络与备份；原作业不要求无条件上线。

## 6. 零执行替代与验收

教程扩展：50 分钟，零网络、平台/AI、安装、导入、测试、浏览器、构建、服务、迁移、数据库和远程写入，仅纸面假数据，不编辑原作业。

1. 10 分钟画三条 UI→验证→存储链路，标出 FastAPI lifespan、Django migrate、Flask import 的初始化时点与库路径；列出运行前隔离条件。
2. 10 分钟填原评分证据卡：三目录/语言属于源码事实，Bolt 使用与耗时属于报告自述，功能与持久化属于未运行；不得自行填分数或通过。
3. 15 分钟手算契约矩阵中的 null 标题、`"false"`、列表 JSON 和缺字段 PUT，给 Django 注明 CSRF 前置条件；拟定统一业务预期及框架适配，不发送请求。
4. 15 分钟画两条时间线：创建已提交但响应丢失后再次点击；窗口 A 改标题后窗口 B 用旧 task 切换完成。列重启、迁移、依赖锁、端口冲突、失败 UI 与窄屏验收计划及未知项。

验收为三架构图、一评分卡、一契约矩阵、两时间线及复现检查表。静态答案：Django/Flask 的 null 可变 `"None"`，字符串 false 可变 true；Django 非对象可在 `.get`失败，Flask 对象检查拒绝；所有整对象 PUT 都需审查缺字段重置与旧值覆盖。响应丢失不等于服务器没写，重试没有幂等约束可能重复；缺少版本冲突控制时旧 toggle 可覆盖新标题。写下这些预测不证明实际出现重复或丢失，也不满足三应用、Bolt 生成与功能运行的原要求。

## 7. 自测与关联

**问：三个目录加 Python 后端就完成作业了吗？** 没有；静态结构、Bolt 来源、README 可复现、功能/持久化和详细报告需分别留证据。

**问：有效 JSON 就不会造成服务器错误吗？** 不成立；JSON 可是列表/null，Django parser 的 `.get`要求对象；类型强制转换也可能改变业务含义。

**问：with sqlite3 连接退出就一定关闭了吗？** 不会，仅事务语义；React 栈 helper 未显式 close，Flask 则用 teardown 关闭，两条机制不同。

**问：await load、删除确认与漂亮截图能证明失败恢复吗？** 不能；内部 catch、交叠请求、重复提交和丢失响应仍需实际验证。CSS/HTML 存在不证明移动端或可访问性通过。

[第 09 章](../../../chapters/09-delivery-operations.md)集中讲同功能验收、持久化与失败恢复，本页解释三份具体快照；[第 07 章](../../../chapters/07-testing-review.md)提供独立预期与分层测试，[第 08 章](../../../chapters/08-security.md)连接公开部署的边界变化。复用[环境、测试与实验模板](../../../reference/templates.md)，不新增重复模板。[课堂解读](lecture-end-to-end-app.md)的 Bolt 舞伴案例不是这些 Focus Tasks 源码，也不补足本周平台生成证据。
