import pandas as pd

def load_ucas_data(file_path):
    """
    Load the 'ucas_data' file using pandas.

    Parameters:
    - file_path (str): The path to the 'ucas_data' file.

    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame, or None if an error occurs.
    """
    try:
        # Load 'ucas_data' file using pandas
        ucas_data = pd.read_csv(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_data.xlsx")  # Update parameters if your file format is different

        # Check if the loaded DataFrame has exactly 8 columns
        if ucas_data.shape[1] == 5:
            return ucas_data
        else:
            print(f"Error: The 'ucas_data' file does not have the expected number of columns (8).")
            return None
    except Exception as e:
        print(f"Error loading 'ucas_data' file: {e}")
        return None

def check_data_types(ucas_data):
    """
    Check the data types of specific columns in the 'ucas_data' DataFrame.

    Parameters:
    - ucas_data (pd.DataFrame): The 'ucas_data' DataFrame.

    Returns:
    - bool: True if the data types match the expected data types, False otherwise.
    """
    try:
        # Define expected data types for specific columns
        expected_data_types = {'Country Provider': str, 'Year': int, 'Entry of Application': str, 'Ethnic Group': str, 'Number of Applicantions': int}

        # Get actual data types from the DataFrame
        actual_data_types = ucas_data.dtypes.to_dict()

        # Check if the data types match the expected data types
        for column, expected_type in expected_data_types.items():
            if actual_data_types.get(column) != expected_type:
                print(f"Error: Data type mismatch for column '{column}'. Expected {expected_type}, got {actual_data_types.get(column)}.")
                return False

        return True

    except Exception as e:
        print(f"Error checking data types: {e}")
        return False
