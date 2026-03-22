from selenium.webdriver.common.by import By


class LoginPageLocators():
    login_title = [By.XPATH, ".//*[contains(text(), 'Вход')]"]
    recover_password_button = [By.XPATH, ".//*[contains(text(), 'Восстановить пароль')]"]
    email_input = [By.NAME, "name"]
    password_input = [By.NAME, "Пароль"]
    login_button = [By.XPATH, ".//*[contains(text(), 'Войти')]"]
