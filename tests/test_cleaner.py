# Import the relevant library
import pandas as pd
from src.cleaner import DataCleaner

def test_missing_values():
    data = {'A': [1, 2, None], 'B': [None, 5, 6]}
    df = pd.DataFrame(data)
    cleaner = DataCleaner(df)
    assert cleaner.check_missing_values().sum() == 2 # Two columns have missing values


def test_imputation():
    data = {'A': [1, None, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    cleaner = DataCleaner(df)
    cleaner.handle_missing_values("A", method = "mean")
    assert.cleaner.get_cleaned_data()["A"].isnull().sum() == 0    # No more missing values
    