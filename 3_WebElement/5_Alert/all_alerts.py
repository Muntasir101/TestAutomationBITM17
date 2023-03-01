from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def handle_alert():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Normal JS alert
    normal_alert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type("
                                                         "1) > button")))

    normal_alert_button.click()
    time.sleep(5)

    normal_alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Verify JS alert open
    try:
        assert normal_alert.text == "I am a JS Alert"
        print("Test Passed.Normal Alert open.")
    except AssertionError:
        print("Test Failed.Normal Alert is not open")

    # close the alert
    normal_alert.accept()  # click on OK

    # test 1: Verify that alert in closed
    try:
        alert_text = normal_alert.text
        assert False, "Test Failed.Alert still open"
    except NoAlertPresentException:
        print("Test Passed.Normal Alert closed.")
        pass

    driver.close()


handle_alert()
