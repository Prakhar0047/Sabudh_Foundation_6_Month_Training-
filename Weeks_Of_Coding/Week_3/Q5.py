# ques 5. Write a numpy program to extract all the elements of the first row from a given (4x4) array.
# original array:

# [[ 0 1 2 3]

# [ 4 5 6 7]

# [ 8 9 10 11]

# [12 13 14 15]]

import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: First row")
print(arra_data[0])