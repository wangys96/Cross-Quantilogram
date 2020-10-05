import pandas as pd
import numpy as np
import time
from .stationarybootstrap import Bootstrap
from .crossquantilogram import CrossQuantilogram
from .qtests import LjungBoxQ

def CQBS(data1,a1,data2,a2,k,cqcl=0.95,testf=LjungBoxQ,testcl=0.95,n=1000,verbose=True):
    '''
    Calculate Cross-Quantilogram statistics for a series of lags [1,k] at 1 specific quantile pair (a1,a2) from data2 to data1.
    Generating CQ data for bar plotting. And Return a DataFrame. Shape:[lag, item(a dict{"cq","cq_lower","cq_upper","q","qc"})]
    
    Input
    -----
        data1: array-like, serie-1.
        a1: float between (0,1), quantile of serie-1.
        data2: array-like, serie-2 (k lagged).
        a2: float between (0,1), quantile of serie-2.
        k: non-negative integer, the serie-2's max lag.
        cqcl: optional float between (0,1), the level of confidence interval of CQ, 0.95 as default.
        testf: optional function, a function calculating the test statistics Q, qtests.LjungBoxQ as default.
        testcl: optional float between (0,1), the critical level of Q statistics, 0.95 as default. 
        n: optional integer, the repeating time of bootstrap, 1000 as default.
        verbose: optional boolean, if it will print the procedure.

    Output
    ------
        pandas.DataFrame containing k rows and 5 cols("cq","cq_upper","cq_lower","q","qc")

    '''
    length = data1.shape[0]
    cqlist,qlist=[],[] 
    for i in range(n):
        cqbs,proced=[0]*k,int(n*0.05)
        if verbose and proced>0 and i%proced==0:
            print("Bootstraping {}/{}".format(i,n),end='\r')
        for lag in range(1,k+1):
            bs1,bs2 = Bootstrap(data1,data2,lag,length,verbose=False)
            cqbs[lag-1] = CrossQuantilogram(bs1,a1,bs2,a2,lag)
        cqlist.append(cqbs)
        qlist.append(testf(cqbs,k,length))
        
    cqsample = [CrossQuantilogram(data1,a1,data2,a2,i) for i in range(1,k+1)]
        
    cqdata = np.vstack(cqlist)
    qdata = np.vstack(qlist)
    
    cquc,cqlc = (1+cqcl)/2,(1-cqcl)/2
    cq_upper = np.quantile(cqdata,cquc,0,interpolation="higher")
    cq_lower = np.quantile(cqdata,cqlc,0,interpolation="lower")
    qc = np.quantile(qdata,testcl,0,interpolation="higher")
    if verbose:
        print("Bootstraping CQ done      ")
    return pd.DataFrame({"cq":cqsample,"cq_upper":cq_upper,"cq_lower":cq_lower,
                           "q":testf(cqsample,k,length),"qc":qc},index=list(range(1,k+1)))

def CQBS_alphas(data1,a1list,data2,a2list,k=1,cqcl=0.95,testf=LjungBoxQ,testcl=0.95,
                all=False,n=1000,verbose=True):
    '''
    Calculate Cross-Quantilogram result for a series of lags [1,k] and {a1list}×{a2list} quantiles from data2 to data1.
    Generating CQ data for many line plottings or heatmap plotting.
    Return a 2D list of DataFrame(if all=True) or a 2D list of dict(if all=False). Shape:[row(data2),col(data1)]
    It's slow beacuse of calling CQBS for len(a1list)×len(a2list) times.

    Input
    -----
        data1: array-like, serie-1.
        a1list: array-like and between (0,1), quantiles of serie-1.
        data2: array-like, serie-2 (k lagged).
        a2list: array-like and between (0,1), quantiles of serie-2.
        k: optional non-negative integer, the serie-2's max lag, 1 as default.
        cqcl: optional float between (0,1), the level of confidence interval of CQ, 0.95 as default.
        testf: optional function, a function calculating the test statistics Q, qtests.LjungBoxQ as default.
        testcl: optional float between (0,1), the critical level of Q statistics, 0.95 as default.
        all: optional boolean, True if you want to save all [1,k] results so the 2D list will contain DataFrame; 
            False if you want to save the last result (only for lag k) so the 2D list will contain dict, False as default.
        n: optional integer, the repeating time of bootstrap, 1000 as default.
        verbose: optional boolean, if it will print the procedure.

    Output
    ------
        2D list, rows(1D) are data2, cols(2D) are data1, items are dicts or DataFrame(return of CQ_lags)
    '''
    mat,total,count=[],len(a1list)*len(a2list),1
    for a2 in a2list:
        mat.append([])
        for a1 in a1list:
            if verbose:
                print("Processing {}/{}   ".format(count,total),end='\r')
                count+=1
            res=CQBS(data1,a1,data2,a2,k,cqcl,testf,testcl,n,False)
            if all:mat[-1].append(res)
            else:mat[-1].append(dict(res.iloc[k-1]))            
    mat=np.array(mat)
    if verbose:
        print("Bootstraping CQ done      ")
    return mat

def CQBS_years(data1,a1,data2,a2,k=1,window=1,cqcl=0.95,testf=LjungBoxQ,testcl=0.95,
                all=False,n=1000,verbose=True):
    '''
    Calculate rolling Cross-Quantilogram result on lags [1,k] and (a1,a2) quantile from data2 to data1.
    Generating CQ data for rolling line plotting.
    Return 1 DataFrame(if all=False) or a list of DataFrame(if all=True) at lag∈[1,k].
    It's slow beacuse of calling CQBS for #years times.

    Input
    -----
        data1: array-like, serie-1.
        a1: float between (0,1), quantile of serie-1.
        data2: array-like, serie-2 (k lagged).
        a2: float between (0,1), quantile of serie-2.
        k: optional non-negative integer, the serie-2's max lag, 1 as default.
        window: optional positive integer, the rolling window (years), 1 as default.
        cqcl: optional float between (0,1), the level of confidence interval of CQ, 0.95 as default.
        testf: optional function, a function calculating the test statistics Q, qtests.LjungBoxQ as default.
        testcl: optional float between (0,1), the critical level of Q statistics, 0.95 as default.
        all: optional boolean, True if you want to save all [1,k] results so the list will contain k DataFrame, 
            False if you want to save the last result (only for lag k) so it will return 1 DataFrame, False as default.
        n: optional integer, the repeating time of bootstrap, 1000 as default.
        verbose: optional boolean, if it will print the procedure.

    Output
    ------
        pandas.DataFrame(return of CQ_lags) or a list of pandas.DataFrame(if all=True).
    '''
    startyear,endyear = data1.index[0].year,data1.index[-1].year
    if window>1+endyear-startyear:
        raise ValueError("length of window must <= data range")

    cqres,yearlist=[],[(str(x),str(x+window-1)) for x in range(startyear,endyear-window+2)]
    for start,end in yearlist:
        if verbose:
            print("Processing {}/{}   ".format(end,endyear),end='\r')
        cqres.append(CQBS(data1[start:end],a1,data2[start:end],a2,k,cqcl,testf,testcl,n,False))

    res,yearindex=[],[str(x) for x in range(startyear+window-1,endyear+1)]
    if all:
        for i in [[df.iloc[x] for df in cqres] for x in range(k)]:
            merged = pd.concat(i,ignore_index=True)
            merged.index = yearindex
            res.append(merged)        
    else:
        res=pd.concat(cqres,ignore_index=True)
        res.index = yearindex
    if verbose:
        print("Bootstraping CQ done      ")
    return res
 
