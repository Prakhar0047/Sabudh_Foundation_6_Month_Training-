# Q1. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [12, 14, 16, 18, 20], [11, 13, 15, 17, 19]

import pandas as pd

s1 = pd.Series(data=[12,14,16,18,20])
s2 = pd.Series(data=[11,13,15,17,19])

output_add = s1.add(s2)
print("Addition")
print(output_add)

output_sub = s1.subtract(s2)
print("Substration")
print(output_sub)

output_multiply = s1.mul(s2)
print("Multiply")
print(output_multiply)

output_division = s1.div(s2)
print("Division")
print(output_division)