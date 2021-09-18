import pandas as pd
 
# SERIES -- Basic block of panda. It can hold a lot of data types. Int, float, dict, etc.

sample_series = pd.Series(data=[1,2,3,4,5], index=[100,101,102,103,104], dtype="int32")
# print(sample_series)

# If we give index=None then default index will start from 0 asusual.
# Variation

animal_size = ['small','tiny','medium','large','massive','titanic']
animal_name = ['Tiger','Rabbit','Elephant','Dianasor','Titanaboa','Tartoras']

animal_series = pd.Series(data=animal_name, index=animal_size, name="Animals", dtype='str')
# print(animal_series)

animal_series.loc['Molecular']='Bacteria'
# print(animal_series)

human_series = pd.Series(data=['Avery','John','Jonas','Jordan','Terry','Jared','Evan'], index=None)

animallisting = animal_series.iloc[5]
float_series = pd.Series(data=[12,234,4,332,23], index=[1.1,1.2,1.3,1.4,1.5], dtype='float32')
# print(float_series.loc[1.1])

data_dict = {
	'name':'A',
	'Age':'12',
	'Gender':'Male'
}

dict_series = pd.Series(data_dict)
# print(dict_series)

# DATAFRAME
# ,['Prakhar',20,'CSE'],['Prakhar',20,'CSE']

list_df =pd.DataFrame(data=[['Prakhar',20,'CSE']], columns=['Name','Age','Branch'], index=[1,2,3,4,5,6])
# print(list_df.head())

# No Index Single row -- Singlr Row, 10 Index single row - It will duplicate it., 10 index more than 1 row -- Throw an error.

# DICTIONARY AS DATAFRAME
# If we use it this way then it will consider key as column and its value as row.

dict_data = {
    "name" : ["apple", "orange", "banana", "onion"],
    "price" : [10, 20, 30, 40]
}
dict_df = pd.DataFrame(dict_data)
# print(dict_df)

# Accessing single column
# print(dict_df["price"])

# Adding Column In Existing DF
dict_df['Age'] = ['Old','young','tiny','Ultra Age']
# print(dict_df)

# We can use empty string, None, Null

ques_df = pd.DataFrame(data=[[35,21],[41,34]], columns=['Apples','banana'], index=['2017 Sales','2018 Sales'])

print(ques_df)