from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import urllib.request
import json

def get_h2s(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req, timeout=10).read()
        soup = BeautifulSoup(html, 'html.parser')
        return [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
    except Exception as e:
        return [f"Error: {e}"]

results = []
try:
    with DDGS() as ddgs:
        for r in ddgs.text("実家 古いカメラ 買取", max_results=5):
            url = r['href']
            h2s = get_h2s(url)
            results.append({"title": r['title'], "url": url, "h2s": h2s})
except Exception as e:
    print(f"Search error: {e}")

print(json.dumps(results, indent=2, ensure_ascii=False))
