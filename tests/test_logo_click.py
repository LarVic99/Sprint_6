import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogo:

    def test_logo_main_page(self, driver):
        # кликаем по лого "Самокат"
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Header_LogoScooter__3lsAR"))
        )
        logo.click()

        # ждем, пока URL станет главной страницей
        WebDriverWait(driver, 10).until(
            lambda d: "scooter" in d.current_url or d.current_url.endswith("/")
        )

        # финальная проверка по URL вместо title
        assert "scooter" in driver.current_url or driver.current_url.endswith("/")

    def test_logo_dzen(self, driver):
        # кликаем по лого "Яндекс"
        logo_dzen = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Header_LogoYandex__3TSOI"))
        )
        logo_dzen.click()

        # переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[1])

        # ждем, пока URL загрузится
        WebDriverWait(driver, 20).until(
            lambda d: "dzen" in d.current_url or "yandex" in d.current_url
        )

        # финальная проверка по URL вместо title
        assert "dzen" in driver.current_url or "yandex" in driver.current_url
