from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # ARRANGE
    url = 'http://selenium1py.pythonanywhere.com/' \
          'catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, url)
    page.open()
    # ACT
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # ASSERT
    page.should_have_product_added_notification()
    page.should_have_basket_price_notification()
