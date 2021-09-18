# ques 3. 

# a. Given an array of random numbers, push all the zeros of a given array to the end of the array. The order of all other elements should be the same.
# for example:

# input array: [3, 6, 8, 8, 0, 0, 1, 4, 0, 6, 0, 5]

# output array: [3, 6, 8, 8, 1, 4, 6, 5, 0, 0, 0, 0]

# b. Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
# example:

# input : [0, -2, 1, -3, 1]

# output : [-2, 1, 1]

# Part 3A
arr = [3, 6, 8, 8, 0, 0, 1, 4, 0, 6, 0, 5]

for i in arr:
	if i == 0:
		arr.remove(i)
		arr.append(i)

# print(arr)

# Part 3B
arr2 = [0, -2, 1, -3, 1]
found = False

arr2.sort()

for i in range(0, len(arr2)):
	l = i+1
	r = len(arr2)-1
	x = arr2[i]
	while l<r:
		if (x+arr2[l]+arr2[r]==0):
			print(x,arr2[l],arr2[r])
			l+=1
			r+=1
			found = True
			if found == True:
				break
		elif (x+arr2[l]+arr2[r]<0):
			l+=1
		else:
			r-=1

if found == False:
	print("Not Such Triplet exist.")
 