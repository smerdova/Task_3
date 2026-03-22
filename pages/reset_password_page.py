import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import paths as paths
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
            
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ищем иконку "Показать/скрыть пароль" и нажимаем на неё')
    def click_icon_input(self):
        self.driver.find_element(*ResetPasswordPageLocators.icon_input).click()

    @allure.step('Проверяем, что поле "Пароль" становится активным и подсвечивается') 
    def check_password_input(self):
        element = self.driver.find_element(*ResetPasswordPageLocators.password_input)
        classes = element.get_attribute("class")

        assert "input__placeholder-focused" in classes

    @allure.step('Ожидаем загрузки страницы восстановления пароля')
    def wait_for_load_reset_password_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(ResetPasswordPageLocators.password_input))

    @allure.step('Проверяем загрузку страницы восстановления пароля')
    def check_reset_password_url(self):
        assert self.driver.current_url == paths.RESET_PASSWORD_URL 
