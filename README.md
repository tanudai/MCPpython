# MCPpython - Complete FastMCP Project & Analysis

This repository contains the complete FastMCP project along with comprehensive analysis and learning materials.

## About This Repository

This is a complete copy of the FastMCP project with additional analysis and examples for learning purposes. FastMCP is a comprehensive Python framework for building Model Context Protocol (MCP) servers and clients.

### What's Included

🔥 **Complete FastMCP Source Code**
- Full source code from https://github.com/jlowin/fastmcp
- All original examples and documentation
- Complete test suite and build configuration

📚 **Learning Materials & Analysis**
- `fastmcp_project_summary.md` - Comprehensive project analysis
- `analysis/` - Technical architecture notes and insights
- Custom examples demonstrating key concepts

## Quick Start

### Installation
```bash
pip install fastmcp
# or with uv
uv pip install fastmcp
```

### Basic Example
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

## What is FastMCP?

FastMCP is the "fast, Pythonic way to build MCP servers and clients." The Model Context Protocol (MCP) is a standardized way to provide context and tools to Large Language Models - often described as "the USB-C port for AI."

### Key Features
- 🚀 **Fast**: High-level interface with minimal boilerplate
- 🍀 **Simple**: Decorator-based API for tools, resources, and prompts  
- 🐍 **Pythonic**: Natural Python development experience
- 🔍 **Complete**: Full ecosystem from development to production

## Repository Structure

```
MCPpython/
├── README.md                    # This file
├── fastmcp_project_summary.md   # Comprehensive analysis
├── analysis/                    # Technical notes
├── src/fastmcp/                # Complete FastMCP source code
├── examples/                   # All original examples + custom ones
├── tests/                      # Complete test suite
├── docs/                       # Full documentation
└── ...                         # All other FastMCP files
```

## Original Project

- **Original Repository**: https://github.com/jlowin/fastmcp
- **Documentation**: https://gofastmcp.com
- **Author**: Jeremiah Lowin (Prefect)
- **License**: Apache 2.0

## Learning Resources

1. **Start Here**: Read `fastmcp_project_summary.md` for a comprehensive overview
2. **Architecture**: Check `analysis/architecture_notes.md` for technical insights
3. **Examples**: Explore the `examples/` directory for practical implementations
4. **Documentation**: Visit https://gofastmcp.com for complete docs

## Running Examples

```bash
# Run a basic server
python examples/simple_echo.py

# Run with client
python examples/client_example.py
```

## Development

This repository includes the complete FastMCP development environment:

```bash
# Install dependencies
uv sync

# Run tests
pytest

# Run static checks
pre-commit run --all-files
```

## Contributing

This is a learning repository. Feel free to:
- Add your own analysis and examples
- Document interesting patterns you discover
- Share insights about MCP and FastMCP usage
- Create additional learning materials

## License

- **This repository**: MIT License (for analysis and custom content)
- **FastMCP source code**: Apache 2.0 License (original project license)

---

*This repository is for educational purposes and contains the complete FastMCP project for learning and development.*