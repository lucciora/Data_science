# corvariance
from Data_Science.chapter4_vector import dot
from Data_Science.chapter5_dispersion import de_mean
from numpy import std

x = [1,2,3,4,5,6,7,8,9]
y = [19, 18, 17, 16, 15, 14, 13, 12, 11]
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

print(covariance(x,y))


# 상관계수
def correlation(x, y):
    stdev_x = std(x)
    
    stdev_y = std(y)
    if stdev_x > 0 and stdev_y >0:
        return covariance(x, y)/stdev_x / stdev_y
    else:
        return 0
    
print(correlation(x, y))