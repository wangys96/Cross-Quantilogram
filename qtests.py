#import pandas as pd
#import numpy as np

def BoxPierceQ(cqlist,maxp,T):
    return [T*sum(x**2 for x in cqlist[:p]) for p in range(1,maxp+1)]

def LjungBoxQ(cqlist,maxp,T):    
    return [T*(T+2)*sum((x**2)/(T-k-1) for k,x in enumerate(cqlist[:p])) for p in range(1,maxp+1)]