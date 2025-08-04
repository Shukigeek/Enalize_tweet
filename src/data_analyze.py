import pandas as pd
from pandas import DataFrame

from src.Load_data import LoadData

df = LoadData.csv_to_df(r'C:\Users\shuki\Desktop\analize_tweet\data\tweet_dataset.csv')

class DataAnalyzer:
    # loading data at initialize
    def __init__(self,data:DataFrame):
        self.df = data

    # counting the tweet in each category
    def category_count(self):
        self.anti = int((self.df['Biased'] == 1).sum())
        self.not_anti = int((self.df['Biased'] == 0).sum())
        self.undefined = int((~self.df['Biased'].isin([0,1])).sum())

        return {
            'anti':self.anti,
            'not_anti':self.not_anti,
            'undefined':self.undefined,
            'total':self.anti + self.not_anti + self.undefined
        }


a = DataAnalyzer(df)
print(a.category_count())