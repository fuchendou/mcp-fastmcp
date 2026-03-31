# 部署说明

本仓库当前提供三类运行方式：`stdio`、HTTP、SSE。

## 1. 本地 `stdio`

适合 Claude Code / Claude Desktop。

```bash
uv run --package example-mcp example-mcp
```

## 2. 本地 HTTP

在 [`.env`](../.env.example) 中设置：

```dotenv
MCP_TRANSPORT=http
MCP_HOST=0.0.0.0
MCP_PORT=8000
MCP_PATH=/mcp
```

然后运行：

```bash
uv run --package example-mcp example-mcp
```

## 3. 本地 SSE

在 [`.env`](../.env.example) 中设置：

```dotenv
MCP_TRANSPORT=sse
MCP_HOST=0.0.0.0
MCP_PORT=8001
MCP_PATH=/sse
```

然后运行：

```bash
uv run --package example-mcp example-mcp
```

## 4. Docker 镜像构建

使用统一镜像模板 [`docker/Dockerfile`](../docker/Dockerfile)：

```bash
docker build -f docker/Dockerfile -t example-mcp \
  --build-arg MCP_PACKAGE=example-mcp \
  --build-arg MCP_ENTRYPOINT=example-mcp \
  .
```

## 5. Docker Compose

### HTTP

```bash
docker compose --profile http up --build
```

### SSE

```bash
docker compose --profile sse up --build
```

## 6. FastMCP 服务配置样例

- `stdio`：[`configs/servers/example-mcp.fastmcp.json`](../configs/servers/example-mcp.fastmcp.json)
- HTTP：[`configs/servers/example-mcp.http.fastmcp.json`](../configs/servers/example-mcp.http.fastmcp.json)
- SSE：[`configs/servers/example-mcp.sse.fastmcp.json`](../configs/servers/example-mcp.sse.fastmcp.json)

## 7. 推荐部署策略

- 开发阶段：默认 `stdio`
- 集成环境：优先 HTTP
- 需要特定客户端兼容时：启用 SSE
- 保持同一套业务代码，通过环境变量切换传输层

