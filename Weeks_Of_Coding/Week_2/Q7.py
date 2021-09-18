# Ques 7. (a). Write a Python program to read an entire text file.
# Sample Txt File: https://filesamples.com/samples/document/txt/sample1.txt

# (b). Write a Python program to read first n lines of a file.

# Part 1

file_object = open("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_2/Sample_Text_1.txt")
print(file_object.readlines())
file_object.close()

# Part 2

file_object_2 = open("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_2/Sample_Text_1.txt")

for line in file_object_2.readlines():
	print(line)
