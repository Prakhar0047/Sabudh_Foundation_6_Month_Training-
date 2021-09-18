# In Numpy dimentions are called Axes. Eg: 1D would be called 1 axes similarly
# 2d as 2 axes etc 
# To use numpy its mandatory to import it.
import numpy as np
import time
import sys

# Declaration of Numpy Array
a = np.array([1,2,3])
# print(a)

# Calling/Extracting element is same
# print(a[0])

# Numpy array are more fast, convienent and consume less space so we prefer them more.
# Size Comparision.

# Py list
b = range(1000)
# print(sys.getsizeof(5)*len(b))

# Numpy Array
c = np.array(1000)
# print(c.size*c.itemsize)
