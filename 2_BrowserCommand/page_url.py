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
    assert "https://www.google.com/" in driver.current_url
    print("Assertion passed. URL Correct")
except AssertionError:
    print(str(AssertionError) + " URL is incorrect !!!")

time.sleep(2)
driver.close()
print("Test complete")
