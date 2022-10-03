import logging

from constants.header import HeaderConstants
from pages.base_page import BasePage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()

    log = logging.getLogger("[Header]")

    def navigate_to_create_post_page(self):
        # Click Create Post button
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    def verify_profile_button(self):
        # Verify success Sign Up using 'My profile' button
        assert self.get_element(self.constants.MY_PROFILE_BUTTON_XPATH).is_enabled, f"Registration failed"

    def sign_out_click(self):
        # Click Sign Out button
        self.click(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)
        self.log.info("button 'Sign Out' clicked")

    def navigate_to_chat(self):
        self.click(self.constants.CHAT_BUTTON_XPATH)
        from pages.chat import Chat
        return Chat(self.driver)
