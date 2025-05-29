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



def get_driver_2(browser_name,headless_mode):
    if browser_name=="chrome":
       chrome_options=webdriver.ChromeOptions()
       if headless_mode:
           chrome_options.add_argument("--headless=new")
           chrome_options.add_argument("--windows-size=1920,1080")
       driver= webdriver.Chrome(options=chrome_options)
       driver.implicitly_wait(10)
       return driver
    elif browser_name=="firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless_mode:
            firefox_options.add_argument("--headless=new")
            firefox_options.add_argument("--windows-size=1920,1080")
        driver = webdriver.Firefox(options=firefox_options)
        driver.implicitly_wait(10)
        return driver
    else:
        print("We are not supporting safari I will open Chrome for you")
        chrome_options = webdriver.ChromeOptions()
        if headless_mode:
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--windows-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        return driver

