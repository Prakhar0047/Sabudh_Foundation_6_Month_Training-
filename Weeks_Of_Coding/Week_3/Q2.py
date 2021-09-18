# ques 2.

# a. an array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero.

#       array: [1, 90, -20, 10, -90, 85]

# b. Given four arrays containing integer elements and an integer sum, the task is to count the quadruplets such that each element is chosen from a different array and the sum of all the four elements is equal to the given sum.

# for example:

# p = [ 2, 2]

# q = [-3, -2]

# r = [5, 1]

# s = [ 9, -1]

# sum = 3

# expected output : 2

# Part 2A
a = [1,90,-20,10,-90,85]
l = 0
r = len(a)-1
print(r)
b = sorted(a)
print(b)
min_sum = 34686797568
min_l, min_r, sum_b = 0,0,0

while l<r:
	sum_b = b[l]+b[r]

	if (abs(sum_b) <= abs(min_sum)):
		min_sum = sum_b
		min_l = l
		min_r = r
		if(sum_b<0):
			l+=1
		else:
			r-=1
	if sum_b == 0:
		break
	
print("Sum is:",b[min_l],b[min_r])