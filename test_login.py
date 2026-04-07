from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://example.com/login")

# Enter username
driver.find_element(By.ID, "username").send_keys("testuser")

# Enter password
driver.find_element(By.ID, "password").send_keys("password")

# Click login
driver.find_element(By.ID, "loginBtn").click()

time.sleep(3)
driver.quit()
