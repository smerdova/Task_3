import allure
from pages.base_page import BasePage
from pages.main_page import MainPage

class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    @allure.description('На странице ищем кнопку "Конструктор" и переходим по ней')
    def test_navigate_to_the_constructor_button_positive_result(self, driver):
        base_page = BasePage(driver)
        base_page.click_orders_feed_button()
        base_page.click_constructor_button()
        main_page = MainPage(driver)
        main_page.check_assemble_the_burger_title()

    @allure.title('Проверка увеличения каунтера ингредиента, при добавлении его в заказ"')
    @allure.description('На странице ищем ингредиент, добавляем его в заказ и проверяем увеличение каунтера ингредиента')
    def test_counter_is_incremented_positive_result(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_first_element()
        main_page.check_counter_is_incremented()
