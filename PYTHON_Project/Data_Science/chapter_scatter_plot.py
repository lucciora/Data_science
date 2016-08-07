
from numpy import random
from matplotlib import pyplot

x = [random.randint(1,30) for _ in range(10)]
y = [random.randint(1,30) for _ in range(10)]
labels= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

pyplot.scatter(x, y)

for label, x_count, y_count in zip(labels, x, y):
    pyplot.annotate(label, xy=(x_count,y_count), xytext=(5, -5), textcoords='offset points')

pyplot.title("x and y")
pyplot.xlabel("x")
pyplot.ylabel('y')
pyplot.show()
