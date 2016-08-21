
from random import randint
from sklearn import linear_model
import numpy as np
from matplotlib import pyplot
X = [[randint(1, 30)] for _ in range(1000)]
X_train = X[:-100]
X_test = X[-100:]

Y= [[randint(1, 30)] for _ in range(1000)]
Y_train = Y[:-100]
Y_test = Y[-100:]

regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train)

print('Coefficients: \n', regr.coef_)
print("Residual sum of squares : %.2f"
      % np.mean((regr.predict(X_test) - Y_test) ** 2))

print('Variance score: %.2f' % regr.score(X_test, Y_test))


pyplot.scatter(X_test, Y_test, color='blue')
pyplot.plot(X_test, regr.predict(X_test), color='red', linewidth=3)

pyplot.xticks(())
pyplot.yticks(())

pyplot.show()



# Plot outputs

