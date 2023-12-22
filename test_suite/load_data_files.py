import pandas as pd


def load_excel_data(file_path, sheet_name=None):
    """
    Load data from an Excel file using pandas.


    Parameters:
    - file_path (str): The path to the Excel file.
    - sheet_name (str, optional): The name of the sheet to load. Defaults to None (loads the entire file).


    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame, or None if an error occurs.
    """
    try:
        #Load Excel file using pandas
        excel_data = pd.read_excel(file_path, engine='openpyxl', sheet_name=sheet_name)
        return excel_data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None


def main():
    """
    Example usage of the load_excel_data function.
    """
    #Loading apprenticeship_data file path
    appt_file_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\attp_data.xlsx"
   
    #Load appt_data sheet
    df = load_excel_data(appt_file_path, sheet_name='appt_data')
    if df is not None:
        print("appt_data loaded successfully:")
        print(df.head())


    #Loading ucas_data file path
    ucas_file_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_data.xlsx"
    #Load ucas_data sheet
    df2 = load_excel_data(ucas_file_path, sheet_name='ucas_data')
    if df2 is not None:
        print("ucas_data loaded successfully:")
        print(df2.head())


if __name__ == "__main__":
    main()
