# ques 7. Plot the following distributions:

# a distribution that varies at equal probability between 2 and -2.
# you want to be able to pick random item from a list. For example, say that you want to choose randomly between red, green, and blue, such that the probability of green being picked is twice that of the others (hint- use random.choice())

import numpy, pandas, random
from scipy.stats import binom
import matplotlib.pyplot as plt
from collections import Counter

# n = 5
# p = 0.5

# r_values = list(range(-2,3))

# mean, var = binom.stats(n,p)

# dist = [binom.pmf(r,n,p) for r in r_values]

# plt.bar(r_values, dist)
# plt.show()

l=['red','green','blue','green']
d = Counter(l)
print('Probability of {} is {} '.format("Red", (d["red"]/4)))
print('Probability of {} is {} '.format("Red", (d["green"]/4)))
print('Probability of {} is {} '.format("Red", (d["blue"]/4)))