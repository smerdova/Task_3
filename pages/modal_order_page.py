import allure
from pages.base_page import BasePage
from locators.modal_order_page_locators import ModalOrderPageLocators


class ModalOrderPage(BasePage):
                    
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем, что появилась надпись "Состав" в модальном окне с деталями заказа')
    def check_composition_title(self):
        element = self.find_element(ModalOrderPageLocators.composition_title)
        
        assert element.is_displayed()
