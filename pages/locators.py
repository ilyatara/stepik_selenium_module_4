from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.ID, 'login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    USER_ICON = (By.CLASS_NAME, 'icon-user')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    REG_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REG_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REG_PASSWORD_CONFIRM_FIELD = (By.ID, 'id_registration-password2')
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_PRODUCT_NOTIFICATION = (By.CSS_SELECTOR, '.alert:nth-of-type(1) .alertinner')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert:nth-of-type(1) .alertinner strong')
    BASKET_PRICE_NOTIFICATION = (By.CSS_SELECTOR, '.alert:nth-of-type(3) .alertinner')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert:nth-of-type(3) .alertinner strong')


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
