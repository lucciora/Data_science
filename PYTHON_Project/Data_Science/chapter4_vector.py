# 숫자 데이터를 벡터로 표현할 수 있다.

David_height_weight_age = [120, 40, 12]
Ann_height_weight_age= [110, 35, 11]

x= David_height_weight_age
y= Ann_height_weight_age
# 더하기
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]  

print(vector_add(x, y))

# 뺴기
def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# 합계 구하기
def vector_sum(vectors):
    result = 0
    for vector in vectors: 
        result +=vector
    return result

print(vector_sum(x))

// scalar 곱하기
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))







