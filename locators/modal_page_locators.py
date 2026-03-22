from selenium.webdriver.common.by import By


class ModalPageLocators():
    order_title = [By.XPATH, ".//*[contains(text(), 'Ваш заказ начали готовить')]"]
    modal_close_button = [By.XPATH, ".//*[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    id_order = [By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]
