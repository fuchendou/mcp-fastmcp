from example_mcp.settings import ExampleMCPSettings
from example_mcp.tools import build_health_payload


def test_build_health_payload_uses_settings_defaults() -> None:
    settings = ExampleMCPSettings()

    payload = build_health_payload(service_name="example-mcp", settings=settings)

    assert payload["service"] == "example-mcp"
    assert payload["status"] == "ok"
    assert payload["environment"] == "development"
    assert payload["owner"] == "platform-team"

