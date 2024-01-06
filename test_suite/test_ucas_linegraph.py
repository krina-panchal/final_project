import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from load_ucas_linegraph import load_ucas_linegraph

class TestLoadUCASLineGraph(unittest.TestCase):
    @patch('sys.stdout')  # Mocking stdout to avoid unnecessary prints during the test
    def test_x_axis_labels(self, mock_stdout):
        """
        Test case for checking if x-axis labels match the expected years.

        Parameters:
        - mock_stdout (MagicMock): Mock object to capture the printed output.

        Returns:
        None
        """
        # Define the expected x-axis labels
        expected_years = ['2016/17', '2017/18', '2018/19', '2019/20', '2020/21']

        # Redirect stdout to capture print statements
        with patch('sys.stdout', new_callable=StringIO):
            # Execute the load_ucas_linegraph function with a mocked stdout
            load_ucas_linegraph(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\test_suite\ucas_ungrad.csv")

        # Perform the test
        # Access the argument passed to the mock (the printed output)
        actual_output = mock_stdout.getvalue().strip()
        actual_years = actual_output.splitlines()[-1].split()

        # Check if the actual x-axis labels match the expected ones
        self.assertEqual(actual_years, expected_years)

if __name__ == '__main__':
    unittest.main()
