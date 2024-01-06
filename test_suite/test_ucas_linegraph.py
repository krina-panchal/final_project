import unittest
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_data():
    data_path = Path(__file__).parent / 'test_suite' / 'ucas_ungrad.csv'
    return pd.read_csv(data_path)

# Data cleansing
def clean_data(df):
    df['Time'] = df['Time'].str.extract('(\d{4}/\d{2})', expand=False)
    return df

# Filter out rows with missing values
def filter_data(df):
    return df.dropna(subset=['Percentage'])

class TestDataProcessing(unittest.TestCase):

    def test_numeric_percentage(self):
        ucas_ungrad = load_data()
        ucas_ungrad = clean_data(ucas_ungrad)
        ucas_ungrad = filter_data(ucas_ungrad)
        self.assertTrue((ucas_ungrad['Percentage'].apply(lambda x: str(x).replace('%', ''))).apply(pd.to_numeric, errors='coerce').notnull().all())

if __name__ == '__main__':
    unittest.main()