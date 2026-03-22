import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop


class MainPage(BasePage):
            
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ищем кнопку "Войти в аккаунт" и нажимаем на неё') 
    def click_login_to_account_button(self):
        self.driver.find_element(*MainPageLocators.login_to_account_button).click()

    @allure.step('Ожидаем загрузки страницы')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.assemble_the_burger_title))

    @allure.step('Ищем первый элемент и нажимаем на него') 
    def click_first_element(self):
        self.driver.find_element(*MainPageLocators.first_element).click()

    @allure.step('Проверяем, что надпись "Соберите бургер" отображается')
    def check_assemble_the_burger_title(self):
        element = self.driver.find_element(*MainPageLocators.assemble_the_burger_title)
        
        assert element.is_displayed()

    @allure.step('Ищем исходный элемент и перетаскиваем его') 
    def drag_and_drop_first_element(self):
        source = self.driver.find_element(*MainPageLocators.first_element)
        target = self.driver.find_element(*MainPageLocators.target_element)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ищем третий элемент и перетаскиваем его') 
    def drag_and_drop_third_element(self):
        source = self.driver.find_element(*MainPageLocators.third_element)
        target = self.driver.find_element(*MainPageLocators.target_element)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ищем седьмой элемент и перетаскиваем его') 
    def drag_and_drop_seventh_element(self):
        source = self.driver.find_element(*MainPageLocators.seventh_element)
        target = self.driver.find_element(*MainPageLocators.target_element)
        drag_and_drop(self.driver, source, target)

    @allure.step('Проверяем, что увеличивается каунтер данного ингредиента')
    def check_counter_is_incremented(self):
        element = self.driver.find_element(*MainPageLocators.counter)
        counter = element.text
        
        assert counter == '2'

    @allure.step('Ищем кнопку "Оформить заказ" и нажимаем на нее') 
    def click_place_an_order_button(self):
        self.driver.find_element(*MainPageLocators.place_an_order_button).click()
