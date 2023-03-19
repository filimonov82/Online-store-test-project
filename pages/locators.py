from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    FIRST_ITEM_AT_BASKET = (By.CSS_SELECTOR, '#basket_formset .basket-items:nth-of-type(1)')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary[value="Register"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1).alert.alert-success')
