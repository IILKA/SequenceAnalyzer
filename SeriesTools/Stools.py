import pandas as pd 
import numpy as np

def ShiftTool(data, shift, info = True):
    #data should be a set of float numbers 
    #shift should be a positive integer
    data = np.array(data)
    if info:
        print("before shift: ", data.shape)
    #X should be at size (data.shape[0] - shift, shift)
    X = []
    for i in range(shift):
        X.append(data[i: -shift+i])
    X = np.array(X).T
    if info:
        print("X shape: ", X.shape)
    #y should be at size (data.shape[0] - shift, 1)
    y = data[shift:]
    if info:
        print("y shape: ", y.shape)
    return X, y

def main():
    df = pd.read_csv("/Users/fan/SequenceAnalyzer/SeriesTools/test_data.csv")
    shifted = ShiftTool(df["test1"], 5)
    print(shifted[0].shape)
    print(shifted[1].shape)
    print(shifted[0])
    print(shifted[1])

if __name__ == '__main__':
    main()

    
