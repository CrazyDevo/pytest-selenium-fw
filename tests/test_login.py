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

def test_invalid_login(browser):
    login_page=LoginPage(browser)
    login_page.load()
    login_page.login("invalid","invalid")
    print(login_page.get_text_login_message())
    assert "invalid" in login_page.get_text_login_message()
