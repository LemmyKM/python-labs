# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import requests
from pprint import pprint
from bs4 import BeautifulSoup
import webbrowser

URL = "https://en.wikipedia.org/wiki/Web_scraping"  # url al aanwezig
headers= {'User-Agent':'Mozilla/5.0'}
response = requests.get(URL)
soup = BeautifulSoup(response.text)

cont = soup.find_all('p') # 'p' looks for <p> in html code (p refers to paragraph?)
for c in cont:
    print(c.text)

# links = soup.find_all('a')   # to get all the url's type find_all
# for link in links:
#     print(link.get('href'))


url_open = 'https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct'
response2 = requests.get(url_open)
soup2 = BeautifulSoup(response2.text, 'html.parser')

# content = soup2.find_all('p')
# for c in content:
#     print(c.text)

content = soup2.get_text()
with open('coc.txt', mode='w', encoding='utf-8') as coc:
    for c in content:
        coc.writelines(c)
