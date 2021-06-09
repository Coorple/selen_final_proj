import time

import pytest

from selen_final_proj.pages.basket_page import BasketPage
from selen_final_proj.pages.product_page import ProductPage

test_links = []
with open("links_for_test.txt") as f:
    test_links = f.readlines()
test_links = [line.rstrip('\n') for line in test_links]


# @pytest.mark.parametrize('link', test_links)
@pytest.mark.skip()
def test_special_event(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.special_event()


@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.check_success_msg()


@pytest.mark.skip()
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.check_success_msg()


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.succes_msg_dissapeared()


@pytest.mark.skip()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip()
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.click_on_cart()
    #page = BasketPage(browser, browser.current_url)
    page.empty_car_check()
    page.empty_cart_message()
