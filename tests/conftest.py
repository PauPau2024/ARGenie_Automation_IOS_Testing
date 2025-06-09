# conftest.py

import pytest
from drivers.ios_driver import create_ios_driver, quit_driver
from config import env_config
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

@pytest.fixture(scope="session")
def driver():
    """Fixture to initialize and quit the Appium driver for each test."""
    # Initialize driver using values from env_config
    driver = create_ios_driver(
        appium_server_url=env_config["base_url"],  # Use the BrowserStack URL from config
    )

    yield driver  # This will make the driver available in the test

    # Clean up after test (quit the driver)
    quit_driver(driver)


def pytest_collection_modifyitems(config, items):
    """
    Reorder collected items so that:
      1) files are sorted alphabetically (so test_1_*.py comes before test_2_*.py)
      2) within each file, tests run in source‐order (by line number)
    """
    items.sort(key=lambda item: item.location)
