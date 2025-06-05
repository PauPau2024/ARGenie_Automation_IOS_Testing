import pytest
import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    WebDriverException
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


def enter_credentials(driver, email, password, timeout=10):
    driver.implicitly_wait(timeout)
    try:
        # 1) Find and fill the email field
        email_field = driver.find_element(
            by=AppiumBy.CLASS_NAME,
            value="XCUIElementTypeTextField"
        )
        email_field.clear()
        email_field.send_keys(email)
        
        # 2) Find and fill the password field
        password_field = driver.find_element(
            by=AppiumBy.CLASS_NAME,
            value="XCUIElementTypeSecureTextField"
        )
        password_field.clear()
        password_field.send_keys(password)
        
        return True
    except (NoSuchElementException, ElementNotInteractableException, WebDriverException) as e:
        print(f"[ERROR] enter_credentials failed: {e}")
        return False
