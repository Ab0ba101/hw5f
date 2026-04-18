import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

all_titles = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("h3")
    for book in books:
        title = book.find("a")["title"]
        all_titles.append(title)

for i, title in enumerate(all_titles, 1):
    print(f"{i}. {title}")
