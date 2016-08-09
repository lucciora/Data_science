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

# matrix 표현, 중심성 중 방향성 있는 네트워크로 표현될 수 있을 듯!
directed_network = [(0,0), (1,0), (1,1), (2,0), (2,2), (3,0), (3,2), (4,1), (6,4)]
print(directed_network[1])

def finding_max_row(nodes_data):
    maxValue=0
    for i in nodes_data:
        if maxValue < i[0]:
            maxValue=i[0]
    return maxValue

def finding_max_col(nodes_data):
    maxValue=0
    for i in nodes_data:
        if maxValue < i[1]:
            maxValue=i[1]
    return maxValue

 
def make_node_matrix(nodes_data, entry_fn):
    return [[entry_fn(i,j, nodes_data) for j in range(finding_max_col(nodes_data))] 
            for i in range(finding_max_row(nodes_data))]

def all_zero_but_one(i, j, nodes_data):
    return 1 if (i, j) in nodes_data else 0
    
print(make_node_matrix(directed_network, all_zero_but_one))
# 아직 에러 (6, 4)가 출력되지 않음
    
