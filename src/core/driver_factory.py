from selenium import webdriver

from src.config import settings

def create_driver():
    opcoes = webdriver.ChromeOptions()
    if settings.HEADLESS:
        opcoes.add_argument("--headless=new")
    opcoes.add_argument("--window-size=1366,900")
    return webdriver.Chrome(options=opcoes)
