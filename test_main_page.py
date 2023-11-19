from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/')
    login_link = browser.find_element(By.ID, 'login_link')
    login_link.click()
