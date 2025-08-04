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
        self.anti = self.df[self.df['Biased'] == 1]
        self.anti_sum = int(self.anti['Biased'].count())

        self.not_anti = self.df[self.df['Biased'] == 0]
        self.not_anti_sum = int(self.not_anti['Biased'].count())

        self.undefined = self.df[~self.df['Biased'].isin([0,1])]
        self.undefined_sum = int(self.undefined['Biased'].count())

        return {
            'antisemitic':self.anti_sum,
            'not_antisemitic':self.not_anti_sum,
            'undefined':self.undefined_sum,
            'total':self.anti_sum + self.not_anti_sum + self.undefined_sum
        }

    # counting the length of each tweet per category
    def average_tweet(self):
        self.avg_len_anti = float(self.anti['Text'].apply(lambda x: len(str(x).split())).mean())
        self.avg_len_not_anti = float(self.not_anti['Text'].apply(lambda x: len(str(x).split())).mean())
        self.avg_len_undefined = float(self.undefined['Text'].apply(lambda x: len(str(x).split())).mean())
        return {
            'antisemitic tweet len': self.avg_len_anti,
            'not antisemitic tweet len': self.avg_len_not_anti,
            'undefined tweet len': self.avg_len_undefined
            }


a = DataAnalyzer(df)
print(a.category_count())
print(a.average_tweet())