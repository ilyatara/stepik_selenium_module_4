from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_have_product_added(self, product_name):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert added_product_name == product_name, \
            f'Expected added product name: "{product_name}", got: "{added_product_name}"'

    def should_have_basket_price(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert basket_price == product_price, \
            f'Expected basket price: {product_price}, got: {basket_price}'

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION), \
            'Success message is present'

    def should_have_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION), \
            'Success message haven\'t disappeared'

    @property
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    @property
    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
