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
    """Retries until OK"""

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
