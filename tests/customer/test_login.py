import pytest

from src.interface import verify_url
from src.pages import customer_page, home_page


@pytest.mark.cliente
@pytest.mark.positivo
@pytest.mark.alta
def test_login_como_cliente(driver):
    home_page.open_home_page(driver)

    home_page.login_as_customer(driver, "Harry Potter")

    verify_url(driver, "/account")
    customer_page.verify_customer_name(driver, "Harry Potter")
