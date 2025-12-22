from selenium import webdriver
import pytest
import time
from Pages.Launch_website_application import Launch_website_application
from credentails import credentials
from Pages.login import Login as login
from Pages.Add_employee_admin import Add_employee_admin
global launch_browser
@pytest.mark.regression
@pytest.mark.smoke
def test_start_the_application(launch_browser):
    launch = Launch_website_application(launch_browser)
    launch.load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    launch_browser.save_screenshot("launch_browser.png")
    print("Website launched successfully")

@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.smoke  
def test_login_to_application(launch_browser):
    try:
        login_page = login(launch_browser)
        login_page.load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page.login_to_application(credentials.username, credentials.password)
        launch_browser.save_screenshot("login_successful.png")
        print("Login to application successful")
        assert "OrangeHRM" in launch_browser.title
        time.sleep(2)
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        assert False, f"Test failed: {e}"
    except Exception as e:
        print(f"An error occurred during login: {e}")
        assert False, f"Login failed with error: {e}"
    finally:
        print("Login test completed")

@pytest.mark.regression
def test_navigate_to_admin_section(launch_browser):
    launch = Add_employee_admin(launch_browser)
    launch.add_employee(credentials.username, credentials.password, credentials.emp_id)
    launch_browser.save_screenshot("admin_section.png")
    print("Navigated to Admin section successfully")
    assert "Admin" in launch_browser.page_source
    time.sleep(10)


    

