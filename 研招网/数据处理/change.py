import pandas as pd
import re
pdcsv=pd.read_csv('school_info_li.csv')
values=pdcsv.values
count=0
for value in values:
    count+=1
    text=value[5]
    pattern = re.search('<ahref="(.*?)"target="_blank">查看</a>', text, re.S)
    if(pattern.group(1)=="" or pattern.group(1)==None):
        print(value)
    value[5]="https://yz.chsi.com.cn"+pattern.group(1)
pdcsv.to_csv('school_info_li2.csv',index=False,encoding='utf_8_sig',mode='a',header=False)
