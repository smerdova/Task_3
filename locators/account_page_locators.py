from selenium.webdriver.common.by import By


class AccountPageLocators():
    profile_button = [By.XPATH, ".//*[contains(text(), 'Профиль')]"]
    order_history_button = [By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and contains(text(), 'История заказов')]"]
    logout_button = [By.XPATH, ".//*[contains(text(), 'Выход')]"]
    text_order = [By.XPATH, ".//*[@class='text text_type_digits-default']"]
    