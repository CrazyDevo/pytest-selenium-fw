import time

from selenium import webdriver


def get_driver(browser_name="chrome"):
    if browser_name=="chrome":
       driver= webdriver.Chrome()
       driver.maximize_window()
       return driver
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver
    else:
        print("We are not supporting safari I will open Chrome for you")
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

