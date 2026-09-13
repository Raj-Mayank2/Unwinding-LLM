import feedparser


RSS_FEEDS = {
    "technology": "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "science": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
    "world": "https://feeds.bbci.co.uk/news/world/rss.xml",
}


def get_news(category: str = "technology", limit: int = 3):
    """Fetch recent news from RSS."""

    feed_url = RSS_FEEDS.get(category.lower())

    if not feed_url:
        return {
            "error": f"Unsupported category: {category}",
            "available_categories": list(RSS_FEEDS.keys()),
        }

    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries[:limit]:
        articles.append(
            {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "content": entry.get("summary", ""),
            }
        )

    return articles