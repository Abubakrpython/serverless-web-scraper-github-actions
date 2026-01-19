from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"

def parse_quotes(session, max_pages=300):
    page = 1
    results = []

    while True:
        url = f"{BASE_URL}/page/{page}/"
        print(f"Scraping page {page}")

        response = session.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.select(".quote")

        if not quotes:
            break

        for q in quotes:
            text = q.select_one(".text").get_text(strip=True)
            author = q.select_one(".author").get_text(strip=True)
            results.append([text, author])

        # Pagination limit (portfolio safety)
        if page >= max_pages:
            break

        page += 1

    return results
