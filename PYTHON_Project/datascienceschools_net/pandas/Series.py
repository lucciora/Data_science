import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4])
#print(s)
#print(s.values)
#print(s.index)
#print(s*2)
#print(np.exp(s))

s2 = pd.Series([10,20,30,40], index=['a', 'b', 'c', 'd'])
#print(s2)

#print(s2.index)
#print(s2['a'])
#print(s2.b)
#print(s2['b':'d'])
#print(s2[['a','c']])
#print(s2[3])
#print(s2[2:4])
#print(s2[[3,1,2]])
#print(s2[s2>=20])
#print(s2.iteritems())
#for k, v in s2.iteritems():
#    print(k, v)

#dict 데이터의 활용
dictdata = {'kim':30,'kang':30, 'han':14, 'sun':10}
s3  = pd.Series(dictdata)
#print(s3)
lastnames = ['kang', 'kim', 'han','jung']
s4 = pd.Series(dictdata, index = lastnames)
#print(s4)
#print(pd.isnull(s4))
#print(pd.notnull(s4))
#print(s3.values, s4.values)
#print(s3.values + s4.values) # 같은 열을 더함
#print(s3+s4) # 10명인 han도 NaN로 나옴 순서 주의!


s4.name = "the number of last_names"
s4.index.name = "last_names"
#print(s4)


#print(s4.index)
#s4.index = ['song', 'yook', 'kong', 'seo']
#print(s4)












