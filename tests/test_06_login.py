from utils.login import enter_credentials
from drivers.driver_utils import click_button_by_accessibility,get_texts_status
import time 

def test_login_but_use_as_a_guest(driver):
    assert click_button_by_accessibility(driver, "Session"), "Failed to click 'Session' button"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"  
    assert click_button_by_accessibility(driver,"Use as Guest"), "Failed to click 'Use as Guest' Button"
    # Array of text elements to check for on the meeting screen
    texts_to_check = [
        "Hey Guest User!",
        "Welcome to AR Genie!",
        "Empower Your Work",
        "Online, App is Ready to connect",
        "Join session"
    ]
    # Call the common function to get the status of the texts
    status = get_texts_status(driver, texts_to_check)
    # Identify missing texts
    missing_texts = [txt for txt, present in status.items() if not present]
    # Assert that no texts are missing
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
    

def test_login_wrong_email_and_wrong_password(driver):
    assert click_button_by_accessibility(driver,"Session"), "Failed to click 'Session' button"
    #wrong email and  wrong password
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    assert enter_credentials(driver, "user@example.com", "MySecret!23"), "Failed to enter wrong email and/or wrong password"
    assert click_button_by_accessibility(driver,"Hide"), "Failed to click 'Un-Hide' Password Button"
    assert click_button_by_accessibility(driver,"Show"), "Failed to click 'Hide' Password Button"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"

def test_login_correct_email_and_wrong_password(driver):
    #correct email and wrong password 
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"    
    assert enter_credentials(driver, "sujal@staging.com", "MySecret!23"), "Failed to correct email and/or wrong password"
    assert click_button_by_accessibility(driver,"Hide"), "Failed to click 'Un-Hide' Password Button"
    assert click_button_by_accessibility(driver,"Show"), "Failed to click 'Hide' Password Button"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"
    
def test_login_wrong_email_and_correct_password(driver):
    #wrong email and correct password
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"    
    assert enter_credentials(driver, "user@example.com", "Kingfisher@123"), "Failed to enter wrong email and/or correct password"
    assert click_button_by_accessibility(driver,"Hide"), "Failed to click 'Un-Hide' Password Button"
    assert click_button_by_accessibility(driver,"Show"), "Failed to click 'Hide' Password Button"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"

def test_login_correct_email_and_correct_password(driver):
    assert click_button_by_accessibility(driver, "Session"), "Failed to click 'Session' button"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    assert enter_credentials(driver, "user@example.com", "MySecret!23"), "Failed to enter wrong email and/or wrong password"   
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"    
    time.sleep(2)
    assert enter_credentials(driver, "sujal@staging.com", "MySecret!23"), "Failed to correct email and/or wrong password"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"    
    time.sleep(2)
    assert enter_credentials(driver, "user@example.com", "Kingfisher@123"), "Failed to wrong email and/or correct password"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"    
    time.sleep(2)
    assert enter_credentials(driver, "sujal@staging.com", "Kingfisher@123"), "Failed to correct email and/or correct password"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    time.sleep(5)