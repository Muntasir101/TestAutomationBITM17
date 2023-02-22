from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(2)

# Step 1: Open Google
driver.get('https://google.com/')
time.sleep(3)

# Step 2: Open Apple
driver.get('https://apple.com')
time.sleep(3)

# Step 3: back to Google
driver.back()
print(driver.title)  # Google
time.sleep(3)

# Step 4: forward to apple
driver.forward()
print(driver.title)  # Apple
time.sleep(5)

# Step 5: refresh apple
driver.refresh()

driver.close()
