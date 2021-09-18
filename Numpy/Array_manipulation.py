# Changing Shape

import numpy as np

# np.array will create an array acc. to you but array will create a array for range(user defined.) 
a = np.arange(10)

# We can't put random number in it as we have a total of 9 items so we have to put a multiple of 9 items.  
b = a.reshape(2,5)
c = a.reshape(5,2)
# print(b)
# print(c)

# Flatten converts multi-dimentional into Single Dimension

d = c.flatten()
# print(d)

# Flatten Order F = Flatten wrt Column major order, C = Flatten wrt row major order
# Default is C
e = c.flatten(order="F")
# print(e)

# Transpose
trans = np.transpose(c)
# print(trans)

# DOUBT

# RollAxis a little Complex
f = np.rollaxis(b,2)

# Swap Axis
g=np.swapaxes(b,1,2)
print(g)