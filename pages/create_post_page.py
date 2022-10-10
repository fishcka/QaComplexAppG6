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

    def create_post(self, post, page_driver):
        """Create post"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.log.info(f"'{post.title}' entered to Title field")
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.log.info(f"'{post.body}' entered to Title field")
        # Click checkbox if needed
        if post.unique == "yes":
            self.click(xpath=self.constants.CHECK_BOX_XPATH)
        # Click option
        page_driver.get_element(xpath=self.constants.SELECT_OPTION_XPATH.format(option=post.visibility)).click()
        # Click Save
        self.click(xpath=self.constants.SAVE_NEW_POST_BUTTON_XPATH)
        self.log.info("Post created")

    def verify_successfully_created(self):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"
        self.log.info(f"Message '{self.constants.SUCCESS_MESSAGE_TEXT}' was verified")

    def verify_all_attributes(self, post):
        # Verify Title
        assert self.get_element_text(xpath=self.constants.TITLE_XPATH.format(title=post.title)) == post.title, f"Title '{post.title}' not found"
        self.log.info(f"Title '{post.title}' was verified")
        # Verify Body
        assert self.get_element_text(xpath=self.constants.BODY_XPATH.format(body=post.body)) == post.body, f"Body '{post.body}' not found"
        self.log.info(f"Body '{post.body}' was verified")
        # Verify uniqueness
        assert self.get_element_text(xpath=self.constants.UNIQUE_XPATH.format(unique=post.unique)) == f"Is this post unique? : {post.unique}", \
            f"Uniqueness '{post.unique}' not found "
        self.log.info(f"Uniqueness '{post.unique}' was verified")
        # Verify visibility
        assert self.get_element_text(xpath=self.constants.VISIBILITY_XPATH.format(visibility=post.visibility)) == post.visibility, \
            f"Option '{post.visibility}' not found"
        self.log.info(f"Visibility '{post.visibility}' was verified")
