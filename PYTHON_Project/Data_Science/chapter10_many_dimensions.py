from Data_Science.chapter5_correlation import correlation
dataset= [[1,2,3,], [4,5,6], [7,8,9]]
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_column(A, j):
   return [A_i[j] for A_i in A] 

def entry_fn(i, j):
    return 1 if (i, j) else 0

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]



def correlation_matrix(data):
    _, num_columns = shape(data)
    
    def matrix_enry(i,j):
        return correlation(get_column(data, i), get_column(data, j))
    
    return make_matrix(num_columns, num_columns, matrix_enry)
    
    
print(correlation_matrix(dataset))