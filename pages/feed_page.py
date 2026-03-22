import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
        
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузки страницы лента заказов')
    def wait_for_load_feed_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(FeedPageLocators.orders_feed_title))

    @allure.step('Проверяем, что надпись "Лента заказов" отображается') 
    def check_orders_feed_title(self):
        element = self.driver.find_element(*FeedPageLocators.orders_feed_title)
        
        assert element.is_displayed()

    @allure.step('Выбираем первый в списке заказ и нажимаем на него') 
    def click_first_order_button(self):
        self.driver.find_element(*FeedPageLocators.first_order_button).click()

    @allure.step('Получаем список заказов из ленты заказов') 
    def get_feed_order_list(self):
        id_order_list = []
        elements = self.driver.find_elements(*FeedPageLocators.text_order)
        for element in elements:
            id_order_list.append(element.text)
        
        return id_order_list
    
    @allure.step('Получаем количество выполненных заказов за все время') 
    def get_order_completed_for_all_time(self):
        return self.driver.find_element(*FeedPageLocators.counter_completed_for_all_time).text

    @allure.step('Получаем количество выполненных заказов за сегодня') 
    def get_order_completed_today(self):
        return self.driver.find_element(*FeedPageLocators.counter_completed_today).text
    
    @allure.step('Получаем id заказа, находящегося в работе') 
    def get_id_order_at_work(self):
        id_order_list = []
        elements = self.driver.find_elements(*FeedPageLocators.id_order_at_work)
        for element in elements:
            id_order_list.append(int(element.text))
        
        return id_order_list
      
    @allure.step('Ожидаем загрузки id заказа в раздел в работе')
    def wait_for_load_id_order_at_work(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(FeedPageLocators.id_order_at_work))
    