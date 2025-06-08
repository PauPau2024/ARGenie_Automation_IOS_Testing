from utils.main_tabs import get_main_tabs_status

def test_main_tabs_present(driver):
    """
    Test to verify that all three main tabs ('Home', 'Session', 'Profile') are present.
    It will fail with a message indicating which tabs are missing.
    """
    status = get_main_tabs_status(driver)  # Get the status of the tabs
    missing_tabs = [tab for tab, present in status.items() if not present]  # Identify missing tabs

    # Assert that no tabs are missing
    assert not missing_tabs, f"Missing main tab(s): {', '.join(missing_tabs)}"
