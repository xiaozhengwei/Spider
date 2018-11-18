import requests

data={'name':'germey','age':'22'}
r=requests.post("https://yz.chsi.com.cn/sch/search.do?ssdm=&yxls=&b211=1",data=data)
print(r.text)