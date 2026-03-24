from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators():
    email_input = [By.NAME, "name"]
    recover_button = [By.XPATH, ".//*[contains(text(), 'Восстановить')]"]
