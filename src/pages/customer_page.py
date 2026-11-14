from src.interface import by_css, verify_text

CUSTOMER_NAME = by_css("span.fontBig")


def verify_customer_name(driver, name):
    verify_text(driver, CUSTOMER_NAME, name)
