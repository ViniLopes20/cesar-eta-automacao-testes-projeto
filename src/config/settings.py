import os

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#"

TIMEOUT = 10

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


def url(path):
    return BASE_URL + path
