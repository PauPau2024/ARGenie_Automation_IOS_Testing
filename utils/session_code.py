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


def join_session_code_input(driver, session_code, timeout=15):
    driver.implicitly_wait(timeout)
    try:
        text_field = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
        text_field.clear()
        text_field.send_keys(session_code)
        return True

    except (NoSuchElementException, ElementNotInteractableException) as e:
        print(f"[ERROR] Join session flow Session Code Input : {e}")
        return False