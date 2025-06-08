from utils.session_code import join_session_code_input
from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain,get_texts_status
from utils.comments import comment
import time

def test_join_session_annotation_joining(driver):
    assert click_button_by_accessibility(driver, "Home"), "Failed to Click 'Home' Button"
    time.sleep(1)
    assert click_button_by_accessibility(driver, "Join session"), "Failed to Click 'Join session' Button"
    assert join_session_code_input(driver,"580281443"), "Failed to complete join session flow"
    time.sleep(2)
    assert click_button_by_accessibility(driver,"Join"), "Failed to click 'Join' Button"
    time.sleep(10)

def test_presence_text_in_the_session(driver):    
    texts_to_check = [
        "580-281-443",
        "Leave",
        "Guest User"
    ]
    # Verify these texts are present after joining
    status = get_texts_status(driver, texts_to_check)
    missing_texts = [txt for txt, present in status.items() if not present]
    assert not missing_texts, f"Missing text(s) after joining session: {', '.join(missing_texts)}"

def test_session_microphone_on_and_off(driver):
    assert click_by_class_chain(driver,'**/XCUIElementTypeButton[`name == "Microphone Off"`]'),  "Failed to tap the 'Microphone-ON' button in the Session"

def test_session_videocall_on_and_off(driver):
    assert click_by_class_chain(driver,"**/XCUIElementTypeButton[`name == \"Video Camera Off\"`]"),  "Failed to tap the 'VideoCall-ON' button in the Session"
    assert click_button_by_accessibility(driver, "Facetime Video Call"),  "Failed to tap the 'VideoCall-OFF' button in the Session"
    assert click_by_class_chain(driver,"**/XCUIElementTypeButton[`name == \"Video Camera Off\"`]"),  "Failed to tap the 'VideoCall-ON' button again in the Session"

def test_session_comment(driver):
    comment(driver,'TEST_VALUE')

def test_session_mini_screen(driver):
    assert click_by_class_chain(driver, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther" ) , "Failed to Click the Mini Video Screen"
    