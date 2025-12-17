from selenium import webdriver
import pytest

@pytest.fixture(scope="session")
def launch_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()