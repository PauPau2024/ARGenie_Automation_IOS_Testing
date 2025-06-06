from drivers.driver_utils import click_button_by_accessibility,click_by_class_chain

def ar_annotation_feature_sequence(driver):
    assert click_button_by_accessibility(driver, "line.3.horizontal"), \
        "Failed to click 'AR Options' Annotation button"
    assert click_button_by_accessibility(driver, "arrowshape.right.fill"), \
        "Failed to click 'arrowshape.right.fill' Annotation button"
    assert click_button_by_accessibility(driver, "circle"), \
        "Failed to click 'circle' Annotation button"
    assert click_button_by_accessibility(driver, "scribble.variable"), \
        "Failed to click 'scribble.variable' Annotation button"
    assert click_button_by_accessibility(driver, "flashlight.off.fill"), \
        "Failed to click 'Flash-ON Button' after annotation"
    assert click_button_by_accessibility(driver, "flashlight.on.fill"), \
        "Failed to click 'Flash-OFF Button' after annotation"
    assert click_button_by_accessibility(driver, "xmark.circle"), \
        "Failed to click 'close' after annotation"
    assert click_button_by_accessibility(driver, "chevron.down"), \
        "Failed to click 'Close AR Annotaion button' after annotation"
    

def ar_annotation_feature_sequence_with_clearing(driver):
    assert click_button_by_accessibility(driver, "line.3.horizontal"), \
        "Failed to click 'AR Options' Annotation button"
    assert click_button_by_accessibility(driver, "arrowshape.right.fill"), \
        "Failed to click 'arrowshape.right.fill' Annotation button"
    assert click_button_by_accessibility(driver, "xmark.circle"), \
        "Failed to click 'close' after annotation"
    assert click_button_by_accessibility(driver, "chevron.down"), \
        "Failed to click 'Close AR Annotaion button' after annotation"
    
    assert click_button_by_accessibility(driver, "line.3.horizontal"), \
        "Failed to click 'AR Options' Annotation button"
    assert click_button_by_accessibility(driver, "circle"), \
        "Failed to click 'circle' Annotation button"
    assert click_button_by_accessibility(driver, "xmark.circle"), \
        "Failed to click 'close' after annotation"
    assert click_button_by_accessibility(driver, "chevron.down"), \
        "Failed to click 'Close AR Annotaion button' after annotation"
    
    assert click_button_by_accessibility(driver, "line.3.horizontal"), \
        "Failed to click 'AR Options' Annotation button"
    assert click_button_by_accessibility(driver, "scribble.variable"), \
        "Failed to click 'scribble.variable' Annotation button"
    assert click_button_by_accessibility(driver, "xmark.circle"), \
        "Failed to click 'close' after annotation"
    assert click_button_by_accessibility(driver, "chevron.down"), \
        "Failed to click 'Close AR Annotaion button' after annotation"

    assert click_button_by_accessibility(driver, "line.3.horizontal"), \
        "Failed to click 'AR Options' Annotation button"
    assert click_button_by_accessibility(driver, "arrowshape.right.fill"), \
        "Failed to click 'arrowshape.right.fill' Annotation button"
    assert click_button_by_accessibility(driver, "xmark.circle"), \
        "Failed to click 'close' after annotation"
    assert click_button_by_accessibility(driver, "chevron.down"), \
        "Failed to click 'Close AR Annotaion button' after annotation"