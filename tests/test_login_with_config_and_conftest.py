
from pages.login_page import LoginPage
from utils.configuration_reader import read_config


def test_valid_login(my_driver):
    config_data = read_config()
    login_page=LoginPage(my_driver)
    login_page.load()
    username=config_data["login"]["username"]
    password=config_data["login"]["password"]
    login_page.login(username,password)
    login_page.is_login_successful()

