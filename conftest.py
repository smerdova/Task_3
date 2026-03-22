import random
import pytest
import requests
import paths as paths
from driver_factory import WebDriverFactory


@pytest.fixture
def driver():
    driver = WebDriverFactory.get_webdriver("chrome", headless=False)
    driver.get(paths.BASE_URL)

    yield driver
    
    driver.quit()

@pytest.fixture
def user():
    user = {}
    user['email'] = f"email{random.randint(1, 999999999)}@gmail.com"
    user['password'] = f"password{random.randint(1, 999999999)}"
    user['name'] = f"name{random.randint(1, 999999999)}"
    response_register = requests.post(paths.REGISTER_URL, data=user)
    r = response_register.json()
    token = r['accessToken']

    yield user

    requests.delete(paths.USER_URL, headers={'authorization': token})
