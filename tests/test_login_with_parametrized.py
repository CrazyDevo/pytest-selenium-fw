from pickle import FALSE

import pytest

from pages.login_page import LoginPage
from utils.configuration_reader import read_config

@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        ("tomsmith","SuperSecretPassword!",True), # valid login
        ("tomsmith", "wrongPassword!", False),  # invalid login
        ("wrongusername", "wrongPassword!", False),  # invalid login
        ("", "", False)  # empty creds
    ]
)
def test_valid_login(username,password,expected_result,my_driver):

    login_page=LoginPage(my_driver)
    login_page.load()
    username=username
    password=password
    login_page.login(username,password)

    if expected_result:
        login_page.is_login_successful()
    else:
      assert "invalid" in login_page.get_text_login_message()



