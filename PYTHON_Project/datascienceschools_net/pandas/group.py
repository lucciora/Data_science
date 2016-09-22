import pandas as pd
import numpy as np

data = {
        'id' : ['sam', 'sam', 'sam', 'quin', 'quin' ],
        'price' : [1,3,2,1,3],
        'keys_' : ['a', 'a', 'b', 'b', 'b'],
        'values_' : [20, 30, 40, 50, 60]}

df = pd.DataFrame(data, index = [2011, 2012, 2013, 2014, 2015])
#print(df['price'].groupby(df.id).sum())


gf = df.values_.groupby(df.keys_)
#for n, g in gf:
#    print(n)
#    print(g)
#    print(g.sum())

#std = df.price.groupby(df.keys_).std()
#print(std)

np.random.seed()
state = pd.DataFrame(np.random.randn(5,5),
                     columns = [1,2,3,4,5],
                     index = ['ace', 'box', 'cat', 'doll', 'egg'] )

#print(state)
#for n, g in state.groupby(state.index):
#    print(n)
#    print(g)

#mapping = {'ace':'a', 'box':'o', 'cat' : 'a', 'doll': 'o', 'egg':'e' }
#for n, g in state.groupby(mapping):
#    print(n)
#    print(g.sum())












