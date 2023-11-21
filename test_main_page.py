from selenium.webdriver.common.by import By


def go_to_login_page(browser):
    login_link = browser.find_element(By.ID, 'login_link')
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/')
    go_to_login_page(browser)
