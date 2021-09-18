import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q1.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData = df ['facecream'].tolist()
faceWashSalesData = df ['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')
plt.xticks(monthList)
plt.title('Facewash and facecream sales data')
plt.show()