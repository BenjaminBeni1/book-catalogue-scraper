import requests

from bs4 import BeautifulSoup

#Task 2

info = requests.get("https://books.toscrape.com")

# print(info.text)
# print(info.status_code)

soup = BeautifulSoup(info.text, "html.parser")

#Task 5

books= []
all_books = soup.find_all("article", class_ = "product_pod")



for book in all_books:
    h3 = book.find("h3")
    title_link = h3.find("a")

    price = book.find("p", class_ = "price_color")
  
    rating = book.find("p", class_ = "star-rating")
  
    availability = book.find("p", class_ = "availability")
    
    books.append({
        "title" : title_link["title"],
        "url" : title_link["href"],
        "price" : price.get_text(strip=True),
        "rating" : rating["class"],
        "availability" : availability.get_text(strip=True),
    })
print(len(books))


