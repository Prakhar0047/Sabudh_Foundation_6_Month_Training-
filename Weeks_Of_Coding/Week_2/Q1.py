# Ques 1. (a). Write a Python program to count the number of even and odd numbers from a series of numbers. Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# (b).  Write a Python function to sum all the numbers in a list.

# Part 1a
def count_even_odd(l):
	od, ev = 0, 0
	for i in l:
		if i%2 == 0:
			ev+=1
		else:
			od+=1
	return [od,ev]

# Part 1b
def summation(l):
	s = 0
	for i in l:
		s+=i
	
	return s

List_of_number = [1,2,3,4,5,6,7,8,9]

odev = count_even_odd(List_of_number)
s = summation(List_of_number)

print("Number Of Odds",odev[0])
print("Number Of Odds",odev[1])
print("Summation Of Given Number is: ",s)