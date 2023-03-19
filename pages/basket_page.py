from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_at_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FIRST_ITEM_AT_BASKET),\
            'The basket is not empty, but should be'

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty.' in empty_basket_message,\
            'There is no empty basket message, but should be'
