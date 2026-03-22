from selenium.webdriver.common.by import By


class IngredientDetailsPageLocators():
    ingredient_details_title = [By.XPATH, ".//*[contains(text(), 'Детали ингредиента')]"]
    modal_close_button = [By.XPATH, ".//*[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
