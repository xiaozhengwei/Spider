import requests
from requests.packages import urllib3

urllib3.disable_warnings()
# response=requests.get("https://www.12306.cn",verify=False)
response=requests.get("https://www.12306.cn")
print(response.status_code)
