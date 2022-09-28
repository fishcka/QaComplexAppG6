import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=3)

    def wait_until_displayed(self, xpath):
        """Wait until element is displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)),
                                 message=f"XPATH: '{xpath}' is not displayed or cannot be found")

    def wait_until_clickable(self, xpath):
        """Wait until element is clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)),
                                 message=f"XPATH: '{xpath}' is not clickable or cannot be found")

    def is_exists(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def fill_field(self, xpath, value):
        """Find field and fill it"""
        element = self.wait_until_clickable(xpath=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Click element"""
        self.wait_until_clickable(xpath=xpath).click()

    def get_element(self, xpath):
        """Find element"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element

    def get_element_text(self, xpath):
        """Find element text"""
        element = self.wait_until_displayed(xpath=xpath)
        return element.text
