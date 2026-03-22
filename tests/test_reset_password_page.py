import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

class TestResetPasswordPage:
    @allure.title('Проверить, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('На страницах ищем элементы и проходим по этапам восстановления пароля')
    def test_password_recovery_positive_result(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_to_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.set_email_input('smerdovaTest@gmail.com')
        forgot_password_page.click_recover_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_load_reset_password_page()
        reset_password_page.click_icon_input()
        reset_password_page.check_password_input()
