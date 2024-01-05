import unittest
import pandas as pd
from load_ucas_linegraph import create_line_graph
from io import StringIO

class TestLineGraph(unittest.TestCase):

    def test_create_line_graph(self):
        # Assuming your data is available in a CSV file
        data_csv = """
        Year,Ethnicity,Percentage
        2020/01,Asian,20
        2020/01,Black,15
        2020/01,White,65
        2021/01,Asian,25
        2021/01,Black,18
        2021/01,White,57
        """

        df = pd.read_csv(StringIO(data_csv))
        create_line_graph(df)

        # If the function runs without errors, the test passes
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
