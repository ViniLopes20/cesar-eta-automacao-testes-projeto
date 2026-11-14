from src.interface import by_css, by_id, click, navigate_to, select_option, verify_visible

CUSTOMER_LOGIN_BUTTON = by_css("button[ng-click='customer()']")
MANAGER_LOGIN_BUTTON = by_css("button[ng-click='manager()']")
CUSTOMER_NAME_SELECT = by_id("userSelect")
SUBMIT_LOGIN_BUTTON = by_css("form button[type='submit']")


def open_home_page(driver):
    navigate_to(driver, "/login")


def login_as_customer(driver, name):
    click(driver, CUSTOMER_LOGIN_BUTTON)
    select_option(driver, CUSTOMER_NAME_SELECT, name)
    click(driver, SUBMIT_LOGIN_BUTTON)


def verify_login_options(driver):
    verify_visible(driver, CUSTOMER_LOGIN_BUTTON)
    verify_visible(driver, MANAGER_LOGIN_BUTTON)
