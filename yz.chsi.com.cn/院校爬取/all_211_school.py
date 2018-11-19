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
school_name = [];
school_province = []
school_subjection = []
for i in range(6):
    r=requests.get("https://yz.chsi.com.cn/sch/search.do?b211=1&start={}".format(i*20),headers=headers)
    # print(r.text)

    pattern=re.search('<tbody>(.*?)</tbody>',r.text,re.S)
    results=re.findall('<tr>(.*?)</tr>',pattern.group(1),re.S)

    # clear_results=[re.sub('\s+|进入|查询|<a(.*?)>|</a>',"",result) for result in results]
    # print(clear_results)
    # df=pd.DataFrame(clear_results)
    # print(df.values)


    for result in results:
        content=re.sub('\s+','',result)
        tds =re.findall('<td.*?>(.*?)</td>',content,re.S)
        list=[]
        for i in range(3):
            text=re.sub('<a(.*?)>|</a>|进入|查询|','', tds[i])
            if(i==0):
                school_name.append(text)
            elif(i==1):
                school_province.append(text)
            else:
                school_subjection.append(text)
datas=pd.DataFrame({"大学名称":school_name,"大学所在省份":school_province,"大学隶属":school_subjection})
print(datas.to_csv('all_211_school.csv',encoding='utf_8_sig',index=False,sep=','))
