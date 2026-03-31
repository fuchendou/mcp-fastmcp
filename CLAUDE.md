# Claude Code 协作约定

本仓库用于持续开发多个基于 FastMCP 的 MCP 服务。Claude Code 在修改本仓库时应遵守以下规则。

## 1. 总体原则

- 优先在现有分层内修改，不要随意新增平铺文件
- 共享能力放入 `packages/mcp_shared/`
- 业务能力放入对应 `apps/<mcp_name>/`
- 优先编写可测试的纯函数，再在 `server.py` 中完成 FastMCP 注册
- 所有新增 Python 代码必须兼容 Python 3.12

## 2. 新增 MCP 的标准结构

每个新 MCP 应至少包含：

- `pyproject.toml`
- `src/<mcp_name>/settings.py`
- `src/<mcp_name>/server.py`
- `src/<mcp_name>/tools.py`
- `src/<mcp_name>/resources.py`
- `src/<mcp_name>/prompts.py`
- 必要时添加该 MCP 自己的 `README.md`

## 3. 代码组织要求

- `server.py` 只负责创建 `FastMCP` 实例、装载配置、注册模块、暴露 `mcp`
- 具体业务逻辑尽量不要直接写在装饰器函数里
- 装饰器函数优先调用普通 Python 函数，保证单元测试简单
- 公共配置项优先从 `.env` 读取，并通过 `pydantic-settings` 建模

## 4. 测试与质量要求

修改后优先确保以下命令可通过：

```bash
uv run ruff check .
uv run pyright
uv run pytest
```

## 5. 目录约束

- 不要把业务测试直接塞进源代码目录，统一放在根目录 `tests/`
- 不要把某个具体 MCP 的私有常量放进 `mcp_shared`
- 不要在根目录新增临时脚本，除非它们是长期维护资产

## 6. 配置与安全

- 示例配置写入 `.env.example`
- 严禁把真实密钥提交到仓库
- 客户端示例配置统一放入 `configs/clients/`
- 服务配置基线统一放入 `configs/servers/`

