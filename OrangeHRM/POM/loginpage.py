from Utilities.XLUtils import *


locator = read_locators("locators")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def usernaem_text_field(self, un):
        name = self.driver.find_element(*locator["username_tf"])
        name.send_keys(un)
    def password_text_field(self,pwd):
        password = self.driver.find_element(*locator["password_tf"])
        password.send_keys(pwd)

    def login_button(self):
        button = self.driver.find_element(*locator["login_btn"])
        button.click()