"""Resource registration for the example MCP."""

from __future__ import annotations

from fastmcp import FastMCP

from example_mcp.settings import ExampleMCPSettings


def register_resources(mcp: FastMCP, settings: ExampleMCPSettings) -> None:
    """Register read-only resources on the provided FastMCP server."""

    @mcp.resource("example://config")
    def config_resource() -> dict[str, str]:
        """Expose non-sensitive configuration metadata for the server."""
        return {
            "server_name": settings.server_name,
            "environment": settings.environment,
            "owner": settings.owner,
        }

