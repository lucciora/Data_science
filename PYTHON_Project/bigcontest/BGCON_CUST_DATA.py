import pandas as pd
import matplotlib.pyplot as plt


cust_data = pd.read_csv("C:/workplace/bc_data/BGCON_CUST_DATA.csv")
cust_frame = pd.DataFrame(cust_data)
cust_length = len(cust_frame)
print(cust_frame.loc[[1]])
claim_data = pd.read_csv("C:/workplace/bc_data/BGCON_CLAIM_DATA.csv")
claim_frame = pd.DataFrame(claim_data)
claim_length = len(claim_frame)

for i in range(cust_length):
    count=0
    dict_ = {}
    for j in range(claim_length):
        if cust_frame["CUST_ID"][i] ==claim_frame["CUST_ID"][j]:
            #concat = pd.concat(cust_frame.loc[[i]], claim_frame.loc[[j]])
            count+=1
            
        
            

'''
bad_customers = framedata.loc[framedata["SIU_CUST_YN"]=="Y"]
writer = pd.ExcelWriter('bad_customers.xlsx', engine='xlsxwriter')
bad_customers.to_excel(writer, sheet_name='Sheet1')
writer.save()
'''