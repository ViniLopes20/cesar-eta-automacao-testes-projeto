from src.interface import by_css, by_id, click, open_page, select_option

CUSTOMER_LOGIN_BUTTON = by_css("button[ng-click='customer()']")
NAME_SELECT = by_id("userSelect")
LOGIN_BUTTON = by_css("form button[type='submit']")


def load(driver):
    open_page(driver, "/login")


def login_as_customer(driver, name):
    click(driver, CUSTOMER_LOGIN_BUTTON)
    select_option(driver, NAME_SELECT, name)
    click(driver, LOGIN_BUTTON)
