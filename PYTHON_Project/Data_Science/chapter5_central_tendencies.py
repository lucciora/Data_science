from collections import Counter
x = [1,2,3,4,5,6,10]

def mean(x):
    return sum(x)/len(x)

print(mean(x))

def median(v):
    n= len(v)
    sorted_v=sorted(v)
    midpoint = n//2
    
    if n % 2 ==1:
        return sorted_v[midpoint]
    
    else:
        lo = midpoint-1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
    
print(median(x))
    
def quantile(x, p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

print(quantile(x, 0.4))

# 최빈수
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

# 모두 1개씩만 들어있다면, 모든 값을 리스트로 출력. dict -> keys(), values(), items()
print(mode(x))


