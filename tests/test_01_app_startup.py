from utils.startup import is_correct_app_running,is_app_opened,get_main_tabs_status
import pytest 

def test_correct_app_running(driver):
    assert is_correct_app_running(driver), "Incorrect app is running or app failed to launch."

def test_app_launch(driver):
    """Test to verify that app launched successfully. """
    assert is_app_opened(driver), "App did not launch properly or 'Home' element not found."

