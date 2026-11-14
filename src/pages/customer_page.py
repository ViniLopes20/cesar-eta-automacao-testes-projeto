from src.interface import by_css, by_id, click, select_option, verify_text

CUSTOMER_NAME = by_css("span.fontBig")
ACCOUNT_SELECT = by_id("accountSelect")
TRANSACTIONS_TAB = by_css("button[ng-click='transactions()']")


def select_account(driver, account):
    select_option(driver, ACCOUNT_SELECT, account)


def click_transactions_tab(driver):
    click(driver, TRANSACTIONS_TAB)


def verify_customer_name(driver, name):
    verify_text(driver, CUSTOMER_NAME, name)
