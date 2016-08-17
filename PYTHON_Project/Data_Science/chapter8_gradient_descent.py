import random
from Data_Science.chapter4_vector import distance


def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)

# 미분
def difference_quotient(f, x, h):
    return (f(x+h) - f(x)) / h

# 편미분
def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h = 0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]
    

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]
    

# gradient 기울기
def sum_of_squares_gradient(v):
    return [2*v_i for v_i in v]

v = [random.randint(-10, 10) for i in range(3)]
print(v)


tolerance = 0.001


while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

