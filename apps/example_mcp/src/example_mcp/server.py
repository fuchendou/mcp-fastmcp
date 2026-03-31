"""FastMCP server assembly for the example application."""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from example_mcp.prompts import register_prompts
from example_mcp.resources import register_resources
from example_mcp.settings import ExampleMCPSettings
from example_mcp.tools import register_tools
from mcp_shared.logging import configure_logging


def build_server(settings: ExampleMCPSettings | None = None) -> FastMCP:
    """Build and configure the FastMCP server instance."""
    resolved_settings = settings or ExampleMCPSettings()
    configure_logging(resolved_settings.log_level)

    server = FastMCP(name=resolved_settings.server_name)
    register_tools(server, resolved_settings)
    register_resources(server, resolved_settings)
    register_prompts(server, resolved_settings)
    return server


def build_run_kwargs(settings: ExampleMCPSettings) -> dict[str, Any]:
    """Build transport-specific runtime kwargs for the FastMCP server."""
    kwargs: dict[str, Any] = {
        "transport": settings.transport,
        "log_level": settings.log_level,
    }

    if settings.transport != "stdio":
        kwargs.update(
            {
                "host": settings.host,
                "port": settings.port,
                "path": settings.server_path,
            }
        )

    return kwargs


mcp = build_server()


def main() -> None:
    """Run the example MCP using the transport configured via environment."""
    settings = ExampleMCPSettings()
    server = build_server(settings)
    server.run(**build_run_kwargs(settings))


if __name__ == "__main__":
    main()

