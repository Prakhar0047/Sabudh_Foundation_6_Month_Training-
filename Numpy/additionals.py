import numpy as np

# Row + Row
a = np.array([(1,2,3),(4,5,6)])
print(a.sum(axis=0))

# Column + Column
b = np.array([(1,2,3),(4,5,6)])
print(b.sum(axis=1))

#  Square root and Standard Deviation.
print(np.sqrt(a))
print(np.std(a))

# Ravel Function = Sets all elementrs as column
print(np.ravel())

# Log10 = Base 10 for 2 use 2
print(np.log10(a))