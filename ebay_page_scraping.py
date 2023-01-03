import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.ebay.fr/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=canon&_sacat=0'

def get_data(url):
     r = requests.get(url)
     soup = BeautifulSoup(r.text, 'html.parser')
     return soup

def parse(soup):
    productlist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        product = {
            'title':      item.find('div', {'class': 's-item__title'}).find('span', {'role': 'heading'}).text,
            'soldprice':  item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(',', '').replace('EUR', '').strip(),
            'link':        item.find('a', {'class': 's-item__link'})['href'],
        }
        productlist.append(product)
    return productlist

def output(productlist):
    productdf = pd.DataFrame(productlist)
    productdf.to_csv('output.csv', index = False)
    print("Saved to CSV")
    return productdf

soup = get_data(url)
productlist = parse(soup)
productdf = output(productlist)
print(productdf.head())