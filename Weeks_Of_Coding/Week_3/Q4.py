# ques 4. given an array a containing n integers. The task is to check whether the array is monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.

# an array a is monotone increasing if for all i <= j, a[i] <= a[j]. An array a is monotone decreasing if for all i <= j, a[i] >= a[j].

# return “true” if the given array a is monotonic else return “false” (without quotes).

# example:

# input : [7 6 4 4]
# output : true

def check_monotonic(input_list, length_of_list):
	for i in range(length_of_list):
		if sorted_mono[i] < sorted_mono[i+1]:
			pass
		else:
			return True

	for i in range(length_of_list):
		if sorted_mono[i+1] < sorted_mono[i]:
			pass
		else:
			return True

monotonic_list = [7,6,4,4]
sorted_mono = sorted(monotonic_list)

answers = check_monotonic(sorted_mono,len(monotonic_list))
print(answers)