from src.interface import by_css, by_id, by_xpath, click, select_option, type_text, verify_text

CUSTOMER_NAME = by_css("span.fontBig")
ACCOUNT_SELECT = by_id("accountSelect")
ACCOUNT_INFO = by_xpath(
    "//div[@ng-hide='noAccount' and contains(normalize-space(), 'Account Number')]"
)
TRANSACTIONS_TAB = by_css("button[ng-click='transactions()']")
DEPOSIT_TAB = by_css("button[ng-click='deposit()']")
AMOUNT_INPUT = by_css("input[ng-model='amount']")
SUBMIT_AMOUNT_BUTTON = by_css("form button[type='submit']")
MESSAGE = by_css("span.error")
HOME_BUTTON = by_css("button[ng-click='home()']")


def select_account(driver, account):
    select_option(driver, ACCOUNT_SELECT, account)


def click_transactions_tab(driver):
    click(driver, TRANSACTIONS_TAB)


def click_home_button(driver):
    click(driver, HOME_BUTTON)


def deposit(driver, amount):
    click(driver, DEPOSIT_TAB)
    type_text(driver, AMOUNT_INPUT, amount)
    click(driver, SUBMIT_AMOUNT_BUTTON)


def verify_customer_name(driver, name):
    verify_text(driver, CUSTOMER_NAME, name)


def verify_message(driver, expected):
    verify_text(driver, MESSAGE, expected)


def verify_account_info(driver, expected):
    verify_text(driver, ACCOUNT_INFO, expected)
