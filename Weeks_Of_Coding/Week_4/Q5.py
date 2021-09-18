# Part 1

import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:/Users/prakh/Desktop/6_Month-Training/Weeks_Of_Coding/Week_4/q5.csv")

x = df['x'].tolist()
y = df['y'].tolist()
z = df['z'].tolist()

plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('New plot')
plt.show()

# Part 2

fig, multi = plt.subplots()
multi.plot(x,y)
multi.plot(x,z)
plt.show()