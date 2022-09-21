from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, xpath, value):
        """Find field and fill it"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Click element"""
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def get_element(self, xpath):
        """Find element"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element

    def get_element_text(self, xpath):
        """Find element text"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element.text
