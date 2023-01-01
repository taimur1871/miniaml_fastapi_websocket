"""
scripts to process csv files for data
"""
import pandas as pd


def process_csv(df: pd.DataFrame):
    """
    process csv file
    """
    print(df.iloc[1])


if __name__ == '__main__':
    csv_path = 'data.csv'
    dataframe = pd.read_csv(csv_path)