import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    print(dir(soup))

def main():
    html = get_html('https://www.kinopoisk.ru/')
    get_data(html)

if __name__ == "__main__":
    main()