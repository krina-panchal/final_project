import unittest
from load_appt_file_col import load_appt_data

class TestDataProcessing(unittest.TestCase):

    def test_load_appt_data(self):
        # Define the path to the 'appt_data' file
        appt_data_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\attp_data.xlsx"

        # Load the 'appt_data' file
        appt_data = load_appt_data(appt_data_path)

        # Assert that the loaded data is not None
        self.assertIsNotNone(appt_data)

        # Assert that the loaded DataFrame has exactly 8 columns
        self.assertEqual(appt_data.shape[1], 8)

if __name__ == '__main__':
    unittest.main()
