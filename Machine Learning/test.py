import numpy as np
import math
import matplotlib.pyplot as plt

def gen(n,m,sigma):
  X = np.random.rand(n,m+1)
  X[:,0] = 1

  E = np.random.normal(0,sigma,(n,1))
  B = np.random.rand(m+1,1)
  Y = np.matmul(X,B) + E

  return X,Y,B

X,Y,B = gen(2000,10,0.01)

print(X.shape)
print(Y.shape)
print(B.shape)

def cost(Y, y_pred):
  return np.square(np.subtract(Y,y_pred)).mean()

def deri(X,Y,y_pred,n):
  return ((-2/n)*np.sum(np.matmul((Y-y_pred).T,X)))

def predict(X,Y,k,t):
  lr = 0.001
  p = X.shape[0]
  q = Y.shape[1]

  beta_n = np.random.rand(q,1)
  old = 100000000000

  for i in range(k):
    y_pred = np.mutmul(X, beta_n)
    new = cost(Y,y_pred)
    if abs(old-new) <=t:
      break
    else:
      old = new
      beta_n = beta_n - (lr*deri(X,Y, y_pred, p))

  return beta_n, new, y_pred

beta_n,newnew = predict(X,Y,1000,0.001)

print(newnew)
print(beta_n.shape)