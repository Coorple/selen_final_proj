from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_BTN = (By.CSS_SELECTOR, '.btn-group a.btn-default')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_ADDED_NAME = (By.XPATH, '// *[ @ id = "messages"] / div[1] / div / strong')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')


class CartPageLocators:
    PURCHASES_IN_CART = (By.CSS_SELECTOR, '.basket-title')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
