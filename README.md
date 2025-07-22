# **Documentation: Running Tests on AWS Device Farm**

## **Overview**

This project is designed for automated testing of mobile applications using Appium and Python. It utilizes the **pytest** framework to execute tests. This documentation provides a step-by-step guide on how to set up, configure, and run your tests on **AWS Device Farm**.

## **Project Structure**

The project structure is as follows:

```
├── cmd_line.txt                  # Command line instructions for Device Farm
├── config                         # Appium and device configurations
│   ├── appium_config.json         # Appium-specific configuration
│   ├── env_config.json            # Environment configuration for Device Farm
│   ├── ios_capabilities.json     # iOS-specific capabilities for Device Farm
│   └── ios_device_farm_capabilities.json # iOS Device Farm capabilities
├── demo_test                      # Sample test files
│   └── test_01_app_startup.py     # Test scripts
├── drivers                        # Appium driver utilities for interacting with devices
│   ├── ios_driver.py              # iOS driver setup
├── pytest.ini                     # pytest configuration
├── README.md                      # Project overview
├── reports                        # Test reports (logs, HTML, JUnit, etc.)
│   ├── console
│   ├── html
│   ├── logs
│   └── xml
├── requirements.txt               # Python dependencies
├── resources                      # App and screenshot resources
├── tests                          # Test cases
├── utils                          # Utility functions for tests
└── config                         # Configuration files for device capabilities
```

---

### **1. AWS Account and Device Farm Setup**

Ensure that you have an **AWS account** with access to **Device Farm**. Access the AWS Device Farm console here: [AWS Device Farm Console](https://console.aws.amazon.com/devicefarm).

Create a New Project within the Deivce Farm:

1. **Choose Application**:
   Upload your mobile application's APK (Android) or IPA (iOS) file to Device Farm for testing.

2. **Configure**:

   * **Setup Test Framework**:
     Choose the test type you want to use. If you don't have custom test scripts, select **Built-in: Fuzz** to let AWS automatically fuzz test your app.

     * **Upload Appium Python Tests**: If you have written your own Appium Python tests, upload a `.zip` file containing your tests.
     * **Advanced Configuration (Optional)**: Configure any additional settings or advanced options based on your test requirements.

3. **Select Devices**:
   Choose the device pool (Android/iOS) where you want to run your tests.

4. **Specify Device State**:
   Configure settings such as device locale, radio states, and network profiles to customize the environment in which your tests will run.

5. **Review and Start Run**:
   Review all your settings and configurations. Once everything looks good, click **Start Run** to begin the test execution on your selected devices.


---
### **2. Appium Configuration**

In the `config` folder, make sure that your Appium configuration files (e.g., `appium_config.json`, `ios_capabilities.json`) are properly set up to match your target devices.

Example (`ios_device_farm_capabilities.json`):

```json
{
        "platformName": "iOS",
        "appium:deviceName": "ZD22224VV3",
        "appium:automationName": "XCUITest",
        "appium:connectHardwareKeyboard": true,
        "appium:autoAcceptAlerts": true
}
```
---
### **3. Test Setup**

Ensure the test files are located in the `tests` folder. These tests are written using the **pytest** framework. Each test case in the `tests` folder contains functional tests for the mobile app.

The Capabilities are being used using `conftest.py` which is allowing the Generation of Drivers for the Device Farm.

Example (`tests/test_01_app_startup.py`):

```python
import pytest
from utils.startup import app_startup

def test_app_startup():
    assert app_startup() == "App Started"
```
---
### **4. Setting up the Test_Bundle Zip Configuration File**

We **strongly recommend** setting up a **Python virtual environment** for developing and packaging the test cases. This helps ensure that only the necessary dependencies are included in your test package, preventing any unnecessary packages from being bundled.

1. **Clone the GitHub repository**:

   Start by cloning the repository that contains the tests and necessary files:

   ```bash
   $ git clone https://github.com/PauPau2024/ARGenie_Automation_IOS_Testing.git
   $ cd ARGenie_Automation_IOS_Testing
   ```

2. **Activate the already existing virtual environment**:

   ```bash
   $ source bin/activate
   ```

   **Tip:**

   * Do **not** create a virtual environment with the `--system-site-packages` option. This would allow your virtual environment to inherit global packages, which can lead to unnecessary dependencies being included in your test package.
   * Ensure that your tests do not rely on dependencies that require native libraries, as these libraries may not be present in the Device Farm instances where your tests are run.

3. **Installing dependencies for our virtual environment**:

   ```bash
   $ pip install pytest
   ```

4. **Collecting all the Existing Test Cases**:
   By default, Device Farm expects your tests to be stored in the `tests/` directory. You can use the following command to list all the files in the `tests/` folder:

   ```bash
   $ pytest --collect-only ./tests/
   ```

   Confirm that these files contain the test suites you intend to run on Device Farm. For example:

   ```
   tests/
   tests/my-first-tests.py
   tests/my-second-tests.py
   ```

   Confirm that the output displays the tests you want to run on Device Farm.

5. **Clean up cached files**:
   It's important to clean up any Python bytecode files or caches in your `tests/` folder before packaging. Use the following commands:

   ```bash
   $ find . -name '__pycache__' -type d -exec rm -r {} +
   $ find . -name '*.pyc' -exec rm -f {} +
   $ find . -name '*.pyo' -exec rm -f {} +
   $ find . -name '*~' -exec rm -f {} +
   ```

6. **Create the zipped test package**:
   Device Farm expects a specific folder structure in the zipped test package. Some archiving tools may alter this structure, so we recommend using command-line utilities rather than file managers like Finder or Windows Explorer.

   A Test_Bundle.zip file already exist in the Repository. If any changes are made in the repository cosider Zipping an New Test_Bundle.zip file for the running the new changes.


   * For **Python 3**, you can directly package your tests and `requirements.txt` into a zip file:

     ```bash
     $ zip -r test_bundle.zip ./
     ```

---

### **5. AWS Device Farm .yml file Configuration**

Modify the test section of the default yaml file with the below making sure for proper runnign of my python command.

```yaml
  # The test phase contains commands for running your tests.
test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium Python test"
      
      # The following command runs your Appium Python test.
      # Please refer to "https://docs.pytest.org/en/latest/usage.html" for more options
      # on running pytest from the command line.
      - python -m pytest ./tests/ --log-cli-level=INFO   --log-file=pytest.log   --junitxml=junit.xml   --html=report.html   --self-contained-html   --maxfail=5   --capture=tee-sys   2>&1 | tee console_output.txt
```
Modify the artifacts section to `$DEVICEFARM_REPORT_LOGS` for proper storing of all the reports and log files.
```yaml
post_test:
    commands:
     - mv pytest.log  $DEVICEFARM_LOG_DIR
     - mv junit.xml  $DEVICEFARM_LOG_DIR
     - mv report.html  $DEVICEFARM_LOG_DIR
     - mv console_output.txt  $DEVICEFARM_LOG_DIR

artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```
An existing `test_bundle.yml` is present in the repository for using in the Device Farm.


### **9. Retrieving Test Artifacts**

Once the tests are completed, Device Farm will automatically generate and collect the following artifacts 

* **JUnit XML Report**: Located at `$DEVICEFARM_LOG_DIR/junit.xml`
* **HTML Test Report**: Located at `$DEVICEFARM_LOG_DIR/report.html`
* **Console Logs**: Located at `$DEVICEFARM_LOG_DIR/console_output.txt`
* **Pytest Logs**: Located at `$DEVICEFARM_LOG_DIR/pytest.log`

You can download these artifacts from the Device Farm console under the **Test Results** section.

### **10. Troubleshooting**

* **Device Connection Issues**: Verify that the device capabilities in the `config/ios_device_farm_capabilities.json` are correct.
* **Failed Tests**: Review the logs in `$DEVICEFARM_LOG_DIR/pytest.log` to identify why tests failed.
* **Timeouts**: Ensure that your tests have sufficient wait times or polling intervals to accommodate device responsiveness.

---

## **Conclusion**

This documentation provides a step-by-step guide to running your **Appium** tests on **AWS Device Farm**. Ensure your project is configured with the correct capabilities, tests, and artifacts setup before uploading the package to Device Farm.

By following the instructions above, you can run automated tests across multiple devices with detailed reports and logs available for review.

---

Let me know if you need further clarifications or additional details in the documentation! // Give me al the headets 
