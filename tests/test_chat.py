from pages.utils import random_symbols


class TestChat:

    def test_send_message_to_chat(self, login):
        # Login
        send_message = login.header.navigate_to_chat()
        # Send and verify first message
        message1 = random_symbols(8)
        send_message.send_chat_message(message1)
        send_message.verify_chat_messages([message1])
        # Send and verify second message
        message2 = random_symbols(8)
        send_message.send_chat_message(message2)
        send_message.verify_chat_messages([message1, message2])
        # Click Close
        send_message.close_chat()
