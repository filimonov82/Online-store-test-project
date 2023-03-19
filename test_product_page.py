from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                                  pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                                               marks=pytest.mark.xfail),
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_right_product_name_in_message()
    product_page.should_be_right_cart_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_at_cart()
    basket_page.should_be_empty_cart_message()
