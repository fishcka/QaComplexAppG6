import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants.chat import ChatConstants
from pages.base_page import BasePage


class Chat(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ChatConstants()
        from pages.header import Header
        self.header = Header(self.driver)

    log = logging.getLogger("[Chat]")

    def send_chat_message(self, message):
        self.fill_field(xpath=self.constants.CHAT_INPUT_XPATH, value=message + Keys.ENTER)
        self.log.info(f"'{message}' entered to chat field")
        self.log.info("Enter pressed")

    def verify_chat_messages(self, expected_messages):
        # Verify success messages ".//div[@class='chat-message-inner'][contains(.,'{message}')]"
        messages = self.driver.find_elements(by=By.XPATH, value=self.constants.CHAT_MESSAGES_XPATH)
        messages_text = [message.text for message in messages]
        assert messages_text == expected_messages
        self.log.info(f"'{expected_messages}' verified")

    def close_chat(self):
        self.click(self.constants.CLOSE_CHAT_BUTTON_XPATH)
        self.log.info("Button Close clicked")
