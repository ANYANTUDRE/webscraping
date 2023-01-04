                ### import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

                ### set path for Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
s = Service('C:\Program Files (x86)\chromedriver.exe')   #this is chromedriver.exe path
browser = webdriver.Chrome(options= options, service=s)

                ### open the page url in chrome
url = 'https://www.scrapethissite.com/pages/simple/'
browser.get(url)

                ### scrape the data
    #get  country names
elements_list = browser.find_elements(By.CLASS_NAME,  'country-name')
print(elements_list)

countries = []
for country in countries:
    temp = country.text
    countries.append(temp)

print(countries)

    #get populations for the country

populations = browser.find_elements(By.CLASS_NAME, 'country-population')
print(populations)

pop_list = []
for pop in pop_list:
    temp = pop.text
    pop_list.append(temp)
#time.sleep()
browser.close()

            ### Store the scraped data

data = pd.DataFrame()
data['Country'] = countries
data['Populations'] = pop_list
print(data.head())