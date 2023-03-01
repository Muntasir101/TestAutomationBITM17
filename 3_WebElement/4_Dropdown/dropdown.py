import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def select_dropdown():
    # Step1: launch the browser
    driver = webdriver.Firefox()

    # Step2: Go to page
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Step3: Find the dropdown
    dropdown = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dropdown"))))

    # Step4: Find the default option
    # test 1: Verify default option selected or not
    # Get the selected option and check if it is selected
    default_selected_option = dropdown.first_selected_option

    try:
        assert default_selected_option.is_selected, "Please select an option"
        print("Test Case 1: Test passed.'Please select an option' is selected as default. Test passed.")

    except AssertionError:
        print("Test Case 1: Test failed.'Please select an option' is not selected as default. Test failed.")

    # Step5: Select options'
    # dropdown.select_by_value("1")  # Accept String values
    # dropdown.select_by_index(2)  # Accept Integer values
    dropdown.select_by_visible_text("Option 2")  # Accept String values
    time.sleep(5)

    # test 2: Verify option selected or not
    # Get the selected option and check if it is selected
    new_selected_option = dropdown.first_selected_option

    try:
        assert new_selected_option.is_selected, "Option 2"
        print("Test Case 2: Test passed.Option 2 is new selected. Test passed.")

    except AssertionError:
        print("Test Case 2: Test failed.Option 2 is not new selected. Test failed.")

    # test 3: Verify all options available or not
    expected_options_list = ["Please select an option", "Option 1", "Option 2"]

    actual_options_list = []

    # iterate over dropdown options
    for opt in dropdown.options:
        options_text = opt.text
        actual_options_list.append(options_text)

    # compare expected and actual options list
    try:
        assert actual_options_list == expected_options_list
        print("Test Case 3: Test passed.All Options Available.Test passed")
    except AssertionError:
        print("Test Case 3: Test failed.All Options not Available.Test failed")

    # Step6: close Browser
    driver.close()


select_dropdown()
