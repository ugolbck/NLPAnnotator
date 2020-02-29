import pandas as pd

class DataF():

    def __init__(self, fpath):
        self.dataframe = self.load_csv(fpath)
        
    def load_csv(self, fpath):
        return pd.read_csv(fpath).drop('index', axis=1)

    def get_row(self, row):
        return str(self.dataframe.iloc[row, 4])

    def __str__(self):
        print(self.dataframe.head())



