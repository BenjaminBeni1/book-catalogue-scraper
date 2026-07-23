import requests

from bs4 import BeautifulSoup

#Task 2

info = requests.get("https://books.toscrape.com")

# print(info.text)
# print(info.status_code)


#Task 4

soup = BeautifulSoup(info.text, "html.parser")
book = soup.find("article", class_ = "product_pod")


h3 = book.find("h3")
title_link = h3.find("a")
print("title:", title_link["title"])
print("url:", title_link["href"])

price = book.find("p", class_ = "price_color")
print("price:", price.get_text(strip=True))

rating = book.find("p", class_ = "star-rating")
print("rating:", rating["class"])

availability = book.find("p", class_ = "availability")
print("availability:", availability.get_text(strip=True))


# print(soup)
# print(book)

