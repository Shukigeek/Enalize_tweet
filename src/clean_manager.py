from src.Load_data import LoadData
from src.clean_data import Clean




class ManagerClean:
    def __init__(self):
        # loading the original data to data frame
        self.df = LoadData.csv_to_df('data/tweet_dataset.csv')

    # taking the old DataFrame and cleaning it
    def create_clean_df(self):
        new_df = Clean(self.df).save_relevant_column().delete_comma().change_to_lowercase().drop_not_biased().clean_df
        return new_df
    # saving the new data frame into new csv file
    def write_to_csv(self):
        self.create_clean_df().to_csv('results/tweet_dataset_cleaned.csv',index=False)
