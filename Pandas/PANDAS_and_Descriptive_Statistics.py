import pandas as pd

# part 1
dict_data = {
	"Name" : ["Rahul","Rahul","Rahul","Zara","Zara","Zara","Akshay","Akshay","Akshay","Misha","Misha","Misha"],
	"UT" : [1,2,3,1,2,3,1,2,3,1,2,3],
	"Maths" : [22,21,14,20,23,22,23,34,12,15,18,17],
	"Science" : [21,20,19,17,15,18,19,22,25,22,21,18],
	"S.St" : [18,17,15,22,21,19,20,24,19,25,25,20],
	"Hindi" : [20,22,24,24,25,23,15,17,21,22,24,25],
	"English" : [21,24,23,19,15,13,22,21,23,22,23,20]
}

dict_df = pd.DataFrame(dict_data)
# print(dict_df)

# Part 2
minvalue_series = dict_df.min()
# print(minvalue_series)

# Part 3
copy_df = dict_df.set_index("Name")
extracted_rows = copy_df.loc["Misha"]
print(extracted_rows)

# Part 4
sum_values = dict_df.sum()
# print(sum_values)

# Part 5
count_values = dict_df.count()
# print("Count Value of Column")
# print(count_values)

count_values2 = dict_df.count(axis=1)
# print("Count Value of Row")
# print(count_values2)

# Part 6
mean_values = dict_df.mean(numeric_only=True)
# print(mean_values)

# Part 7
median_values = dict_df.median(numeric_only=True)
# print(median_values)

# Part 8
quantile = dict_df.quantile([0.25,0.5,0.75], numeric_only=True)
# print(quantile)

# Part 9
discriptive_stat = dict_df.describe(datetime_is_numeric=False)
# print(discriptive_stat)

# Part 10
sorted_data = dict_df.sort_values(by="Name")
# print(sorted_data)