import time

from selenium import webdriver


def get_driver(browser_name="chrome"):
    if browser_name=="chrome":
       driver= webdriver.Chrome()
       driver.implicitly_wait(10)
       driver.maximize_window()
       return driver
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    else:
        print("We are not supporting safari I will open Chrome for you")
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

