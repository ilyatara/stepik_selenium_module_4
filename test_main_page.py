from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_can_not_see_product_in_basket_opened_from_main_page(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    # ACT
    page.go_to_basket()
    # ASSERT
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_items()
    basket_page.should_have_basket_empty_message()
