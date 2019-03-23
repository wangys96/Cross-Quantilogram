import pandas as pd
import statsmodels.tsa.stattools as ts

def DescriptiveStatistics(data,adflag):
    adf = ts.adfuller(data,adflag)
    return {"mean":data.mean(),
            "median":data.median(),
            "min":data.min(),
            "max":data.max(),
            "std":data.std(),
            "skew":data.skew(),
            "kurt":data.kurt(),
            "adfs":adf[0],
            "adfpv":adf[1]}
    