import pandas as pd 
import numpy as np 




class DataProcessor():
    def __init__(self, df, input , output): #df is the dataFrame, X is the input data, Y is the target data
        self.OriginData = df 
        self.data = df
        self.X = df[input]
        self.Y = df[output]

    def __repr__(self):
        return "DataProcessorType:"+super()
    

def main():
    df = pd.read_csv("/Users/fan/SequenceAnalyzer/SeriesTools/test_data.csv")
    df.shift(1)
    print(df.head())
    

if __name__ == '__main__':
    main()
    

    





