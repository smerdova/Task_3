import allure
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import paths as paths
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
        
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ищем кнопку "Восстановить пароль" и нажимаем на неё') 
    def click_recover_password_button(self):
        self.find_element(LoginPageLocators.recover_password_button).click()

    @allure.step('Логинимся') 
    def login(self, user):
        self.find_element(LoginPageLocators.email_input).send_keys(user['email'])
        self.find_element(LoginPageLocators.password_input).send_keys(user['password'])
        self.find_element(LoginPageLocators.login_button).click()
        self.wait_for_preloader_hide()
        
    @allure.step('Проверяем, что при нажатии на кнопку "Выход" переходишь на страницу входа')
    def check_login_url(self):
        self.wait(3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.login_title))
        assert self.get_current_url() == paths.LOGIN_URL 
