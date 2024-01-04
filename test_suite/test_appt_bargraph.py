# Importing necessary Python data visualization and analysis libraries
import unittest
import pandas as pd
import matplotlib.pyplot as plt
from load_appt_bargraph import create_ethnicity_gender_plot

# Test class for the 'create_ethnicity_gender_plot' function
class TestLoadApptBarGraph(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
                'Ethnic Group': ['A', 'B', 'A', 'B', 'C']}
        self.test_data = pd.DataFrame(data)

    def test_create_ethnicity_gender_plot(self):
        """
        Test whether the 'create_ethnicity_gender_plot' function runs without errors.

        Raises:
        - AssertionError: If an exception is raised during the function execution.
        """
        try:
            create_ethnicity_gender_plot(self.test_data)
        except Exception as e:
            self.fail(f"create_ethnicity_gender_plot() raised an exception: {e}")

    def test_create_ethnicity_gender_plot_output(self):
        """
        Test whether the 'create_ethnicity_gender_plot' function produces the expected output type.

        Raises:
        - AssertionError: If the output type is not as expected.
        """
        # Ensure the function produces the expected output
        expected_output_type = plt.Figure
        actual_output = create_ethnicity_gender_plot(self.test_data)
        self.assertIsInstance(actual_output, expected_output_type)

# Entry point for running the tests
if __name__ == '__main__':
    unittest.main()
