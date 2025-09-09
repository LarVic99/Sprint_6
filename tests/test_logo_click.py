import allure
import pytest
from pages.main_page import MainPage

@allure.suite("Проверка логотипов")
class TestLogo:

    @allure.title("Проверка клика по логотипу 'Самокат'")
    def test_logo_main_page(self, driver):
        main_page = MainPage(driver)

        with allure.step("Кликаем по лого 'Самокат'"):
            main_page.click_on_header_logo_scooter()  # минимальное исправление

        with allure.step("Проверяем, что открыта главная страница"):
            assert main_page.check_displaying_of_main_header()

    @allure.title("Проверка клика по логотипу 'Яндекс.Дзен'")
    def test_logo_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step("Кликаем по лого 'Яндекс'"):
            main_page.click_on_header_logo_yandex()  # минимальное исправление

        with allure.step("Переключаемся на вкладку Дзен"):
            main_page.switch_to_next_tab()  # исправленный метод

        with allure.step("Проверяем, что открыт Яндекс или Дзен"):
            assert "dzen" in driver.current_url or "yandex" in driver.current_url

