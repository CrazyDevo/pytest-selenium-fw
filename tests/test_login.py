import time

import pytest

from pages.login_page import LoginPage


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
    login_page=LoginPage(browser)
    login_page.load()
    login_page.login("tomsmith","SuperSecretPassword!")
    login_page.is_login_successful()