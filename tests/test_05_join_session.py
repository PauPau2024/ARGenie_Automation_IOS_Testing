from utils.session_code import join_session_code_input
from drivers.driver_utils import click_button_by_accessibility
import time

def test_join_session_flow_incorrect_session_id(driver):
    assert click_button_by_accessibility(driver, "Home"), "Failed to Click 'Home' Button"
    assert click_button_by_accessibility(driver,"Join session"), "Failed to click 'Join Session' Button"
    time.sleep(1)
    assert join_session_code_input(driver,"000000000"), "Failed to complete join session flow"
    assert click_button_by_accessibility(driver,"Join"), "Failed to click 'Join' Button"
    assert click_button_by_accessibility(driver,"Clear text"), "Failed to click 'Clear text' Button"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"

def no_test_join_session_flow_incorrect_session_and_correct_session_id(driver):
    assert click_button_by_accessibility(driver, "Home"), "Failed to Click 'Home' Button"
    assert click_button_by_accessibility(driver,"Join session"), "Failed to click 'Join Session' Button"
    time.sleep(1)
    assert join_session_code_input(driver,"000000000"), "Failed to complete join session flow"
    assert click_button_by_accessibility(driver,"Join"), "Failed to click 'Join' Button"
    assert click_button_by_accessibility(driver,"Clear text"), "Failed to click 'Clear text' Button"
    time.sleep(3)
    assert join_session_code_input(driver,"580281443"), "Failed to complete join session flow"
    time.sleep(2)
    assert click_button_by_accessibility(driver,"Join"), "Failed to click 'Join' Button"
    time.sleep(10)
    assert click_button_by_accessibility(driver,"Leave"), "Failed to click 'Leave' Button"
    time.sleep(5)
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"

def no_test_join_session_flow_correct_session_id(driver):
    assert click_button_by_accessibility(driver, "Home"), "Failed to Click 'Home' Button"
    time.sleep(3)
    assert join_session_code_input(driver,"580281443"), "Failed to complete join session flow"
    time.sleep(2)
    assert click_button_by_accessibility(driver,"Join"), "Failed to click 'Join' Button"
    time.sleep(10)
    assert click_button_by_accessibility(driver,"Leave"), "Failed to click 'Leave' Button"
    time.sleep(5)
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"
