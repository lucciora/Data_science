from random import randint
from pip._vendor.progress import counter
from collections import Counter
from matplotlib import pyplot
num_friends =[4, 4, 5, 6, 7, 7, 7, 7,
              8, 9, 9, 10, 10, 10, 11, 
              11, 11, 11, 12, 12, 12, 
              12, 13, 13, 13, 13, 13, 
              13, 14, 14, 14, 14, 16, 16, 
              17, 17, 17, 18, 18, 19, 19, 
              19, 19, 20, 20, 21, 21, 21, 
              21, 22, 22, 23, 23, 23, 26, 
              26, 26, 27, 27, 27, 27, 29,
              29, 29, 30, 31, 32, 33, 34, 
              35, 35, 35, 36, 37, 37, 37,
              38, 39, 39, 40, 42, 42, 42, 
              42, 44, 45, 45, 46, 46, 47, 
              47, 47, 48, 48, 49, 49, 50, 
              50, 50, 100]

minutes_per_day = [39, 36, 34, 26, 34, 38, 34, 
                   35, 25, 26, 21, 35, 26, 24,
                   32, 21, 40, 27, 38, 35, 33,
                   39, 20, 38, 33, 22, 34, 36, 
                   33, 38, 40, 33, 35, 35, 38, 
                   33, 40, 39, 37, 32, 26, 33, 
                   28, 31, 29, 40, 35, 29, 24, 
                   35, 39, 33, 36, 24, 34, 23, 
                   25, 33, 39, 38, 34, 25, 38, 
                   32, 24, 20, 24, 27, 32, 39, 
                   39, 36, 24, 20, 23, 28, 38, 
                   37, 39, 39, 23, 22, 22, 27, 
                   25, 29, 32, 26, 20, 23, 28, 
                   39, 34, 38, 30, 76, 99, 100,
                   120, 160]


outlier = num_friends.index(100)

def outliers(data):
    return [i for i, x in enumerate(data) if x > 50]

print(outliers(num_friends))
print(outliers(minutes_per_day))


#num_friends_good = [x for i, x in enumerate(num_friends) if i != outlier]
num_friends_good = [x for i, x in enumerate(num_friends) if i not in outliers(num_friends)]

print(num_friends_good)
print(len(num_friends_good))


#daily_minutes_good = [x  for i, x in enumerate(minutes_per_day) if i != outlier]
daily_minutes_good = [x for i, x in enumerate(minutes_per_day) if i not in outliers(minutes_per_day)]
print(daily_minutes_good)
print(len(daily_minutes_good))

friends_counts = Counter(num_friends)
xs = range(60)
ys = [friends_counts[x] for x in xs]
pyplot.bar(xs, ys)
pyplot.axis([0, 55, 0, 10])
pyplot.show()



