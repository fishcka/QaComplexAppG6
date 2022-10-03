import logging

from constants.create_post_page import CreatePostPageConstants
from pages.base_page import BasePage


class CreatePostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConstants()
        from pages.header import Header
        self.header = Header(self.driver)

    log = logging.getLogger("[CreatePostPage]")

    def create_post(self, post):
        """Create post"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.log.info(f"'{post.title}' entered to Title field")
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.log.info(f"'{post.body}' entered to Title field")
        self.click(xpath=self.constants.SAVE_NEW_POST_BUTTON_XPATH)
        self.log.info("Post created")

    def verify_successfully_created(self):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"
        self.log.info(f"Message '{self.constants.SUCCESS_MESSAGE_TEXT}' was verified")
