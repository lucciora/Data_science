import pandas as pd
import numpy as np

s5 = pd.Series(np.arange(10, 100, 10))
s6 = s5.drop(1)
#print(s6)
#print(s5)

d1 = pd.DataFrame(np.arange(20).reshape(4,5))
d2 = d1.drop(2, axis=1)

print(d1.values)
