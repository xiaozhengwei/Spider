import requests
import re
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

r=requests.get("https://yz.chsi.com.cn/sch/search.do?ssdm=&yxls=&b211=1",headers=headers)
pattern=re.search('<tbody>(.*?)</tbody>',r.text,re.S)
result=re.findall('<tr>(.*?)</tr>',pattern.group(1),re.S)
print(type(pattern.group(1)))
for i in range(result.__len__()):
    print(i+1,result[i])