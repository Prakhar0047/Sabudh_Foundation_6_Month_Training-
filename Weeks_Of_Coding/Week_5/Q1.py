from scipy import integrate
import numpy as np

def f(x):
    return np.exp(x)

def bounds_y():
    return [0, 0.5]

x = integrate.nquad(f,[bounds_y])
print(x)