import logging
from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants

    log = logging.getLogger("[StartPage]")

    def sign_up_username(self, username):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.log.info(f"'{username}' entered to username field")

    def verify_sign_up_username_error(self, user_error, user_log, user_element):
        assert self.get_element_text(user_element) == user_error, f"Actual message: {self.get_element_text(user_element)}"
        self.log.info(user_log)

    def sign_up_email(self, email):
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.log.info(f"'{email}' entered to email field")

    def verify_sign_up_email_error(self, email_error, email_log, email_element):
        assert self.get_element_text(email_element) == email_error, f"Actual message: {self.get_element_text(email_element)}"
        self.log.info(email_log)

    def sign_up_password(self, pwd):
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=pwd)
        self.log.info(f"'{pwd}' entered to password field")

    def verify_sign_up_password_error(self, pwd_error, pwd_log, pwd_element):
        assert self.get_element_text(pwd_element) == pwd_error, f"Actual message: {self.get_element_text(pwd_element)}"
        self.log.info(pwd_log)

    @wait_until_ok(period=0.5)
    def register(self, username, email, pwd):
        # Fill username, email, password
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.log.info(f"'{username}' entered to username field")
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.log.info(f"'{email}@gmail.com' entered to email field")
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=pwd)
        self.log.info(f"'{pwd}' entered to password field")
        # Click button
        sleep(1)
        self.click_sign_up_and_verify()
        self.log.info(f"button 'Sign up for OurApp' clicked")
        from pages.header import Header
        return Header(self.driver)

    @wait_until_ok(period=0.5)
    def click_sign_up_and_verify(self):
        # Click Sign Up button and verify
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_exists(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def sign_in(self, username, password):
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.log.info(f"'{username}' entered to username field")
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.log.info(f"'{password}' entered to password field")
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        self.log.info(f"button 'Sign In' clicked")
        from pages.header import Header
        return Header(self.driver)

    def verify_sign_in_error(self):
        # Verify invalid Sign In error
        assert self.get_element_text(self.constants.SIGN_IN_ERROR_MESSAGE_XPATH) == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)}"
        self.log.info(f"Error '{self.constants.SIGN_IN_ERROR_MESSAGE_TEXT}' was verified")
