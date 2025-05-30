
---

## **Day 1 – Python Recap: Fundamentals & Functions**

### **1st Hour: Python Basics – Variables, Data Types, Loops, Conditions**

#### **1. Variables & Data Types**
In Python, variables are used to store data. Python supports several data types:

```python
# Example: Variable declaration and basic data types
name = "Alice"         # String
age = 25               # Integer
height = 5.5           # Float
is_active = True       # Boolean

print(name, age, height, is_active)
```

#### **2. Loops**
Loops are used to execute a block of code multiple times.

- **For loop:**
```python
# Example: For loop iterating over a list
for i in range(5):   # Loop 5 times
    print(f"Iteration {i + 1}")
```

- **While loop:**
```python
# Example: While loop iterating as long as a condition is true
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1  # Increment counter
```

#### **3. Conditions (If/Else)**
Conditions allow your program to execute code based on specific criteria.

```python
# Example: If/Else statement
num = 10
if num > 5:
    print("Number is greater than 5")
else:
    print("Number is 5 or less")
```

---

### **2nd Hour: Functions, Modules, Imports, JSON, File Handling**

#### **1. Functions**
Functions allow you to bundle code into reusable blocks.

```python
# Example: Function to add two numbers
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(f"Sum is: {result}")
```

#### **2. Modules and Imports**
You can split code into separate files (modules) and import them when needed.

**Example: `math_utils.py` (module)**
```python
# math_utils.py
def multiply(a, b):
    return a * b
```

**Example: Using the `math_utils.py` module**
```python
# main.py
from math_utils import multiply

result = multiply(4, 5)
print(f"Multiplication result: {result}")
```

#### **3. Working with JSON**
Python has built-in support for working with JSON, a popular format for storing and exchanging data.

**Example: Reading JSON**
```python
import json

# Assuming config.json looks like this:
# { "username": "admin", "password": "secret" }
def read_config():
    with open('config.json') as f:
        return json.load(f)

config = read_config()
print(config['username'], config['password'])
```

#### **4. File Handling**
Reading and writing files in Python is essential for data processing.

**Example: Writing to a file**
```python
with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("Writing to file in Python.")
```

**Example: Reading from a file**
```python
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)
```

---

### **3rd Hour: Create a Utility to Read from `config.json`**

Now, we’ll create a utility that reads a **`config.json`** file.

#### **1. Create `config.json`**
**config.json**
```json
{
  "url": "https://the-internet.herokuapp.com/login",
  "username": "tomsmith",
  "password": "SuperSecretPassword!"
}
```

#### **2. Create Utility to Read the `config.json`**
We'll write a function that loads the `config.json` file and returns the contents.

**utils/config_reader.py**
```python
import json

def read_config():
    with open('config.json') as f:
        return json.load(f)

# Test the function
if __name__ == "__main__":
    config = read_config()
    print(f"URL: {config['url']}")
    print(f"Username: {config['username']}")
    print(f"Password: {config['password']}")
```

---

### **Summary of Day 1**
- We started with basic Python concepts, including variables, loops, and conditions.
- We covered how to define functions and work with Python modules, imports, and file handling.
- Finally, we created a utility to read values from a `config.json` file, which we’ll use for test configuration later in the framework.

---

