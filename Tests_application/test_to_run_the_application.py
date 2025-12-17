from selenium import webdriver
import pytest

from Pages.Launch_website_application import Launch_website_application


def test_start_the_application(launch_browser):
    launch = Launch_website_application(launch_browser)
    launch.load("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    launch_browser.save_screenshot("launch_browser.png")
