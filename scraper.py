import requests

info = requests.get("https://books.toscrape.com")

print(info.text)
print(info.status_code)
