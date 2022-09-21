import pytest

from pages.utils import csv_read


class TestStartPage:

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["username", "user_error", "user_log", "user_element"], csv_read("usernames.csv"))
    def test_registration_username_field(self, page_driver, username, user_error, user_log, user_element):
        # Fill username
        page_driver.sign_up_username(username)

        # Verify error
        page_driver.verify_sign_up_username_error(user_error, user_log, user_element)

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["email", "email_error", "email_log", "email_element"], csv_read("emails.csv"))
    def test_registration_email_field(self, page_driver, email, email_error, email_log, email_element):
        # Fill email without @ symbol
        page_driver.sign_up_email(email)

        # Verify error
        page_driver.verify_sign_up_email_error(email_error, email_log, email_element)

    @pytest.mark.repeat(1)
    @pytest.mark.parametrize(["pwd", "pwd_error", "pwd_log", "pwd_element"], csv_read("passwords.csv"))
    def test_registration_password_field(self, page_driver, pwd, pwd_error, pwd_log, pwd_element):
        # Fill password with less than 12 symbols
        page_driver.sign_up_password(pwd)

        # Verify error
        page_driver.verify_sign_up_password_error(pwd_error, pwd_log, pwd_element)

    @pytest.mark.repeat(1)
    def test_registration(self, page_driver, random_symbols):
        username = random_symbols
        email = f"{random_symbols}@gmail.com"
        pwd = random_symbols
        # Fill username, email, password and click Sign up
        page_driver.sign_up(username, email, pwd)

        # Verify registration
        page_driver.verify_profile_button()

        # Click 'Sign Out' button
        page_driver.sign_out_click()
