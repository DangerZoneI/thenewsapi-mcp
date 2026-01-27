import os
import requests
from typing import Optional
from fastmcp import FastMCP

mcp = FastMCP("TheNewsAPI")

BASE_URL = "https://api.thenewsapi.com/v1/news"

def get_api_key():
    """Get API key from environment"""
    return os.getenv("NEWS_API_KEY")

@mcp.tool()
def search_all_news(
    search: str,
    language: Optional[str] = None,
    published_after: Optional[str] = None,
    published_before: Optional[str] = None,
    categories: Optional[str] = None,
    source_ids: Optional[str] = None,
    domains: Optional[str] = None,
    exclude_domains: Optional[str] = None,
    locale: Optional[str] = None,
    limit: int = 10,
    page: int = 1,
    sort: str = "published_at"
) -> str:
    """
    Search all historical and live news articles.
    
    Args:
        search: Keywords to search for
        language: Language code (en, es, fr, de, it, pt, etc.)
        published_after: Date in YYYY-MM-DD format
        published_before: Date in YYYY-MM-DD format
        categories: Comma-separated (tech,business,sports,science,health,entertainment,general)
        source_ids: Comma-separated source IDs
        domains: Comma-separated domains to include
        exclude_domains: Comma-separated domains to exclude
        locale: Country code (us, gb, ca, au, etc.)
        limit: Number of results (1-100)
        page: Page number for pagination
        sort: Sort order (published_at, relevance)
    """
    params = {
        "api_token": get_api_key(),
        "search": search,
        "limit": min(limit, 100),
        "page": page,
        "sort": sort
    }
    
    if language:
        params["language"] = language
    if published_after:
        params["published_after"] = published_after
    if published_before:
        params["published_before"] = published_before
    if categories:
        params["categories"] = categories
    if source_ids:
        params["source_ids"] = source_ids
    if domains:
        params["domains"] = domains
    if exclude_domains:
        params["exclude_domains"] = exclude_domains
    if locale:
        params["locale"] = locale
    
    response = requests.get(f"{BASE_URL}/all", params=params, timeout=15)
    return str(response.json())

@mcp.tool()
def get_top_news(
    locale: Optional[str] = None,
    language: Optional[str] = None,
    categories: Optional[str] = None,
    source_ids: Optional[str] = None,
    domains: Optional[str] = None,
    exclude_domains: Optional[str] = None,
    published_after: Optional[str] = None,
    published_before: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 10,
    page: int = 1
) -> str:
    """
    Get top and breaking news stories.
    
    Args:
        locale: Country code (us, gb, ca, au, de, fr, etc.)
        language: Language code (en, es, fr, de, it, pt, etc.)
        categories: Comma-separated categories
        source_ids: Comma-separated source IDs
        domains: Comma-separated domains to include
        exclude_domains: Comma-separated domains to exclude
        published_after: Date in YYYY-MM-DD format
        published_before: Date in YYYY-MM-DD format
        search: Optional search keywords
        limit: Number of results (1-100)
        page: Page number
    """
    params = {
        "api_token": get_api_key(),
        "limit": min(limit, 100),
        "page": page
    }
    
    if locale:
        params["locale"] = locale
    if language:
        params["language"] = language
    if categories:
        params["categories"] = categories
    if source_ids:
        params["source_ids"] = source_ids
    if domains:
        params["domains"] = domains
    if exclude_domains:
        params["exclude_domains"] = exclude_domains
    if published_after:
        params["published_after"] = published_after
    if published_before:
        params["published_before"] = published_before
    if search:
        params["search"] = search
    
    response = requests.get(f"{BASE_URL}/top", params=params, timeout=15)
    return str(response.json())

@mcp.tool()
def get_headlines(
    locale: str = "us",
    language: str = "en"
) -> str:
    """
    Get latest headlines organized by category (Google News style).
    
    Args:
        locale: Country code (us, gb, ca, au, etc.)
        language: Language code (en, es, fr, de, etc.)
    """
    params = {
        "api_token": get_api_key(),
        "locale": locale,
        "language": language
    }
    
    response = requests.get(f"{BASE_URL}/headlines", params=params, timeout=15)
    return str(response.json())

@mcp.tool()
def get_similar_articles(
    uuid: str,
    limit: int = 10,
    page: int = 1,
    published_after: Optional[str] = None,
    published_before: Optional[str] = None,
    language: Optional[str] = None
) -> str:
    """
    Find articles similar to a specific article.
    
    Args:
        uuid: The UUID of the article to find similar articles for
        limit: Number of results (1-100)
        page: Page number
        published_after: Date in YYYY-MM-DD format
        published_before: Date in YYYY-MM-DD format
        language: Language code
    """
    params = {
        "api_token": get_api_key(),
        "limit": min(limit, 100),
        "page": page
    }
    
    if published_after:
        params["published_after"] = published_after
    if published_before:
        params["published_before"] = published_before
    if language:
        params["language"] = language
    
    response = requests.get(f"{BASE_URL}/similar/{uuid}", params=params, timeout=15)
    return str(response.json())

@mcp.tool()
def get_sources(
    locale: Optional[str] = None,
    language: Optional[str] = None,
    category: Optional[str] = None
) -> str:
    """
    Get available news sources.
    
    Args:
        locale: Filter by country code
        language: Filter by language code
        category: Filter by category (tech, business, sports, etc.)
    """
    params = {"api_token": get_api_key()}
    
    if locale:
        params["locale"] = locale
    if language:
        params["language"] = language
    if category:
        params["category"] = category
    
    response = requests.get(f"{BASE_URL}/sources", params=params, timeout=15)
    return str(response.json())

@mcp.tool()
def get_categories() -> str:
    """Get list of available news categories"""
    return str({
        "categories": [
            "general",
            "business",
            "tech",
            "science",
            "sports",
            "health",
            "entertainment"
        ]
    })

@mcp.tool()
def get_locales() -> str:
    """Get list of supported country/locale codes"""
    return str({
        "locales": [
            "us", "gb", "ca", "au", "nz", "ie",  # English
            "de", "at", "ch",  # German
            "fr", "be",  # French
            "es", "mx", "ar",  # Spanish
            "it",  # Italian
            "nl",  # Dutch
            "pt", "br",  # Portuguese
            "ru",  # Russian
            "jp", "cn", "kr", "in"  # Asia
        ]
    })

@mcp.tool()
def get_languages() -> str:
    """Get list of supported language codes"""
    return str({
        "languages": [
            "en", "es", "fr", "de", "it", "pt", "nl", "ru",
            "ar", "zh", "ja", "ko", "hi", "sv", "no", "da"
        ]
    })

if __name__ == "__main__":
    # Railway sets PORT environment variable
    port = int(os.getenv("PORT", 8000))
    
    # CRITICAL: Must bind to 0.0.0.0 for Railway, not 127.0.0.1
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port
    )
