
---

## **Day 3 – Selenium Integration + Framework Structure**

### **1st Half Hour: Install Selenium, Pytest, ChromeDriver Setup**

#### **1. Install Selenium**

First, you need to install **Selenium** and **Pytest** in your Python environment. You can do this using `pip`:

```bash
pip install selenium pytest
```

#### **2. Install ChromeDriver**

To run Selenium tests with **Google Chrome**, you'll need **ChromeDriver**. ChromeDriver is a separate executable that Selenium uses to interact with Chrome.

- Download the version of **ChromeDriver** that matches your version of Chrome from here: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- After downloading, make sure **ChromeDriver** is available in your system's **PATH**. You can add its directory to your **PATH** or provide its location explicitly in your tests.

You can also configure ChromeDriver directly in the `get_driver` method if you want to specify the path like this:

```python
from selenium import webdriver

def get_driver(browser_name="chrome"):
    if browser_name == "chrome":
        chrome_driver_path = "/path/to/chromedriver"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Optional: run in headless mode
        return webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    elif browser_name == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
```

Now your setup is ready!

---

### **2nd Hour: Create Project Structure (Tests, Pages, Utils, etc.)**

We'll create a simple **Page Object Model (POM)** structure for your Selenium tests. The main advantage of POM is that it helps separate the web page interaction logic from the actual test logic, which makes the tests more maintainable and scalable.

#### **Example Project Structure**

```
selenium-framework/
│
├── pages/
│   ├── login_page.py
│
├── tests/
│   ├── test_login.py
│
├── utils/
│   ├── driver_factory.py
│
└── conftest.py
```

#### **Explanation of Each Folder/File**

1. **`pages/`** – Contains the page object classes that define methods for interacting with the web elements on the page (e.g., `LoginPage`).
2. **`tests/`** – Contains the test files where you will use the page object classes to perform actual tests.
3. **`utils/`** – Contains helper utility functions, such as a function to create the driver (`get_driver`).
4. **`conftest.py`** – This is used to configure fixtures for the entire test suite (e.g., setting up the browser, creating the driver, etc.).

---

### **3rd Hour: Create LoginPage Using POM, Run First Selenium Test**

#### **1. Create the `LoginPage` (POM) Class**

Let's create the `LoginPage` class inside the **`pages/`** folder. This class will define methods to interact with the login form fields.

```python
# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.ID, "flash")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        return "secure_area" in self.driver.current_url

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
```

#### **2. Create the `test_login.py` File**

Now, let's write a simple test file to test the login functionality using the **`LoginPage`** class.

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    # Setup for the browser and driver, using get_driver utility (similar to Day 2)
    from utils.driver_factory import get_driver
    driver = get_driver(browser_name="chrome")
    yield driver
    driver.quit()

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword")
    assert login_page.is_login_successful() is True

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("tomsmith", "wrongpassword")
    assert login_page.get_error_message() == "Your username is invalid!"
```

#### **3. Running the Test**

Now that we have set up our test, you can run the tests using `pytest`:

```bash
pytest tests/test_login.py
```

If everything is set up correctly, the test will launch Chrome, navigate to the login page, and attempt to log in with the provided credentials. The test will pass if the login is successful or fail if the error message appears.

---

### **Summary of Day 3**

- We set up the necessary **Selenium** and **ChromeDriver** configurations.
- We created a simple **Page Object Model (POM)** with a `LoginPage` class to interact with the login page's web elements.
- We wrote a **Selenium test** using the `LoginPage` class and ran it with Pytest.

