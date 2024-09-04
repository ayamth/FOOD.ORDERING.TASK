
import csv

def load_data(file_path):
    """
    Load data from a CSV file into a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def save_data(file_path, data):
    """
    Save data to a CSV file from a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.
        data (list): A list of dictionaries where each dictionary represents a row to be saved in the CSV file.
    """
    if not data:
        return 
    
    fieldnames = data[0].keys()  # Get the column names from the keys of the first dictionary
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
