import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.modal_page import ModalPage
from pages.account_page import AccountPage

class TestAccountPage:
    @allure.title('Проверка входа в "Личный кабинет"')
    @allure.description('На странице ищем "Личный кабинет", логинимся и заходим в аккаунт')
    def test_entrance_in_account_positive_result(self, user, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account_button()
        login_page.login(user)
        login_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.check_account_url()

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('В аккаунте ищем кнопку "История заказов" и переходим по ней')
    def test_order_history_positive_result(self, user, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account_button()    
        login_page.login(user)
        main_page = MainPage(driver)
        main_page.drag_and_drop_first_element()
        main_page.drag_and_drop_third_element()
        main_page.drag_and_drop_seventh_element()
        main_page.click_place_an_order_button()
        modal_page = ModalPage(driver)
        modal_page.click_modal_close_button()
        modal_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_order_history_button()
        account_page.check_order_history()

    @allure.title('Проверка выхода из "Личного кабинета"')
    @allure.description('В аккаунте ищем кнопку выхода и нажимаем на нее')
    def test_logout_from_account_positive_result(self, user, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account_button()
        login_page.login(user)
        login_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        login_page.check_login_url()
