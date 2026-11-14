import pytest

from src.interface import verify_url
from src.pages import customer_page, home_page


@pytest.mark.navegacao
@pytest.mark.positivo
@pytest.mark.baixa
def test_ct13_voltar_a_tela_inicial_com_home(driver):
    home_page.open_home_page(driver)

    home_page.login_as_customer(driver, "Harry Potter")
    verify_url(driver, "/account")

    customer_page.click_home_button(driver)
    verify_url(driver, "/login")
    home_page.verify_login_options(driver)
