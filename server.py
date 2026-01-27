import os
import requests
from fastmcp import FastMCP

mcp = FastMCP("news")

@mcp.tool()
def search_news(query: str, limit: int = 5) -> str:
    """Search news articles"""
    api_key = os.getenv("NEWS_API_KEY")
    response = requests.get(
        "https://api.thenewsapi.com/v1/news/all",
        params={"api_token": api_key, "search": query, "limit": limit}
    )
    return str(response.json())

@mcp.tool()
def top_news(locale: str = "us", limit: int = 5) -> str:
    """Get top news"""
    api_key = os.getenv("NEWS_API_KEY")
    response = requests.get(
        "https://api.thenewsapi.com/v1/news/top",
        params={"api_token": api_key, "locale": locale, "limit": limit}
    )
    return str(response.json())

# THIS IS REQUIRED - runs the HTTP server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
