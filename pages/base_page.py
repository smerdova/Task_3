import allure
import paths as paths
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    @allure.step('Ищем кнопку "Личный Кабинет" и нажимаем на неё') 
    def click_personal_account_button(self):
        self.driver.find_element(*BasePageLocators.personal_account_button).click()

    @allure.step('Ищем кнопку "Конструктор" и нажимаем на неё') 
    def click_constructor_button(self):
        self.driver.find_element(*BasePageLocators.constructor_button).click()

    @allure.step('Ищем кнопку "Лента Заказов" и нажимаем на неё') 
    def click_orders_feed_button(self):
        self.driver.find_element(*BasePageLocators.orders_feed_button).click()

    @allure.step('Ожидаем исчезновения прелоадера') 
    def wait_for_preloader_hide(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(BasePageLocators.preloader_with_text))
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(BasePageLocators.preloader_with_circles))

    def click_with_offset(self, element):
        self.actions.move_to_element_with_offset(element, 2, 2).click().perform()
