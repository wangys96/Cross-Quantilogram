import pandas as pd
import numpy as np
import time
from .stationarybootstrap import Bootstrap
from .crossquantilogram import CrossQuantilogram
from .qtests import LjungBoxQ

def CQ_lags(data1,a1,data2,a2,k,cqcl=0.95,testf=LjungBoxQ,lbqcl=0.95,n=1000,verbose=True):
    """
    Calculate Cross-Quantilogram result on many lags [1,k] and 1 particular quantile (a1,a2) from data2 to data1.

    input:
        data1: array-like, serie-1.
        a1: float between (0,1), quantile of serie-1.
        data2: array-like, serie-2 (k lagged).
        a1: float between (0,1), quantile of serie-2.
        k: non-negative integer, the serie-2's max lag.
        cqcl: optional float between (0,1), the level of confidence interval of CQ, 0.95 as default.
        lbqcl: optional float between (0,1), the critical level of Q statistics, 0.95 as default. 
        n: optional integer, the repeating time of bootstrap, 1000 as default.
        verbose: optional boolean, if it will print the procedure.
    output:
        pandas.DataFrame containing k rows and 5 cols("cq","cq_upper","cq_lower","lbq","lbqc")
    """
    length = data1.shape[0]
    cqlist,lbqlist=[],[] # (n,k) matrix
    for i in range(n): #n次bs重复
        cqbs,proced=list(),int(n*0.05)
        if verbose and proced>0 and i%proced==0:
            print("Bootstraping {}/{}".format(i,n),end='\r')
        for lag in range(1,k+1): #对每个k延迟重复bs
            bs1,bs2 = Bootstrap(data1,data2,lag,length,False)
            cqbs.append(CrossQuantilogram(bs1,a1,bs2,a2,lag))
        cqlist.append(cqbs)
        lbqlist.append(testf(cqbs,k,length))
        
    cqsample = []
    for i in range(1,k+1):
        cqsample.append(CrossQuantilogram(data1,a1,data2,a2,i))
        
    cqdf = pd.DataFrame(cqlist,columns=list(range(1,k+1)))
    lbqdf = pd.DataFrame(lbqlist,columns=list(range(1,k+1)))
    
    cq_upper,cq_lower,lbqc,cquc,cqlc = [],[],[],(1+cqcl)/2,(1-cqcl)/2
    for i in range(1,k+1):
        cq_upper.append(cqdf[i].quantile(cquc,"higher"))
        cq_lower.append(cqdf[i].quantile(cqlc,"lower"))
        lbqc.append(lbqdf[i].quantile(lbqcl,"higher"))
    if verbose:
        print("Calculation done      ")
    return pd.DataFrame({"cq":cqsample,"cq_upper":cq_upper,"cq_lower":cq_lower,
                           "lbq":testf(cqsample,k,length),"lbqc":lbqc},index=list(range(1,k+1)))

def CQ_alphas(data1,a1list,data2,a2list,lag=1,cqcl=0.95,testf=LjungBoxQ,lbqcl=0.95,n=1000,verbose=True):
    mat,txt,total,count=[],[],len(a1list)*len(a2list),1
    for a2 in a2list:
        mat.append([])
        txt.append([])
        for a1 in a1list:
            res=CQ_lags(data1,a1,data2,a2,lag,cqcl,testf,lbqcl,n,False)
            mat[-1].append(res["cq"][lag])
            if (res["cq"][lag]>res["cq_upper"][lag] or res["cq"][lag]<res["cq_lower"][lag]) and res["lbq"][lag]>res["lbqc"][lag]:
                txt[-1].append("*")
            else:
                txt[-1].append("")
            if verbose:
                print("Processing {}/{}   ".format(count,total),end="\r")
                count+=1
    mat=np.array(mat)
    print("Calculation done      ")
    return mat,txt