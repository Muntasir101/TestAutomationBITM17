import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def upload_file():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to page
    driver.get("https://the-internet.herokuapp.com/upload")
    time.sleep(5)

    choose_file_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-upload")))

    file_path = "E:\\BITM_Online_17\\Files\\Software Requirement Specification.pdf"

    try:
        choose_file_button.send_keys(file_path)
        print("File Available.")

        upload_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "file-submit")))
        upload_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

        try:
            assert "File Uploaded!" in success_message.text
            print("Test Passed! File Uploaded!")
        except AssertionError:
            print("Test Failed! File didn't Uploaded!")

    except Exception:
        print("File Not Available.Exception: " + str(Exception))

    driver.close()


upload_file()
