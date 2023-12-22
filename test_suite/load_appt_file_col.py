import pandas as pd

def load_appt_data(file_path):
    """
    Load the 'appt_data' file using pandas.

    Parameters:
    - file_path (str): The path to the 'appt_data' file.

    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame, or None if an error occurs.
    """
    try:
        # Load 'appt_data' file using pandas
        appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\attp_data.xlsx")  # Update parameters if your file format is different

        # Check if the loaded DataFrame has exactly 8 columns
        if appt_data.shape[1] == 8:
            return appt_data
        else:
            print(f"Error: The 'appt_data' file does not have the expected number of columns (8).")
            return None
    except Exception as e:
        print(f"Error loading 'appt_data' file: {e}")
        return None
