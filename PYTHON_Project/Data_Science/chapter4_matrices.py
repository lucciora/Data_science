''' 행렬은 2차원  lists of lists '''

a = [[1,2,3],
     [4,5,6]]
# 2행 3열
b = [[1,2],
     [3,4],
     [5,6]]
# 3열 2행

def shape(x):
    num_rows = len(x)
    num_cols = len(x[0]) if x else 0
    return num_rows, num_cols
# 튜플로 반환

def get_rows(x, i):
    return x[i]

def get_cols(x, i):
    return [x_i[i] for x_i in x]

print(get_cols(a, 1))

# making a matrix, entry_fn에 주의할 것
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def zero_or_one(i, j):
    return 1 if i==j else 0

print(make_matrix(5, 4, zero_or_one))
