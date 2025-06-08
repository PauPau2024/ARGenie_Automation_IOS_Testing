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
from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain,perform_draw

def session_annotation(driver):
    assert click_button_by_accessibility(driver, "Drag") , "Failed to Click the AR Annotation Menu Button"
    assert click_button_by_accessibility(driver, "circle"),  "Failed to click 'circle' Annotation button"
    assert click_button_by_accessibility(driver, "scribble.variable"), "Failed to click 'scribble.variable' Annotation button"
    #assert click_button_by_accessibility(driver, "Change Text Size"),  "Failed to click 'Change Text Size' Annotation button"
    #text_input = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    #time.sleep(2)
    #text_input.send_keys("test")
    #time.sleep(2)
    #assert click_button_by_accessibility(driver, "OK"), "Failed to click 'OK' in text‐size dialog"
    assert click_button_by_accessibility(driver, "Flashlight"), "Failed to click 'Flash-ON Button' after annotation"
    assert click_button_by_accessibility(driver, "flashlight.on.fill"), "Failed to click 'Flash-OFF Button' after annotation"
    assert click_button_by_accessibility(driver, "More"), "Failed to Click More Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Right"), "Failed to Click Right Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Up"), "Failed to Click Up Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Left"), "Failed to Click Left Arrow Direction Button"
    perform_draw(driver,89,413,0.1)    
    assert click_button_by_accessibility(driver, "Close"), "Failed to Click Close Annotation Menu Button"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"

def session_annotation_with_close(driver):
    #assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    #assert click_button_by_accessibility(driver, "Drag") , "Failed to Click the AR Annotation Menu Button"
    #assert click_button_by_accessibility(driver, "Close"), "Failed to Click Close Annotation Menu Button"

    assert click_button_by_accessibility(driver, "circle"),  "Failed to click 'circle' Annotation button"
    assert click_button_by_accessibility(driver, "Close"), "Failed to Click Close Annotation Menu Button"

    assert click_button_by_accessibility(driver, "scribble.variable"), "Failed to click 'scribble.variable' Annotation button"
    assert click_button_by_accessibility(driver, "Close"), "Failed to Click Close Annotation Menu Button"

    #assert click_button_by_accessibility(driver, "Change Text Size"),  "Failed to click 'Change Text Size' Annotation button"
    #text_input = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    #text_input.clear()
    #text_input.send_keys("test")
    #assert click_button_by_accessibility(driver, "OK"), "Failed to click 'OK' in text‐size dialog"
    
    assert click_button_by_accessibility(driver, "Flashlight"), "Failed to click 'Flash-ON Button' after annotation"
    assert click_button_by_accessibility(driver, "flashlight.on.fill"), "Failed to click 'Flash-OFF Button' after annotation"
    
    assert click_button_by_accessibility(driver, "More"), "Failed to Click More Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Right"), "Failed to Click Right Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Up"), "Failed to Click Up Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Left"), "Failed to Click Left Arrow Direction Button"
    perform_draw(driver,89,413,0.1)      
    assert click_button_by_accessibility(driver, "Close"), "Failed to Click Close Annotation Menu Button"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"

def session_annotation_with_back(driver):
    #assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    #assert click_button_by_accessibility(driver, "Drag") , "Failed to Click the AR Annotation Menu Button"
    #assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"

    assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    assert click_button_by_accessibility(driver, "circle"),  "Failed to click 'circle' Annotation button"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"

    assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    assert click_button_by_accessibility(driver, "scribble.variable"), "Failed to click 'scribble.variable' Annotation button"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"
    
    #assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
   # assert click_button_by_accessibility(driver, "Change Text Size"),  "Failed to click 'Change Text Size' Annotation button"
    #text_input = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    #text_input.clear()
    #text_input.send_keys("test")
    #assert click_button_by_accessibility(driver, "OK"), "Failed to click 'OK' in text‐size dialog"
    #assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"
    
    assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    assert click_button_by_accessibility(driver, "Flashlight"), "Failed to click 'Flash-ON Button' after annotation"
    assert click_button_by_accessibility(driver, "flashlight.on.fill"), "Failed to click 'Flash-OFF Button' after annotation"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"
    
    assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    assert click_button_by_accessibility(driver, "More"), "Failed to Click More Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Right"), "Failed to Click Right Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Up"), "Failed to Click Up Arrow Direction Button"
    assert click_button_by_accessibility(driver, "Left"), "Failed to Click Left Arrow Direction Button"
    perform_draw(driver,89,413,0.1)      
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"
    
    assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]") , "Failed to Click the Mini Video Screen"
    assert click_button_by_accessibility(driver, "Close"), "Failed to Click Close Annotation Menu Button"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click Back Button from annotation"