"""Settings for the example MCP service."""

from __future__ import annotations

from pydantic_settings import SettingsConfigDict

from mcp_shared.settings import BaseMCPSettings


class ExampleMCPSettings(BaseMCPSettings):
    """Private settings for the example MCP server."""

    model_config = SettingsConfigDict(
        env_prefix="EXAMPLE_MCP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

    server_name: str = "Example MCP"
    greeting: str = "Hello from example-mcp"
    owner: str = "platform-team"

