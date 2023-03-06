import time
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def mouse_hover_demo():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to page
    driver.get("https://demo.opencart.com/")
    time.sleep(5)

    menu_desktops = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Desktops")))

    actions = ActionChains(driver)
    actions.move_to_element(menu_desktops).perform()

    try:
        submenu_mac1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Mac (1)")))
        submenu_mac1.click()

        # Verify that Mac page is open
        assert "Mac" in driver.title
        print("Test Passed. Mac page open.")
    except AssertionError:
        print("Mac page not found!!")

    driver.close()


mouse_hover_demo()
