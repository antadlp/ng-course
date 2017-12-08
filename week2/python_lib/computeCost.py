import numpy as np

def computeCost(X, y, theta):
    
    m = y.shape[0]
    
    # to only do once the matrix multiplication 
    # the variable h_y was added    
    h_y = np.matmul(X, theta) - y
    
    # [0, 0] argument is to only give the value and not an
    # array of arrays
    return (1/(2*m))*np.matmul(h_y.transpose(), h_y)[0,0]


