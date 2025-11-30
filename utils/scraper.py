# utils/scraper.py
import requests
from bs4 import BeautifulSoup

class GoogleScraper:
    def search(self, query: str):
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}

        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")

        results = [p.get_text() for p in soup.find_all("span")][:5]
        return results
