import pandas as pd

class DataF():

    def __init__(self, frame):
        self.frame = frame

    def __str__(self):
        print(self.frame.head())



