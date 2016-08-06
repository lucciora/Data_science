from matplotlib import pyplot
variance = [2**(n-1) for n in range(1, 10)]
bias_squared =[int(256*0.5**(n-1)) for n in range(1, 10)]
total_error =[x+y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)] # for ~ enumerate 사용, 1~
# x축

pyplot.plot(xs, variance, 'g-', label = 'variance')
pyplot.plot(xs, bias_squared, 'r', label = 'bias^2')
pyplot.plot(xs, total_error, 'b-', label = 'total_error')

pyplot.legend(loc=9)
pyplot.xlabel("Model complexity")
pyplot.title("This Bias-Variance Tradeoff")
pyplot.show()
