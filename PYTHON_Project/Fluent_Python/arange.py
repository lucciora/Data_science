import numpy
arrays = numpy.arange(10)
print(arrays)
print(type(arrays))
arrays.shape = 2,5
print(arrays)
print(arrays[1][2])
# 열 뽑기
print(arrays[:, 2])
print(arrays.transpose())