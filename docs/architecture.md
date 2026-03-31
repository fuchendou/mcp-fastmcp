# 架构说明

## 为什么使用单仓库多 MCP

当团队需要维护多个 MCP 服务时，单仓库更容易实现：

- 统一 lint / typing / test 规则
- 统一依赖升级
- 统一共享模块治理
- 统一客户端配置示例和 CI 策略

## 工作区设计

### 根工作区

根目录通过 `uv workspace` 管理所有子包：

- `apps/*`：每个业务 MCP
- `packages/*`：共享包

根目录不作为可发布包，只负责：

- 开发工具配置
- 工作区组织
- 团队文档
- CI 配置

## 单个 MCP 的建议边界

### `settings.py`

负责该 MCP 私有配置，避免不同 MCP 的环境变量相互污染。

### `tools.py`

承载工具注册逻辑与可测试的业务函数。

### `resources.py`

承载资源读取接口，例如运行信息、配置快照、只读元数据。

### `prompts.py`

承载复用提示模板，尤其适合团队把操作规范沉淀为 prompt。

### `server.py`

负责：

- 加载设置
- 初始化日志
- 创建 `FastMCP`
- 注册 tools / resources / prompts
- 暴露统一的 `mcp` 对象

## 共享包边界

`mcp_shared` 只做跨服务复用能力：

- 基础配置模型
- 通用日志
- 通用错误
- 共享 schema / model

如果某段代码只被一个 MCP 使用，就不要提前抽到共享层。

## 演进路径

### 当前阶段

- 本地 `stdio` 开发优先
- Claude Code / Claude Desktop 接入优先
- 测试与类型系统先打稳基础
- Docker 作为本地与部署环境对齐手段

### 下一阶段

- 增加第 2、3 个 MCP 服务
- 引入更明确的版本管理策略
- 为每个 MCP 建立独立发布标签
- 在容器环境中补齐 HTTP / SSE 部署配置

## 部署分层建议

### `stdio`

适合 Claude Code、Claude Desktop、本地联调。

### `http`

适合内部服务化接入、网关代理、容器部署。

### `sse`

适合需要基于 SSE 方式对接 MCP 的客户端或网关场景。

建议保持统一入口：同一个 [`server.py`](../apps/example_mcp/src/example_mcp/server.py) 通过环境变量切换传输层，而不是为不同传输层分叉多套业务实现。

