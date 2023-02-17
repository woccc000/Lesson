from bs4 import BeautifulSoup


soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.title.p 
soup.title.p['class']
soup.a 
soup.find_all('a')
soup.find(id="link3")

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

