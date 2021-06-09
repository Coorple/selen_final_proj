from selen_final_proj.pages.product_page import ProductPage


def test_special_event(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.special_event()