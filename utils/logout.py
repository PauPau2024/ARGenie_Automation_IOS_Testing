from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain


def logout(driver):
    assert click_by_class_chain(
        driver,
        '**/XCUIElementTypeButton[`name == "Logout"`]'
    ), "Failed to tap the 'Log-Out ' button in the Profile"
    assert click_button_by_accessibility(driver, "Logout"), "Failed to Click 'Logouts' Button"
    