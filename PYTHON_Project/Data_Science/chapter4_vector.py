# 숫자 데이터를 벡터로 표현할 수 있다.
from random import randint
import math

David_height_weight_age = [120, 40, 12]
Ann_height_weight_age= [110, 35, 11]

# 더하기
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]  


# 뺴기
def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# 합계 구하기
def vector_sum(vectors):
    result = 0
    for vector in vectors: 
        result +=vector
    return result


# scalar 곱하기
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return 1/n * vector_sum(vectors)

x = [randint(1,20) for _ in range(2)]
y = [randint(1,20) for _ in range(2)]


# 벡터의 내적, 벡터*벡터는 스칼라가 됨
x = [1,1]
y = [1,2]
def dot(v, w):
    return sum(v_i*w_i for v_i, w_i in zip(v, w))

print(dot(x,y))

# 정사각형
def sum_of_squares(v):
    return dot(v,v)

print(sum_of_squares(x))


def magnitude(v):
    return math.sqrt(sum_of_squares(v))



def squared_distance(v, w):
#(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

print(distance(x, y))
  








