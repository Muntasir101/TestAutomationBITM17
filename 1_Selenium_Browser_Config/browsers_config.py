from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(2)
driver.get('https://google.com/')
time.sleep(2)
driver.close()
