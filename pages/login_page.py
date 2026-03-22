import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import paths as paths
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
        
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ищем кнопку "Восстановить пароль" и нажимаем на неё') 
    def click_recover_password_button(self):
        self.driver.find_element(*LoginPageLocators.recover_password_button).click()

    @allure.step('Ищем поле "Email" и заполняем его')
    def set_email_input(self, user):
        self.driver.find_element(*LoginPageLocators.email_input).send_keys(user['email'])

    @allure.step('Ищем поле "Пароль" и заполняем его')
    def set_password_input(self, user):
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(user['password'])

    @allure.step('Ищем кнопку "Войти" и нажимаем на неё') 
    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.login_button).click()

    @allure.step('Ожидаем загрузки страницы логина')
    def wait_for_load_login_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.login_title))

    @allure.step('Проверяем, что при нажатии на кнопку "Выход" переходишь на страницу входа')
    def check_login_url(self):
        assert self.driver.current_url == paths.LOGIN_URL 
