import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/wearelikewise/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

scripts = soup.find_all('div', class_ = '')

print(scripts)