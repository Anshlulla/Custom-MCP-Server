from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math-server")

@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y

@mcp.tool()
def multiply(x: int, y: int) -> int:
    """Multiply two integers."""
    return x * y

if __name__ == "__main__":
    mcp.run(transport="stdio")
    