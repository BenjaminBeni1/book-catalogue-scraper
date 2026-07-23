# Task breakdown

## Setup
- [x] 1. Environment setup. Create venv, install requests + beautifulsoup4, generated requirements.txt.

## Fetching
- [x] 2. Fetch page 1 and print the raw HTML. Use requests to get the first page of the catalogue and check the status code is 200.

## Understanding the page
- [x] 3. map where the 5 fields live. Open the books to scrape website in your browser, inspect a book and write down the tag/class that holds the title, price, rating, availability and URL.

## Parsing
- [ ] 4. Extract the five fields for one book and print them with BeautifulSoup using the selectors noted in task 3.

- [ ] 5. Extract all books on page 1, similar to task 4 but now inside a loop to loop over each book on the page. Should end with a list of around 20 dictionaries.

- [ ] 6. Clean the data during extraction. Remove symbols like "£" and convert the value into availability float. Rating: convert the word "three" into an int "3".

## Pagination
- [ ] 7. Loop over all 50 pages. Figure out how the URL's change. Collect every page's books into one list which should be approximately 1,000.

## Storage
- [ ] 8. Using SQLite. Create a database, table and insert everything via code that will make these. View and verify with DB Browser that the count is around 1,000.

- [ ] 9. Write the same list via Python's built-in csv module.

## Politeness & resilience
- [ ] 10. Delay between requests. This can be done via time.sleep.

- [ ] 11. Retries + skip-and-log. Wrap the fetch so a failure retries up to 3 times. If it continues to fail log which page broke and continue instead of crashing.

## End
- [ ] 12. Complete the README. Install instructions, run instructions with an example command and sample the output. Tick all 5 original deliverables boxes.
