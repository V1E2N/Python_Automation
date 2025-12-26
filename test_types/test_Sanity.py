from selenium import webdriver
import pytest
import time
from Pages.Launch_website_application import Launch_website_application
from credentails import credentials
from Pages.login import Login as login
from Pages.Add_employee_admin import Add_employee_admin
global launch_browser


@pytest.mark.smoke
@pytest.mark.regression
def test_start_the_application (launch_browser):
    launch = Launch_website_application(launch_browser)
    launch.load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    launch_browser.save_screenshot("D:/Python_Automation/screenshots/launch_browser.png")
    print("Website launched successfully")
 #----------------------------LOGIN --------------------------#  

@pytest.mark.regression
@pytest.mark.smoke
def test_login_to_application(launch_browser):
    login_page = login(launch_browser)
    login_page.load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login_to_application(credentials.username, credentials.password)
    launch_browser.save_screenshot("D:/Python_Automation/screenshots/login_successful.png")
    print("Login to application successful")
    assert "OrangeHRM" in launch_browser.title
    time.sleep(2)
   

