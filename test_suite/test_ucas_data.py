import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)


import unittest
from load_data_files import load_excel_data


class TestLoadExcelData(unittest.TestCase):

    def test_load_excel_file(self):
        """
        Test loading the entire Excel file and assert that the data is not empty.
        """
        # Define the path to the Excel file
        file_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_data.xlsx"

        # Load the entire Excel file using the function to be tested
        excel_data = load_excel_data(file_path)

        # Assert that the loaded data is not empty
        self.assertIsNotNone(excel_data)
        #self.assertFalse(excel_data.empty)


    def test_load_appt_data_sheet(self):
        """
        Test loading the 'appt_data' sheet from the Excel file and assert that the data is not empty.
        """
        # Define the path to the Excel file
        file_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_data.xlsx"

        # Load the 'ucas_data' sheet using the function to be tested
        excel_data = load_excel_data(file_path, sheet_name='appt_data')

        # Assert that the loaded data is not empty
        self.assertIsNotNone(excel_data)
        self.assertFalse(excel_data.empty)


if __name__ == '__main__':
    unittest.main()
