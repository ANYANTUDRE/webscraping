# 1) Pick a website and describe your objective
"""
       Project Outline:

_ We're going to scrape https://github.com/topics
_ We'll get a list of topics. For each topic, we'll get topic title, topic page URL and topic description
_ For each topic, we'll get the top 25 repositories in the topic from the topic page
_ For each repository, we'll grab the repo name, username, stars and repo URL
_ For each topic, we'll create a CSV file in the following format:

"""

# 2) Use the requests library to download web pages

import requests

topics_url = "https://github.com/topics"
response = requests.get(topics_url)        # it's to download the url page

# print(response.status_code)              # return the statut code
# print(len(response.text))                # to print the number of letters


page_contents = response.text
# print(page_contents[:1000])

"""with open('webpage.html', 'w') as f:
    f.write(page_contents)"""


# 3) Use Beautiful Soup to parse and extract information
from bs4 import BeautifulSoup
doc = BeautifulSoup(page_contents, 'html.parser')      # create a beautiful soup object


topic_title_tags = doc.find_all('p', {'class': 'f3 lh-condensed mb-0 mt-1 Link--primary'})
# print(len(topic_title_tags))
# print(topic_title_tags[:5])

desc_selector = doc.find_all('p', {'class': 'f5 color-fg-muted mb-0 mt-1'})
# print(len(desc_selector))
# print(desc_selector[:5])

topic_link_tags = doc.find_all('a', {'class', 'no-underline flex-1 d-flex flex-column'})
# print(len(topic_link_tags))

topic0_url = 'https://github.com'+topic_link_tags[0]['href']  # example to show the 1st link
# print(topic0_url)


topic_titles = []
topic_description = []
topic_url = []
base_url = 'https://github.com'

for tag in topic_title_tags:
    topic_titles.append(tag.text)
for tag in desc_selector:
    topic_description.append(tag.text.strip())
for tag in topic_link_tags:
    topic_url.append(base_url + tag['href'])

# print(topic_titles)
# print(topic_description[:5])
# print(topic_url)


# 4)Create CSV file(s) with the extracted information
import pandas as pd

topics_dict = {
    'title': topic_titles,
    'description': topic_description,
    'url': topic_url,
}

topic_df = pd.DataFrame(topics_dict)
# print(topic_df)
# topic_df.to_csv('topic.csv', index=False)











# Getting information out of a topic page url

topic_page_url = topic_url[1]
# (topic_url)

response0 = requests.get(topic_page_url)

topic_doc = BeautifulSoup(response0.text, 'html.parser')

repo_tags = topic_doc.find_all('h3', {'class': 'f3 color-fg-muted text-normal lh-condensed'})
print(len(repo_tags))
# print(repo_tags[0])

username0 = repo_tags[0].find_all('a')
print(username0[0].text.strip())
print(username0[1].text.strip())
print(base_url + username0[1]["href"])

star = topic_doc.find_all('span', {'id' : 'repo-stars-counter-star'})
# print(len(star))
print(star[1].text)


def parse_star_count(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1] == 'k':
        return int(float(stars_str[:-1]) * 1000)
    return int(stars_str)


usernames = []
repos = []
repos_links = []

"""for tag in repo_tags:
    username = repo_tags.
    usernames.append()

"""


# 5) Document and share your work