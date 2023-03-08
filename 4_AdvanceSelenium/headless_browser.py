import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def headless():
    # Step1: launch the browser
    firefox_options = Options()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(options=firefox_options)

    # Step2: Go to page
    driver.get("https://google.com")
    time.sleep(5)

    print(driver.title)

    # Open a new window
    driver.execute_script("window.open('https://apple.com');")
    time.sleep(5)

    total_windows = driver.window_handles
    print(total_windows)

    # Switch to new window[apple]
    driver.switch_to.window(total_windows[1])
    time.sleep(5)
    print("Switch to new Window: " + driver.title)
    time.sleep(3)

    # Back to Old window[Google]
    driver.switch_to.window(total_windows[0])
    print("Switch to old Window: " + driver.title)
    time.sleep(3)

    driver.quit()


headless()

