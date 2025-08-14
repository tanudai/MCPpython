"""
FastMCP Client Example
Demonstrates how to connect to and interact with an MCP server.
"""

import asyncio
from fastmcp import Client

async def main():
    # Connect to a server via stdio (running a Python script)
    async with Client("basic_server.py") as client:
        print("Connected to server!")
        
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")
        
        # Call some tools
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"5 + 3 = {result.text}")
        
        result = await client.call_tool("multiply", {"a": 4.5, "b": 2.0})
        print(f"4.5 * 2.0 = {result.text}")
        
        result = await client.call_tool("greet", {"name": "FastMCP User"})
        print(f"Greeting: {result.text}")
        
        # Read resources
        resources = await client.list_resources()
        print(f"Available resources: {[r.uri for r in resources]}")
        
        version = await client.read_resource("config://version")
        print(f"Server version: {version.text}")
        
        info = await client.read_resource("info://server")
        print(f"Server info: {info.text}")

if __name__ == "__main__":
    asyncio.run(main())