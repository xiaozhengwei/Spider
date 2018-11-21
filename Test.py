import requests
import re
import random

headersinfo=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/201001', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134']

headers = {
            'User-Agent': "{}".format(headersinfo[random.randint(0, 3)])
        }
r = requests.get("https://yz.chsi.com.cn/zsml/kskm.jsp?id=1000121048081202031", headers=headers)
content = re.sub('\s+', '', r.text)
pattern = re.search(
    """<tbodyclass="zsml-res-items">(.*?)</tbody>""",
    content, re.S)
resultssss=re.findall("<td>(.*?)<span",pattern.group(1))
for i in resultssss:
    print(i,end="")
# one = [pattern.group(1)]
# two = [pattern.group(2)]
# three = [pattern.group(3)]
# four = [pattern.group(4)]
# print(one,two,three,four)