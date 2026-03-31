from fastmcp import FastMCP

from example_mcp.server import build_server, mcp
from example_mcp.settings import ExampleMCPSettings


def test_example_server_exports_mcp() -> None:
    assert isinstance(mcp, FastMCP)


def test_build_server_returns_fastmcp_instance() -> None:
    server = build_server(ExampleMCPSettings())

    assert isinstance(server, FastMCP)

