from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Microsoft Edge
driver = webdriver.Edge()

try:
    # Open login page
    driver.get("http://127.0.0.1:5000")

    # Maximize browser
    driver.maximize_window()

    # -------------------------
    # Login
    # -------------------------

    username = driver.find_element(By.ID, "username")
    username.send_keys("admin")

    password = driver.find_element(By.ID, "password")
    password.send_keys("admin123")

    login_button = driver.find_element(By.ID, "login_button")
    login_button.click()

    time.sleep(2)

    # -------------------------
    # Check Student Page
    # -------------------------

    if "Student Management" not in driver.page_source:
        print("CRUD TEST: FAIL - Student page not opened")
        exit()

    # -------------------------
    # Create Student
    # -------------------------

    student_name = driver.find_element(By.ID, "student_name")
    student_name.send_keys("Selenium Student")

    student_email = driver.find_element(By.ID, "student_email")
    student_email.send_keys("selenium@gmail.com")

    add_button = driver.find_element(By.ID, "add_student_button")
    add_button.click()

    time.sleep(2)

    # -------------------------
    # Verify Student
    # -------------------------

    page_text = driver.find_element(By.TAG_NAME, "body").text

    if "Selenium Student" in page_text:
        print("CRUD TEST: PASS")
    else:
        print("CRUD TEST: FAIL")

finally:
    driver.quit()