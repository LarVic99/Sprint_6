from selenium.webdriver.common.by import By


class MainPageLocators:
    # Хедер и секции
    main_header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    # Вопросы FAQ (список!)
    faq_questions = [
        (By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'),
        (By.XPATH, '//div[@id="accordion__heading-7"]/parent::div'),
    ]

    # Ответы FAQ (тоже список!)
    faq_answers = [
        (By.XPATH, '//div[@id="accordion__panel-0"]'),
        (By.XPATH, '//div[@id="accordion__panel-1"]'),
        (By.XPATH, '//div[@id="accordion__panel-2"]'),
        (By.XPATH, '//div[@id="accordion__panel-3"]'),
        (By.XPATH, '//div[@id="accordion__panel-4"]'),
        (By.XPATH, '//div[@id="accordion__panel-5"]'),
        (By.XPATH, '//div[@id="accordion__panel-6"]'),
        (By.XPATH, '//div[@id="accordion__panel-7"]'),
    ]

    # Кнопки заказа
    order_button_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    order_button_in_header = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]')

    # Логотипы
    header_logo_scooter = (By.XPATH, '//a[contains(@class, "Header_LogoScooter__3lsAR")]')
    header_logo_yandex = (By.XPATH, '//a[contains(@class, "Header_LogoYandex__3TSOI")]')
