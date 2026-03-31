"""Prompt registration for the example MCP."""

from __future__ import annotations

from fastmcp import FastMCP

from example_mcp.settings import ExampleMCPSettings


def register_prompts(mcp: FastMCP, settings: ExampleMCPSettings) -> None:
    """Register reusable prompt templates on the provided FastMCP server."""

    @mcp.prompt(name="example_team_prompt")
    def example_team_prompt(task: str) -> str:
        """Return a reusable task prompt aligned with team conventions."""
        return (
            f"{settings.greeting}\n"
            f"Owner: {settings.owner}\n"
            f"Environment: {settings.environment}\n"
            f"Task: {task}"
        )

