import pytest

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.skip
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


def test_guest_can_not_see_success_message_after_adding_product_to_basket(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    # ASSERT
    assert page.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)


def test_guest_cant_see_success_message(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    # ACT
    page.open()
    # ASSERT
    assert page.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)


def test_message_disappeared_after_adding_product_to_basket(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    # ASSERT
    assert page.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION)
