import pymysql
# 打开数据库连接
db = pymysql.connect("47.93.221.205", "root", "1998zh2003", "utunan")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
import pandas as pd
file_path="all_211_school.csv"
all=pd.read_csv(file_path)
l=all.values


count=0
for i in l:
    sql="INSERT INTO school(schoolName,schoolProvince,schoolSubjection) VALUES ('{}','{}','{}')".format(i[0],i[1],i[2])
    try:
        cursor.execute(sql)
        db.commit()
        count+=1;
    except:
        db.rollback()
db.close()
print(count)