from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

try:
    driver.get("http://127.0.0.1:5000")
    driver.maximize_window()

    # Enter username
    driver.find_element(By.ID, "username").send_keys("admin")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("admin123")

    # Click login
    driver.find_element(By.ID, "login_button").click()

    time.sleep(2)

    # Print what Selenium actually sees
    print("CURRENT URL:", driver.current_url)
    print("PAGE TITLE:", driver.title)
    print("PAGE TEXT:")
    print(driver.find_element(By.TAG_NAME, "body").text)

    if "Student Management" in driver.page_source:
        print("LOGIN TEST: PASS")
    else:
        print("LOGIN TEST: FAIL")

finally:
    driver.quit()