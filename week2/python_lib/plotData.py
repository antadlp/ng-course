import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plotData(x, y):
    
    phi = (1 + np.sqrt(5))/2
    height = 10
    width = 8*phi

    plt.figure(figsize=(width, height))
    plt.plot(x, y, 'rx', markersize=10)
    plt.grid(True)
    plt.ylabel('Profit in $10,000s')
    plt.xlabel('Population of City in 10,000s')
    
    return
