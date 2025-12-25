import pytest
from selenium import webdriver
from Pages.Launch_website_application import Launch_website_application
from credentails import credentials

class Logout:
    def __init__(self, driver):
        self.driver = driver

    def logout_from_application(self):
        try:
            # Click on the user dropdown menu
            user_dropdown = self.driver.find_element_by_css_selector("p.oxd-userdropdown-name")
            user_dropdown.click()
            # Click on the logout option
            logout_option = self.driver.find_element_by_xpath("//a[text()='Logout']")
            logout_option.click()
            print("Logout from application successful")
            return True
        except Exception as e:
            print(f"An error occurred during logout: {e}")
            return False