import pandas as pd
import statsmodels.tsa.stattools as ts
import pickle

def DescriptiveStatistics(data,maxlag):
    adf = ts.adfuller(data,maxlag)
    return {"mean":data.mean(),
            "median":data.median(),
            "min":data.min(),
            "max":data.max(),
            "std":data.std(),
            "skew":data.skew(),
            "kurt":data.kurt(),
            "adfs":adf[0],
            "adfpv":adf[1]}

def save(data,path):
    with open(path, 'wb+') as f:
        pickle.dump(data, f)

def load(data,path):
    with open(path, 'rb+') as f:
        return pickle.load(f)