# Ques 6.
# Write a Python program to create a set.
# Write a Python program to create a tuple with different data types.

# Part 1

x = int(input("Enter Number of Element in Set: "))
s = set()
for i in range(x):
	a = input("Enter values for Set: ")
	s.add(a)

print(s)

# Part 2

tuple_ele = int(input("Enter Number of Element in Tuple: "))
l = []

for i in range(tuple_ele):
	a = input("Enter Element of Tuple: ")
	l.append(a)
	
print(tuple(l))