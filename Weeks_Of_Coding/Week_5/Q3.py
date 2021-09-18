# Write a program with the name sqrttwo.py to determine roots of f(x) = (x^3)- 2 (x^2) using the bisection algorithm and fsolve function. Choose a tolerance for the approximation of the root of 10^-8.

import numpy as np
from scipy.optimize import fsolve

def f(x):
	return (x**3)-(2*(x**2))

def bi(a,b,tolarence):
	left_x = a
	right_x = b
	while (np.abs(left_x-right_x) >= tolarence):
		c = (left_x+right_x)/2
		prod = f(left_x)*f(c)
		if prod > tolarence:
			left_x = c
		else:
			if prod < tolarence:
				right_x = c
	return c

answer = bi(-5,5,1e-8)
print("BiSection Answer :",answer)

quike = fsolve(f,[-1.5,1.5])
print(quike)