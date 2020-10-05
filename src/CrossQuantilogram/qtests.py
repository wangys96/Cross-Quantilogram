import numpy as np

def BoxPierceQ(cqlist,maxp,T):
    cq = np.array(cqlist[:maxp])
    return T*np.cumsum(np.power(cq,2))

def LjungBoxQ(cqlist,maxp,T):
    cq = np.array(cqlist[:maxp])
    return T*(T+2)*np.cumsum(np.power(cq,2)/np.arange(T-1,T-maxp-1,-1))