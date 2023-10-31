import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links1 = soup.select('.titleline')
subtext1 = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links1 + links2
mega_subtext = subtext1 + subtext2

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.select('a')[0].get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
