from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_right_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_to_cart_message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE).text
        assert product_name == add_to_cart_message, 'Wrong product name in message'

    def should_be_right_cart_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total_message = self.browser.find_element(*ProductPageLocators.CART_TOTAL_MESSAGE).text
        assert product_price == cart_total_message, 'Wrong cart total'
