import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrolling():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to page
    driver.get("https://www.apple.com/")
    time.sleep(5)

    # scroll to the bottom
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)

    # scroll back to top
    driver.execute_script('window.scrollTo(0,0)')
    time.sleep(3)

    # scroll to specific element
    iPad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-unit-id='ipad'] .unit-wrapper > [target]")))

    driver.execute_script("arguments[0].scrollIntoView(true);", iPad)
    time.sleep(5)

    driver.close()


scrolling()
