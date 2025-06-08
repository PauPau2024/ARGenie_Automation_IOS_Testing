from drivers.driver_utils import click_button_by_accessibility,get_texts_status,click_by_class_chain

def test_home_screen_texts_present(driver):
    # Array of text elements to check for on the meeting screen
    assert click_button_by_accessibility(driver,"Home"), "Failed to click the 'Home' Button"
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

def test_login_screen_elements(driver):
    assert click_button_by_accessibility(driver,"Session"), "Failed to click the 'Home' Button"
    # Array of text elements to check for on the meeting screen
    texts_to_check = [
        "Log in Required",
        "Please log in to access session feature",
        "Login"
    ]
    # Call the common function to get the status of the texts
    status = get_texts_status(driver, texts_to_check)
    # Identify missing texts
    missing_texts = [txt for txt, present in status.items() if not present]
    # Assert that no texts are missing
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
    

def test_profile_screen_texts(driver):
    assert click_button_by_accessibility(driver, "Profile"), "Failed to click 'Profile' button"
    # Array of text elements to check for on the meeting screen
    texts_to_check = [
        "Login to your Account",
        "General Setting",
        "AR Demo Mode"
    ]
    # Call the common function to get the status of the texts
    status = get_texts_status(driver, texts_to_check)
    # Identify missing texts
    missing_texts = [txt for txt, present in status.items() if not present]
    # Assert that no texts are missing
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"

def test_join_session_text(driver):
    assert click_button_by_accessibility(driver,"Home"), "Failed to click the 'Home' Button"
    assert click_button_by_accessibility(driver,"Join session"), "Failed to click 'Join Session' Button"
    texts_to_check = ["Enter Meeting ID","Join"]
    status = get_texts_status(driver, texts_to_check)
    missing_texts = [txt for txt, present in status.items() if not present]
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"

def test_login_screen_texts(driver):
    assert click_button_by_accessibility(driver,"Session"), "Failed to click 'Session' Button"
    assert click_button_by_accessibility(driver,"Login"), "Failed to click 'Login' Button"
    texts_to_check = [
        "Forget Password?",
        "Login",
        "Use as Guest"
    ]
    status = get_texts_status(driver, texts_to_check)
    missing_texts = [txt for txt, present in status.items() if not present]
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"

def test_click_login_to_account_from_profile(driver):
    assert click_button_by_accessibility(driver, "Profile"), "Failed to click 'Profile' button"
    # Call the function to click the 'Login to your Account' text
    assert click_by_class_chain(driver,"**/XCUIElementTypeStaticText[`name == \"Login to your Account\"`]"), "Failed to click 'Login to your Account'"
    texts_to_check = [
        "Forget Password?",
        "Login",
        "Use as Guest"
    ]
    status = get_texts_status(driver, texts_to_check)
    missing_texts = [txt for txt, present in status.items() if not present]
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
    assert click_button_by_accessibility(driver,"Back"), "Failed to click 'back' Button"
