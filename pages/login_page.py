from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("login") >= 0, "Wrong login page url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print("kek")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()

