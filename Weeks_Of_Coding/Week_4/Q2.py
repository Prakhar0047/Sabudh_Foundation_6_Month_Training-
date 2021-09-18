import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q1.csv")
profitList = df ['toothpaste'].tolist()
monthList  = df ['month_number'].tolist()
print(profitList)
print(monthList)
plt.scatter(monthList, profitList)
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.grid(True, linewidth= 1, linestyle="-")
plt.yticks([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
plt.show()