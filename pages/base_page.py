from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver, timeout=6):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        element.click()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        element = self.wait_visibility_of_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator):
        return self.wait_visibility_of_element(locator).text

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        return self.driver.title

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        try:
            return self.wait_visibility_of_element(locator).is_displayed()
        except:
            return False
    @allure.step("Подождать полной загрузки страницы")
    def wait_for_page_loaded(self, timeout=10):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
