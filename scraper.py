import requests

from bs4 import BeautifulSoup

#Task 2

info = requests.get("https://books.toscrape.com")
info.encoding = "utf-8"

soup = BeautifulSoup(info.text, "html.parser")

books = []
all_books = soup.find_all("article", class_ = "product_pod")

rating_map = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
    }

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

print(len(books))

print(books)


