import re

import pandas as pd
from src.Load_data import LoadData

df = LoadData.csv_to_df(r'C:\Users\shuki\Desktop\analize_tweet\data\tweet_dataset.csv')
class Clean:
    def __init__(self,data:pd.DataFrame):
        self.clean_df = data
    # saving only the 2 important columns
    def save_relevant_column(self):
        self.clean_df = self.clean_df[['Text','Biased']].copy()
        return self

    # deleting all comma
    def delete_comma(self):
        self.clean_df['Text'] = self.clean_df['Text'].apply(
            lambda x: re.sub(r'[^\w\r ]+', '', x)
        )
        return self

    # changing all char to small
    def change_to_lowercase(self):
        self.clean_df["Text"] = self.clean_df['Text'].apply(
            lambda x : ' '.join(word.lower() for word in str(x).split())
        )
        return self

    # deleting tweets the do not biased
    def drop_not_biased(self):
        self.clean_df = self.clean_df[self.clean_df['Biased'].isin([0, 1])]
        return self

if __name__ == '__main__':

    a  = Clean(df)
    print(a.save_relevant_column().delete_comma().change_to_lowercase().drop_not_biased().clean_df.head(10))
