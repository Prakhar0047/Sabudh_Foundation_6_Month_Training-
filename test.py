import numpy as np

x = np.arange(20)
y = x.reshape(20,1)

print(y)

for i in range(len(y)):
	y[i] = 0

print(y[1])
