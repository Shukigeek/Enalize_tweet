import pandas as pd
from pandas import DataFrame

from src.Load_data import LoadData

df = LoadData.csv_to_df(r'C:\Users\shuki\Desktop\analize_tweet\data\tweet_dataset.csv')

class DataAnalyzer:
    # loading data at initialize
    def __init__(self,data:DataFrame):
        self.df = data
        self.anti = self.df[self.df['Biased'] == 1].copy()
        self.not_anti = self.df[self.df['Biased'] == 0].copy()
        self.undefined = self.df[~self.df['Biased'].isin([0, 1])].copy()

    # counting the tweet in each category
    def category_count(self):
        self.anti_sum = int(self.anti['Biased'].count())
        self.not_anti_sum = int(self.not_anti['Biased'].count())
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

    # find the 3 longest tweet by category
    def three_longest_tweets(self):
        self.anti['len'] = self.anti['Text'].apply(lambda x : len(str(x)))
        self.three_longest_anti = self.anti.sort_values(by=['len'],ascending=False)[0:3]


        self.not_anti['len'] = self.not_anti['Text'].apply(lambda x : len(str(x)))
        self.three_longest_not_anti = self.not_anti.sort_values(by=['len'],ascending=False)[0:3]


        self.undefined['len'] = self.undefined['Text'].apply(lambda x : len(str(x)))
        self.three_longest_undefined = self.undefined.sort_values(by=['len'],ascending=False)[0:3]


        return {
            'longest three tweets': {
                    'antisemitic':self.three_longest_anti['Text'].tolist(),
                    'not antisemitic': self.three_longest_not_anti['Text'].tolist(),
                    'undefined':self.three_longest_undefined['Text'].tolist()
                    }
        }


a = DataAnalyzer(df)
print(a.category_count())
print(a.average_tweet())
print(a.three_longest_tweets())