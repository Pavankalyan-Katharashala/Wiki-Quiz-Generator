import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0"
    })

    soup = BeautifulSoup(response.text, "html.parser")

    # SAFE title extraction
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "Unknown Title"

    paragraphs = soup.find_all("p")

    text = ""
    for p in paragraphs:
        text += p.get_text()

    summary = paragraphs[0].get_text() if paragraphs else "No summary available."

    return {
        "title": title,
        "summary": summary,
        "text": text
    }
