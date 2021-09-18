# Ques 7.
# 1. Write a Python program to test whether a passed letter is a vowel or not.

# 2. Write a Python program to display the current date and time.

	# Sample Output :
	# Current date and time :
	# 2021-07-16 05:54:38

# 3. Write a Python program to display the first and last colors from the following list.
	# color_list = ["Red","Green","White" ,"Black"]

# 4. Write a python program to generate a random number from the range 0,60 and using seed 100.

# Part 1
_str = input("Enter the letter/Alphabet: ")
vowels = ['a','e','i','o','u']
_str = _str.lower()

if _str in vowels:
	print("Yes it is a vowel.")
else:
	print("No it is not a vowel.")

# Part 2
import datetime 
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Part 3
color_list = ["Red","Green","White" ,"Black"]
print("First",color_list[0])
print("Last",color_list[-1])

# Part 4
import random
random.seed(100)
print("Random: ",random.randrange(60))