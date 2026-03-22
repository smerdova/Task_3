from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebDriverFactory:
    
    @staticmethod
    def get_webdriver(browser_name, headless=False):
        browser_name = browser_name.lower()
        driver = None

        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается")
        
        return driver
