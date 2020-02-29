import pandas as pd

class DataF():

    def __init__(self, fpath):
        self.dataframe = self.load_csv(fpath)
        
    def load_csv(self, fpath):
        return pd.read_csv(fpath).drop('index', axis=1)

    def get_row(self, row):
        return str(self.dataframe.iloc[row, 4])

    def get_index_null(self):
        return self.dataframe[self.dataframe['tag'].isnull()].index.tolist()

    def __str__(self):
        print(self.dataframe.head())



