# Ques 5.
# Write a Python program to add a key to a dictionary.
# Write a Python program to concatenate following dictionaries to create a new one.

# Data:
# {1:'RED', 2:'BLUE'}, {3:'GREEN', 4:'YELLOW'}, {5:'PURPLE',6:'ORANGE'}

# Part 1
e_dict = {}
e_dict['New_Key'] = 47

# Part 2
sample_dict_1 = {1:'Red', 2:'Blue'}
sample_dict_2 = {3:'Green', 4:'Yellow'}
sample_dict_3 = {5:'Purple', 6:'Orange'}

in_dict = [sample_dict_1, sample_dict_2, sample_dict_3]

def dict_merger(input_dict):
	final = {}

	for i in input_dict:
		final.update(i)
	return final

final_dict = dict_merger(in_dict)
print(final_dict)