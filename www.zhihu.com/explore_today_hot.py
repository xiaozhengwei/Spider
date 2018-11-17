import requests
import re
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
r=requests.get("https://www.zhihu.com/explore",headers=headers)
print(r.text)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(pattern,r.text)
print(titles)