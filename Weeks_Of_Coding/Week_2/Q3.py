# Ques 3. Write a Python function to check whether a number falls in a given range. Where the range is 3 to 9.

def check_range(n):
	if n>=2 and n<=9:
		print("It falls under range.")
	else:
		print("It don't fall under range.")

check_range(1)
check_range(43)
check_range(7)