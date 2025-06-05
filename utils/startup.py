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



def is_app_opened(driver, timeout=10):
    driver.implicitly_wait(timeout)
    try:
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Home") 
        return True
    except NoSuchElementException:
        return False
    
#Checking the Backgroung Process of the Application via bundle_ID
def is_correct_app_running(driver, expected_bundle_id="com.nublara.argenie.ARGenie"):
    try:
        result = driver.execute_script("mobile: activeAppInfo")
        return result.get("bundleId") == expected_bundle_id
    except Exception as e:
        print(f"Error checking active app info: {e}")
        return False
    
def get_main_tabs_status(driver, timeout=10):
    """
    Check if the main tabs ('Home', 'Session', 'Profile') are present.
    Returns a dictionary with the tab name as the key and a boolean indicating presence as the value.
    """
    driver.implicitly_wait(timeout)
    
    # Check for 'Home' tab
    try:
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Home")
        home_status = True
    except NoSuchElementException:
        home_status = False
    
    # Check for 'Session' tab
    try:
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Session")
        session_status = True
    except NoSuchElementException:
        session_status = False

    # Check for 'Profile' tab
    try:
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile")
        profile_status = True
    except NoSuchElementException:
        profile_status = False
    
    # Return the status for each tab
    status = {
        "Home": home_status,
        "Session": session_status,
        "Profile": profile_status
    }

    return status
