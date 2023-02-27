from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def login_orangeHRM_valid():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to Login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Step3: Enter Username
    Username = driver.find_element(By.NAME, "username")
    Username.send_keys("Admin")
    time.sleep(5)

    # Step4: Enter Password
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("admin123")
    time.sleep(5)

    # Step5: Click Login button
    LoginButton = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    LoginButton.click()
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


def login_orangeHRM_invalid():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to Login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Step3: Enter Username
    Username = driver.find_element(By.NAME, "username")
    Username.send_keys("Admin123")
    time.sleep(5)

    # Step4: Enter Password
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("admin1233323")
    time.sleep(5)

    # Step5: Click Login button
    LoginButton = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    LoginButton.click()
    time.sleep(5)

    # Step6: Expected Result : Verify by Error Message
    Expected_Error_Message = "Invalid credentials"

    # Step7: Actual Result : Verify by Error Message
    Actual_Error_Message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text").text

    # Step8: Test Result
    try:
        assert Expected_Error_Message == Actual_Error_Message
        print("Invalid Test Case Result: Passed")
    except AssertionError:
        print("Invalid Test Case Result: Failed")

    # Step9: Close the browser
    driver.close()


login_orangeHRM_valid()
login_orangeHRM_invalid()