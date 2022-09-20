import csv
import logging
import random
import string

import pytest
from selenium import webdriver

from constants.base import BASE_URL
from pages.start_page import StartPage

log = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def page_driver():
    # Create driver
    driver = webdriver.Firefox()
    # Open page
    driver.get(BASE_URL)
    # Maximize window
    driver.maximize_window()
    log.info("firefox window opened")
    yield StartPage(driver)
    # Close driver
    driver.close()
    log.info("firefox window closed")


@pytest.fixture(scope="function")
def random_symbols():
    characters = list(string.ascii_letters + string.digits)
    # shuffling the characters
    random.shuffle(characters)
    # picking random characters from the list
    symbols_list = []
    for i in range(20):
        symbols_list.append(random.choice(characters))
    # shuffling the resultant symbols list
    random.shuffle(symbols_list)
    # converting the list to string
    symbols = "".join(symbols_list)
    return symbols


def csv_read(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar="|")
        csv_result = [tuple(row) for row in reader]
        return csv_result
