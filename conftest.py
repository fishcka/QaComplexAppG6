import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage

log = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def page_driver():
    # Create driver
    driver = webdriver.Firefox(DRIVER_PATH)
    # Maximize window
    driver.maximize_window()
    # Open page
    driver.get(BASE_URL)
    driver.implicitly_wait(1)
    log.info("firefox window opened")
    yield StartPage(driver)
    # Close driver
    driver.close()
    log.info("firefox window closed")


@pytest.fixture()
def login(page_driver):
    # Login with registered user
    return page_driver.sign_in("ludmilaa", "ludmilaagmailcom")
