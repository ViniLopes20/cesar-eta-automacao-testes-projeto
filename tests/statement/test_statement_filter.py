import pytest

from src.interface import verify_url
from src.pages import customer_page, home_page, transactions_page

ACCOUNT = "1001"
START_DATE = "2015-01-02T00:00"
END_DATE = "2015-01-03T23:59"
ROWS_IN_PERIOD = [
    "Jan 2, 2015 12:00:00 AM 30 Credit",
    "Jan 2, 2015 12:00:00 AM 4 Debit",
    "Jan 3, 2015 12:00:00 AM 30 Credit",
    "Jan 3, 2015 12:00:00 AM 4 Debit",
]


@pytest.mark.extrato
@pytest.mark.positivo
@pytest.mark.media
def test_ct10_filtrar_extrato_por_periodo(driver):
    home_page.open_home_page(driver)

    home_page.login_as_customer(driver, "Hermoine Granger")
    verify_url(driver, "/account")

    customer_page.select_account(driver, ACCOUNT)

    customer_page.click_transactions_tab(driver)
    verify_url(driver, "/listTx")

    transactions_page.filter_by_period(driver, START_DATE, END_DATE)

    transactions_page.verify_rows(driver, ROWS_IN_PERIOD)
