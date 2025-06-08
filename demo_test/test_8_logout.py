from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain
from utils.logout import logout

def test_logout_flow(driver):
    assert click_button_by_accessibility(driver,"Profile"), "Failed to click the 'Profile' Button"
    assert click_button_by_accessibility(driver, "Sujal, Testing doon"), "Failed to Click 'Sujal, Testing doon' Button"
    assert logout(driver) , "Failed at Log-Out"
    assert click_button_by_accessibility(driver, "Back"), "Failed to Click 'Back' Button"