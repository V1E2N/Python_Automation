import time

from selenium import webdriver
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#------------------Launch Website Application Class---------------------#

class Launch_website_application:
    def __init__(self,driver):
        self.driver = driver

    def load(self,url):
        self.driver.get(url)
        print("Website launched successfully")
        time.sleep(5)

    def login(self,username,password):
        #self.driver.find("name","username").send_keys(username)
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
        username_field.send_keys(username)
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
        password_field.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
        
   



