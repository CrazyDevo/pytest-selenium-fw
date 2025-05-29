from email.policy import default

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Chrome browser: chrome or firefox")
    parser.addoption("--headless",action="store_true",default=False,help="You can run in headless mode")



@pytest.fixture(scope="function")
def my_driver(request):
    browser_name=request.config.getoption("--browser")
    headless_mode=request.config.getoption("--headless")