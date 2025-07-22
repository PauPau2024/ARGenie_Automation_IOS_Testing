
# Android Automation Testing Framework

## Overview

This project provides an automated testing framework for Android applications using **Appium** and **Python (pytest)**. It allows developers and QA teams to write and run UI tests across real devices or emulators to ensure application quality.

## Tech Stack

* **Language:** Python 3.x
* **Framework:** Pytest
* **Automation Tool:** Appium
* **Device Support:** Android Emulators, Physical Devices, AWS Device Farm 
* **Dependency Manager:** pip

## Project Structure

```
APPPIUM-ANDROID-TEST-AUTOMATION/
├── config/                     # Configuration files (e.g., Appium capabilities)
├── drivers/                    # Driver setup and initialization
│   └── android_driver.py
├── driver_utils.py             # Utility functions for driver management
├── reports/                    # Test execution reports
│   └── logs/
├── resources/                  # Test data and assets
│   └── app/                    # APKs or app references
│   └── screenshots/            # Screenshots captured during test runs
├── tests/                      # Organized test cases
│   ├── test_01_start_up.py
│   ├── test_02_intro_slides.py
│   ├── ...
│   └── test_20_logout.py
├── utils/                      # Helper modules and utilities
├── conftest.py                 # Pytest fixture definitions
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── pytest.ini                  # Pytest configuration
```

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/PauPau2024/ARGenie_Automation_IOS_Testing.git
   cd android-automation
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Appium**

   * Via npm:

     ```bash
     npm install -g appium
     ```
   * Start the Appium server:

     ```bash
     appium
     ```

4. **Set up Android Environment**

   * Android Studio with SDK tools
   * Enable USB debugging on your Android device or emulator

5. **Verify setup**

   ```bash
   adb devices
   ```

## Running the Tests

### Locally:

```bash
pytest -v tests/ --html=reports/report.html
```

### On AWS Device Farm (Optional):

* Upload your test package (e.g., as a `.zip`)
* Use `cmd_line.txt` with:

  ```bash
  pytest tests/ --device-name "Samsung Galaxy S10" --platform-version "10"
  ```

## 🧪 Sample Test Code

```python
def test_login(driver):
    driver.find_element_by_id("com.example:id/username").send_keys("admin")
    driver.find_element_by_id("com.example:id/password").send_keys("admin123")
    driver.find_element_by_id("com.example:id/login").click()
    assert driver.find_element_by_id("com.example:id/dashboard").is_displayed()
```

## 📄 Reporting

* HTML Report:

  ```bash
  pytest --html=reports/report.html
  ```
* Allure support (optional):

  ```bash
  pytest --alluredir=allure-results
  allure serve allure-results
  ```

## 🧠 Best Practices

* Keep test data and locators separate
* Use page object model (POM) for maintainability
* Run tests on both emulators and real devices
* Use CI tools (GitHub Actions, Jenkins) for scheduled runs

## 📬 Contact

For questions or support, feel free to open an [issue](https://github.com/your-username/android-automation/issues) or contact the maintainer.

---

Would you like to include CI/CD instructions, support for multiple environments, or a sample `capabilities.json`?
