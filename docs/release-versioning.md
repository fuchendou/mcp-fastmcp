# 版本与发布策略

## 1. 版本原则

本仓库采用“单仓库、多包、独立版本”策略：

- 根目录工作区不发布
- 每个 MCP 服务独立维护自己的版本号
- 共享包 [`packages/mcp_shared/`](../packages/mcp_shared/) 独立维护自己的版本号

## 2. 版本语义

推荐使用 SemVer：`MAJOR.MINOR.PATCH`

- `MAJOR`：破坏性变更
- `MINOR`：向后兼容的新能力
- `PATCH`：向后兼容的修复

## 3. 标签约定

- `example-mcp-v0.1.0`
- `mcp-shared-v0.1.0`

未来新增 MCP 时，延续同样格式：

- `search-mcp-v0.1.0`
- `docs-mcp-v0.1.0`

## 4. 推荐发布流程

1. 在目标包的 [`pyproject.toml`](../pyproject.toml) 中更新版本号
2. 更新对应文档或变更记录
3. 合并到主分支
4. 打发布标签，例如 `example-mcp-v0.1.0`
5. 由 [`.github/workflows/release.yml`](../.github/workflows/release.yml) 自动执行校验与构建

## 5. 自动化基线

当前发布工作流会：

- 安装工作区依赖
- 执行 Ruff、Pyright、Pytest
- 根据 Git 标签识别目标包
- 构建该包的源码分发与 wheel
- 附加到 GitHub Release

## 6. 后续增强建议

- 为每个包维护独立 `CHANGELOG.md`
- 引入自动版本计算策略
- 增加镜像发布到容器仓库的流水线
- 为 HTTP / SSE 服务构建专用运行镜像标签

