from src.interface import by_css, by_id, click, set_input_value, verify_count, verify_texts

START_DATE = by_id("start")
END_DATE = by_id("end")
ROWS = by_css("table tbody tr")
RESET_BUTTON = by_css("button[ng-click='reset()']")
BACK_BUTTON = by_css("button[ng-click='back()']")


def filter_by_period(driver, start, end):
    set_input_value(driver, START_DATE, start)
    set_input_value(driver, END_DATE, end)


def click_reset_button(driver):
    click(driver, RESET_BUTTON)


def click_back_button(driver):
    click(driver, BACK_BUTTON)


def verify_rows(driver, expected_rows):
    verify_texts(driver, ROWS, expected_rows)


def verify_no_rows(driver):
    verify_count(driver, ROWS, 0)
