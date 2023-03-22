from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.CSS_SELECTOR, ".orangehrm-login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()

