# ios_driver.py - Appium iOS driver setup utilizing capabilities from ios_capabilities.json

import json
from appium import webdriver
from appium.options.common.base import AppiumOptions
import os

def load_capabilities_from_json(file_path):
    """
    Loads desired capabilities from a JSON file.
    """
    with open(file_path, 'r') as file:
        capabilities = json.load(file)
    return capabilities

def create_ios_driver(appium_server_url, capabilities_file="config/ios_device_farm_capabilities.json"):
    """
    Creates and returns an Appium driver instance for iOS devices.
    """
    # Load capabilities from the JSON file
    capabilities = load_capabilities_from_json(capabilities_file)
    
    # Set the app path dynamically (overwrite the app path from json if needed)
    #capabilities["appium:app"] = app_path
    
    # Setup Appium options
    options = AppiumOptions()
    options.load_capabilities(capabilities)

    # Initialize the driver with the loaded capabilities
    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(10)  # Timeout for finding elements

    return driver

def quit_driver(driver):
    """
    Quit the Appium driver.
    """
    if driver:
        driver.quit()
