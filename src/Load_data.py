import pandas as pd


class LoadData:
    @staticmethod
    def csv_to_df(path):
        return pd.read_csv(path)