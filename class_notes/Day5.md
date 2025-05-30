
---

## **Day 5 – Parametrize, Reporting, Final Polish**

### **1st Hour: Use `@pytest.mark.parametrize` for Multiple Login Cases**

One of the strengths of **pytest** is the ability to easily parametrize tests using `@pytest.mark.parametrize`. This allows us to run the same test with multiple sets of data, which is particularly useful for testing login functionality with different valid and invalid credentials.

#### **Step 1: Define Multiple Test Data**

We will parametrize the login test to check multiple combinations of valid and invalid usernames and passwords.

Example `test_login.py`:

```python
import pytest
from utils.config_reader import read_config
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("tomsmith", "SuperSecretPassword", True),  # valid login
        ("tomsmith", "wrongpassword", False),  # invalid password
        ("wronguser", "SuperSecretPassword", False),  # invalid username
        ("", "", False),  # empty credentials
    ]
)
def test_login(username, password, expected_result, browser):
    config = read_config()
    login_page = LoginPage(browser)
    login_page.load(config['login']['url'])
    login_page.login(username, password)
    
    if expected_result:
        assert login_page.is_login_successful() is True
    else:
        assert login_page.get_error_message() == "Your username is invalid!"  # Or any relevant error message
```

In this code:

- `@pytest.mark.parametrize` takes a list of **test cases**. Each test case is a tuple containing `username`, `password`, and the expected result.
- The `test_login` function will be run for each combination of the username and password.

#### **Step 2: Run Parametrized Test**

You can run the tests normally using `pytest`:

```bash
pytest
```

This will run the test for all the provided sets of data.

---

### **2nd Hour: Add Reporting (Allure, HTML, or Logging)**

To improve the visibility of test results, adding **reports** is essential. We’ll integrate **Allure** reports for rich, HTML-based reporting, but we will also mention **HTML reports** and **logging** for alternatives.

#### **Step 1: Install Allure Reporting**

Allure provides detailed reports with beautiful graphs and logs. To use Allure with `pytest`, you need to install the necessary dependencies.

```bash
pip install allure-pytest
```

Additionally, make sure to install **Allure Commandline** on your machine to generate reports. Download it from [Allure’s official site](https://allure.qatools.ru/).

#### **Step 2: Add Allure Reporting to `pytest`**

In your `pytest.ini` file (or create one if it doesn’t exist), you can enable Allure reporting by adding the following configuration:

```ini
[pytest]
addopts = --alluredir=allure-results
```

Now, after running the tests, Allure will generate results in the `allure-results` folder.

#### **Step 3: Run Tests and Generate Allure Report**

Run your tests using `pytest`:

```bash
pytest
```

After the tests have finished, generate the Allure report:

```bash
allure serve allure-results
```

This will launch a local server and show the results in a browser.

#### **Step 4: Add HTML Reporting (Alternative)**

If you prefer a simpler HTML report, you can use `pytest-html`. Install it with:

```bash
pip install pytest-html
```

Then run the tests with:

```bash
pytest --html=report.html
```

This will generate a `report.html` file with the test results.

#### **Step 5: Add Logging (Optional)**

Sometimes, logging can be helpful for debugging or capturing detailed runtime information. You can add logging to your tests.

Example logging in `test_login.py`:

```python
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("tomsmith", "SuperSecretPassword", True),
        ("tomsmith", "wrongpassword", False),
        ("wronguser", "SuperSecretPassword", False),
        ("", "", False),
    ]
)
def test_login(username, password, expected_result, browser):
    logger.info(f"Testing login with username: {username} and password: {password}")
    
    config = read_config()
    login_page = LoginPage(browser)
    login_page.load(config['login']['url'])
    login_page.login(username, password)
    
    if expected_result:
        assert login_page.is_login_successful() is True
    else:
        assert login_page.get_error_message() == "Your username is invalid!"
    
    logger.info("Test completed")
```

This will log information during test execution, which can be helpful for debugging or keeping track of test progress.

---

### **3rd Hour: Final Cleanup, Structure, README, Git Init**

Now that you have your tests, parametrization, and reporting set up, it's time to **clean up** your project, organize your files, and create a **README** for documentation. Additionally, we'll initialize a **Git** repository to track your changes.

#### **Step 1: Project Structure**

Ensure your project structure is clean and organized:

```
your_project/
├── tests/
│   ├── test_login.py
│   └── ...
├── pages/
│   ├── login_page.py
│   └── ...
├── utils/
│   ├── config_reader.py
│   └── ...
├── config.json
├── pytest.ini
└── requirements.txt
```

- **`tests/`**: Contains all your test files.
- **`pages/`**: Contains page object models (like `login_page.py`).
- **`utils/`**: Utility functions (like `config_reader.py`).
- **`config.json`**: Store dynamic test data here.
- **`pytest.ini`**: Configuration for pytest.
- **`requirements.txt`**: List of dependencies.

#### **Step 2: Write a README File**

A **README.md** file is essential for describing your project, installation instructions, usage, and any other important details.

Example `README.md`:

```markdown
# Selenium Pytest Framework

## Project Overview
This is a Python-based automation framework for testing web applications using **Selenium**, **Pytest**, and **Page Object Model**.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`

## Features
- Parametrized login tests with multiple cases
- Reporting with Allure
- Dynamic browser selection and headless mode using CLI options
```

#### **Step 3: Initialize Git**

Finally, initialize a Git repository to version control your project:

```bash
git init
git add .
git commit -m "Initial commit"
```

Push it to your remote repository (GitHub, GitLab, etc.):

```bash
git remote add origin <your-repository-url>
git push -u origin master
```

---

### **Summary of Day 5**

- We learned how to **parametrize** tests with `@pytest.mark.parametrize` to test multiple sets of login credentials.
- We added **reporting** with Allure for rich HTML reports and **HTML reports** with `pytest-html`. We also covered **logging**.
- We completed the **final cleanup**, organized the project structure, wrote a **README**, and initialized a **Git** repository.

