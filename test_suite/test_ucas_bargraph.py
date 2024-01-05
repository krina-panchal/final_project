import unittest
from load_ucas_bargraph import load_ucas_bargraph
import matplotlib.pyplot as plt

class TestLoadUcasBargraph(unittest.TestCase):

    def test_load_ucas_bargraph(self):
        try:
            load_ucas_bargraph()

            # Get the tick labels from the x-axis
            x_labels = [label.get_text() for label in plt.gca().get_xticklabels()]

            # Define the expected order of ethnic groups
            expected_order = ['Asian ethnic group', 'Black ethnic group', 'Mixed ethnic group', 'Other ethnic group', 'White ethnic group']

            # Check if each ethnic group is present in the x-axis labels
            for ethnic_group in expected_order:
                self.assertIn(ethnic_group, x_labels, f"{ethnic_group} not found in the x-axis labels: {x_labels}")

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
