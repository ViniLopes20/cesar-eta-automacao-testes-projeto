from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from src.config import settings


def wait_for(driver, condition):
    return WebDriverWait(driver, settings.TIMEOUT).until(condition)


def navigate_to(driver, path):
    driver.get(settings.url(path))


def find(driver, locator):
    return wait_for(driver, EC.visibility_of_element_located(locator))


def find_all(driver, locator):
    return driver.find_elements(*locator)


def click(driver, locator):
    wait_for(driver, EC.element_to_be_clickable(locator)).click()


def type_text(driver, locator, text):
    campo = find(driver, locator)
    campo.clear()
    campo.send_keys(text)


def get_text(driver, locator):
    return find(driver, locator).text.strip()


def select_option(driver, locator, text):
    Select(find(driver, locator)).select_by_visible_text(text)


def get_alert_text_and_accept(driver):
    alerta = wait_for(driver, EC.alert_is_present())
    texto = alerta.text
    alerta.accept()
    return texto
