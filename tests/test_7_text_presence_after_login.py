from drivers.driver_utils import click_button_by_accessibility,get_texts_status

def test_home_screen_texts_present_after_login(driver):
    assert click_button_by_accessibility(driver,"Home"), "Failed to click 'Home' Button"
    # Array of text elements to check for on the meeting screen
    texts_to_check = [
        "Hey Sujal!",
        "Welcome to AR Genie!",
        "Empower Your Work",
        "Online, App is Ready to connect",
        "Join session",
        "Create Session"
    ]
    # Call the common function to get the status of the texts
    status = get_texts_status(driver, texts_to_check)
    # Identify missing texts
    missing_texts = [txt for txt, present in status.items() if not present]
    # Assert that no texts are missing
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"

def test_profile_screen_texts_after_login(driver):
    # Array of text elements to check for on the meeting screen
    assert click_button_by_accessibility(driver, "Profile"), "Failed to Click 'Profile' Button" 
    texts_to_check = [
        "Sujal",
        "Testing doon",
        "General Setting",
        "AR Demo Mode"
    ]
    # Call the common function to get the status of the texts
    status = get_texts_status(driver, texts_to_check)
    # Identify missing texts
    missing_texts = [txt for txt, present in status.items() if not present]
    # Assert that no texts are missing
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
     


def test_user_profile_details_after_login(driver):
    assert click_button_by_accessibility(driver, "Sujal, Testing doon"), "Failed to Click 'Sujal, Testing doon' Button"
    # Array of text elements to check for on the meeting screen
    texts_to_check = [
        "Back",
        "Profile",
        "e-mail",
        "sujal@staging.com",
        "Logout",
        "Sujal",
        "Testing doon"
    ]
    # Call the common function to get the status of the texts
    status = get_texts_status(driver, texts_to_check)
    # Identify missing texts
    missing_texts = [txt for txt, present in status.items() if not present]
    # Assert that no texts are missing
    assert not missing_texts, f"Missing text: {', '.join(missing_texts)}"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click 'Back' Button"    
