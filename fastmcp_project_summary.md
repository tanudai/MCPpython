# FastMCP Project Summary

## Overview

**FastMCP** is a comprehensive Python framework for building Model Context Protocol (MCP) servers and clients. It's designed to be the "fast, Pythonic way" to work with MCP, providing a high-level interface that abstracts away the complex protocol details while offering production-ready features.

## What is MCP?

The Model Context Protocol (MCP) is a standardized way to provide context and tools to Large Language Models (LLMs). It's often described as "the USB-C port for AI" - a uniform way to connect LLMs to external resources and functionality. MCP enables:

- **Resources**: Read-only data sources (like GET endpoints)
- **Tools**: Executable functions (like POST endpoints) 
- **Prompts**: Reusable templates for LLM interactions

## Key Features

### Core Functionality
- **Simple Server Creation**: Create MCP servers with minimal boilerplate using decorators
- **Tool Management**: Convert Python functions into MCP tools with automatic schema generation
- **Resource Management**: Expose data sources with static and dynamic (templated) resources
- **Prompt Management**: Define reusable prompt templates
- **Context Access**: Rich context object for logging, LLM sampling, HTTP requests, and progress reporting

### Advanced Features
- **Multiple Transports**: Support for STDIO, HTTP, and SSE transports
- **Authentication & Security**: Built-in auth providers for production deployments
- **Proxy Servers**: Create intermediary servers for bridging transports or adding logic layers
- **Server Composition**: Mount multiple FastMCP instances or import servers
- **OpenAPI Integration**: Generate servers from OpenAPI specs or FastAPI applications
- **Client Library**: Comprehensive client for interacting with any MCP server
- **Testing Framework**: In-memory testing capabilities
- **Middleware System**: Extensible middleware for request/response processing

## Architecture

### Core Components

1. **FastMCP Server**: Central server class that manages tools, resources, and prompts
2. **Tool Manager**: Handles tool registration, validation, and execution
3. **Resource Manager**: Manages static and dynamic resource endpoints
4. **Prompt Manager**: Handles prompt templates and generation
5. **Client**: Full-featured client for connecting to MCP servers
6. **Context**: Rich context object providing server capabilities to tools/resources

### Project Structure
```
fastmcp/
├── src/fastmcp/
│   ├── server/          # Server implementation
│   ├── client/          # Client implementation  
│   ├── tools/           # Tool management
│   ├── resources/       # Resource management
│   ├── prompts/         # Prompt management
│   ├── utilities/       # Shared utilities
│   └── contrib/         # Community contributions
├── examples/            # Usage examples
├── tests/              # Test suite
└── docs/               # Documentation
```

## Usage Examples

### Basic Server
```python
from fastmcp import FastMCP

mcp = FastMCP("Demo Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

### Resource with Template
```python
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: int):
    return {"name": f"User {user_id}", "status": "active"}
```

### Context Usage
```python
from fastmcp import Context

@mcp.tool
async def process_data(uri: str, ctx: Context):
    await ctx.info(f"Processing {uri}...")
    data = await ctx.read_resource(uri)
    summary = await ctx.sample(f"Summarize: {data.content}")
    return summary.text
```

### Client Usage
```python
from fastmcp import Client

async with Client("my_server.py") as client:
    result = await client.call_tool("add", {"a": 5, "b": 3})
    print(result.text)
```

## Key Differentiators

1. **Pythonic Design**: Feels natural to Python developers with decorator-based APIs
2. **Production Ready**: Built-in auth, middleware, deployment tools
3. **Comprehensive**: Goes beyond basic protocol - includes clients, testing, integrations
4. **High Performance**: Optimized for speed and efficiency
5. **Extensible**: Plugin architecture with middleware and composition patterns
6. **Well Documented**: Comprehensive docs at gofastmcp.com

## Development & Community

- **Language**: Python 3.10+
- **License**: Apache 2.0
- **Maintainer**: Jeremiah Lowin (Prefect)
- **Repository**: https://github.com/jlowin/fastmcp
- **Documentation**: https://gofastmcp.com
- **Package**: Available on PyPI as `fastmcp`

## Installation

```bash
uv pip install fastmcp
# or
pip install fastmcp
```

## Evolution

FastMCP has evolved through two major versions:
- **v1.0**: Basic server building capabilities (now incorporated into official MCP SDK)
- **v2.0**: Complete ecosystem with clients, auth, deployment, testing, and production features

## Use Cases

- Building AI assistants with external tool access
- Creating API bridges for LLM integration
- Developing modular AI applications
- Prototyping LLM-powered tools
- Production AI system deployment
- Testing and development of MCP-based applications

FastMCP represents a mature, production-ready framework that significantly simplifies working with the Model Context Protocol while providing the flexibility and features needed for real-world AI applications.