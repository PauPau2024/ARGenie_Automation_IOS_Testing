Here’s a **README** file that outlines the steps for setting up your **Appium Python iOS Testing Project**.

### `README.md`

````markdown
# ARGenie_Automation_IOS_Testing

This repository contains the Appium-based Python test automation framework for testing iOS applications.

## Requirements

Before you start, ensure you have the following dependencies installed:

- **Python 3.8+**  
  Make sure you have Python 3.8 or a later version installed on your system.

- **Appium**  
  Install Appium for driving mobile devices via its server. Follow the [Appium installation guide](https://appium.io/docs/en/about-appium/intro/) for instructions.

- **Xcode** (for macOS)  
  If you're running tests on an iOS device or simulator, you'll need Xcode installed for building and running the iOS tests.

- **Node.js**  
  Appium requires Node.js. You can install it from [here](https://nodejs.org/).

- **Xcode Command Line Tools** (for macOS)  
  Install the necessary command line tools for working with Xcode and iOS simulators.

- **BrowserStack** (Optional, if you're using BrowserStack for remote testing)  
  [BrowserStack](https://www.browserstack.com) allows you to run tests on real devices on the cloud.

## Setting Up the Project

### Step 1: Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/PauPau2024/ARGenie_Automation_IOS_Testing.git
````

### Step 2: Install Dependencies

Navigate to the project directory:

```bash
cd ARGenie_Automation_IOS_Testing
```

Install the required Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries, including `Appium-Python-Client`, `pytest`, and others required for iOS testing.

### Step 3: Set Up Appium

* Install Appium globally:

  ```bash
  npm install -g appium
  ```

* Start the Appium server:

  ```bash
  appium
  ```

  By default, Appium runs on `http://localhost:4723/wd/hub`. You can configure this if you are using a different server (e.g., BrowserStack).

### Step 4: Configure Desired Capabilities

The **desired capabilities** for running tests on an iOS device or simulator are located in the `config/ios_capabilities.json` file. You should configure the following:

* **platformName**: iOS (or Android, if you switch to Android testing)
* **platformVersion**: Your iOS version (e.g., 16.0)
* **deviceName**: The device or simulator you want to use
* **app**: The path to your `.ipa` or `.app` file (the app you want to test)
* **appium\:automationName**: XCUITest (for iOS)
* **appium\:deviceOrientation**: portrait or landscape
* **appium\:autoAcceptAlerts**: true (auto-accept any alerts that appear)

You may also want to configure other settings in **`env_config.json`** for services like BrowserStack if you are running your tests remotely.

### Step 5: Running Tests Locally or Remotely

#### Running Locally

To run the tests locally on your iOS device or simulator, use the following command:

```bash
pytest tests/
```

This will run all the test cases in the `tests/` folder.

#### Running on BrowserStack

If you are running your tests remotely on BrowserStack or another cloud-based service, make sure your **`env_config.json`** contains the correct URL for the remote server.

Ensure your BrowserStack credentials are set up correctly in **`env_config.json`**:

```json
{
  "base_url": "https://your_browserstack_username:your_browserstack_key@hub-cloud.browserstack.com/wd/hub",
  "browserstack_user": "your_browserstack_username",
  "browserstack_key": "your_browserstack_key",
  "app_url": "bs://your_browserstack_app_url"
}
```

Then, you can run the tests in the same way:

```bash
pytest tests/
```

### Step 6: Viewing Test Results

The test results will be printed in the terminal after the tests complete. You can also generate more detailed reports, including **HTML reports**, by running:

```bash
pytest --maxfail=5 --disable-warnings -v --html=report.html
```

This will generate a **`report.html`** file that you can view in your browser.

## Folder Structure

Here is the project directory structure:

```plaintext
ARGenie_Automation_IOS_Testing/
├── config/                # Configuration files (e.g., iOS capabilities, environment config)
├── drivers/               # Appium driver setup
├── tests/                 # Test scripts for different functionalities
├── utils/                 # Helper functions and utilities for tests
├── requirements.txt       # Python dependencies
├── pytest.ini             # pytest configuration
├── run_tests.py           # Main script to run the tests
└── README.md              # Project setup and documentation
```


Let me know if you'd like to add more details or customize it further!
```
