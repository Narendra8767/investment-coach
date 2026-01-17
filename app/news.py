import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_market_news():
    params = {
        "category": "business",
        "language": "en",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    articles = response.json().get("articles", [])

    if not articles:
        return "No recent market news available."

    news_text = []
    for a in articles:
        title = a.get("title", "")
        desc = a.get("description", "")
        source = a.get("source", {}).get("name", "")

        news_text.append(f"- {title} ({source})\n  {desc}")

    return "\n".join(news_text)
