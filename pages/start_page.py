import logging
from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants

    log = logging.getLogger(__name__)

    def sign_up_username(self, username):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.log.info(f"'{username}' entered to username field")
        sleep(1)

    def verify_sign_up_username_error(self, user_error, user_log, user_element):
        assert self.get_element_text(user_element) == user_error, f"Actual message: {self.get_element_text(user_element)}"
        self.log.info(user_log)
        sleep(1)

    def sign_up_email(self, email):
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.log.info(f"'{email}' entered to email field")
        sleep(1)

    def verify_sign_up_email_error(self, email_error, email_log, email_element):
        assert self.get_element_text(email_element) == email_error, f"Actual message: {self.get_element_text(email_element)}"
        self.log.info(email_log)
        sleep(1)

    def sign_up_password(self, pwd):
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=pwd)
        self.log.info(f"'{pwd}' entered to password field")
        sleep(1)

    def verify_sign_up_password_error(self, pwd_error, pwd_log, pwd_element):
        assert self.get_element_text(pwd_element) == pwd_error, f"Actual message: {self.get_element_text(pwd_element)}"
        self.log.info(pwd_log)
        sleep(1)

    def sign_up(self, username, email, pwd):
        # Fill username, email, password
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.log.info(f"'{username}' entered to username field")
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.log.info(f"'{email}@gmail.com' entered to email field")
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=pwd)
        self.log.info(f"'{pwd}' entered to password field")
        sleep(1)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        self.log.info(f"button 'Sign up for OurApp' clicked")
        sleep(1)

    def verify_profile_button(self):
        """Verify success Sign Up using 'My profile' button"""
        assert self.get_element(self.constants.MY_PROFILE_BUTTON_XPATH).is_enabled, f"Registration failed"
        sleep(1)

    # TODO: next page
    def sign_out_click(self):
        self.click(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)
        self.log.info("button 'Sign Out' clicked")
        sleep(1)
