import pytest

from pages.utils import csv_read, random_symbols


class TestStartPage:

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["username", "user_error", "user_log", "user_element"], csv_read("../files/usernames.csv"))
    def test_registration_username_field(self, page_driver, username, user_error, user_log, user_element):
        # Fill username
        page_driver.sign_up_username(username)
        # Verify error
        page_driver.verify_sign_up_username_error(user_error, user_log, user_element)

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["email", "email_error", "email_log", "email_element"], csv_read("../files/emails.csv"))
    def test_registration_email_field(self, page_driver, email, email_error, email_log, email_element):
        # Fill email
        page_driver.sign_up_email(email)
        # Verify error
        page_driver.verify_sign_up_email_error(email_error, email_log, email_element)

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["pwd", "pwd_error", "pwd_log", "pwd_element"], csv_read("../files/passwords.csv"))
    def test_registration_password_field(self, page_driver, pwd, pwd_error, pwd_log, pwd_element):
        # Fill password
        page_driver.sign_up_password(pwd)
        # Verify error
        page_driver.verify_sign_up_password_error(pwd_error, pwd_log, pwd_element)

    @pytest.mark.repeat(1)
    def test_registration(self, page_driver):
        # Fill username, email, password fields with generated values and click Sign up
        header = page_driver.register(random_symbols, f"{random_symbols}@gmail.com", random_symbols)
        # Verify registration
        header.verify_profile_button()
        # Click 'Sign Out' button
        header.sign_out_click()

    def test_incorrect_login(self, page_driver):
        # Login as a user
        page_driver.sign_in("User11", "Pwd11")
        # Verify error
        page_driver.verify_sign_in_error()

    def test_empty_login(self, page_driver):
        # Login as a user
        page_driver.sign_in("", "")
        # Verify error
        page_driver.verify_sign_in_error()

    def test_login(self, page_driver):
        # Login as a user
        header = page_driver.sign_in("ludmilaa", "ludmilaagmailcom")
        # Verify login
        header.verify_profile_button()
        # Click 'Sign Out' button
        header.sign_out_click()
