# FastMCP 多 MCP 工作区脚手架

这是一个面向团队协作的 Python + FastMCP 工作区模板，目标是为后续持续新增多个 MCP 服务提供稳定的开发基线。

## 设计目标

- 使用 `uv` 管理工作区依赖与锁文件
- 使用单仓库承载多个 MCP 服务
- 把公共能力沉淀到共享包，降低重复代码
- 优先支持 Claude Code / Claude Desktop 的本地 `stdio` 开发
- 保留后续扩展到 HTTP / SSE / 容器化部署的空间
- 内置 Ruff、Pyright、Pytest、GitHub Actions CI

## 目录结构

```text
.
├── .dockerignore
├── .github/workflows/ci.yml
├── .github/workflows/release.yml
├── apps/
│   └── example_mcp/
│       ├── pyproject.toml
│       └── src/example_mcp/
├── configs/
│   ├── clients/
│   │   └── claude-desktop.example.json
│   └── servers/
│       └── example-mcp.fastmcp.json
├── docker/
│   └── Dockerfile
├── docker-compose.yml
├── docs/
│   ├── architecture.md
│   ├── create-new-mcp.md
│   ├── deployment.md
│   └── release-versioning.md
├── packages/
│   └── mcp_shared/
│       ├── pyproject.toml
│       └── src/mcp_shared/
├── tests/
│   ├── integration/
│   └── unit/
├── CLAUDE.md
└── pyproject.toml
```

## 快速开始

### 1. 安装依赖

```bash
uv sync --all-packages --dev
```

### 2. 运行质量检查

```bash
uv run ruff check .
uv run pyright
uv run pytest
```

### 3. 本地启动示例 MCP

```bash
uv run --package example-mcp example-mcp
```

默认使用 `stdio`，适合 Claude Code / Claude Desktop 直接对接。

### 4. 以 HTTP 启动示例 MCP

把 [`.env.example`](.env.example) 复制为 [`.env`](.env) 后，调整以下变量：

```dotenv
MCP_TRANSPORT=http
MCP_HOST=127.0.0.1
MCP_PORT=8000
MCP_PATH=/mcp
```

然后执行：

```bash
uv run --package example-mcp example-mcp
```

### 5. 使用 Docker Compose 启动

```bash
docker compose --profile http up --build
```

SSE 示例：

```bash
docker compose --profile sse up --build
```

## 核心约定

### 1. `apps/`

每个 MCP 独立放在 `apps/` 下，建议每个服务都具备自己的：

- `settings.py`：服务私有配置
- `server.py`：FastMCP 实例和注册入口
- `tools.py`：工具定义与注册
- `resources.py`：资源定义与注册
- `prompts.py`：提示模板定义与注册

### 2. `packages/mcp_shared/`

只放跨 MCP 复用的能力，例如：

- 通用环境配置
- 日志初始化
- 错误类型
- 通用数据模型
- 认证 / 追踪 / 监控扩展点

不要把某个 MCP 的业务逻辑放进共享包。

### 3. `configs/`

- `configs/clients/`：放 Claude Desktop / 客户端示例配置
- `configs/servers/`：放 FastMCP 服务配置、部署基线样例

### 5. `docker/`

- 放统一容器镜像构建资产
- 通过构建参数切换目标 MCP 包
- 与 `docker-compose.yml` 配合，支持本地 HTTP / SSE 演练

### 4. `tests/`

统一放在仓库根目录，方便按层级做测试治理：

- `tests/unit/`：纯函数、配置、轻量模块测试
- `tests/integration/`：服务装配、入口、跨模块集成测试

## 适合 Claude Code 的原因

- 模块边界清晰，便于 AI 在局部上下文中稳定修改
- 共享代码与业务代码分离，降低误改范围
- 每个 MCP 的入口统一，后续复制模板更快
- `CLAUDE.md` 为后续自动化协作提供明确规则

## 可行性评估

这套结构对“后续会持续新增多个 MCP”的场景是高可行的：

- **优点**：规范统一、扩展稳定、便于 CI、适合多人协作
- **成本**：初期目录会显得更重，但能显著减少后期重构成本
- **结论**：适合作为长期演进的团队基线，而不是一次性 demo 项目

## 下一步建议

1. 先基于 `apps/example_mcp/` 再复制出第一个真实业务 MCP
2. 把团队通用中间件逐步沉淀进 `packages/mcp_shared/`
3. 当新增第二个 MCP 后，开始为每个服务配置独立发布标签与容器镜像策略

## 部署与发布补充

- 容器与 HTTP / SSE 部署说明见 [`docs/deployment.md`](docs/deployment.md)
- 版本与发布策略见 [`docs/release-versioning.md`](docs/release-versioning.md)
- 发布自动化基线见 [`.github/workflows/release.yml`](.github/workflows/release.yml)

