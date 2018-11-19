import requests
import re
data="""
网络安全,
网络空间安全,
信息内容安全
"""

data=re.sub('\s+','',data)
zymc=data.split(',')
print(zymc)