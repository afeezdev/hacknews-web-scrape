import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
print(soup.title)
