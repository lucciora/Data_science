import pandas as pd
import numpy as np

d1 = pd.DataFrame(np.arange(12).reshape(4,3), columns =['seoul', 'deagu', 'kyunggi'] )
d2 = d1.ix[(1,3), ['seoul', 'deagu']]
#print(d2)
d3 = d1.ix[1:4, 0:2]
print(d3)
