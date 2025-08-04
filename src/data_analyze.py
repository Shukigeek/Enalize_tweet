from collections import Counter
import pandas as pd
from src.Load_data import LoadData

df = LoadData.csv_to_df(r'C:\Users\shuki\Desktop\analize_tweet\data\tweet_dataset.csv')
class DataAnalyzer:
    def __init__(self, data: pd.DataFrame):
        self.df = data

        # new columns to count word and char and uppercase
        self.df['word_count'] = self.df['Text'].apply(lambda x: len(str(x).split()))
        self.df['char_count'] = self.df['Text'].apply(lambda x: len(str(x)))
        self.df['uppercase_words'] = self.df['Text'].apply(
            lambda x: sum(1 for word in str(x).split() if word.isupper())
        )

    # counts how many tweets is antisemitic and how many is not
    def category_count(self):
        counts = self.df['Biased'].value_counts(dropna=False)
        antisemitic = counts.loc[1]
        not_antisemitic = counts.loc[0]
        undefined = self.df[~self.df['Biased'].isin([0, 1])].shape[0]

        return {
            'antisemitic': int(antisemitic),
            'not_antisemitic': int(not_antisemitic),
            'undefined': int(undefined),
            'total': int(len(self.df))
        }

    # count the avg length of tweet per category
    def average_tweet(self):
        grouped = self.df.groupby('Biased')['word_count'].mean()
        total = self.df['word_count'].mean()
        return {
            'antisemitic tweet len': float(grouped.loc[1]),
            'not antisemitic tweet len': float(grouped.loc[0]),
            'undefined tweet len': float(self.df[~self.df['Biased'].isin([0, 1])]['word_count'].mean()),
            'total tweet len':float(total)
        }

    # holds the three longest tweet per category
    def three_longest_tweets(self):
        result = {}
        for label, name in [(1, 'antisemitic'), (0, 'not antisemitic')]:
            top = self.df[self.df['Biased'] == label].nlargest(3, 'char_count')['Text'].tolist()
            result[name] = top
        # undefined
        undefined_top = self.df[~self.df['Biased'].isin([0, 1])].nlargest(3, 'char_count')['Text'].tolist()
        result['undefined'] = undefined_top

        return {'longest three tweets': result}

    # hold the 10 must common words
    def common_ten_word(self):
        words = ' '.join(self.df['Text'].astype(str)).split()
        return Counter(words).most_common(10)

    # counts the uppercase words per category
    def uppercase_words(self):
        grouped = self.df.groupby('Biased')['uppercase_words'].sum()
        return {
            'antisemitic': int(grouped.loc[1]),
            'not_antisemitic': int(grouped.loc[0]),
            'undefined': int(self.df[~self.df['Biased'].isin([0, 1])]['uppercase_words'].sum())
        }
