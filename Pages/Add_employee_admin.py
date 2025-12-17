import time
from selenium import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentails import credentials
from Pages.Launch_website_application import Launch_website_application
from Pages.login import Login 


class Add_employee_admin:
    def __init__(self,driver):
        self.driver = driver

    def add_employee(self, first_name, last_name, emp_id):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
        time.sleep(3)
        click_add_button = self.driver.find_element(By.XPATH,"//button[contains(@class,'oxd-button--secondary') and normalize-space()='Add']")
        click_add_button.click()
        time.sleep(4)

        # - Choose User Role (click and select Admin) -
        Choose_user_role = self.driver.find_element(By.XPATH, "//div[contains(@class,'oxd-select-text-input') and normalize-space()='-- Select --']").click()
        Choose_user_role_option = self.driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'Admin')]").click()
        time.sleep(2)

        # — Employee Name (type and select suggestion) —
        emp_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[./div/label[text()='Employee Name']]//input")
        ))
        emp_input.send_keys("Alice")  # partial name

        # Wait for suggestion list to appear and click correct suggestion
        suggestion = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='option']//span[contains(text(),'Alice')]")
            ))
        suggestion.click()
        time.sleep(2)

        # — Status (click and select Enabled) —
        status_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text-input')]")))
        status_select.click()
        time.sleep(1)
        status_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[normalize-space()='Enabled']")))
        status_option.click()
        time.sleep(2)
       #//div[@role='listbox']//span[normalize-space()='Enabled']
