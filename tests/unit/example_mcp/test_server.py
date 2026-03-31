from example_mcp.server import build_run_kwargs
from example_mcp.settings import ExampleMCPSettings


def test_build_run_kwargs_for_stdio() -> None:
    settings = ExampleMCPSettings(transport="stdio", log_level="INFO")

    kwargs = build_run_kwargs(settings)

    assert kwargs == {
        "transport": "stdio",
        "log_level": "INFO",
    }


def test_build_run_kwargs_for_http() -> None:
    settings = ExampleMCPSettings(
        transport="http",
        host="0.0.0.0",
        port=9000,
        server_path="/mcp",
        log_level="DEBUG",
    )

    kwargs = build_run_kwargs(settings)

    assert kwargs == {
        "transport": "http",
        "log_level": "DEBUG",
        "host": "0.0.0.0",
        "port": 9000,
        "path": "/mcp",
    }
