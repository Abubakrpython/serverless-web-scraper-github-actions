🚀 Serverless Web Scraper with GitHub Actions
📌 Overview

This project demonstrates a serverless, automated web scraping system built with Python and GitHub Actions.
It is designed to scrape large-scale datasets (3,000+ records per run) from internal-style websites and execute daily without any server infrastructure.

The project reflects a real-world scraping workflow commonly requested by clients on platforms like Upwork.

✨ Key Features

✅ Daily automated scraping using GitHub Actions (cron jobs)

✅ Serverless architecture (no VPS, no cloud server)

✅ Pagination support for large datasets (3,000+ records)

✅ Modular Python codebase (auth, parser, runner)

✅ CSV data export

✅ Production-ready project structure

✅ Authentication-ready (simulated internal website access)

🧰 Tech Stack

Python 3.10

Requests

BeautifulSoup4

GitHub Actions

Cron scheduling

📁 Project Structure
.
├── .github/workflows/
│   └── scrape.yml        # GitHub Actions workflow
│
├── scraper/
│   ├── __init__.py
│   ├── auth.py           # Authentication/session handling
│   ├── parser.py         # Pagination scraping logic
│   └── scraper.py        # Main entry point
│
├── data/
│   └── output.csv        # Scraped data output
│
├── requirements.txt
└── README.md

⚙️ How It Works

GitHub Actions triggers the workflow daily (or manually).

A Python environment is set up automatically.

The scraper:

Initializes a session (simulating internal website access)

Iterates through paginated pages

Collects structured data

Results are saved as a CSV file.

Updated data is committed back to the repository.

📊 Data Scale & Pagination

The scraper supports hundreds of pages via pagination.

Logic is designed to handle 3,000+ records per execution.

Demo website limits the available pages, but the pagination logic is fully scalable and production-ready.

▶️ Run Locally
pip install -r requirements.txt
python -m scraper.scraper

🕒 GitHub Actions Automation

The workflow runs automatically using cron scheduling:

schedule:
  - cron: "0 6 * * *"


This ensures hands-free daily scraping without maintaining any server.

🧑‍💼 Client / Portfolio Use Case

This project is ideal for:

Internal website scraping

Scheduled data collection

Serverless automation

Upwork & freelance portfolio demonstration

Example client description:

Built a serverless Python scraping system using GitHub Actions to automatically collect large datasets on a daily schedule without any server infrastructure.

⚠️ Disclaimer

This repository uses a public demo website for demonstration purposes only.
The architecture and logic are intended to represent internal or authenticated website scraping workflows.

📬 Contact

If you’re looking for:

Automated web scraping

GitHub Actions automation

Serverless data pipelines

Feel free to reach out.
