import pandas as pd
import numpy as np
"""
class BSDistribution:
    '''
    A Distribution for geometric distribution p(s)=γ(1-γ)^(s-1)
    '''  
    def __init__(self,turning=0.01,maxlen=1500):
        self.Calculate(turning,maxlen)

    def Calculate(self,turning,maxlen):
        self.pdfarray = self.PDF(turning,maxlen)
        self.dfarray = self.DF(self.pdfarray)
        self.turning = turning
        self.maxlen = maxlen
        self.mean = 1/turning

    def DF(self,PDF):
        '''
        return a distribution function array from pdf array
        '''       
        return np.cumsum(PDF)

    def PDF(self,turning,maxlen):
        '''
        return a probability density function array
        '''
        pdf=np.power(np.full(maxlen,(1-turning)),np.arange(maxlen))*turning
        return np.concatenate(([1-np.sum(pdf)],pdf))

# 1500 times can be enough precise.Turning parameter usually takes 0.01.
dist = BSDistribution(0.01,1500)
"""

def Bootstrap(x1,x2,lag,bslength,verbose=True):
    '''
    Generate bootstrapped data
    Input: 
        x1: array-like, serie-1, 
        x2: array-like, serie-2, 
        lag: integer, x2's lag, 
        bslength: integer, output length,
        verbose: boolean, 
    Output:
        A tuple including 2 bootstrapped series x1,x2
    '''
    #if not isinstance(bsd,BSDistribution):
    #    raise TypeError("bsd must be BSDistribution instance")
    total,dtlen = 0,x1.shape[0]-lag
    K,L = [],[]
    while total<bslength:
        if verbose:
            print("Generating random blocks:{}/{}({:.1f}%)".format(total,bslength,(total/bslength*100)),end='\r')
        K.append(np.random.randint(dtlen-lag,size=10))
        #L.append(np.random.choice(bsd.maxlen+1,size=10,p=bsd.pdfarray))
        L.append(np.random.geometric(p=0.01, size=10))
        total+=L[-1].sum()
    K,L = np.concatenate(K),np.concatenate(L)
    newx1,newx2=np.concatenate([x1[lag:]]*(L.max()//dtlen+2)),np.concatenate([x2[:dtlen]]*(L.max()//dtlen+2))
    x1output,x2output,total=[],[],0
    for Ki,Li in zip(K,L):
        if verbose:
            print("Generating samples:{}/{}({:.1f}%)".format(total,bslength,(total/bslength*100)),end='\r')
        if Li==0:continue
        x1output.append(newx1[Ki:Ki+Li])
        x2output.append(newx2[Ki:Ki+Li])
        total+=Li
        if total>=bslength:break
    if verbose:
        print("Generating samples:{}/{}(100%)   ".format(total,bslength))
    return np.concatenate(x1output)[:bslength],np.concatenate(x2output)[:bslength]

