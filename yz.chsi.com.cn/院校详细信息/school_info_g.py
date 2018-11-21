import pandas as pd
import requests
import re
import time
import socket
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

}
# dwmc_sss=pd.read_csv('all_211_school.csv',encoding='utf_8_sig',sep=',').values
# for i in dwmc_sss:
#     dwmc.append(i[0])
# print(dwmc)

dwmcs = {'11':['北京大学', '中国人民大学', '清华大学', '北京交通大学', '北京工业大学', '北京航空航天大学', '北京理工大学', '北京科技大学', '北京化工大学', '北京邮电大学', '中国农业大学',
         '北京林业大学', '北京中医药大学', '北京师范大学', '北京外国语大学', '中国传媒大学', '中央财经大学', '对外经济贸易大学', '北京体育大学', '中央音乐学院', '中央民族大学',
          '中国政法大学', '华北电力大学','中国矿业大学(北京)','中国石油大学(北京)','中国地质大学(北京)'],
         '12':['南开大学', '天津大学', '天津医科大学'],
         '13':['华北电力大学(保定)', '河北工业大学'],
         '14':['太原理工大学'],
         '15':['内蒙古大学'],
         '21':['辽宁大学', '大连理工大学','东北大学', '大连海事大学'],
         '22':['吉林大学', '延边大学', '东北师范大学'],
         '23':[ '哈尔滨工业大学', '哈尔滨工程大学', '东北农业大学', '东北林业大学'],
         '31':['复旦大学', '同济大学', '上海交通大学','华东理工大学', '东华大学', '华东师范大学', '上海外国语大学', '上海财经大学', '上海大学','海军军医大学'],
         '32':['南京大学', '苏州大学', '东南大学', '南京航空航天大学', '南京理工大学','中国矿业大学', '河海大学', '江南大学', '南京农业大学', '中国药科大学', '南京师范大学'],
         '33':['浙江大学'],
         '34':['安徽大学', '中国科学技术大学', '合肥工业大学'],
         '35':['厦门大学', '福州大学'],
         '36':['南昌大学'],
         '37':['山东大学', '中国海洋大学', '中国石油大学(华东)'],
         '41':['郑州大学'],
         '42':['武汉大学', '华中科技大学', '中国地质大学(武汉)', '武汉理工大学', '华中农业大学', '华中师范大学','中南财经政法大学'],
         '43':['湖南大学', '中南大学', '湖南师范大学','国防科技大学'],
         '44':['中山大学', '暨南大学', '华南理工大学', '华南师范大学'],
         '45':['广西大学'],
         '46':['海南大学'],
         '50':['重庆大学','西南大学'],
         '51':['四川大学', '西南交通大学', '电子科技大学', '四川农业大学','西南财经大学'],
         '52':['贵州大学'],
         '53':['云南大学'],
         '54':['西藏大学'],
         '61':['西北大学', '西安交通大学', '西北工业大学', '西安电子科技大学','长安大学', '西北农林科技大学', '陕西师范大学','空军军医大学'],
         '62':['兰州大学'],
         '63':['青海大学'],
         '64':['宁夏大学'],
         '65':['新疆大学', '石河子大学']}
yjxkdms = ['0812', '0835', '0839']
number=[11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,51,52,53,54,61,62,63,64,65,71,81,82]
numbers=[str(i) for i in number]
zymcs = [
    ['★信息安全', '★智能科学与技术', '保密科学与技术', '大数据科学与工程', '服务科学与工程', '高可靠嵌入式系统', '工程施工装备及其自动化', '集成电路与系统', '计算机科学与技术',
         '计算机控制技术', '计算机控制与建筑智能化', '计算机软件与理论', '计算机系统结构', '计算机应用技术', '计算机智能测控与机电工程', '金融信息工程', '空天信息技术', '数据科学',
         '数据科学和信息技术', '数据科学与技术', '数字媒体技术', '网络信息安全', '物联网工程', '物联网工程与技术', '物联网技术', '物联网技术及应用', '信息安全', '信息与计算科学',
         '医疗信息技术', '智能计算与系统', '智能交通技术', '智能科学与技术', '智能应用技术'],
    ['金融领域软件工程', '领域软件工程', '人工智能与机器学习', '软件服务工程', '软件工程', '软件工程技术', '软件工程理论与方法', '软件工程理论与计算复杂性', '数据科学', '数据科学与工程', '数字表演', '数字媒体技术', '图像传播工程', '网络与信息系统安全', '信息安全', '信息与计算科学'],
    ['网络安全', '网络空间安全', '信息内容安全']
]

dirct={"0812":zymcs[0],"0835":zymcs[1],"0839":zymcs[2]}

headersinfo=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/201001', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134']
#学校
schools=[]
# 考试方式
test_types = []
# 院系所
colleges = []
# 专业
majors = []
# 研究方向
researchs = []
# 学习方式
study_types = []
# 人数
peoples = []
# 详情超链接
major_info=[]
i=0
search=""
for dwmc in dwmcs:
    for d in dwmcs[dwmc]:
        for yjxkdm in yjxkdms:
            for zymc in dirct[yjxkdm]:
                if(i%100==1):
                    time.sleep(10)
                try:
                    headers = {
                        'User-Agent': "{}".format(headersinfo[random.randint(0,3)])
                    }
                    search= """https://yz.chsi.com.cn/zsml/querySchAction.do?ssdm={}&dwmc={}&mldm=08&mlmc=&yjxkdm={}&xxfs=1&zymc={}""".format(
                            dwmc,d, yjxkdm, zymc)
                    r = requests.get(search
                       ,headers=headers)
                    print(r,d,yjxkdm,zymc)

                    pattern = re.search('<tbody>(.*?)</tbody>', r.text, re.S)
                    results = re.findall('<tr>(.*?)</tr>', pattern.group(1), re.S)
                    for result in results:
                        content = re.sub('\s+', '', result)
                        tds = re.findall('<td.*?>(.*?)</td>', content, re.S)
                        # 学校
                        school=[d]
                        # 考试方式
                        test_type=[tds[0]]
                        # 院系所
                        college=[tds[1]]
                        # 专业
                        major=[tds[2]]
                        # 研究方向
                        research=[tds[3]]
                        #专业详情
                        major_info=[tds[7]]
                        dfdata=pd.DataFrame({"学校":school,"考试方式":test_type,"院系所":college,"专业":major,"研究方向":research,"专业详情":major_info})
                        dfdata.to_csv('school_info.csv',index=False,encoding='utf_8_sig',mode='a',header=False)
                except:
                    print("*************")
                    print(search);