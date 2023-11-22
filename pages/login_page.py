from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_CONFIRM_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url,\
            f'"login" is not a substring of the current url: {current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM),\
            'Registration form is not present'
