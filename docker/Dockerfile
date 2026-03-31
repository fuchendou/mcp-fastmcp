FROM python:3.12-slim

ARG UV_VERSION=0.8.15
ARG MCP_PACKAGE=example-mcp
ARG MCP_ENTRYPOINT=example-mcp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MCP_PACKAGE=${MCP_PACKAGE}
ENV MCP_ENTRYPOINT=${MCP_ENTRYPOINT}

WORKDIR /workspace

RUN pip install --no-cache-dir "uv==${UV_VERSION}"

COPY pyproject.toml .python-version README.md CLAUDE.md ./
COPY apps ./apps
COPY packages ./packages
COPY configs ./configs
COPY docs ./docs

RUN uv sync --all-packages --no-dev

EXPOSE 8000

CMD ["sh", "-c", "uv run --package ${MCP_PACKAGE} ${MCP_ENTRYPOINT}"]
