# ques 6. let’s look at the game of craps. You roll two dice, and you win when you get a 7 as a sum of the numbers appearing on the dice. In total there are 6 ways to win. Roll 2 dice 400 times and see how many times you won. Use seed 24.

# (hint- plot a binomial distribution)

import numpy, pandas, random
from scipy.stats import binom
import matplotlib.pyplot as plt

n = 400
win_count = 0
Lose_count = 0
win_prob=0.5

random.seed(24)
for i in range(n):
	a=random.randint(1,7)
	b=random.randint(1,7)
	if a+b == 7 or a+b > 7:
		win_count+=1
	else:
		Lose_count+=1

print("Win: ",win_count)
print("Lose: ",Lose_count)

mean, var = binom.stats(n,win_prob)
values = [1,2,3,4,5,6,7,8,9,10,11,12]
dist = [binom.pmf(r,n,win_prob) for r in values]

print(mean,var)
print(dist)

plt.bar(values, dist)
plt.show()