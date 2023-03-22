import pytest
from selenium import webdriver
from utils.common import get_config_value


@pytest.fixture(scope="session")
def driver(request):
    """
    this function creates a webdriver object and quites it when the test run is complete.
    :param request:
    :return:
    """
    browser = get_config_value("test_settings", "browser")
    url = get_config_value("test_settings", "url")

    # Create a WebDriver Object
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser '{browser}' ")

    # maximize the browser
    driver.maximize_window()

    # Open URL
    driver.get(url)

    # Quit the driver
    driver.quit()


