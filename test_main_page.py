from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_login_page_opens(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/'
    main_page = MainPage(browser, url)
    main_page.open()
    # ACT
    main_page.go_to_login_page()
    # ASSERT
    login_page = LoginPage(browser, url)
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    login_page.should_be_login_page()
