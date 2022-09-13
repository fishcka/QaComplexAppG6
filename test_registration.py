# - Створити тест на реєстрацію.
# Нюанс номер 1: Тест має проходити більше 1 разу, тобто данні в полях мають бути повністю
# або чатсково випадковими (Оскільки той самий юзер не може бути зареєстрований двічі)
# Нюанс номер 2: Вам потрібно самостійно придумати перевірку, що буде підверджувати успішність реєстрації.
# Це може бути перевірка наявності якогось поля, його значення, повідомлення або первірка URL.

import string
import random
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

characters = list(string.ascii_letters + string.digits)


@pytest.fixture(scope="function")
def random_symbols():
    # shuffling the characters
    random.shuffle(characters)
    # picking random characters from the list
    symbols_list = []
    for i in range(20):
        symbols_list.append(random.choice(characters))
    # shuffling the resultant symbols list
    random.shuffle(symbols_list)
    # converting the list to string
    symbols = "".join(symbols_list)
    return symbols


@pytest.fixture(scope="class")
def login_page():
    # Create driver
    driver = webdriver.Firefox()
    # Maximize window
    driver.maximize_window()
    # Open page
    driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    yield driver
    # Close driver
    driver.close()


class TestRegistration:
    def test_registration(self, random_symbols, login_page):
        # Fill login
        login = login_page.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        login.send_keys(random_symbols)
        sleep(1)

        # Fill email
        password = login_page.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        password.send_keys(random_symbols + "@gmail.com")
        sleep(1)

        # Fill password
        password = login_page.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys(random_symbols)
        sleep(1)

        # Click button
        button = login_page.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)

        # Verify registration
        profile_button = login_page.find_element(by=By.XPATH, value=".//img[@alt='My profile']")
        assert profile_button.is_enabled(), f"Registration failed"
        sleep(2)
