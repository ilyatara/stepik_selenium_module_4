from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    # ADDED_PRODUCT_NOTIFICATION = (By.CSS_SELECTOR, '.alert:nth-of-type(1) .alertinner')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert:nth-of-type(1) .alertinner strong')
    # BASKET_PRICE_NOTIFICATION = (By.CSS_SELECTOR, '.alert:nth-of-type(3) .alertinner')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert:nth-of-type(3) .alertinner strong')
