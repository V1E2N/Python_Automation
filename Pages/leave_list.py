import time

from selenium import webdriver
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from credentails import credentials

#------------------Leave List Page Class---------------------#
class Leave_list_page:
    def __init__(self,driver):
        self.driver = driver

    def navigate_to_leave_list(self):
        wait = WebDriverWait(self.driver, 10)
        # Click on Leave Module
        leave_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']")))
        leave_module.click()
        time.sleep(3)

        # Click on Leave List
        leave_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and normalize-space()='Leave List']")))
        leave_list.click()
        time.sleep(5)
        print("Navigated to Leave List page successfully")
        # Fill in From Date and To Date
    def choose_from_to_date(self):
        from_date = self.driver.find_element(By.XPATH, "//label[text()='From Date']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        from_date.clear()
        from_date.send_keys(credentials.from_date)
        to_date = self.driver.find_element(By.XPATH, "//label[text()='To Date']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        to_date.clear()
        to_date.send_keys(credentials.to_date)
        # Click on Search button
        search_button = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input' and text()='Select']/parent::div")
        search_button.click()
        leave_type= self.driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(),'CAN - Vacation US')]")
        leave_type.click()
        time. sleep(2)