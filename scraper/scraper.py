from scraper.parser import parse_quotes
from scraper.auth import get_session
import csv
import os

OUTPUT_PATH = "data/output.csv"

def run():
    session = get_session()
    data = parse_quotes(session, max_pages=300)

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["quote", "author"])
        writer.writerows(data)

    print(f"Total scraped records: {len(data)}")

if __name__ == "__main__":
    run()
