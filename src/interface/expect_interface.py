from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from src.config import settings
from src.interface.actions_interface import find_all


def wait_until(driver, check):
    try:
        WebDriverWait(driver, settings.TIMEOUT).until(check)
        return True
    except TimeoutException:
        return False


def get_text_if_present(driver, locator):
    elementos = find_all(driver, locator)
    return elementos[0].text.strip() if elementos else None


def verify_url(driver, path):
    esperada = settings.url(path)
    assert wait_until(driver, lambda d: d.current_url == esperada), (
        f"URL esperada {esperada}, mas está em {driver.current_url}"
    )


def verify_text(driver, locator, expected):
    assert wait_until(driver, lambda d: get_text_if_present(d, locator) == expected), (
        f"Texto esperado '{expected}', mas está '{get_text_if_present(driver, locator)}'"
    )


def verify_visible(driver, locator):
    assert wait_until(driver, lambda d: any(e.is_displayed() for e in find_all(d, locator))), (
        f"Elemento {locator} deveria estar visível"
    )


def verify_not_visible(driver, locator):
    assert wait_until(driver, lambda d: not any(e.is_displayed() for e in find_all(d, locator))), (
        f"Elemento {locator} não deveria estar visível"
    )


def verify_count(driver, locator, expected):
    assert wait_until(driver, lambda d: len(find_all(d, locator)) == expected), (
        f"Esperado {expected} elemento(s) {locator}, mas há {len(find_all(driver, locator))}"
    )
