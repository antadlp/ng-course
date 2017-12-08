import numpy as np
from python_lib.computeCost import *

def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(X)
    J_history = np.ones((num_iters, 1))
    
    # it = iter
    for it in range(num_iters):
        theta = theta - (alpha/m) \
        *np.matmul(X.transpose(), (np.matmul(X, theta) - y))
        
        J_history[it] = computeCost(X, y, theta)
        
    return theta, J_history[-1][0]

