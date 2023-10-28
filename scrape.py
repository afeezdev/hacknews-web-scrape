import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# using css selector
# print(soup.select('.score'))
# print(soup.select('#score_38043033'))
links = soup.select('.titleline')
votes = soup.select('.score')
# print(votes[0].get('id'))
# print(votes[0].contents[0])


