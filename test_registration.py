import csv
import logging
import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

log = logging.getLogger(__name__)
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
def page_driver():
    # Create driver
    driver = webdriver.Firefox()
    # Open page
    driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
    # Maximize window
    driver.maximize_window()
    log.info("firefox window opened")
    yield driver
    # Close driver
    driver.close()


class TestRegistration:
    log = logging.getLogger(__name__)

    with open("user_names.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        usernames = [tuple(row) for row in reader]

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["username", "user_error", "user_log"], usernames)
    def test_registration_username_field(self, page_driver, username, user_error, user_log):
        # Fill username
        login = page_driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        login.send_keys(username)
        self.log.info(f"'{username}' entered to username field")
        sleep(2)

        # Verify error
        err_mess = page_driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']")
        assert err_mess.text == user_error, f"Actual message: {err_mess.text}"
        login.clear()
        self.log.info(user_log)
        sleep(2)

    @pytest.mark.repeat(1)
    def test_registration_email_field(self, page_driver):
        # Fill email without @ symbol
        email = page_driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys("randommail")
        self.log.info("'randommail' entered to email field")
        sleep(2)

        # Verify error
        err_mess = page_driver.find_element(by=By.XPATH, value=".//div[contains(text(),'You must provide a valid email address.')]")
        assert err_mess.text == "You must provide a valid email address.", f"Actual message: {err_mess.text}"
        email.clear()
        self.log.info("email without @ verified")
        sleep(2)

    @pytest.mark.repeat(1)
    def test_registration_password_field(self, page_driver):
        # Fill password with less than 12 symbols
        password = page_driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys("pass")
        self.log.info("'pass' entered to password field")
        sleep(2)

        # Verify error
        err_mess = page_driver.find_element(by=By.XPATH, value=".//div[contains(text(),'Password must be at least 12 characters.')]")
        assert err_mess.text == "Password must be at least 12 characters.", f"Actual message: {err_mess.text}"
        password.clear()
        self.log.info("password with less than 12 symbols verified")
        sleep(2)

        # Fill password with more than 50 symbols
        password.send_keys("veryverylongpasswordmuchmorethanfiftycharacterslong")
        self.log.info("'veryverylongpasswordmuchmorethanfiftycharacterslong' entered to password field")
        sleep(2)

        # Verify error
        err_mess = page_driver.find_element(by=By.XPATH, value=".// div[contains(text(), 'Password cannot exceed 50 characters.')]")
        assert err_mess.text == "Password cannot exceed 50 characters.", f"Actual message: {err_mess.text}"
        password.clear()
        self.log.info("password with more than 50 symbols verified")
        sleep(2)

    @pytest.mark.repeat(1)
    def test_registration(self, random_symbols, page_driver):
        # Fill login
        login = page_driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        login.send_keys(random_symbols)
        self.log.info(f"'{random_symbols}' entered to username field")
        sleep(2)

        # Fill email
        email = page_driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys(random_symbols + "@gmail.com")
        self.log.info(f"'{random_symbols}@gmail.com' entered to email field")
        sleep(2)

        # Fill password
        password = page_driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys(random_symbols)
        self.log.info(f"'{random_symbols}' entered to password field")
        sleep(2)

        # Click 'Sign up for OurApp' button
        button = page_driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        self.log.info(f"button 'Sign up for OurApp' clicked")
        sleep(2)

        # Verify registration
        profile_button = page_driver.find_element(by=By.XPATH, value=".//img[@alt='My profile']")
        assert profile_button.is_enabled(), f"Registration failed"
        self.log.info("registration was successful")
        sleep(2)

        # Click 'Sign Out' button
        button = page_driver.find_element(by=By.XPATH, value=".//button[@class='btn btn-sm btn-secondary']")
        button.click()
        self.log.info(f"button 'Sign Out' clicked")
        sleep(2)
