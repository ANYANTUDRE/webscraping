from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.imdb.com/chart/toptv/'
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

movies = []
scraped_movies = soup.find_all('td', class_='titleColumn')
# print(scraped_movies)

for movie in scraped_movies:
    movie = movie.get_text()
    movie = movie.replace('\n', '').strip()
    movies.append(movie)
# movies


Ratings = []
scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')

for rate in scraped_ratings:
    rate = rate.get_text().strip()
    Ratings.append(float(rate))

# Ratings

df = pd.DataFrame()
df['Movies'] = movies
df['Ratings'] = Ratings
print(df)

# df.to_csv('Movies and Ratings.csv')