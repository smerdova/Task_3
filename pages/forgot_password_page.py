import allure
from pages.base_page import BasePage
import paths as paths
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ищем поле "Email" и заполняем его')
    def set_email_input(self, email):
        self.driver.find_element(*ForgotPasswordPageLocators.email_input).send_keys(email)

    @allure.step('Ищем кнопку "Восстановить" и нажимаем на неё') 
    def click_recover_button(self):
        self.driver.find_element(*ForgotPasswordPageLocators.recover_button).click()

    @allure.step('Проверяем url страницы восстановления пароля')
    def check_forgot_password_url(self):
        assert self.driver.current_url == paths.FORGOT_PASSWORD_URL
