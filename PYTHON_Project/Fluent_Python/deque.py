from _collections import deque
len_ = 10
dq = deque(range(len_), maxlen=len_)
print(dq)
dq.rotate(2)
print(dq)
dq.append(10)
print(dq)