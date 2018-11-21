import pandas as pd

data1=pd.read_csv("school_info.csv")
data2=pd.read_csv("school_info.csv")
values1=data1.values
values2=data2.values
for i in range(1522):
    if(values1[i][5]!=values2[i][5]):
        print(i)