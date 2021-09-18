# Ques 4. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

# Sample Output: 25 48.

def operation(ele1, ele2):
	
	part_1 = lambda ele1: ele1 + 15
	part_2 = lambda ele1,ele2: ele1*ele2

	return [part_1(ele1), part_2(ele1,ele2)]

answer = operation(25, 48)
print(answer[0])
print(answer[1])