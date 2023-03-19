from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_at_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.FIRST_ITEM_AT_CART),\
            'The cart is not empty, but should be'

    def should_be_empty_cart_message(self):
        empty_cart_message = self.browser.find_element(*BasketPageLocators.EMPTY_CART_MESSAGE).text
        assert 'Your basket is empty.' in empty_cart_message,\
            'There is no empty cart message, but should be'
