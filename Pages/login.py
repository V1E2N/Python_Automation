import pytest
from selenium import webdriver
from Pages.Launch_website_application import Launch_website_application
from credentails import credentials
class Login:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)
        print("Website launched successfully")

    def login_to_application(self,username,password):
        launch = Launch_website_application(self.driver)
        launch.login(username,password)
        assert "OrangeHRM" in self.driver.title
        print("Login to application verified successfully")