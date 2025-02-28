
# Import relevant libraries
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename="datacleaner.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


# Create a class
class DataCleaner:
    def __init__(self, df):
        self.df = df

    # Create a method to check for missing data
    def check_missing_values(self):
        """Check and summarise missing values."""
        missing_summary = self.df.isnull().sum()
        missing_summary = missing_summary[missing_summary > 0]
        logging.info(f"Checked missing values: \n{missing_summary}")
        return missing_summary

    def handle_missing_values(self, column, method = "drop", fill_value = "None"):
        """Handle missing values by dropping or imputing."""
        if method == "drop":
            self.df = self.df.dropna(subset=[column])
            logging.info(f"Dropped missing values in column: {column}")
        elif method == "mean":
            self.df[column] = self.df[column].fillna(self.df[column].mean())
            logging.info(f"Imputed missing values in column: {column} with mean")
        elif method == "median":
            self.df[column] = self.df[column].fillna(self.df[column].median())
            logging.info(f"Imputed missing values in column: {column} with median")
        elif method == "mode":
            self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
            logging.info(f"Imputed missing values in column: {column} with mode")
        elif method == "fill" and fill_value is not None:
            self.df[column] = self.df[column].fillna(fill_value)
            logging.info(f"Filled missing values in column: {column} with custom value: {fill_value}")
        return self.df

    def get_cleaned_data(self):
        """Return the cleaned DataFrame"""
        return self.df

    
            


