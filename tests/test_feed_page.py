import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from pages.modal_page import ModalPage
from pages.account_page import AccountPage
from pages.modal_order_page import ModalOrderPage


class TestFeedPage:
    @allure.title('Проверка перехода по клику в "Ленту заказов"')
    @allure.description('На странице ищем кнопку "Лента заказов" и переходим по ней')
    def test_navigate_to_the_orders_feed_button_positive_result(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_orders_feed_button()
        feed_page.check_orders_feed_title()

    @allure.title('Проверка открытия всплывающего окна с деталями заказа при нажатии на заказ')
    @allure.description('На странице ищем кнопку "Лента заказов", переходим по ней, выбираем первый заказ и нажимаем на него')
    def test_open_popup_window_order_positive_result(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_orders_feed_button()
        feed_page.click_first_order_button()
        modal_order_page = ModalOrderPage(driver)
        modal_order_page.check_composition_title()

    @allure.title('Проверка отображения заказов пользователя на странице "Лента заказов"')
    @allure.description('Создаем заказ под залогиненным пользователем и проверяем его в "Ленте заказов"')
    def test_open_order_in_feed_order_positive_result(self, user, driver):
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
        account_page_orders = account_page.get_order_history_list()
        feed_page = FeedPage(driver)
        feed_page.click_orders_feed_button()
        feed_page_orders = feed_page.get_feed_order_list()
        
        assert set(account_page_orders).issubset(set(feed_page_orders))

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Сохраняем количество заказов "Выполнено за всё время", создаем заказ и проверяем, что количество увеличилось')
    def test_counter_increment_completed_for_all_time_positive_result(self, user, driver):
        feed_page = FeedPage(driver)
        feed_page.click_orders_feed_button()
        old_quantity = feed_page.get_order_completed_for_all_time()
        feed_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(user)
        main_page = MainPage(driver)
        main_page.drag_and_drop_first_element()
        main_page.drag_and_drop_third_element()
        main_page.drag_and_drop_seventh_element()
        main_page.click_place_an_order_button()
        modal_page = ModalPage(driver)
        modal_page.click_modal_close_button()
        modal_page.click_orders_feed_button()
        feed_page = FeedPage(driver)
        new_quantity = feed_page.get_order_completed_for_all_time()

        assert int(new_quantity) > int(old_quantity)

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Сохраняем количество заказов "Выполнено за сегодня", создаем заказ и проверяем, что количество увеличилось')
    def test_counter_increment_completed_today_positive_result(self, user, driver):
        feed_page = FeedPage(driver)
        feed_page.click_orders_feed_button()
        old_quantity = feed_page.get_order_completed_today()
        feed_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(user)
        main_page = MainPage(driver)
        main_page.drag_and_drop_first_element()
        main_page.drag_and_drop_third_element()
        main_page.drag_and_drop_seventh_element()
        main_page.click_place_an_order_button()
        modal_page = ModalPage(driver)
        modal_page.click_modal_close_button()
        modal_page.click_orders_feed_button()
        new_quantity = feed_page.get_order_completed_today()

        assert int(new_quantity) > int(old_quantity)

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Cоздаем заказ, сохраняем его id и проверяем, что заказ появился в разделе В работе')
    def test_id_order_in_section_at_work_positive_result(self, user, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account_button()             
        login_page.login(user)
        main_page = MainPage(driver)
        main_page.drag_and_drop_first_element()
        main_page.drag_and_drop_third_element()
        main_page.drag_and_drop_seventh_element()
        main_page.click_place_an_order_button()
        modal_page = ModalPage(driver)
        id_order = modal_page.get_id_order()
        modal_page.click_modal_close_button()
        modal_page.click_orders_feed_button()
        feed_page = FeedPage(driver)
        id_orders_at_work = feed_page.get_id_order_at_work()

        assert id_order in id_orders_at_work
