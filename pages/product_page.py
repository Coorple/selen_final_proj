import time

from selen_final_proj.pages.base_page import BasePage
from selen_final_proj.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def special_event(self):
        self.browser.find_element(*ProductPageLocators.ADD_BTN).click()
        self.solve_quiz_and_get_code()
        #time.sleep(40)
        assert self.browser.find_element(*ProductPageLocators.BOOK_ADDED_NAME).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, \
            "Wrong book's name in pop-in message "
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == \
               self.browser.find_element(*ProductPageLocators.CART_PRICE).text, \
            "Different prices of book in cart and page "

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BTN).click()


    def check_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message has appeared'

    def succes_msg_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success massage has not dissapeared'


