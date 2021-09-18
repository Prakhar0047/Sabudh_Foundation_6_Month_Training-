import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea 

# Part 1

df = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q67.csv")
price = df['price'].tolist()
carat = df['carat'].tolist()

# print("Price::",price[:10])
# print("Carat::",carat[:10])

plt.scatter(price, carat)
plt.xlabel('Price')
plt.ylabel('carat')
plt.title('Price Vs carat')
plt.show()

# Part 2

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(8)
plt.scatter(price, carat)
plt.show()

# Part 3
data = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q67.csv")
# sea.histplot(df, x="price")
sea.histplot(df, x="price")
plt.show()