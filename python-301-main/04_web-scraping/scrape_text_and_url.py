import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Aircraft'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# to get the url's :
links = soup.find_all('a')
for link in links:  
    print(link.get('href'))

# to print ALL tekst :
#print(soup.get_text())

#print hoofdtekst
cont = soup.find_all('p') # 'p' looks for <p> in html code (p refers to paragraph?)
for c in cont:
    print(c.text)