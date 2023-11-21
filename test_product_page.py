from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/' \
          'catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # ASSERT
    page.should_have_product_added(page.product_name)
    page.should_have_basket_price(page.product_price)
