# morning_call.py
from mcp.server.fastmcp import FastMCP
import sys
import logging

logger = logging.getLogger('Goodmorning')

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

# Create an MCP server
mcp = FastMCP("Goodmorning")

# Add a morning call tool
@mcp.tool()
def goodmorning() -> dict:
    """A simple Good Morning greeting tool that returns (Good morning in Chinese)."""
    greeting = "hihihi"
    logger.info(f"Goodmorning executed, returning: {greeting}")
    return {"success": True, "result": greeting}

# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
