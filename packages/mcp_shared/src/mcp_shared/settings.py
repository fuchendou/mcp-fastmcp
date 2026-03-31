"""Base settings shared by all MCP services."""

from __future__ import annotations

from typing import Literal

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseMCPSettings(BaseSettings):
    """Shared environment settings used by all services."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

    environment: Literal["development", "test", "production"] = Field(
        default="development",
        validation_alias=AliasChoices("MCP_ENVIRONMENT"),
    )
    log_level: str = Field(
        default="INFO",
        validation_alias=AliasChoices("MCP_LOG_LEVEL"),
    )
    transport: Literal["stdio", "http", "sse"] = Field(
        default="stdio",
        validation_alias=AliasChoices("MCP_TRANSPORT"),
    )
    host: str = Field(
        default="127.0.0.1",
        validation_alias=AliasChoices("MCP_HOST"),
    )
    port: int = Field(
        default=8000,
        validation_alias=AliasChoices("MCP_PORT"),
    )
    server_path: str = Field(
        default="/mcp",
        validation_alias=AliasChoices("MCP_PATH"),
    )

