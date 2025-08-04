from src.data_analyze import DataAnalyzer
from src.Load_data import LoadData
import json

class ManagerAnalyzer:
    def __init__(self):
        # loading the original data to data frame
        self.df = LoadData.csv_to_df('data/tweet_dataset.csv')


    # analyzing the data
    def analyze(self):
        analyzer = DataAnalyzer(self.df)
        return {
            "total_tweets": analyzer.category_count(),
            "average_length": analyzer.average_tweet(),
            "common_words": analyzer.common_ten_word(),
            "longest_three_tweets": analyzer.three_longest_tweets(),
            "uppercase_word": analyzer.uppercase_words()
        }

    # writing the analysis of the data into json file
    def write_to_json(self):
        with open('results/results.json','w') as file:
            json.dump(self.analyze(),file,indent=4)




