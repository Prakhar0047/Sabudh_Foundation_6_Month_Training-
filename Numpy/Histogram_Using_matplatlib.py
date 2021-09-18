import numpy as np
from matplotlib import pyplot as plt

a = np.array([20,76,25,32,33,12,23,67,4,8,78,9,34,74,2,0])
plt.hist(a, bins = [0,20,40,60,80]) # hist = Histogram
plt.title("Histogram") # Title 
plt.show() 