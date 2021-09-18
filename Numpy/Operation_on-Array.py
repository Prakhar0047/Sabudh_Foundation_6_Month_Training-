# Slicing 
# array[start:end] Start is exclusive and end is inclusive.
# array(start:end:step) 3rd patrameter is optional
# Step == Jump

import numpy as np

a = np.arange(20)

# print(a[2:16:2])

# ITERATING OVER ARRAY

for c in np.nditer(a):
	# print(c)
	pass

# Iteration order in c-style and f-style
# print("Styles.")

for c in np.nditer(a, order='F'):
	# print(c)
	pass

for c in np.nditer(a, order='C'):
	# print(c)
	pass

# JOINING ARRAY

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.arange(10).reshape(2,5)
d = np.arange(10).reshape(2,5)

# print(np.concatenate((a,b)))
# print(np.concatenate((c,d)))

# Note:: It will give error if dimentions are diffrent.
# Joining along the axis. Default Axis 0
# Axis 0 means Row-Wise and Axis 1 means X Column-Wise

print("Along Axis 1")
print(np.concatenate((c,d),axis = 0))

#  SPLITING ARRAY
z = np.arange(9)
print(np.split(z,3))

# RESIZING ARRAY
# Like other there is no restriction of matching dimension in this/.
# if dimensions doesnt matches then it just repeats the data 

e = np.array([[1,2,3],[4,5,6]])
f = np.resize(e,(2,3))
print(f)
g = np.resize(e,(3,3))
print(g)
