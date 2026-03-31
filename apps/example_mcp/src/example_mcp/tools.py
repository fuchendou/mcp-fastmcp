"""Tool registration and pure business helpers for the example MCP."""

from __future__ import annotations

from fastmcp import FastMCP

from example_mcp.settings import ExampleMCPSettings


def build_health_payload(service_name: str, settings: ExampleMCPSettings) -> dict[str, str]:
    """Return a small health payload that is easy to test and extend."""
    return {
        "service": service_name,
        "status": "ok",
        "environment": settings.environment,
        "owner": settings.owner,
    }


def register_tools(mcp: FastMCP, settings: ExampleMCPSettings) -> None:
    """Register tool endpoints on the provided FastMCP server."""

    @mcp.tool
    def service_health(service_name: str = "example-mcp") -> dict[str, str]:
        """Return a simple health report for the example MCP service."""
        return build_health_payload(service_name=service_name, settings=settings)

