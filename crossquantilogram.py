import pandas as pd
import numpy as np

def CrossQuantilogram(x1,alpha1,x2,alpha2,lag):
    """
    Calculate Cross-Quantilogram rho
    input: x1 series,
            x1's quantile level,
            x2 serie, 
            x2's quantile level,
            x2's lag
    """
    if lag==0:
        array_x1 = np.array(x1)
        array_x2 = np.array(x2)
    elif lag > 0:
        array_x1 = np.array(x1[lag:])
        array_x2 = np.array(x2[:-lag])
    elif lag < 0:
        array_x1 = np.array(x1[:lag])
        array_x2 = np.array(x2[-lag:])

    if len(array_x2.shape)>1:
        raise ValueError("x2 must be 1D array")
        
    if len(array_x1.shape)==1:
        array_x1=array_x1.reshape(array_x1.shape[0],1)

    q1 = np.percentile(array_x1, alpha1*100, axis=0, interpolation='higher')
    q2 = np.percentile(array_x2, alpha2*100, axis=0, interpolation='higher')
    
    psi1 = (array_x1 < q1) - alpha1
    psi2 = (array_x2 < q2) - alpha2
    
    numerator = np.sum(np.multiply(psi1, psi2.reshape(psi2.shape[0],1)),axis=0)
    denominator = np.multiply(np.sqrt(np.sum(np.square(psi1),axis=0)), \
                                np.sqrt(np.sum(np.square(psi2))))

    return np.divide(numerator, denominator)[0]