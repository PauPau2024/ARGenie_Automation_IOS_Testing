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
    
def get_texts_status(driver, texts, timeout=10):
    """
    Check the presence of texts on the screen.
    Takes an array of text elements and checks their presence using IOS_PREDICATE.
    
    :param driver: The Appium driver instance.
    :param texts: Array of texts to check for on the screen.
    :param timeout: Time to wait for elements (default 10 seconds).
    :return: A dictionary with the text as keys and the presence status (True/False) as values.
    """
    driver.implicitly_wait(timeout)
    status = {}

    # Loop through the texts and check each one
    for txt in texts:
        try:
            # For static text, use IOS_PREDICATE
            driver.find_element(
                by=AppiumBy.IOS_PREDICATE,
                value=f"name == '{txt}'"
            )
            status[txt] = True
        except NoSuchElementException:
            status[txt] = False

    return status

def click_button_by_accessibility(driver, button_value, timeout=10):
    driver.implicitly_wait(timeout)
    
    try:
        button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=button_value)
        button.click()
        return True
    except (NoSuchElementException, ElementNotInteractableException) as e:
        print(f"[ERROR] Could not click button '{button_value}': {e}")
        return False

def click_by_class_chain(driver, class_chain, timeout=10):
    """
    Tap the element specified by an iOS class chain selector.
    Returns True if the element was found & tapped, False otherwise.
    """
    driver.implicitly_wait(timeout)
    try:
        el = driver.find_element(
            by=AppiumBy.IOS_CLASS_CHAIN,
            value=class_chain
        )
        el.click()
        return True
    except (NoSuchElementException, ElementNotInteractableException) as e:
        print(f"[ERROR] Could not tap '{class_chain}': {e}")
        return False    

def perform_draw(driver,start_x, start_y, pause):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(pause)
    actions.w3c_actions.pointer_action.release()
    actions.perform()