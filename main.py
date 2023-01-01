#importer les packages

import requests
from bs4 import BeautifulSoup
import pandas as pd

#saisir l'url
url = 'http://feeds.bbci.co.uk/news/rss.xml'

#importer le code de la page

reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, "html.parser")

#print(soup)

#pour recuperer toutes les infos dans les balises item
items = soup.findAll('item')
item = items[0]

#print(item)

news_items = []

#pour recuperer des dictionnaires contenant les infos dans chaque element dans les items
for i in items:
    news_i = {}
    news_i['title'] = i.title.text
    news_i['description'] = i.description.text
    news_i['pubdate'] = i.pubdate.text
    print(news_i)
    news_items.append(news_i)

#print(news_items)


df = pd.DataFrame(news_items, columns = ['title', 'description', 'pubdate'])


#print(df.head(20))

df.to_csv('bbc_web_scraping.csv', index= False, encoding= 'utf-8')