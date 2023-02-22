from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(2)
driver.get('https://google.com/')

# fetch webpage title from browser
google_title = driver.title
print(google_title)

# verify title is correct
try:
    assert "Google" in driver.title
except AssertionError:
    print(str(AssertionError) + " Title is incorrect !!!")

time.sleep(2)
driver.close()
print("test complete")
