# Import modules
from bs4 import BeautifulSoup
import requests

# get page url
url = 'https://www.thehindu.com/sci-tech/technology/year-in-review-top-tech-stories-year-2022/article66323467.ece?art=package'
page = requests.get(url)

# display page content
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#find the image src link
img_tag = soup.find('source')
print(img_tag)

img_url = img_tag['srcset']

# Download the image from url
image = requests.get(img_url)
    # storethe image in file
with open('web_image.png', 'wb') as file:
    for chunk in image.iter_content(chunk_size=1024):
        file.write(chunk)


# To Download a powerpoint doc from url
ppt_url = ''
ppt = requests.get(ppt_url)
    # storethe ppt in file
with open('web_ppt.pptx', 'wb') as file:
    for chunk in ppt.iter_content(chunk_size=1024):
        file.write(chunk)

# To Download a Video from url
video_url = ''
video = requests.get(video_url)
    # storethe video in file
with open('web_video.mp4', 'wb') as file:
    for chunk in video.iter_content(chunk_size=1024):
        file.write(chunk)
