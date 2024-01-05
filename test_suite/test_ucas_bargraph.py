import unittest
from load_ucas_bargraph import load_ucas_bargraph
import matplotlib.pyplot as plt

class TestLoadUcasBargraph(unittest.TestCase):
    """
    Unit test class for the load_ucas_bargraph function.

    Attributes:
        None

    Methods:
        test_load_ucas_bargraph: Tests the load_ucas_bargraph function by checking the correctness of the generated plot.
    """

    def test_load_ucas_bargraph(self):
        """
        Tests the load_ucas_bargraph function by checking the correctness of the generated plot.

        The test includes checking the order of ethnic groups on the x-axis, the presence of correct years, and
        the presence of specific ethnic groups on the y-axis.

        Raises:
            AssertionError: If the test fails due to any unexpected exceptions or incorrect plot elements.
        """
        try:
            load_ucas_bargraph()

            # Get the tick labels from the x-axis
            x_labels = [label.get_text() for label in plt.gca().get_xticklabels()]

            # Define the expected order of ethnic groups
            expected_order = ['Asian ethnic group', 'Black ethnic group', 'Mixed ethnic group', 'Other ethnic group', 'White ethnic group']

            # Check if each ethnic group is present in the x-axis labels
            for ethnic_group in expected_order:
                self.assertTrue(any(ethnic_group in label for label in x_labels), f"{ethnic_group} not found in the x-axis labels: {x_labels}")

            # Check if the correct years are in the plot
            x_ticks = plt.xticks()[1]
            self.assertIn('2019', x_ticks, "Year 2019 not found in the plot")
            self.assertIn('2020', x_ticks, "Year 2020 not found in the plot")

            # Check if the correct ethnic groups are in the y-axis ticks
            y_ticks = plt.yticks()[0]
            ethnic_groups_to_check = ['Asian ethnic group', 'Black ethnic group', 'Mixed ethnic group', 'Other ethnic group', 'White ethnic group']
            for ethnic_group in ethnic_groups_to_check:
                self.assertIn(ethnic_group, y_ticks, f"{ethnic_group} not found in the y-axis ticks: {y_ticks}")

        except Exception as e:
            self.fail(f"load_ucas_bargraph() raised an exception: {str(e)}")

        finally:
            plt.close()

if __name__ == '__main__':
    unittest.main()
