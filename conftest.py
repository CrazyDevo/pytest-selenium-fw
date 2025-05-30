import time
from email.policy import default

import pytest
from utils.driver_factory import get_driver_2

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Chrome browser: chrome or firefox")
    parser.addoption("--headless",action="store_true",default=False,help="You can run in headless mode")
    parser.addoption("--env",action="store",default="test1",help="You can control your environment from here")




@pytest.fixture(scope="function")
def my_driver(request):
    browser_name=request.config.getoption("--browser")
    headless_mode=request.config.getoption("--headless")

    driver=get_driver_2(browser_name,headless_mode)

    yield driver

    time.sleep(5)
    driver.quit()