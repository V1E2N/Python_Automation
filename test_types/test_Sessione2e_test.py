from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from Pages.Launch_website_application import Launch_website_application
from credentails import credentials
from Pages.login import Login as login
from Pages.Add_employee_admin import Add_employee_admin
from Pages.leave_list import Leave_list_page

global launch_browser
@pytest.mark.regression
@pytest.mark.smoke
def test_start_the_application(launch_browser):
    launch = Launch_website_application(launch_browser)
    launch.load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    launch_browser.save_screenshot("launch_browser.png")
    print("Website launched successfully")

@pytest.mark.regression
@pytest.mark.additional
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
    try:
        launch = Add_employee_admin(launch_browser)
        launch.add_employee(credentials.username, credentials.password, credentials.emp_id)
        launch_browser.save_screenshot("admin_section.png")
        print("Navigated to Admin section successfully")
        assert "Admin" in launch_browser.page_source
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred during navigation to admin section: {e}")
        assert False, f"Navigation to admin section failed with error: {e}"
    
@pytest.mark.regression
def test_leave_list(launch_browser):
    # Placeholder for leave list test
    leave = Leave_list_page(launch_browser)
    leave.navigate_to_leave_list()
    launch_browser.save_screenshot("leave_list.png")
    assert "Leave List" in launch_browser.page_source
    print("Leave List page verified successfully")
    time.sleep(5)
    leave.choose_from_to_date()
    launch_browser.save_screenshot("leave_list_filtered.png")
    print("Leave List filtered by date successfully")

@pytest.mark.regression
@pytest.mark.smoke
    #placeholder for logout test
def test_logout(launch_browser):
    try:
        wait = WebDriverWait(launch_browser, 10)
        # Click on user dropdown
        user_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
        user_dropdown.click()
        time.sleep(2)

        # Click on Logout button
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']")))
        logout_button.click()
        time.sleep(5)

        launch_browser.save_screenshot("logout_successful.png")
        print("Logout from application successful")
        assert "Login" in launch_browser.page_source
    except Exception as e:
        print(f"An error occurred during logout: {e}")
        assert False, f"Logout failed with error: {e}"
    

    

  

    

