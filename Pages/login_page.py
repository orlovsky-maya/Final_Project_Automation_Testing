from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *

class LoginPage(BasePage):
    # Getting

    def get_login_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (LoginFormLocators.LOGIN_BUTTON))

    def get_email_field(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (LoginFormLocators.EMAIL_FIELD))

    def get_password_field(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (LoginFormLocators.PASSWORD_FIELD))

    def get_enter_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (LoginFormLocators.ENTER_BUTTON))

    # Actions
    def go_to_login_form(self):
        self.get_login_button().click()

    def input_email(self, email):
        self.get_email_field().send_keys(email)


    def input_password(self, password):
        self.get_password_field().send_keys(password)

    def click_enter_button(self):
        self.get_enter_button().click()

    # Methods

    def authorization(self, login_name, login_password):
        self.open()
        self.go_to_login_form()
        self.input_email(login_name)
        self.input_password(login_password)
        self.click_enter_button()
        print('User is logged in')
