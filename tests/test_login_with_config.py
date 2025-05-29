import time

import pytest

from pages.login_page import LoginPage
from utils.configuration_reader import read_config


@pytest.fixture
def browser():
    # set up
    from utils.driver_factory import get_driver
    driver=get_driver()

    yield driver

    # tear down

    time.sleep(5)
    driver.quit()


def test_valid_login(browser):
    config_data = read_config()
    login_page=LoginPage(browser)
    login_page.load()
    username=config_data["login"]["username"]
    password=config_data["login"]["password"]
    login_page.login(username,password)
    login_page.is_login_successful()

