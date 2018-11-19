import pymysql
import pandas as pd
# 打开数据库连接
db = pymysql.connect("47.93.221.205", "root", "1998zh2003", "utunan")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
file_path="all_985_school.csv"
all=pd.read_csv(file_path)
l=all.values
for i in l:
    print(i[0])
    sql="""UPDATE school 
            SET schoolType ='985 211' 
            WHERE schoolName='{}'
        """.format(i[0])
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()