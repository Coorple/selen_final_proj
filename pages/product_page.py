import time

from selen_final_proj.pages.base_page import BasePage
from selen_final_proj.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def special_event(self):
        self.browser.find_element(*ProductPageLocators.ADD_BTN).click()
        self.solve_quiz_and_get_code()
        # time.sleep(90)
        assert self.browser.find_element(*ProductPageLocators.BOOK_ADDED_NAME).text == "The shellcoder's handbook", \
            "Wrong book's name in pop-in message "
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == \
               self.browser.find_element(*ProductPageLocators.CART_PRICE).text, \
            "Different prices of book in cart and page "
