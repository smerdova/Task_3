import allure
from pages.main_page import MainPage
from pages.ingredient_details_page import IngredientDetailsPage

class TestIngredienDetailsPage:
    @allure.title('Проверка появления всплывающего окна с деталями ингредиентов"')
    @allure.description('На странице ищем ингредиент и нажимаем на него')
    def test_the_appearance_of_a_popup_window_with_details_positive_result(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_element()
        ingredient_details_page = IngredientDetailsPage(driver)
        ingredient_details_page.check_ingredient_details_title()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиентов кликом по крестику"')
    @allure.description('На странице ищем крестик и нажимаем на него')
    def test_closing_the_popup_window_positive_result(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_element()
        ingredient_details_page = IngredientDetailsPage(driver)
        ingredient_details_page.click_modal_close_button()
        main_page.check_assemble_the_burger_title()
