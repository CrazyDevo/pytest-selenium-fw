from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://the-internet.herokuapp.com/login"
        self.username_textbox=(By.ID,"username")
        self.password_textbox=(By.ID,"password")
        self.login_btn=(By.CSS_SELECTOR,"button[type='submit']")
        self.login_message=(By.ID,"flash")

    def load(self):
        self.driver.get(self.url)


    def login(self,username,password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def is_login_successful(self):
        assert "secure area" in self.driver.find_element(*self.login_message).text
