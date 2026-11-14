from selenium.webdriver.common.by import By


def by_id(value):
    return (By.ID, value)


def by_css(value):
    return (By.CSS_SELECTOR, value)


def by_xpath(value):
    return (By.XPATH, value)
