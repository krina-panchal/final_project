import unittest
import io
import matplotlib.pyplot as plt
from unittest.mock import patch
from load_ucas_linegraph import load_and_plot_ucas_data

class TestLoadUCASLineGraph(unittest.TestCase):

    @patch("load_ucas_linegraph.plt.show", return_value=None)  # Mocking plt.show to prevent displaying the plot during tests
    def test_create_line_graph(self, mock_show):
        # Provide a test file path or mock the file loading if needed
        file_path = r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\ucas_ungrad.csv"

        # Use the Agg backend to capture the plot
        plt.switch_backend('Agg')

        # Call the function
        load_and_plot_ucas_data(file_path)

        # Get the plot as an image buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Check if the image buffer is not empty
        self.assertTrue(buffer.readable())
        buffer.close()

if __name__ == '__main__':
    unittest.main()

