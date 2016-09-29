import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import scipy.stats
from datascienceschools_net.sklearn.decision_tree import plot_decision_regions




def mode(x):
    return scipy.stats.mode(x)[0][-1]

def make_excel_file(data):
    writer = pd.ExcelWriter('result.xlsx', engine = 'xlsxwriter')
    data.to_excel(writer, sheet_name = 'result')
    writer.save()


claim_data = pd.read_csv("C:/workplace/bc_data/BGCON_CLAIM_DATA.csv")
cust_data = pd.read_csv("C:/workplace/bc_data/BGCON_CUST_DATA.csv")

claim_df = pd.DataFrame(claim_data)
cust_df = pd.DataFrame(cust_data)

claim_df = claim_df[['CUST_ID', 'ACCI_OCCP_GRP1', 'ACCI_DVSN',
                   'DMND_RESN_CODE', 'HOUSE_HOSP_DIST',
                    'HOSP_SPEC_DVSN', 'PAYM_AMT', 'NON_PAY_RATIO']]


cust_id = cust_df["CUST_ID"]
cust_id = cust_id.sort_values()
cust_id.index+=1

HOSP_SPEC_DVSN = cust_df["SIU_CUST_YN"]
HOSP_SPEC_DVSN.index +=1

HOSP_SPEC_DVSN_most = claim_df['HOSP_SPEC_DVSN'].groupby(claim_df['CUST_ID']).agg(mode)
HOSP_SPEC_DVSN_most.index+1

PAYM_AMT = claim_df['PAYM_AMT'].groupby(claim_df['CUST_ID']).mean()
PAYM_AMT.index+1

SEX = cust_df["SEX"]
SEX.index+=1

ESI_TYPE_CODE = cust_df["RESI_TYPE_CODE"]
ESI_TYPE_CODE.index+=1

FP_CAREER=cust_df["FP_CAREER"]
FP_CAREER.index+=1

MAX_PRM = cust_df['MAX_PRM']
MAX_PRM.index +=1

JPBASE_HSHD_INCM = cust_df["JPBASE_HSHD_INCM"]
JPBASE_HSHD_INCM.index+=1


#print(most)

result = pd.concat([HOSP_SPEC_DVSN, SEX, HOSP_SPEC_DVSN_most, round(PAYM_AMT),FP_CAREER, MAX_PRM,JPBASE_HSHD_INCM], axis=1)
result_1 = pd.DataFrame(result)
result_1.fillna(0, inplace=True)
#print(result_1)
X = result_1[["HOSP_SPEC_DVSN", 'MAX_PRM']] 
y = result_1[["SIU_CUST_YN"]]
tree1 = DecisionTreeClassifier(criterion="entropy", max_depth=1, random_state=0).fit(X,y)
plot_decision_regions(X, y, tree1, "Depth 1")





