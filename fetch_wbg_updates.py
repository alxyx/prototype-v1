import feedparser
from datetime import datetime

rss_feeds = [
    "https://www.eetasia.com/feed/",
    "https://www.semiconductor-digest.com/feed/",
    "https://www.techinasia.com/feed/",
    "https://www.eetasia.com/tag/wide-bandgap/feed/",
]

keywords = ["wide bandgap", "SiC", "GaN", "semiconductor", "power electronics", "ultrawide bandgap"]

articles = []
for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        link = entry.get("link", "")
        published = entry.get("published", "")
        if any(keyword.lower() in (title + summary).lower() for keyword in keywords):
            articles.append({
                "title": title,
                "summary": summary,
                "link": link,
                "published": published
            })

def parse_date(article):
    try:
        return datetime.strptime(article["published"], "%a, %d %b %Y %H:%M:%S %Z")
    except:
        return datetime.min

articles.sort(key=parse_date, reverse=True)

with open("updates/WBG_APAC.md", "w", encoding="utf-8") as f:
    f.write("# 🌏 Wide Bandgap Semiconductor Updates - APAC Region\n\n")
    f.write(f"_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_\n\n")
    for article in articles:
        f.write(f"## [{article['title']}]({article['link']})\n")
        f.write(f"**Published:** {article['published']}\n\n")
        f.write(f"{article['summary']}\n\n")
        f.write("---\n\n")
