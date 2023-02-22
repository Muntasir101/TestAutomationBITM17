from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(2)
driver.get('https://google.com/')

# Step 1: get the current window size
maximize_window_size = driver.get_window_size()
print("maximize_window_size: width = {}px, height = {}px".format(maximize_window_size['width'], maximize_window_size['height']))

# Step 2: set window size
driver.set_window_size(800, 500)
time.sleep(3)
set_window_size = driver.get_window_size()
print("set_window_size: width = {}px, height = {}px".format(set_window_size['width'], set_window_size['height']))

# Step 3: verify the window size
try:
    assert set_window_size['width'] == 800 and set_window_size['height'] == 500, "Window size is not 500 * 800"
    print("Set window size correct")
except AssertionError:
    print(str(AssertionError) + " Set Window Size incorrect")

time.sleep(5)
driver.close()
print("Test complete")
