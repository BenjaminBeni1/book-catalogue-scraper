import requests
import sqlite3
import csv
import time 
from bs4 import BeautifulSoup

books = []

rating_map = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
    }

for page_number in range(1, 51):
    print(f"Fetching page {page_number}...")
    info = requests.get(f"https://books.toscrape.com/catalogue/page-{page_number}.html")
    info.encoding = "utf-8"
    soup = BeautifulSoup(info.text, "html.parser")
    all_books = soup.find_all("article", class_ = "product_pod")
    time.sleep(1)

    for book in all_books:
        h3 = book.find("h3")
        title_link = h3.find("a")

        price = book.find("p", class_ = "price_color")
    
        rating = book.find("p", class_ = "star-rating")
    
        availability = book.find("p", class_ = "availability")
        
        books.append({
            "title" : title_link["title"],
            "url" : title_link["href"],
            "price": float(price.get_text(strip = True)[1:]),
            "rating" : rating_map.get(rating["class"][1]),
            "availability" : availability.get_text(strip = True),
        })

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS books")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            price REAL,
            rating INTEGER,
            availability TEXT,
            url TEXT
        )
    """)

for book in books:
    cursor.execute(
        "INSERT INTO books (title, url, price, rating, availability) VALUES (?, ?, ?, ?, ?)",
        (
        book["title"],
        book["url"],
        book["price"],
        book["rating"],
        book["availability"],
         )
    )

connection.commit()
connection.close()

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "url", "price", "rating", "availability"])
    writer.writeheader()
    writer.writerows(books)




