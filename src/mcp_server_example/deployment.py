from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(x: int, y: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return x + y