import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def drag_and_drop():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to page
    driver.get("https://material.angular.io/cdk/drag-drop/examples")
    time.sleep(5)

    source_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "cdk-drag-drop-axis-lock-example .example-box:nth-of-type(2)")))

    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "cdk-drag-drop-axis-lock-example .example-box:nth-of-type(1)")))

    actions = ActionChains(driver)

    actions.drag_and_drop(source_element, target_element).perform()


drag_and_drop()