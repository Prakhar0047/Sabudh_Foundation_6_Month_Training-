# ques 1. 
# a. Write a numpy program to get the unique elements of an array.
#         array: [10 10 20 20 30 30]

# b. Write a numpy program to compare two given arrays.
#           array a: [1 2], array b: [4 5] 

# c. Write a numpy program to calculate the arithmetic means of corresponding elements of two given arrays of the same size.
#           array a: ([[2, 5, 2], [1, 5, 5]]) b: ([[5, 3, 4],  [3, 2, 5]]) 

# d. Write a numpy program to replace the negative values in a numpy array with 0.
#           array: [-1 -4 0 2 3 4 5 -6]

import numpy as np

# Part 1A
a = np.array([10,10,20,20,30,30])
print(np.unique(a))

# Part 1B
b1 = np.array([1,2])
b2 = np.array([4,5])
print("B1 greater than B2",np.greater(b1,b2))
print("B1 greater than B2",np.greater_equal(b1,b2))
print("B1 greater than B2",np.less(b1,b2))
print("B1 greater than B2",np.less_equal(b1,b2))

# Part 1C
c1 = np.array([[2,5,2],[1,5,5]])
c2 = np.array([[5,3,4],[3,2,5]])

c_sum = np.add(c1,c2)
c_mean = np.divide(c_sum,2)
print(c_mean)

# Part 1D
d = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
d_zeroed = np.where(d<0, 0, d)
print(d_zeroed)