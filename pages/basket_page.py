from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            'Items list is present'

    def should_have_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE),\
            '"Your basket is empty" message is not present'
