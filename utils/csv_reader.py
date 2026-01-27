import csv
import os


def read_csv_data(file_path):
    """
    Read CSV data and return as list of dictionaries
    """
    test_data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append(row)
    return test_data


def get_login_data():
    """
    Get login test data from CSV file
    """
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(current_dir, 'data', 'login_data.csv')
    return read_csv_data(csv_path)
