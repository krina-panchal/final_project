import unittest
import pandas as pd
from load_ucas_file_datatype import load_ucas_data, check_data_types

class TestDataProcessing(unittest.TestCase):

    def test_load_ucas_data(self):
        # Define the path to the 'ucas_data' file
        ucas_data_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_data.xlsx"

        # Load the 'ucas_data' file
        ucas_data = load_ucas_data(ucas_data_path)

        # Assert that the loaded data is not None
        self.assertIsNotNone(ucas_data)

        # Assert that the loaded DataFrame has exactly 8 columns
        self.assertEqual(ucas_data.shape[1], 5)

    def test_check_data_types(self):
        # Example dataset with specific data types
        test_data = {
            'Country Provider': ['USA', 'Canada', 'UK'],
            'Year': [2021, 2022, 2023],
            'Column3': ['Value1', 'Value2', 'Value3'],
            'Column4': ['Category1', 'Category2', 'Category3']
        }
        test_dataset = pd.DataFrame(test_data)

        # Check if the data types of specific columns match the expected data types
        result = check_data_types(test_dataset)

        # Assert that the result is True (indicating that data types match the expected types)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
