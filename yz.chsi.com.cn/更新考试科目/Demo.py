import requests
import pandas as pd
import re
import time
import random

headersinfo=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/201001', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134']

csv_data=pd.read_csv('school_info.csv')

values=csv_data.values
i=0
for value in values:
    try:
        if i%100==1:
            time.sleep(2)
        i+=1
        print(i)
        headers = {
            'User-Agent': "{}".format(headersinfo[random.randint(0, 3)])
        }

        r = requests.get(value[5], headers=headers)
        content = re.sub('\s+', '', r.text)
        pattern = re.search(
            """<tbodyclass="zsml-res-items">(.*?)</tbody>""",
            content, re.S)
        resultssss = re.findall("<td>(.*?)<span", pattern.group(1))
        school=[value[0]]
        one=[ resultssss[0]]
        two=[ resultssss[1]]
        three=[ resultssss[2]]
        four=[ resultssss[3]]
        dfdata = pd.DataFrame(
            {"学校":school,"政治": one, "英语": two, "数学": three, "专业": four})
        dfdata.to_csv('major.csv', index=False, encoding='utf_8_sig', mode='a', header=False)
    except:
        print("程序崩了")
        print(value)
        print("-------")
