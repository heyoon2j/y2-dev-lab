import pandas as pd

def read_excel(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel file '{file_path}': {str(e)}")
        return None

def write_excel(data, file_path):
    try:
        data.to_excel(file_path, index=False)
        print(f"Data written to Excel file '{file_path}' using pandas.")
    except Exception as e:
        print(f"Error writing data to Excel file '{file_path}': {str(e)}")

def read_json(file_path):
    try:
        return pd.read_json(file_path)
    except Exception as e:
        print(f"Error reading JSON file '{file_path}': {str(e)}")
        return None

def write_json(data, file_path):
    try:
        data.to_json(file_path, orient='records', lines=True)
        print(f"Data written to JSON file '{file_path}' using pandas.")
    except Exception as e:
        print(f"Error writing data to JSON file '{file_path}': {str(e)}")