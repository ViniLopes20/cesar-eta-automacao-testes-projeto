from src.interface import by_css, by_id, click, navigate_to, select_option

CUSTOMER_LOGIN_BUTTON = by_css("button[ng-click='customer()']")
NAME_SELECT = by_id("userSelect")
LOGIN_BUTTON = by_css("form button[type='submit']")


def open_home_page(driver):
    navigate_to(driver, "/login")


def login_as_customer(driver, name):
    click(driver, CUSTOMER_LOGIN_BUTTON)
    select_option(driver, NAME_SELECT, name)
    click(driver, LOGIN_BUTTON)
