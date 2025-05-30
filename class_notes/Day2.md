
---

## **Day 2 – Python OOP + Pytest Intro**

### **1st Hour: OOP – Classes, `__init__`, Attributes, Methods**

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes. Here's a recap of the basics:

#### **1. Defining a Class and `__init__` Method**

In Python, classes are used to define objects. The `__init__` method is a special method that initializes the object when it is created.

```python
# Example: Defining a simple class
class Person:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance (object) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling the method
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
person2.greet()  # Output: Hello, my name is Bob and I am 25 years old.
```

#### **2. Attributes and Methods**
- **Attributes** are variables that belong to the object.
- **Methods** are functions that belong to the object and can be used to perform actions related to the object.

```python
# Example: Adding more methods
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

    def stop(self):
        print(f"The {self.brand} {self.model} has stopped.")

# Using the class
my_car = Car("Tesla", "Model S")
my_car.drive()  # Output: The Tesla Model S is driving.
my_car.stop()   # Output: The Tesla Model S has stopped.
```

---

### **2nd Hour: Pytest Basics – Assert, Fixtures, Test Structure**

Now, let's look at the basics of **Pytest** and how you can write tests.

#### **1. Writing Tests with Pytest**

Pytest is a testing framework that allows you to write test functions. Test functions in Pytest typically start with `test_` to make it easier for Pytest to identify them.

```python
# Example: Basic test function
def test_addition():
    assert 1 + 1 == 2  # Simple assertion
```

#### **2. Using Assertions**

Assertions are used to check if the results of your code are as expected. Pytest will report a failure if the condition in the `assert` statement is `False`.

```python
def test_subtraction():
    result = 5 - 3
    assert result == 2  # This will pass because 5 - 3 equals 2
```

#### **3. Fixtures in Pytest**

Fixtures are used to set up any required state or resources for your tests. They are commonly used to set up objects or initialize the environment before each test runs.

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
```

#### **4. Test Structure**
Typically, test files are structured in the following way:

- **test_*.py** – Test file
- **test_*.py** contains test functions.
- Test functions contain **assert** statements to verify expected outcomes.

#### Example Folder Structure:
```
tests/
│
├── test_example.py
└── test_sample.py
```

---

### **3rd Hour: Dummy `LoginPage` Class and Test it Using Pytest**

Let's create a **dummy `LoginPage` class** and test it using Pytest.

#### **1. Creating the `LoginPage` Class**

We'll simulate the behavior of a login page using a class that has methods for entering a username, password, and submitting the form.

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        # In a real scenario, we would find the fields by ID and input values
        print(f"Entering username: {username} and password: {password}")
        # Simulate a successful login
        return "secure_area" in self.driver.current_url
```

#### **2. Creating the Test for `LoginPage`**

Now, let's write a simple test using **Pytest** to test the `LoginPage` class.

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    # We are just simulating the browser here
    class Browser:
        current_url = "https://the-internet.herokuapp.com/login"
        def get(self, url):
            self.current_url = url
    return Browser()

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()  # Simulate loading the page
    assert login_page.login("tomsmith", "SuperSecretPassword") == True

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()  # Simulate loading the page
    assert login_page.login("invalid_user", "wrong_password") == False
```

#### **3. Running the Tests**

To run the tests, simply use the `pytest` command in the terminal:

```bash
pytest tests/test_login.py # to run
```

```bash
pytest -v tests/test_login.py # detailed output
```

```bash
pytest -v --tb=short # output for failed tests traceback
```





### **Summary of Day 2**

- We covered **Object-Oriented Programming (OOP)**, focusing on defining classes, methods, and attributes.
- We learned the basics of **Pytest**, including writing tests, using assertions, and working with fixtures.
- Finally, we created a simple **LoginPage class** and wrote Pytest tests for it, simulating the login functionality and checking if the login works as expected.

---

