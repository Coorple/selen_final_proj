from selen_final_proj.pages.base_page import BasePage
from selen_final_proj.pages.locators import CartPageLocators


class BasketPage(BasePage):
    def empty_car_check(self):
        assert self.is_not_element_present(*CartPageLocators.PURCHASES_IN_CART)

    def empty_cart_message(self):
        assert self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE).text.rsplit('.')[0]\
               == 'Your basket is empty'