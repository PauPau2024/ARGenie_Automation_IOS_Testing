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
from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain

def comment(driver,value):
    assert click_button_by_accessibility(driver,"Comment Lines") , "Failed to click 'Comment' button in the Session"
    comment_input = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    assert comment_input is not None, "Comment text field not found"
    comment_input.send_keys(value)
    
    assert click_button_by_accessibility(driver,"send-icon") , "Failed to click 'Send_Icon' button in the Session"
    assert click_by_class_chain(driver, "**/XCUIElementTypeOther[`name == \"close\"`]") , "Failed to Click the close button of the Comment Box"
