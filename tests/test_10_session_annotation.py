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
from utils.annotation import session_annotation,session_annotation_with_back,session_annotation_with_close

def test_session_annotation(driver):
    session_annotation(driver)

def test_session_annotation_with_close(driver):
    session_annotation_with_close(driver)

def test_session_annotation_with_back_button(driver):
    session_annotation_with_back(driver)