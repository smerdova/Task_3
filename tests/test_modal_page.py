import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.modal_page import ModalPage

class TestModalPage:
    @allure.title('Проверка оформление заказа залогиненным пользователем')
    @allure.description('Логинимся и проходим все этапы оформления заказа')
    def test_create_order_with_auth_positive_result(self, user, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account_button()
        login_page.login(user)
        main_page = MainPage(driver)
        main_page.drag_and_drop_first_element()
        main_page.drag_and_drop_third_element()
        main_page.drag_and_drop_seventh_element()
        main_page.click_place_an_order_button()
        modal_page = ModalPage(driver)
        modal_page.check_order_title()
        