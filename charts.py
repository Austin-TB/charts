from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

CHART_BASE = "https://quickchart.io/chart"

async def get_chart(url: str) -> dict[str, Any] | None:
    """Make a request to quickchart.io with proper error handling."""