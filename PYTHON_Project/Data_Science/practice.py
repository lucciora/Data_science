def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]  

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result
numeric_vectors=[1,2,3]
print(vector_sum(numeric_vectors))