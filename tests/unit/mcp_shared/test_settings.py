from mcp_shared.settings import BaseMCPSettings


def test_base_settings_defaults() -> None:
    settings = BaseMCPSettings()

    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.transport == "stdio"
    assert settings.host == "127.0.0.1"
    assert settings.port == 8000
    assert settings.server_path == "/mcp"


def test_base_settings_support_mcp_prefixed_environment_variables(monkeypatch) -> None:
    monkeypatch.setenv("MCP_ENVIRONMENT", "production")
    monkeypatch.setenv("MCP_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("MCP_TRANSPORT", "http")
    monkeypatch.setenv("MCP_HOST", "0.0.0.0")
    monkeypatch.setenv("MCP_PORT", "9000")
    monkeypatch.setenv("MCP_PATH", "/gateway")

    settings = BaseMCPSettings()

    assert settings.environment == "production"
    assert settings.log_level == "DEBUG"
    assert settings.transport == "http"
    assert settings.host == "0.0.0.0"
    assert settings.port == 9000
    assert settings.server_path == "/gateway"

