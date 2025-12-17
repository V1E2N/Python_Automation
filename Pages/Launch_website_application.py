import time

from selenium import webdriver
import pytest

class Launch_website_application:
    def __init__(self,driver):
        self.driver = driver

    def load(self,url):
        self.driver.get(url)
        print("Website launched successfully")
        time.sleep(4)



