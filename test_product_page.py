import time

import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize(
    'promo',
    ['offer0',  # 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
     pytest.param('offer7', marks=pytest.mark.xfail(reason="won't fix")),
     'offer8', 'offer9']
)
def test_guest_can_add_product_to_basket(browser, promo):
    url = f'http://selenium1py.pythonanywhere.com/' \
          f'catalogue/coders-at-work_207/?promo={promo}'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_have_product_added(page.product_name)
    page.should_have_basket_price(page.product_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_not_have_success_message()


def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.should_not_have_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_have_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.go_to_basket()
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
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.should_have_product_added(page.product_name)
        page.should_have_basket_price(page.product_price)

    def test_user_cant_see_success_message(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        page.should_not_have_success_message()
