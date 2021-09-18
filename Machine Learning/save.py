# Part 2

cof = np.random.randn(input_data.shape[1]).reshape(input_data.shape[1],1)
print(cof)

step_size = 0.01
rmse = -1
for epoch in range(10000):
  old_rmse = rmse
  y_pred = input_data.dot(cof)
  error = y.reshape(len(x),1)-y_pred
  rmse = math.sqrt(error.t.dot(error)/input_data.shape[0])
  print(epoch,":",rmse)
  if abs(rmse-old_rmse) < 0.000000000001:
    break

  derivative = 2*error.T.dot(input_data)/input_data.shape[0]
  cof = cof+step_size*derivative.T