from selenium.webdriver.common.by import By


class BasePageLocators():
    CART_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    FIRST_ITEM_AT_CART = (By.CSS_SELECTOR, '#basket_formset .basket-items:nth-of-type(1)')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    CART_TOTAL_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1).alert.alert-success')
