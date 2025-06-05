from drivers.ios_driver import create_ios_driver, quit_driver
from config import appium_config, ios_capabilities, env_config

def test_login():
    # Initialize driver using values from env_config
    driver = create_ios_driver(
        appium_server_url=env_config["base_url"],  # BrowserStack server URL
        app_path=env_config["app_url"]  # The app URL from BrowserStack
    )

    # Your test steps (for example, checking if login button is present)
    assert driver.find_element_by_accessibility_id("Login Button"), "Login button not found"
    
    # Clean up after test
    quit_driver(driver)
