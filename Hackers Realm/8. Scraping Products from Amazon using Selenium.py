# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd

# set path for Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
s = Service('C:\Program Files (x86)\chromedriver.exe')   # this is chromedriver.exe path
driver = webdriver.Chrome(options=options, service=s)

# load the webpage
driver.get('https://www.amazon.in')
driver.maximize_window()

input_search = driver.find_elements(by= By.ID, value= 'twotabsearchtextbox')
search_button = driver.find_elements(by = By.XPATH, value= '(//input[@type="submit"])[1]')
print(input_search)
print(search_button)
# send the input to the webpage
input_search.send_keys("Smartphones under 10000")
sleep(1)
search_button.click()