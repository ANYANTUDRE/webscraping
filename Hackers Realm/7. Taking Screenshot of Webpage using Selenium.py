# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# set path for Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
s = Service('C:\Program Files (x86)\chromedriver.exe')   # this is chromedriver.exe path
driver = webdriver.Chrome(options=options, service=s)

driver.get("http://selenium.dev")

driver.save_screenshot('test_screenshot.png')

#driver.quit()