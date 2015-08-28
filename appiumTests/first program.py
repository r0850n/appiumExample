__author__ = 'robert'
import os
from selenium import webdriver

chromedriver = "E:/automaty/drivers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()


