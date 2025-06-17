from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
async def get_weather() -> str:
    """Ger the current weather for a given city."""
    return "Mumbai has a rainy weather today."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")