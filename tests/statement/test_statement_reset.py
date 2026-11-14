import pytest

from src.interface import verify_url
from src.pages import customer_page, home_page, transactions_page

DEPOSIT_AMOUNT = "500"
DEPOSIT_SUCCESS_MESSAGE = "Deposit Successful"
ACCOUNT_INFO_AFTER_DEPOSIT = "Account Number : 1004 , Balance : 500 , Currency : Dollar"
ACCOUNT_INFO_AFTER_RESET = "Account Number : 1004 , Balance : 0 , Currency : Dollar"


@pytest.mark.extrato
@pytest.mark.positivo
@pytest.mark.media
def test_ct11_limpar_transacoes_com_reset(driver):
    home_page.open_home_page(driver)

    home_page.login_as_customer(driver, "Harry Potter")
    verify_url(driver, "/account")

    customer_page.deposit(driver, DEPOSIT_AMOUNT)
    customer_page.verify_message(driver, DEPOSIT_SUCCESS_MESSAGE)
    customer_page.verify_account_info(driver, ACCOUNT_INFO_AFTER_DEPOSIT)

    customer_page.click_transactions_tab(driver)
    verify_url(driver, "/listTx")

    transactions_page.click_reset_button(driver)
    transactions_page.verify_no_rows(driver)

    transactions_page.click_back_button(driver)
    verify_url(driver, "/account")

    customer_page.verify_account_info(driver, ACCOUNT_INFO_AFTER_RESET)
