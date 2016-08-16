import math
from matplotlib import pyplot
def normal_cdf(x, mu=0, sigma=1):
    return (1+math.erf((x-mu) / math.sqrt(2)/sigma)) /2
# error function 모두 더하면 1이 되는 누적 분포에 사용

xs = [x/10.0 for x in range(-50, 50)]
pyplot.plot(xs, [normal_cdf(x) for x in xs], '-', label="cumulative")
pyplot.legend(loc=2) # location 숫자에 따라 위치가 바뀜
pyplot.title("Normal cdf")
pyplot.show()