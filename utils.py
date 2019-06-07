import numpy as np

def onehotCategorical(req, limit, store=0):
    arr = np.zeros((limit,))
    arr[req-1] = 1.
    
    return arr
