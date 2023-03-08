import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def browser_arguments():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--window-size=400,300')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=chrome_options)

    time.sleep(10)


browser_arguments()
