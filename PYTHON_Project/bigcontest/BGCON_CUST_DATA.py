import pandas as pd
import matplotlib.pyplot as plt


datafile = pd.read_csv("C:/workplace/bc_data/BGCON_CUST_DATA.csv")
framedata = pd.DataFrame(datafile)


bad_customers = framedata.loc[framedata["SIU_CUST_YN"]=="Y"]
plt.scatter(bad_customers['AGE'], bad_customers['RCBASE_HSHD_INCM'])
plt.show()
'''
good_customers = framedata.loc[framedata["SIU_CUST_YN"]=="N"]
plt.scatter(good_customers['AGE'], good_customers['RCBASE_HSHD_INCM'], c='red')
plt.show()
'''