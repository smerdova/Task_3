from selenium.webdriver.common.by import By


class MainPageLocators():
    login_to_account_button = [By.XPATH, ".//*[contains(text(), 'Войти в аккаунт')]"]
    first_element = [By.XPATH, "(//*[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'])[1]"]
    third_element = [By.XPATH, "(//*[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'])[3]"]
    seventh_element = [By.XPATH, "(//*[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'])[7]"]
    assemble_the_burger_title = [By.XPATH, ".//*[contains(text(), 'Соберите бургер')]"]
    target_element = [By.XPATH, ".//*[@class='BurgerConstructor_basket__list__l9dp_']"]
    counter = [By.XPATH, ".//*[@class='counter_counter__num__3nue1']"]
    place_an_order_button = [By.XPATH, ".//*[contains(text(), 'Оформить заказ')]"]
