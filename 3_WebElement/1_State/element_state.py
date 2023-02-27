from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def webElement_state():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to Login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Step3: Enter Username
    Username = driver.find_element(By.NAME, "username")

    # Verify username is Displayed in login page
    Username_Display_state = Username.is_displayed()

    try:
        assert Username_Display_state == True
        Username.send_keys("Admin")
    except AssertionError:
        print("Username is not available")
    time.sleep(5)

    # Step4: Enter Password
    Password = driver.find_element(By.NAME, "password")

    # Verify password is Enabled in login page
    Password_Enable_state = Password.is_enabled()

    try:
        assert Password_Enable_state == True
        Password.send_keys("admin123")
    except AssertionError:
        print("Password is not enabled")
    time.sleep(5)

    # Step5: Click Login button
    LoginButton = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

    # Verify LoginButton is Disabled in login page
    try:
        assert LoginButton.is_enabled()
        LoginButton.click()
    except AssertionError:
        print("Login Button is not Enabled")
    time.sleep(5)

    # Step6: Expected Result : Verify by URL
    ExpectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # Step7: Actual Result : Verify by URL
    ActualURL = driver.current_url

    # Step8: Test Result
    try:
        assert ExpectedURL == ActualURL
        print("Valid Test Case Result: Passed")
    except AssertionError:
        print("Valid Test Case Result: Failed")

    # Step9: Close the browser
    driver.close()


webElement_state()
