import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

class TestForgotPasswordPage:
    @allure.title('Проверка входа на страницу восстановления пароля')
    @allure.description('На странице ищем кнопку "Восстановить пароль" и проходим по ней')
    def test_check_forgot_password_url_positive_result(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.check_forgot_password_url()

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('На странице ищем поле ввода почты, вводим почту и нажимаем кнопку "Восстановить"')
    def test_click_forgot_password_positive_result(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.set_email_input('smerdovaTest@gmail.com')
        forgot_password_page.click_recover_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_load_reset_password_page()
        reset_password_page.check_reset_password_url()
