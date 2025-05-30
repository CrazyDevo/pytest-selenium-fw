
---

## **Day 4 – Configuration, Fixtures, Headless, CLI Options**

### **1st Hour: Use `config.json` or `.properties` for Dynamic Data**

For **dynamic configuration**, we will store our browser settings (like `username`, `password`, and `URL`) in a **JSON** file (`config.json`) or a `.properties` file. In this case, we will use **JSON** because it's widely used and easy to work with in Python.

#### **Step 1: Create a `config.json` File**

Create a `config.json` file in your project’s root directory to store your dynamic data. This will include the credentials and URLs.

Example `config.json`:

```json
{
  "login": {
    "username": "tomsmith",
    "password": "SuperSecretPassword",
    "url": "https://the-internet.herokuapp.com/login"
  },
  "headless": false,
  "browser": "chrome"
}
```

#### **Step 2: Create a Utility to Read Data from `config.json`**

In the `utils/` folder, create a `config_reader.py` file that will read and parse the `config.json` file.

Example `config_reader.py`:

```python
import json

def read_config():
    with open("config.json", "r") as file:
        config_data = json.load(file)
    return config_data
```

#### **Step 3: Use the Config in Your Tests**

Now, update your tests and page objects to use the values from the `config.json` file.

In your `test_login.py`, you can access the configuration like this:

```python
from utils.config_reader import read_config
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    config = read_config()
    browser_name = config['browser']
    driver = get_driver(browser_name)
    yield driver
    driver.quit()

def test_valid_login(browser):
    config = read_config()
    login_page = LoginPage(browser)
    login_page.load(config['login']['url'])
    login_page.login(config['login']['username'], config['login']['password'])
    assert login_page.is_login_successful() is True
```

---

### **2nd Hour: Add CLI Options `--browser` and `--headless` in `conftest.py`**

You can use **CLI options** to dynamically set the browser type and whether or not the test should run in **headless mode** (i.e., without opening a browser window). This can be set using `pytest` options.

#### **Step 1: Modify `conftest.py` to Add CLI Options**

You can use the `pytest_addoption` hook to add CLI options for `--browser` and `--headless`.

Example `conftest.py`:

```python
import pytest
from utils.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    driver = get_driver(browser_name, headless)
    yield driver
    driver.quit()
```

In this code:

- The `--browser` option allows the user to choose between **Chrome** or **Firefox**.
- The `--headless` option, if set, runs the tests in **headless** mode (without a UI).

#### **Step 2: Pass CLI Options in Command Line**

To run your tests with different browsers and headless mode, you can pass the options when running `pytest`.

For Chrome in headless mode:

```bash
pytest --browser=chrome --headless
```

For Firefox in headless mode:

```bash
pytest --browser=firefox --headless
```

For Chrome with UI:

```bash
pytest --browser=chrome
```

---

### **3rd Hour: Make Test Flow Dynamic Using CLI + Config Values**

Now that you’ve set up dynamic data (from `config.json`) and CLI options, we will make the test flow dynamic based on these inputs.

You can combine the **CLI options** with the values from the `config.json` file to modify your test behavior.

#### **Step 1: Modify `test_login.py` to Combine CLI and Config Values**

In your `test_login.py`, you can dynamically change the flow of your tests by using both the **CLI options** and the **config values**.

Example `test_login.py`:

```python
import pytest
from utils.config_reader import read_config
from pages.login_page import LoginPage

@pytest.fixture
def browser(request):
    config = read_config()
    browser_name = request.config.getoption("--browser") or config['browser']
    headless = request.config.getoption("--headless") or config['headless']
    
    driver = get_driver(browser_name, headless)
    yield driver
    driver.quit()

def test_valid_login(browser):
    config = read_config()
    login_page = LoginPage(browser)
    login_page.load(config['login']['url'])
    login_page.login(config['login']['username'], config['login']['password'])
    assert login_page.is_login_successful() is True

def test_invalid_login(browser):
    config = read_config()
    login_page = LoginPage(browser)
    login_page.load(config['login']['url'])
    login_page.login(config['login']['username'], "wrongpassword")
    assert login_page.get_error_message() == "Your username is invalid!"
```

In this code:

- If no `--browser` or `--headless` option is provided via the CLI, it falls back to the default values in the `config.json` file.
- This allows your tests to be dynamically configurable from both the CLI and the `config.json` file.

#### **Step 2: Run Tests with Both CLI and Config Values**

You can run your tests with different combinations of **browser type** and **headless mode** using the CLI options:

For Chrome in headless mode:

```bash
pytest --browser=chrome --headless
```

For Firefox with UI (using the `config.json`):

```bash
pytest --browser=firefox
```

---

### **Summary of Day 4**

- We **read data from `config.json`** to dynamically control values like `username`, `password`, and `url`.
- We added **CLI options** in `conftest.py` to specify `--browser` and `--headless`.
- We made the test flow **dynamic** by combining **CLI** options with **config values**, allowing flexible configuration without changing the code.

