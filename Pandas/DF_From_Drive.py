import pandas as pd

udemy_df = pd.read_csv("C:/Users/prakh/Downloads/udemy_courses.csv")
# print("Udemy DF Shape",udemy_df.shape)
# print(udemy_df.head())

# Similarly we have a tail objevcvt that shows last 5 rows. 

# Printing All Column
udemy_column = udemy_df.columns
# print(udemy_column)

# Printing All Specific Column
udemy_Specific_column = udemy_df["content_duration"]
# print(udemy_Specific_column)

test_df = udemy_df[['is_paid','price','course_id']].loc[:5].copy()
# print(test_df)

test_df.loc[6] = [False, 1000, 45]
# print('/n')
# print("---------New DF---------")
# print(test_df)

# It describe a lot for all numerical data.
# print(udemy_df.describe())

# Specific Data of column
subset_df = udemy_df[(udemy_df["content_duration"] == 5.0) & (udemy_df["price"] > 10)]
print(subset_df)