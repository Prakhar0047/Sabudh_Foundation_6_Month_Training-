import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q1.csv")
monthList  = df ['month_number'].tolist()

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.3f%%', startangle=0)
plt.legend(loc='upper left')
plt.title('Sales data')
plt.show()