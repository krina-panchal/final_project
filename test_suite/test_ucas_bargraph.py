import unittest
from load_ucas_bargraph import load_ucas_bargraph
import matplotlib.pyplot as plt

class TestLoadUcasBargraph(unittest.TestCase):

    def test_load_ucas_bargraph(self):
        # Since the function is mostly for plotting, we can't check the output directly.
        # We will run the function and check if the correct elements are present in the plot.

        try:
            # Run the function to generate the plot
            load_ucas_bargraph()

            # Check if the correct years and ethnic groups are in the plot
            x_ticks = plt.xticks()[1]
            self.assertIn('2019', x_ticks, "Year 2019 not found in the plot")
            self.assertIn('2020', x_ticks, "Year 2020 not found in the plot")

            # Check if the correct ethnic groups are in the plot
            y_ticks = plt.yticks()[0]
            # Add your ethnic groups to be checked
            ethnic_groups_to_check = ['White ethnic group', 'Asian ethnic group', 'Mixed ethnic group', 'Black ethnic group']
            for ethnic_group in ethnic_groups_to_check:
                self.assertIn(ethnic_group, y_ticks, f"{ethnic_group} not found in the y-axis ticks: {y_ticks}")

        except Exception as e:
            self.fail(f"load_ucas_bargraph() raised an exception: {str(e)}")

        finally:
            # Close the plot to avoid interference with subsequent tests or plots
            plt.close()

if __name__ == '__main__':
    unittest.main()
