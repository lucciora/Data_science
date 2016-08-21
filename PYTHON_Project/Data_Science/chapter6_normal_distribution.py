import math
from matplotlib import pyplot
from Data_Science.chapter8_gradient_descent import tolerance


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2*math.pi)
    return (math.exp(-(x-mu)**2/2/sigma**2)/(sqrt_two_pi*sigma))

xs = [x * 0.01 for x in range(-50, 50)]
'''
print(xs)
pyplot.plot(xs, [normal_pdf(x) for x in xs], '-', label="Normal distribution")
pyplot.legend()
pyplot.show()
'''    
    
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.001):
    if mu != 0 or sigma != 1:
        return mu+sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -5.0, 0
    hi_z, hi_p = 5.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_pdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

'''
pyplot.plot(xs, [inverse_normal_cdf(x) for x in xs], '-', label="inverse_normal_distribution")
pyplot.legend()
pyplot.show()
'''