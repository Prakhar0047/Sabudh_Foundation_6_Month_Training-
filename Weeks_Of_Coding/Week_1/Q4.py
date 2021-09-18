# Ques 4. 
# Write a Python program to calculate the length of a string without using len() function.
# Write a Python program to sum all the items in a list without using sum() function.

# Part 1

def str_lengeth(input_string):
	count = 0

	for i in input_string:
		count+=1

	return count

# Part 2

def sum_list(input_list):
	total = 0

	for i in input_list:
		total+=i

	return total

s = "Training Assignment at Sabudh"
l = [1,2,3,4,5,6,7,8,9,10]

str_len = str_lengeth(s)
list_sum = sum_list(l)

print("Length of String",str_len)
print("Sum of All Item in List", list_sum)