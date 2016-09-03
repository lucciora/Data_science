from array import array
from random import random, seed
import numpy

seed(999)
floats = array('f', (random() for _ in range(100)))
print(floats)
file = open('floats.txt', 'wb')
floats.tofile(file)
file.close()
floats2 = array('f')
file = open('floats.txt', 'rb')
floats2.fromfile(file, 100)
file.close()
print(floats2[0])
print(floats2.typecode)


