import pandas as pd
data = {
        'DEPARTMENT' : ['A', 'A', 'C', 'D'],
        'YEAR' : [2010, 2012,  2014, 2016],
        'AVG_SAL' : [2000, 200, 2500, 3000]
        }
df = pd.DataFrame(data, columns=['DEPARTMENT', 'YEAR', 'AVG_SAL'])

pivot_df = df.pivot("YEAR", 'DEPARTMENT', 'AVG_SAL')
print(pivot_df)

wrong_pivot = df.pivot("AVG_SAL", "DEPARTMENT", "YEAR")
print(wrong_pivot)









