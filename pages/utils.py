import csv
import datetime
import logging
import random
import string
from time import sleep


def csv_read(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar="|")
        csv_result = [tuple(row) for row in reader]
        return csv_result


def random_symbols(length=20):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def wait_until_ok(timeout=5, period=0.5):
    # Retries until OK

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    # Logging actions using docstrings

    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(f"{original_function.__doc__}")
        return result

    return wrapper


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def fill_user_data(self, username="", email="", password=""):
        # Fill user with sample data and values if provided
        self.username = f"{random_symbols()}" if not username else username
        self.email = f"{random_symbols()}@gmail.com" if not email else email
        self.password = f"{random_symbols()}" if not password else password


class Post:

    def __init__(self, title="", body=""):
        self.title = title
        self.body = body

    def fill_default_post(self):
        # Fill fields using random data
        self.title = random_symbols(15)
        self.body = random_symbols(200)
