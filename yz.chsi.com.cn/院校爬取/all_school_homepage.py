"""
    此脚本用于爬取 研招网 所有的211大学的 (大学名称 大学所在地 大学隶属)
    代码质量极差
"""
import requests
import re
import pandas as pd
headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
results=requests.get("https://www.baidu.com",headers=headers);
print(results.text)
school_homepage_urls=[]

datas=pd.DataFrame({"大学名称":school_homepage_urls});
datas.to_csv('all_school_homepage.csv',encoding='utf_8_sig',index=False,sep=',')
