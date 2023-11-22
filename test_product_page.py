import time

import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators


@pytest.mark.need_review
@pytest.mark.parametrize(
    'promo',
    ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
     pytest.param('offer7', marks=pytest.mark.xfail(reason="won't fix")),
     'offer8', 'offer9']
)
def test_guest_can_add_product_to_basket(browser, promo):
    # ARRANGE
    url = f'http://selenium1py.pythonanywhere.com/' \
          f'catalogue/coders-at-work_207/?promo={promo}'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # ASSERT
    page.should_have_product_added(page.product_name)
    page.should_have_basket_price(page.product_price)


@pytest.mark.xfail
def test_guest_can_not_see_success_message_after_adding_product_to_basket(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    # ASSERT
    assert page.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)


def test_guest_can_not_see_success_message(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    # ACT
    page.open()
    # ASSERT
    assert page.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    # ASSERT
    assert page.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)


def test_guest_should_see_login_link_on_product_page(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url)
    # ACT
    page.open()
    # ASSERT
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, url)
    product_page.open()
    # ACT
    product_page.go_to_login_page()
    # ASSERT
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_can_not_see_product_in_basket_opened_from_product_page(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, url)
    # ACT
    product_page.open()
    product_page.go_to_basket()
    # ASSERT
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_items()
    basket_page.should_have_basket_empty_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, url)
        login_page.open()
        timestamp = int(time.time())
        login_page.register_new_user(email=f'{timestamp}@test.com',
                                     password=f'{timestamp}')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # ARRANGE
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        # ACT
        page.add_to_basket()
        # ASSERT
        page.should_have_product_added(page.product_name)
        page.should_have_basket_price(page.product_price)

    def test_user_can_not_see_success_message(self, browser):
        # ARRANGE
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        # ACT
        page.open()
        # ASSERT
        assert page.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)
