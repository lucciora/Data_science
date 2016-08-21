from Data_Science.chapter6_normal_distribution import inverse_normal_cdf
from random import random
from matplotlib import pyplot
from Data_Science.chapter5_correlation import correlation

def random_normal():
    return inverse_normal_cdf(random())


xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
print(ys1)
ys2 = [-x + random_normal() /2 for x in xs]
print(ys2)

pyplot.scatter(xs, ys1, marker='.', color='black', label='ys1')
pyplot.scatter(xs, ys2, marker='.', color='gray', label='ys2')
pyplot.xlabel('xs')
pyplot.ylabel('ys')
pyplot.legend(loc=9)
pyplot.title("Very Different Joint Distributions")
pyplot.show()

print(correlation(xs, ys1))