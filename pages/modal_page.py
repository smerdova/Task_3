import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.modal_page_locators import ModalPageLocators


class ModalPage(BasePage):
    
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем, что появилась надпись "Ваш заказ начали готовить" в новом модальном окне')
    def check_order_title(self):
        element = self.find_element(ModalPageLocators.order_title)
        
        assert element.is_displayed()

    @allure.step('Закрытие модального окна') 
    def click_modal_close_button(self):
        self.wait_for_preloader_hide()
        self.wait(15).until(expected_conditions.visibility_of_element_located(ModalPageLocators.modal_close_button))
        self.find_element(ModalPageLocators.modal_close_button).click()
        self.wait(15).until(expected_conditions.invisibility_of_element_located(ModalPageLocators.modal_close_button))

    @allure.step('Получаем id заказа') 
    def get_id_order(self):
        self.wait_for_preloader_hide()
        return int(self.find_element(ModalPageLocators.id_order).text)
    