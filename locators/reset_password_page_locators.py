from selenium.webdriver.common.by import By


class ResetPasswordPageLocators():
    icon_input = [By.XPATH, ".//div[contains(@class, 'input__icon-action')]/*[local-name()='svg']"]
    password_input = [By.XPATH, ".//input[contains(@name, 'Введите новый пароль')]/preceding-sibling::label"]
