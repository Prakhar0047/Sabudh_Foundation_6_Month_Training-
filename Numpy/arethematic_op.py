import numpy as np

a = np.arange(9).reshape(3,3)
c = np.arange(9).reshape(3,3)
b = np.array([10,10,10])

print("A New Operation.")
print(np.add(a,c))
print("A New Operation.")
print(np.add(a,b))

# If you add same dimenion then the add to their respective ele
# But if dimensions are diffrent then they add to all object.
print("A New Operation.")
print(np.subtract(a,b))
print("A New Operation.")
print(np.multiply(a,b))
print("A New Operation.")
print(np.divide(a,b))

# Similarly For All Operations.