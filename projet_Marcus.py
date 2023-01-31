import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://division2lol.fr/resultats'

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    teams_name = []
    results = soup.find_all('div', {'class': 'ranking-row'})
    for item in results:
        product = {

            '1':        item.find('div', {'class': 'position'}).text,
            '2':        item.find('div', {'class': 'team'}).text.split(),
            '3':          item.find('div', {'class': 'results'}).find('div', {'class': 'played'}).text,
            '4':          item.find('div', {'class': 'results'}).find('div', {'class': 'winned'}).text,
            '5':          item.find('div', {'class': 'results'}).find('div', {'class': 'lossed'}).text,
            '6':        item.find('div', {'class': 'results'}).find('div', {'class': 'points'}).text
        }
        teams_name.append(product)
    return teams_name


def output(teams_name):
    df = pd.DataFrame(teams_name)
    df.to_csv('results.csv', index = False)
    print("Saved to CSV")
    return df

soup = get_data(url)
results = parse(soup)
df = output(results)
print(df.head())
