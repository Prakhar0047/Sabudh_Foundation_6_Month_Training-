import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([1,2,3])

# Gives dimension for each object in array 
dimb = b.ndim
dim = a.ndim

print(dimb)
print(dim)

# Shape is daam important when it comes to DS
shape_a = a.shape
shape_b = b.shape

print(shape_a)
print(shape_b)

# Converting to Float
# You can also convert to Complex = real+imaginary
c = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.float64)
print(c)

# We can also create an array of Zeros or Ones
zero_array = np.zeros((3,4))