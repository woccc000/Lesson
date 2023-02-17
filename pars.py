import requests
from bs4 import BeautifulSoup

URL = 'https://aliexpress.ru/category/202000001/food.html?g=y&page=9&spm=a2g2w.home.category.1.7d1f52'

url = requests.get(URL)

bs = BeautifulSoup(url.text, 'html.parser')

all_links = bs.find_all("div",class_="product-snippet_ProductSnippet__description__1ettdy")
all_names = bs.find_all("div", class_="product-snippet_ProductSnippet__name__1ettdy")


a = 0
for link in all_links:
    a+=1
    print(a, ")","https://aliexpress.ru" + link.a["href"])

    
b = 0
for name in all_names:
    b += 1
    print(b, ")",name.text)
