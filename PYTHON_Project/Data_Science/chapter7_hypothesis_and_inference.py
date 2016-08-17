import math
from Data_Science.chapter6_cumulative_distribution_function import normal_cdf


def normal_approximation_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p*(1-p)*n)
    return mu, sigma


def normal_probability_above(lo, mu = 0, sigma = 1):
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu = 0, sigma = 1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

    