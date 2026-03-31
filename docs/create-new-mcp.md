# 新增 MCP 操作指南

## 推荐步骤

1. 复制 `apps/example_mcp/` 为新的目录，例如 `apps/search_mcp/`
2. 将包名与导入路径统一替换为新名称
3. 修改该 MCP 的 `pyproject.toml`
4. 新建对应测试目录，例如 `tests/unit/search_mcp/`
5. 在 `.env.example` 中补充该 MCP 的环境变量示例
6. 在 `configs/clients/` 中增加客户端连接示例
7. 在 `configs/servers/` 中增加该 MCP 的 `stdio`、HTTP 或 SSE 配置文件
8. 如需容器化运行，为该服务补充对应的 Compose 覆盖或镜像参数说明

## 命名建议

- 目录名：`snake_case`，例如 `search_mcp`
- Python 导入包：`snake_case`
- 分发包名：`kebab-case`，例如 `search-mcp`
- 环境变量前缀：全大写，例如 `SEARCH_MCP_`
- 发布标签：`search-mcp-v0.1.0`

## 何时放入共享包

满足以下至少两条时再考虑抽到 `mcp_shared`：

- 被两个以上 MCP 使用
- 逻辑与业务无关
- 单独测试价值明显
- 后续会持续演化

