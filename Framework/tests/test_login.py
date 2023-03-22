import time

import allure
from selenium import webdriver
from Framework.utils.common import get_config_value
from Framework.pages.LoginPage import LoginPage


@allure.feature("Login Feature")
def test_login():
    # Get the configuration settings
    url = get_config_value("DEFAULT", "url")
    browser = get_config_value("DEFAULT", "browser")
    headless = get_config_value("DEFAULT", "headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless == "True":
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox()

    # navigate to Login page
    driver.get(url)
    time.sleep(5)

    login_page = LoginPage(driver)

    # Enter Username
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_btn()

    driver.quit()


