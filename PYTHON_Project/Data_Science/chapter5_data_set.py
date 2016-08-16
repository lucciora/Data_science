from random import randint
from collections import Counter
from matplotlib import pyplot
num_data=[randint(1,20) for _ in range(100)]
count_data = Counter(num_data)
xs = range(21)
ys = [count_data[x] for x in xs]
pyplot.bar(xs,ys)
pyplot.axis([1,20,0,15])
pyplot.title("histogram")
pyplot.xlabel("# of data")
pyplot.ylabel("#")
pyplot.show()



