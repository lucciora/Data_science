import pandas as pd
import numpy as np

claim_data = pd.read_csv("C:/workplace/bc_data/BGCON_CLAIM_DATA.csv")
cust_data = pd.read_csv("C:/workplace/bc_data/BGCON_CUST_DATA.csv")
df = pd.DataFrame(cust_data).sort(['CUST_ID'])

#cust_id.index = np.arange(1, len(cust_id)+1)
'''
count = df["PAYM_AMT"].groupby(df['CUST_ID']).count()
mean_ = round(df["PAYM_AMT"].groupby(df['CUST_ID']).mean()) 
host_dis= round(df["HOUSE_HOSP_DIST"].groupby(df['CUST_ID']).mean())
'''
print(df)