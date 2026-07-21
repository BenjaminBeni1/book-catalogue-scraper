# Book Catalogue Scraper


Scrapes the full catalogue of [books.toscrape.com](https://books.toscrape.com) into a SQLite database. A portfolio project focused on writing a polite, resilient scraper with clean data handling.

## Deliverables (v1)

- [ ] Scrapes all 50 catalogue pages (~1,000 books), following pagination automatically
- [ ] Extracts five fields per book: title, price, star rating, availability, product URL
- [ ] Saves results to a SQLite database, with an optional CSV export
- [ ] Polite and resilient: delays between requests, retries on failure, logs and skips bad pages instead of crashing
- [ ] This README, updated with install/run instructions and sample output once the scraper works

## v2 ideas (not now)

- Scrape each book's product page for descriptions
- Tests with pytest
- CLI options (page limit, output path)
- Data visualisation / summary stats

## Status

In progress — started July 2026.
