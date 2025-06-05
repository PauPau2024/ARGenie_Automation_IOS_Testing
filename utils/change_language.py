# utils/language_change.py

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, WebDriverException

def change_language(driver, globe_icon_name, language_name, timeout=5):
    """
    Change the language by tapping on the globe icon and selecting the specified language.
    
    :param driver: Appium driver instance.
    :param globe_icon_name: The name/label of the globe icon to interact with (e.g., "Globe").
    :param language_name: The name of the language to select (e.g., "English", "Hindi").
    :param timeout: Time to wait for the elements (default 5 seconds).
    :return: True if the language was changed successfully, False otherwise.
    """
    driver.implicitly_wait(timeout)
    
    # Tap the globe icon
    try:
        globe = driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID,
            value=globe_icon_name)  # Use language_name parameter
        globe.click()
    except (NoSuchElementException, ElementNotInteractableException, WebDriverException) as e:
        print(f"[ERROR] Could not tap globe icon: {e}")
        return False

    # Tap the language option
    try:
        language = driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID,
            value=language_name)  # Use language_name parameter
        language.click()
    except (NoSuchElementException, ElementNotInteractableException, WebDriverException) as e:
        print(f"[ERROR] Could not tap '{language_name}' button: {e}")
        return False

    return True
