import random
from collections import Counter
from matplotlib import pyplot
import math
from Data_Science.chapter6_cumulative_distribution_function import normal_cdf


def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# the mean of Bernoulli(p) is p
# standard deviation is sqrt(p(1-p))


def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    
    histogram = Counter(data)
    pyplot.bar([x - 0.4 for x in histogram.keys()],
               [v / num_points for v in histogram.values()],
               0.8,
               color = '0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1-p))
    xs = range(min(data), max(data)+1)
    ys = [normal_cdf(i+0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    pyplot.plot(xs, ys)
    pyplot.title("Binomial Ditribution vs. Normal Approximation")
    pyplot.show()
    
print(make_hist(0.75, 100, 10000))

