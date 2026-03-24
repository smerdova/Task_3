import allure
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import paths as paths
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем логин при входе "Личный кабинет"')
    def check_account_url(self):
        self.wait(3).until(expected_conditions.element_to_be_clickable(AccountPageLocators.order_history_button))
        assert self.get_current_url() == paths.ACCOUNT_URL

    @allure.step('Ищем кнопку "История заказов" и нажимаем на неё') 
    def click_order_history_button(self):
        self.wait(3).until(expected_conditions.element_to_be_clickable(AccountPageLocators.order_history_button))
        self.click_with_offset(self.find_element(AccountPageLocators.order_history_button))

    @allure.step('Проверяем, что при нажатии на кнопку "История заказов" переходишь в раздел "История заказов"')
    def check_order_history(self):
        self.wait(20).until(expected_conditions.visibility_of_element_located(AccountPageLocators.text_order))
        assert self.get_current_url() == paths.ORDER_HISTORY

    @allure.step('Ищем кнопку "Выход" и нажимаем на неё') 
    def click_logout_button(self):
        self.wait_for_preloader_hide()
        self.find_element(AccountPageLocators.logout_button).click()

    @allure.step('Получаем список заказов из истории заказов') 
    def get_order_history_list(self):
        id_order_list = []
        elements = self.find_elements(AccountPageLocators.text_order)
        for element in elements:
            id_order_list.append(element.text)
        
        return id_order_list
