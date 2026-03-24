import allure
from pages.base_page import BasePage
from locators.ingredient_details_page_locators import IngredientDetailsPageLocators


class IngredientDetailsPage(BasePage):
            
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем, что надпись "Детали ингредиента" отображается')
    def check_ingredient_details_title(self):
        element = self.find_element(IngredientDetailsPageLocators.ingredient_details_title)
        
        assert element.is_displayed()

    @allure.step('Ищем крестик и нажимаем на него') 
    def click_modal_close_button(self):
        self.find_element(IngredientDetailsPageLocators.modal_close_button).click()
