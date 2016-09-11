import pandas as pd

datafile = pd.read_csv("C:/workplace/bc_data/BGCON_FPINFO_DATA.csv", sep=',')

framefile = pd.DataFrame(datafile)
datarange = int(len(framefile)*0.8)
training_set = datafile[:datarange]
validation_set = datafile[datarange:]
print(training_set)
print(validation_set)

