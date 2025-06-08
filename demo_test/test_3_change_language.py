from utils.change_language import change_language

def test_change_language_to_english(driver):
    # Switch to English
    assert change_language(driver, "Globe", "English"), "Failed to change language to English"
'''
def test_change_language_to_hindi(driver):
    # Switch to Hindi
    assert change_language(driver, "Globe", "हिंदी"), "Failed to change language to Hindi"

def test_change_language_to_japanese(driver):
    # Switch to Japanese
    assert change_language(driver, "Globe", "日本語"), "Failed to change language to Japanese"
'''