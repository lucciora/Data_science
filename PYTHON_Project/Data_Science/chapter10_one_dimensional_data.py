import math
from collections import Counter
from matplotlib import pyplot
from random import random


def bucketize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    pyplot.bar(histogram.keys(), histogram.values(), width=bucket_size)
    pyplot.title(title)
    pyplot.show()
    
    
uniform = [200 * random() - 100 for _ in range(10000)]

plot_histogram(uniform, 1)