from time import perf_counter, time
import array
from random import random
import numpy



floats = array.array('f', [random() for _ in range(10**3)])
print(floats[0])
t = perf_counter(); floats /= 3; perf_counter() - t
print(t)
