import time

import pytest

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
