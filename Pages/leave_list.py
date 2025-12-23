import time

from selenium import webdriver
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

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
        leave_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveList']")))
        leave_list.click()
        time.sleep(5)
        print("Navigated to Leave List page successfully")