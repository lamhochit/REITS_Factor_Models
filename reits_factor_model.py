import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def reits_reader(ticker):
    directory = os.path.join("/Users/lamhochit/PycharmProjects/REITS_Factor_Models/","REITS_Data/")
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                if file == ticker + ".csv":
                    df = pd.read_csv(directory + file)
                    return df
    return None


def data_loader(reits, start_date, end_date):
    df1 = reits_reader(reits)
    df1.index = df1['Date'].values
    df2 = reits_reader(reits + 'fundamental')
    df2.index = df2['Date'].values
    df1 = df1.loc[start_date:end_date]
    df2 = df2.loc[start_date:end_date]

    spy = pd.read_csv('SPY.csv')
    spy.index = spy['Date'].values
    spy = spy.loc[start_date:end_date]

    if len(spy) == len(df1):
        print('REITS {0} has been correctly imported.'.format(reits))
    else:
        print('REITS length is different from SPY length')
        return None


if __name__ == '__main__':
    data_loader('DLR', '2019-01-01', '2019-12-31')
