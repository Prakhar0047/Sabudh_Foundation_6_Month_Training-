import seaborn as sea
import matplotlib.pyplot as plt
import pandas as pd
 
# Part 1
data = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q67.csv")
 
sea.countplot(x ='cut', data = data)
 
plt.show()

# Part 2

plt.figure(figsize=(15,8))
sea.boxplot(x='cut', y='price', data = data)
plt.show()