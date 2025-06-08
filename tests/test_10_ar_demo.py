from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain
from utils.ar_demo import ar_annotation_feature_sequence

def test_AR_demo_button(driver):
    assert click_button_by_accessibility(driver, "Profile"), "Failed to Click 'Profile' Button"
    assert click_by_class_chain(
        driver,
        '**/XCUIElementTypeButton[`name == \"AR Demo Mode\"`]'
    ), "Failed to tap the second 'AR Demo Mode' button"


def test_ar_demo_annotation_walkthrough(driver):
    ar_annotation_feature_sequence(driver)


