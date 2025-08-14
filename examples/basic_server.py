"""
Basic FastMCP Server Example
Demonstrates the simplest possible MCP server with a few tools.
"""

from fastmcp import FastMCP

# Create server instance
mcp = FastMCP("Basic Example Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}! Welcome to FastMCP."

@mcp.resource("config://version")
def get_version():
    """Get the server version."""
    return "1.0.0"

@mcp.resource("info://server")
def get_server_info():
    """Get server information."""
    return {
        "name": "Basic Example Server",
        "description": "A simple FastMCP server for demonstration",
        "tools": ["add", "multiply", "greet"],
        "resources": ["config://version", "info://server"]
    }

if __name__ == "__main__":
    mcp.run()