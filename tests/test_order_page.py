import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from data import TestData


@allure.suite("Оформление заказа")
class TestOrderPage:

    @allure.title("Проверка позитивного сценария оформления заказа")
    @allure.description("Сквозное тестирование функциональности оформления заказа из двух точек входа")
    @pytest.mark.parametrize(
        "button, test_data",
        [
            (MainPageLocators.order_button_in_header, TestData.test_data_user1),
            (MainPageLocators.order_button_main, TestData.test_data_user2),
        ]
    )
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)

        with allure.step("Скроллим до кнопки заказа"):
            order_page.scroll_to_element(button)

        with allure.step("Ждём видимость кнопки заказа"):
            order_page.wait_visibility_of_element(button)

        with allure.step("Кликаем по кнопке заказа"):
            order_page.click_on_element(button)

        with allure.step("Заполняем первую форму заказа"):
            order_page.data_entry_first_form(test_data)

        with allure.step("Заполняем вторую форму заказа"):
            order_page.data_entry_second_form(test_data)

        with allure.step("Проверяем, что заказ успешно оформлен"):
            assert order_page.check_displaying_of_button_check_status_of_order()
