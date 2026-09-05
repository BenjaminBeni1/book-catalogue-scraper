# Book Catalogue Scraper

Scrapes the full catalogue of [books.toscrape.com](https://books.toscrape.com) into a SQLite database. A portfolio project focused on writing a polite, resilient scraper with clean data handling.

## Deliverables (v1)

- [x] Scrapes all 50 catalogue pages (~1,000 books), following pagination automatically
- [x] Extracts five fields per book: title, price, star rating, availability, product URL
- [x] Saves results to a SQLite database, with an optional CSV export
- [x] Polite and resilient: delays between requests, retries on failure, logs and skips bad pages instead of crashing
- [x] This README, updated with install/run instructions and sample output once the scraper works

## Installation

```
git clone https://github.com/BenjaminBeni1/book-catalogue-scraper.git
cd book-catalogue-scraper
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the scraper from the terminal:

```
python scraper.py
```

This fetches all 50 pages (~1 minute with the added delay), then creates `books.db` (SQLite) and `books.csv` in the project folder.

## Sample output

### SQLite

The stored data is fully queryable:

```sql
SELECT AVG(price) FROM books;
-- 35.07
```

### CSV

```csv
title,url,price,rating,availability
A Light in the Attic,a-light-in-the-attic_1000/index.html,51.77,3,In stock
Tipping the Velvet,tipping-the-velvet_999/index.html,53.74,1,In stock
Soumission,soumission_998/index.html,50.1,1,In stock
Sharp Objects,sharp-objects_997/index.html,47.82,4,In stock
Sapiens: A Brief History of Humankind,sapiens-a-brief-history-of-humankind_996/index.html,54.23,5,In stock
```

## Tech / Notes

**Built with:** Python, requests, BeautifulSoup, SQLite.

**Notes:** Uses parameterised SQL queries to safely handle values like titles containing apostrophes. Fetches are wrapped in retry logic (3 attempts), and failed pages are logged and skipped rather than crashing the run. Prices and ratings are cleaned to numeric types on the way in, so the stored data is queryable.

## v2 ideas (not now)

- Scrape each book's product page for descriptions
- Tests with pytest
- CLI options (page limit, output path)
- Data visualisation / summary stats

## Status

Finished — built July–August 2026.