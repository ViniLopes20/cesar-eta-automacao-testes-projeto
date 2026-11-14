from src.interface import by_css, by_id, set_input_value, verify_texts

START_DATE = by_id("start")
END_DATE = by_id("end")
ROWS = by_css("table tbody tr")


def filter_by_period(driver, start, end):
    set_input_value(driver, START_DATE, start)
    set_input_value(driver, END_DATE, end)


def verify_rows(driver, expected_rows):
    verify_texts(driver, ROWS, expected_rows)
