import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from data import TestData

@pytest.fixture()
def driver():
    # Если geckodriver в PATH, можно оставить пустым
    service = FirefoxService()
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    
    # Переход сразу на сайт
    driver.get(TestData.scooter_address)
    
    yield driver
    driver.quit()
