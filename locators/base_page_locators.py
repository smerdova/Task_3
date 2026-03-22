from selenium.webdriver.common.by import By


class BasePageLocators():
    personal_account_button = [By.XPATH, ".//*[contains(text(), 'Личный Кабинет')]"]
    constructor_button = [By.XPATH, ".//*[contains(text(), 'Конструктор')]"]
    orders_feed_button = [By.XPATH, ".//*[contains(text(), 'Лента Заказов')]"]
    preloader_with_text = [By.XPATH, "//div[contains(text(), 'Загрузка...')]"]
    preloader_with_circles = [By.XPATH, ".//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]