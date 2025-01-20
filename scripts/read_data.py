import pandas as pd
import numpy as np
import os

# set up reading data function 

def read_data():
    """Read all data from the data folder."""
    try:
        # Read main data
        main_file_path = 'data/dataset - 2020-09-24.csv'
        main_df = pd.read_csv(main_file_path)

        # Read FIFA data
        fifa_file_path = 'data/FIFA-21 Complete.csv'
        fifa_df = pd.read_csv(fifa_file_path)

        # Return the DataFrames
        return main_df, fifa_df

    except FileNotFoundError as e:
        return None, None

    except pd.errors.EmptyDataError as e:
        return None, None
    
def main():
    main_df, fifa_df = read_data()
    if main_df is not None and fifa_df is not None:
        print(main_df.head())
        print(fifa_df.head())
    else:
        print("Error reading data")
