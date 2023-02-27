"""
Locators in Selenium:
1. ID
2. NAME
3. ClassName
4. TagName
5. LinkText
6. PartialLinkText
7. CSS
8. XPATH
"""

from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def locator():
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(2)

    # Step 1: Open Google
    driver.get('https://www.google.com/')
    time.sleep(8)

    # Step 2: Find Username input Field
    username_field = driver.find_element(By.NAME('username'))
    # verify that the element is correct
    if username_field is not None:
        print("Username field is correct")
    else:
        print("No username field")

    # Step 3: Find Password input Field
    password_field = driver.find_element(By.NAME('password'))
    # verify that the element is correct
    if password_field is not None:
        print("Password filed is correct")
    else:
        print("No password field")

    # Step 4: Find Login Button
    login_button = driver.find_element(
        By.XPATH('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))
    # verify that the element is correct
    if login_button is not None:
        print("Login button is correct")
    else:
        print("No Login Button")

    driver.close()
    print("Test Complete")


locator()
