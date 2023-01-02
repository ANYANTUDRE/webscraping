import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.ebay.fr/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=canon&_sacat=0'

def get_data(url):
     r = requests.get(url)
     soup = BeautifulSoup(r.text, 'html.parser')
     return soup

def parse(soup):
    results = soup.find_all('div', {'class': 's-item__details clearfix'})
    for item in results:
        products = {
            #'title':      item.find('div', {'class': 's-item__title'}).text,
            'soldprice':  float(item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(',', '').strip()),
            'link':        item.find('a', {'class': 's-item__link'}).text,
        }
    print(products)
    return

soup = get_data(url)
parse(soup)