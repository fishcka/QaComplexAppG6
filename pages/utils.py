import csv


def csv_read(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar="|")
        csv_result = [tuple(row) for row in reader]
        return csv_result
